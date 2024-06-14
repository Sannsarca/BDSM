# BDSM car BOT

This is a Telegram bot that uses data on rented cars to help users find relevant options. <br />

Link: https://t.me/BDSM_car_bot <br />
The bot is currently disabled. Ask if you want to see how it works.<br /><br />

# Structure<br /><br />
1. 'storage' folder - Folder with saved index structure. Here stored latest index and it is used for fast bot setup.<br />
2. 'tests_and_preparations.ipynb' - Jyputer Notebook with all relevant steps and tests to parse data, create index and chat with LLM model.<br />
3. 'chatbot.py' - Main code with TelegramBot. Here you need to specify your Telebot Token.<br />
4. 'environment.yml' - requirements with all libraries needed.<br /><br />

# How to run<br /><br />
1. Download Files - you can use only 'storage' and 'chatbot.py'.<br />
2. Create environment using 'environment.yml'<br />
3. Create a bot in Telegram using https://t.me/BotFather.<br />
4. In 'chatbot.py' specify keys and token<br />
5. Run<br /><br />

# Requirements<br /><br />

 Requirements to run files:<br />
  libraries:<br />
    &emsp;telebot<br />
    &emsp;os<br />
    &emsp;pandas<br />
    &emsp;langchain<br />
    &emsp;llama_index<br />
    &emsp;openai<br /><br />
  
  keys:<br />
    &emsp;OPENAI_API_KEY: specify your OpenAI key<br />
    &emsp;LANGCHAIN_API_KEY: specify your LangSmith key<br />
    &emsp;Telebot token: specify your Telegram Bot Token<br /><br />  
    
  For some library resolwings also execute:<br />
    &emsp;!pip install -U langchain langchain-openai<br />
    &emsp;!pip install llama-index-llms-langchain<br />
    &emsp;!pip install -U langchain<br />
    &emsp;!pip install llama-index-llms-fireworks<br />
