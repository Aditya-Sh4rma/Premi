# start.py
from pyrogram import Client, filters
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
    
    # Caption text (exactly jaise Waifu bot ne bheja)
    caption = "🌸 Hello I'm alive 🌸! ✨"
    
    # Custom emoji entities for caption
    entities = [
        types.MessageEntityCustomEmoji(
            offset=0,
            length=2,
            document_id=5850355647450714328  # 🌸 pehla
        ),
        types.MessageEntityCustomEmoji(
            offset=20,
            length=2,
            document_id=5850355647450714328  # 🌸 dusra
        ),
        types.MessageEntityCustomEmoji(
            offset=24,
            length=1,
            document_id=5850203446694646751  # ✨
        )
    ]
    
    # Agar tumhare paas video/GIF hai to uska path do
    # Abhi simple text message bhejte hain with entities
    
    result = await client.invoke(
        functions.messages.SendMessage(
            peer=await client.resolve_peer(message.chat.id),
            message=caption,
            entities=entities,
            random_id=client.rnd_id()
        )
    )
    
    print(f"Sent with entities: {result}")

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
