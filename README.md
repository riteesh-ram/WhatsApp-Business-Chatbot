# WhatsApp Business Chatbot

## Project Summary
Welcome to the WhatsApp Business Chatbot project! This chatbot is designed to help businesses interact with customers on WhatsApp, answer their questions, and take product orders automatically. The current version focuses on selling Dairy Milk Silk chocolates, but the system can be easily adapted for other products.

This project combines Artificial Intelligence (AI) and Natural Language Processing (NLP) to understand what users are saying and respond just like a real person. It is built using popular technologies like Python, Flask (for web server), TFLearn/TensorFlow (for machine learning), NLTK (for language processing), and Twilio (for WhatsApp integration).


## Why This Project?
Businesses today need to respond quickly and efficiently to customer queries. This chatbot shows how AI can automate customer support and sales, saving time and improving customer experience. While the demo is for chocolates, you can easily update it for any product or service.


## What Can This Chatbot Do?
- **Chat with Customers:** Understands greetings, questions, and requests using AI.
- **Answer Questions:** Responds to queries about products, timings, and more.
- **Take Orders:** Lets users order different types of Dairy Milk Silk chocolates by replying with simple keywords or numbers.
- **Log Conversations:** Saves every chat in a database for future reference or analysis.


## How Does It Work? (Simple Explanation)
1. **User sends a message on WhatsApp.**
2. **The chatbot reads the message and tries to understand what the user wants.**
3. **It uses AI to match the message to a known question or request.**
4. **The chatbot replies with the best answer or helps the user place an order.**
5. **Every chat is saved in a database for record-keeping.**

For technical users: The chatbot uses a neural network trained on example questions and answers (see `Intent.json`). The model files (`model.tflearn.*`, `checkpoint`) must be present. If you change the questions or add new ones, retrain the model using `chatbotcode1.py`.


## How Are Chats Stored?
Every conversation is saved in a local database file called `chat_bot_data_base.db`. This helps you keep track of customer interactions and can be used for analysis or improving the chatbot.


## Security & Setup Notes
- You need Twilio credentials (Account SID, Auth Token, WhatsApp sandbox number) to connect the chatbot to WhatsApp. Set these as environment variables for safety.
- Never share or commit your credentials to public code repositories.


## What's Inside? (File Guide)
```
WhatsApp-Business-Chatbot/
│
├── app.py                        # Main app: connects WhatsApp, handles messages
├── chatbotcode1.py               # Chatbot logic: AI, NLP, and model training
├── Intent.json                   # List of questions, requests, and answers the bot understands
├── requirements.txt              # List of Python packages needed
├── Procfile                      # For deploying on Heroku
├── runtime.txt                   # Python version for deployment
├── model.tflearn.data-00000-of-00001  # AI model data
├── model.tflearn.index           # AI model index
├── model.tflearn.meta            # AI model metadata
├── checkpoint                    # Model checkpoint
├── README.md                     # This guide
├── WhatsAppBusinessChatbot_RannlabTechnologies_RiteeshRamChander_1800206C203.pdf # Project report
├── nltk.txt                      # (Optional) NLTK data file
```


## How to Set Up and Run (Step-by-Step)
1. **Clone the Project**
   ```bash
   git clone <repo-url>
   cd WhatsApp-Business-Chatbot
   ```
2. **Install Python Packages**
   Make sure you have Python 3.6+ installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```
3. **Download NLTK Data**
   In Python, run:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('stopwords')
   ```
4. **Set Up Twilio for WhatsApp**
   - Create a Twilio account and WhatsApp sandbox.
   - Set your Twilio credentials as environment variables:
     ```bash
     export TWILIO_ACCOUNT_SID=your_account_sid
     export TWILIO_AUTH_TOKEN=your_auth_token
     export TWILIO_WHATSAPP_NUMBER=your_sandbox_number
     ```
   - Update your Twilio sandbox webhook to point to `/botmessage` on your server.
5. **Run the App**
   ```bash
   python app.py
   ```
   The app will start locally. For production, use Gunicorn or deploy to Heroku.
6. **Chat with the Bot**
   - Send a message to your WhatsApp sandbox number.
   - The bot will reply based on its AI model and the questions/answers in `Intent.json`.


## Testing & Troubleshooting
- Test the bot by sending WhatsApp messages to your sandbox number.
- For developers: You can also use tools like Postman to send POST requests to `/botmessage`.
- Check the database file (`chat_bot_data_base.db`) to see saved conversations.


## How It Works (For All Readers)
- You send a message to the WhatsApp bot.
- The bot reads your message and tries to understand what you want.
- It uses AI to match your message to a known question or request.
- The bot replies with the best answer or helps you place an order.
- Every chat is saved for future reference.


## Limitations
- The bot only understands questions and requests listed in `Intent.json`. For new topics, update this file and retrain the model.
- No payment or inventory management is included.
- This is a demo project and not ready for production use without more security and scaling.


## Deployment
- For cloud deployment (like Heroku), use the provided `Procfile` and `runtime.txt`.
- Make sure your Twilio credentials are set securely in your deployment platform.


## How to Extend or Customize
- Add new questions, requests, or answers in `Intent.json`.
- Retrain the AI model using `chatbotcode1.py` if you make changes.
- You can adapt the bot for any product or service by updating the intents and responses.


## License & Credits
This project is for educational purposes. For more details, see the included project report PDF.


For any questions or help, please refer to the project report or contact the author.
