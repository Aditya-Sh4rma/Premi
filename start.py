# start.py
from pyrogram import Client, filters
from pyrogram.raw import functions, types

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
    
    # Direct raw method with InputMessageEntityCustomEmoji
    text = "Hello I'm alive 🐶"
    
    try:
        await client.send(
            functions.messages.SendMessage(
                peer=await client.resolve_peer(message.chat.id),
                message=text,
                entities=[
                    types.MessageEntityCustomEmoji(
                        offset=16,
                        length=2,
                        document_id=5850591660198596754
                    )
                ],
                no_webpage=True,
                random_id=client.rnd_id(),
                reply_to=types.InputReplyToMessage(reply_to_msg_id=message.id)
            )
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
