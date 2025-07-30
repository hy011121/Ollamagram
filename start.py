from telethon import TelegramClient, events
import requests

# === YOUR OWN CREDENTIALS ===
api_id = 26437066
api_hash = '0510d7e69332d99ae36064ca0c70a087'
session_name = 'personal_ai_bot'
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

def ask_ollama(prompt: str, model: str = "phi") -> str:
    """Send a prompt to the local Ollama instance via /api/generate and return the response."""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=120)
        # Debug: Uncomment this if you want to inspect the raw response

        response.raise_for_status()
        data = response.json()
        return data.get("response", "[AI ERROR] Empty response from model.")
    except requests.exceptions.ConnectionError:
        return "[AI ERROR] Couldn’t connect to Ollama. Make sure 'ollama serve' is running on port 11434."
    except requests.exceptions.Timeout:
        return "[AI ERROR] Request to AI timed out."
    except requests.exceptions.HTTPError as e:
        return f"[AI ERROR] HTTP error: {e} - {response.text}"
    except ValueError as e:
        return f"[AI ERROR] Failed to parse JSON: {e}"

def main():
    client = TelegramClient(session_name, api_id, api_hash)
    @client.on(events.NewMessage(incoming=True))
    async def handle_message(event):
        if event.is_private and event.raw_text:
            user_input = event.raw_text.strip()
            ai_response = ask_ollama(user_input, model="phi")
            await event.respond(ai_response)

    print("Local AI bot is running.")
    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
