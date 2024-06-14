import telebot
#Connecting to the bot
bot = telebot.TeleBot('your-token')

###Code from Notebook
import os

#Specifying key for OpenAI model
os.environ["OPENAI_API_KEY"]="your-key"

#Specifying parameters for langchain connection
os.environ["LANGCHAIN_TRACING_V2"]='true'
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"]="your-key"
os.environ["LANGCHAIN_PROJECT"]="langsmith-car-bot"
#Specifying key for OpenAI model

from llama_index.core.memory import ChatMemoryBuffer
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
#Creating memory for LLM model
memory = ChatMemoryBuffer.from_defaults(token_limit=2000)

#Downloading saved data from storage
from llama_index.core import StorageContext, load_index_from_storage

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context=storage_context)

#Specifying prompt
chat_engine = index.as_chat_engine(
    chat_mode="context",
    llm=llm,
    memory=memory,
    system_prompt=(
        "Given a conversation (between Human and Assistant) and a follow up question from Human, \
        answer the question using the data, return ALL data about relevand cars AS A TABLE. \
        If input irrelevant write that there are no cars with such inputs."
    ),
)
###
#Polling all messages and handling based on commands
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Hi, I am AI assistant. You can ask any question about cars you want to rent. I will find one for you!\
                         \n /help - to see this menu.\
                         \n /clear - to make bot forgot previos questions.")
    elif message.text == "/clear":
        bot.send_message(message.from_user.id, "I have cleared all my memory. Waiting for your questions!")
    else:
        response = chat_engine.chat(message.text)
        print(message.text)
        bot.send_message(message.from_user.id, f"<pre>{str(response)}</pre>", parse_mode='HTML')
bot.polling(none_stop=True, interval=0)
