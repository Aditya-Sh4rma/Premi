from pyrogram import Client, filters, enums
from pyrogram.raw import functions, types

BOT_TOKEN = "7937721399:AAHAIOM5pkjrW_EjRinIUNoaJhjhEWzRmPg"
API_ID = 21346925
API_HASH = "908c9a085a238d1cd484a4269c887234"

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
