# start.py
from pyrogram import Client, filters
from pyrogram.enums import ParseMode

BOT_TOKEN = "7692203867:AAGfRNfZ-2E8qwUuIy-szA3o1k6EoR-APEw"
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
    
    # HTML format with custom emoji
    text = 'Hello I\'m alive <emoji id="5850720861404795438">🐶</emoji>'
    
    try:
        await message.reply_text(
            text,
            parse_mode=ParseMode.HTML
        )
        print("✅ Message sent successfully with custom emoji!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
