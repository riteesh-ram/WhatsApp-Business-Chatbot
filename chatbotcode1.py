import json
import tflearn
import random
import numpy
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#import sqlite3

with open("intent.json") as dataset:
    v = json.load(dataset)

words = []
types = []
questions = []
type_question = []

for object in v["objective"]:
    for question in object["questions"]:
        token_words = nltk.word_tokenize(question)
        words.extend(token_words)
        questions.append(token_words)
        type_question.append(object["type"])
    if object["type"] not in types:
        types.append(object["type"])

words = [wordnet_lemmatizer.lemmatize(wrds.lower()) for wrds in words if wrds != "?" and wrds != "!" and wrds != "," and wrds != "'"]
types = sorted(types)
words = sorted(list(set(words)))

stop_words_en = set(stopwords.words('english'))
for w in stop_words_en:
    if w in words:
        words.remove(w)

input_data = []
output_data = []
out_type = [0 for _ in range(len(types))]

for x, q in enumerate(questions):
    bag_of_words = []

    wrds = [wordnet_lemmatizer.lemmatize(wo.lower()) for wo in q]

    for word in words:
        if word in wrds:
            bag_of_words.append(1)
        else:
            bag_of_words.append(0)

    output_type = out_type[:]
    output_type[types.index(type_question[x])] = 1

    input_data.append(bag_of_words)
    output_data.append(output_type)

training_data = numpy.array(input_data)
output_data = numpy.array(output_data)

nodes = 70
alpha = 0.01
input_data = tflearn.input_data(shape=[None, len(training_data[0])])
hidden_layer1 = tflearn.fully_connected(input_data, nodes, activation="LeakyReLU")
hidden_layer2 = tflearn.fully_connected(hidden_layer1, nodes, activation="LeakyReLU")
output_layer = tflearn.fully_connected(hidden_layer2, len(output_data[0]), activation="softmax")
output_layer = tflearn.regression(output_layer, optimizer="adam", loss="categorical_crossentropy", learning_rate=alpha)

model = tflearn.DNN(output_layer)
model.fit(training_data, output_data, n_epoch=1000, batch_size=15, show_metric=True)
model.save("model.tflearn")
no_ans = ["Sorry i don't understand it, do you like to have chocolates? then type yes", "Sorry i didn't get it, ok but are u a chocolate lover? if yes please type yes"]
def chatbot(user_msg):
    response = model.predict([convert_bag(user_msg, words)])[0]
    response_index = numpy.argmax(response)
    type = types[response_index]
    if response[response_index] > 0.7:
        for t in v["objective"]:
            if t['type'] == type:
                answers = t['answers']
        r = random.choice(answers)
        return r
    else:
        ans = random.choice(no_ans)
        return ans

def convert_bag(user_msg, words):
    user_bag = [0 for _ in range(len(words))]

    u_words = nltk.word_tokenize(user_msg)
    u_words = [wordnet_lemmatizer.lemmatize(word.lower()) for word in u_words]
    stop_words_en = set(stopwords.words('english'))
    for w in stop_words_en:
        if w in u_words:
            u_words.remove(w)
    for word in u_words:
        for i, w in enumerate(words):
            if w == word:
                user_bag[i] = 1
    return numpy.array(user_bag)
