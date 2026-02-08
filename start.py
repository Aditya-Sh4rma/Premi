# start.py
from pyrogram import Client, filters
from pyrogram.raw import functions, types
import struct

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
API_ID = 12345678
API_HASH = "your_api_hash_here"

app = Client(
    "my_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    
    # Method 1: Pehle simple message bhejte hain
    text = "Hello I'm alive 🐶"
    
    try:
        result = await client.invoke(
            functions.messages.SendMessage(
                peer=await client.resolve_peer(message.chat.id),
                message=text,
                no_webpage=True,
                entities=[
                    types.MessageEntityCustomEmoji(
                        offset=16,
                        length=2,
                        document_id=5850591660198596754
                    )
                ],
                random_id=client.rnd_id()
            )
        )
        print(f"Message sent successfully: {result}")
    except Exception as e:
        print(f"Error: {e}")
        # Fallback - normal message
        await message.reply_text("Hello I'm alive 🐶")

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
