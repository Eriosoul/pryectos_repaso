import random
import json
import pickle
import numpy as np
import tensorflow as tf

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('D:\pythonProject\pryectos_repaso\CRUD\chatbotdir\intents.json').read())

words = []
classes = []
documents = []
# Ignoraremos algunos signos
ignoreLetters = ['?', '!', '¿', '¡', '.', ',', ';', ':']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((wordList, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# quitamos duplicados y normalizamos las palabras
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignoreLetters]
words = sorted(set(words))  # Asegúrate de que `words` tenga palabras únicas
classes = sorted(set(classes))  # Clases ya están correctamente definidas

# Guardamos las palabras y clases
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]  # Normalizamos las palabras
    for word in words:
        bag.append(1) if word in wordPatterns else bag.append(0)
    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1  # Corregido el índice
    training.append(bag + outputRow)

random.shuffle(training)
training = np.array(training)

trainX = training[:, :len(words)]
trainY = training[:, len(words):]

# Creamos el modelo
model = tf.keras.Sequential()

# Corregido el nombre de la capa 'layer' a 'layers'
model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))

# Optimizador con tasa de aprendizaje y momentum
sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

# Compilamos el modelo
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Entrenamos el modelo
hist = model.fit(np.array(trainX), np.array(trainY), epochs=200, batch_size=5, verbose=1)

# Guardamos el modelo
model.save('chatbot_simple_libro_model.h5', hist)
print("EXECUTE...")