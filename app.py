from chatbotcode1 import chatbot
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
import numpy
import tflearn
import random
import json
import sqlite3

app = Flask(__name__)

@app.route("/botmessage", methods=['POST'])
def bot_reply():
    connect = sqlite3.connect('chat_bot_data_base.db')
    cur = connect.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS chatbot(S_No INTEGER PRIMARY KEY, pattern TEXT, responses TEXT)")
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    user_msg = request.form.get('Body')
    reply = chatbot(user_msg)
    # Create reply
    response = MessagingResponse()
    response.message(reply)
    cur.execute("""INSERT INTO chatbot(pattern, responses) VALUES("{}", "{}")""".format(user_msg, reply))
    connect.commit()
    cur.close()
    connect.close()
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)

