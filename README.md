![4e75d9e5e28bc08665335636a6a39094](https://github.com/user-attachments/assets/0dc78780-3f2d-48cd-bb83-219b2c0db0ea)

---

This bot is built using **Telethon**, a powerful and flexible Python library for interacting directly with the Telegram API. Its main goal is to forward incoming Telegram messages to a local AI model running via **Ollama**, and then send back an automatic reply. Everything runs locally - no external APIs or cloud services involved - making it a great solution for anyone who wants a private AI assistant on Telegram without sending data elsewhere.

Before running the bot, make sure you’ve installed the required Python dependencies:

```bash
pip install telethon requests
```

You’ll also need your **`api_id`** and **`api_hash`** from Telegram. To get them, simply go to [my.telegram.org](https://my.telegram.org), log in with your Telegram account, then head over to **API Development Tools**. Create a new application (you can enter any name and URL), and you’ll be provided with the `api_id` and `api_hash`. These need to be added to your script so the bot can connect to your Telegram account.

On the AI side, this bot uses **Ollama** - a local server for running AI models like `phi`, `llama2`, or `mistral`. If you don’t have Ollama installed yet, just run:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then start the service:

```bash
ollama serve
```

And pull the AI model you want to use, for example:

```bash
ollama pull phi
```

By default, the bot uses the `phi` model, but you can easily switch to any other supported model, as long as it’s already pulled. The communication between the bot and the AI happens via a local endpoint at `http://localhost:11434/api/generate`. Make sure your Ollama server is running smoothly so the bot can respond without delays.

Note: Since this is an early version, you might run into occasional issues - such as timeouts, unrecognized inputs, or failed message delivery if the Ollama server isn’t active. This script is intended as a starting point or proof of concept, so feel free to extend it with better logging, multi-user support, extra validation, or deeper integration with your AI projects.

---
