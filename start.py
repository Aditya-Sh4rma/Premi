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

def get_utf16_length(text):
    """Calculate UTF-16 length for proper entity offsets"""
    return len(text.encode('utf-16-le')) // 2

@app.on_message(filters.command("start"))
async def start_command(client, message):
    
    # Simple test - sirf ek emoji
    text = "🌸"
    
    # UTF-16 mein length calculate karo
    offset = 0
    length = get_utf16_length(text)
    
    print(f"Text: {text}")
    print(f"Offset: {offset}, Length: {length}")
    
    entities = [
        types.MessageEntityCustomEmoji(
            offset=offset,
            length=length,
            document_id=5850355647450714328
        )
    ]
    
    try:
        result = await client.invoke(
            functions.messages.SendMessage(
                peer=await client.resolve_peer(message.chat.id),
                message=text,
                entities=entities,
                random_id=client.rnd_id()
            )
        )
        print(f"Success! Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
