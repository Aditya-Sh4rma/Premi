# start.py
from pyrogram import Client, filters
from pyrogram.types import MessageEntity

# Apna bot token yahan dalo
BOT_TOKEN = "7937721399:AAHAIOM5pkjrW_EjRinIUNoaJhjhEWzRmPg"

# Bot client
app = Client(
    "my_bot",
    bot_token=BOT_TOKEN,
    api_id=123456,  # apni API ID yahan dalo
    api_hash="your_api_hash_here"  # apni API hash yahan dalo
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Premium emoji entity
    entities = [
        MessageEntity(
            type="custom_emoji",
            offset=14,  # "Hello I'm alive" ke baad (14 characters)
            length=2,
            custom_emoji_id="5850509914086052253"
        )
    ]
    
    await message.reply_text(
        "Hello I'm alive 🙀",
        entities=entities
    )

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
