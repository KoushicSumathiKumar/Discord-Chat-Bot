# Discord ChatBot with Wolfram Alpha Integration

This project is a **Discord Chatbot** that uses the [**Wolfram Alpha API**](https://www.wolframalpha.com/) to provide answers to user queries. The bot can respond to messages in **public channels** and **send private responses**. This project was **highly educational** for me, as it was my **first experience** with learning and implementing **asynchronous methods**. Grasping and understanding how **asynchronous methods** work was **challenging** and **time-consuming**, but it was worth it as I found them to be both **powerful** and **extremely useful** which I will definitely will be using in my **future projects**.

## Features

- Responds to user messages in **Discord channels**.
- Sends **private responses** if the message starts with a `?`.
- Uses **Wolfram Alpha API** to get answers for user queries.

## Setup

If you'd like to run the **Python** scripts provided, please ensure that you have **Python** installed on your system. You can download and install Python from the official Python website: [python.org/downloads](https://www.python.org/downloads/).

**Terminial commands for libraries used:**
- `pip install discord.py`
- `pip install python-dotenv`
- `pip install aiohttp`

**Create an `.env` file in the root directory and add your Discord bot token and Wolfram Alpha App ID:**

    ```
    DISCORD_TOKEN=your_discord_token
    WOLFRAM_APP_ID=your_wolfram_app_id
    ```

## Discord ChatBot in Action
Chatting with the bot in a **public channel**:
![image](https://github.com/KoushicSumathiKumar/Discord-Chat-Bot/assets/149502679/15f2e836-ed8e-4036-9887-f48511d557e7)

Message sent in a **public channel**, requesting for **a private respond**:
![image](https://github.com/KoushicSumathiKumar/Discord-Chat-Bot/assets/149502679/8cdeeedd-7f5c-44a9-9c30-7e3d99a959cf)

ChatBot replying in **private dms**: 
![image](https://github.com/KoushicSumathiKumar/Discord-Chat-Bot/assets/149502679/bc6fde43-b93a-41c8-8777-c8b5e1f7823b)




