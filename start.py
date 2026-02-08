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
    # FREE custom emoji IDs (jo bots bhi use kar sakte hain)
    # Ye IDs "free" custom emojis ki hain
    
    text = "Hello I'm alive 🐶"
    
    # Tum jo ID diye the (5850591660198596754) wo shayad premium-only hai
    # Free custom emoji ID try karo (example: popular free packs se)
    
    await client.invoke(
        functions.messages.SendMessage(
            peer=await client.resolve_peer(message.chat.id),
            message=text,
            entities=[
                types.MessageEntityCustomEmoji(
                    offset=16,
                    length=2,
                    document_id=5850591660198596754  # Ye ID try karo
                )
            ],
            random_id=client.rnd_id()
        )
    )

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
