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
    # Premium emoji with custom_emoji_id
    text = "Hello I'm alive <emoji id=5850509914086052253>🙀</emoji>"
    
    await message.reply_text(
        text,
        parse_mode=enums.ParseMode.HTML
    )

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
