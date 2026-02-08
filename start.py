from pyrogram import Client, filters, enums
from pyrofork.raw import functions, types

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
    text = "Hello I'm alive 🐶"
    
    await client.invoke(
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
            random_id=client.rnd_id()
        )
    )

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
