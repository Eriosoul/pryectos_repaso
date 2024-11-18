import numpy as np
import pandas as pd
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pyttsx3
import speech_recognition as sr

nltk.download('punkt')
nltk.download('stopwords')

spanish_stopwords = stopwords.words('spanish')
sbst = SnowballStemmer('spanish')

data = {
    "pregunta": [
        "cuantos meses de garantía dáis",
        "cuánto dura la garantía",
        "qué plazo de soporte y corrección de errores posterior ofrecéis",
        "Plazo de puesta en marcha del servicio",
        "Cuánto tardan en implementar el servicio",
        "Precio del servicio",
        "Cuánto cuesta el servicio",
        "Años de experiencia de la empresa",
        "Cuántos años llevan en el mercado"
    ],
    "respuesta": [
        "Te confirmo que nuestro periodo de garantía es de 12 meses",
        "Dispone de 12 meses de garantías garantizado",
        "Actualmente usted dispone de 12 meses de garantía",
        "El plazo de puesta en marcha del servicio es de 6 meses.",
        "Actualmente el plazo del puesto del servicio serían unos 6 meses",
        "El precio del servicio es de 30€ mensuales.",
        "Disponemos de un precio de 30€ al mes, ¿nada mal no?",
        "Nuestra empresa cuenta con más de 25 años de experiencia en el sector.",
        "Contamos con 25 años de experiencia siendo número 1 en nuestro sector"
    ]
}

df = pd.DataFrame(data)

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in spanish_stopwords]
    stemmed_tokens = [sbst.stem(token) for token in tokens]
    return ' '.join(stemmed_tokens)

df['pregunta_preprocessed'] = df['pregunta'].apply(preprocess_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['pregunta_preprocessed'])
y = df['respuesta']

model = LogisticRegression()
model.fit(X, y)

# Iniciamos el modelo de voz
talk = pyttsx3.init()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        return text
    except sr.UnknownValueError:
        print("No se pudo entender lo que dijiste")
    except sr.RequestError as e:
        print(f"Error al conectarse con el servicio de reconocimiento de voz: {e}")

    return None

def chatbot():
    talk.say("Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte hoy? (Di 'salir' para terminar la conversación)")
    talk.runAndWait()
    print("¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte hoy? (Di 'salir' para terminar la conversación)")

    count = 0
    while True:
        prompt = recognize_speech()
        if prompt:
            if prompt.lower() == 'salir':
                response = "¡Gracias por usar el servicio! Hasta luego."
                talk.say(response)
                talk.runAndWait()
                print(f"Chatbot: {response}")
                break

            prompt_preprocessed = preprocess_text(prompt)
            prompt_vec = vectorizer.transform([prompt_preprocessed])
            respuesta = model.predict(prompt_vec)[0]

            if np.max(prompt_vec.toarray()) == 0:
                count += 1
                if count >= 4:
                    response = "Lo siento, no estoy seguro de cómo ayudarte. Te pondré en contacto con un agente."
                    talk.say(response)
                    talk.runAndWait()
                    print(f"Chatbot: {response}")
                    break
                else:
                    response = "No entiendo, por favor intenta reformular tu pregunta."
                    talk.say(response)
                    talk.runAndWait()
                    print(f"Chatbot: {response}")
            else:
                count = 0
                talk.say(respuesta)
                talk.runAndWait()
                print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    try:
        chatbot()
    except KeyboardInterrupt as k:
        print("Se ha interrumpido el programa", k)
    except Exception as ex:
        print(ex)
