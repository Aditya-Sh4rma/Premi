# start.py
from pyrogram import Client, filters
from pyrogram.types import MessageEntity
from pyrogram import enums
# Apni details yahan dalo
BOT_TOKEN = "7937721399:AAHAIOM5pkjrW_EjRinIUNoaJhjhEWzRmPg"  # @BotFather se milega
API_ID = 21346925  # my.telegram.org se milega (number)
API_HASH = "908c9a085a238d1cd484a4269c887234"  # my.telegram.org se milega (string)

app = Client(
    "my_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Raw API se message bhejenge with premium emoji
    await client.invoke(
        functions.messages.SendMessage(
            peer=await client.resolve_peer(message.chat.id),
            message="Hello I'm alive 🙀",
            entities=[
                types.MessageEntityCustomEmoji(
                    offset=14,
                    length=2,
                    document_id=5850509914086052253
                )
            ],
            random_id=client.rnd_id()
        )
    )

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
