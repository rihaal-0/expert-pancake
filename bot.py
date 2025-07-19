import os
from pyrogram import Client, filters
import subprocess

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document | filters.video)
async def handler(client, message):
    file_name = message.document.file_name if message.document else message.video.file_name
    if not file_name.endswith(".mkv"):
        await message.reply("Please send an MKV file.")
        return

    os.makedirs("downloads", exist_ok=True)
    mkv_path = f"./downloads/{file_name}"
    mp4_path = mkv_path.replace(".mkv", ".mp4")

    await message.reply("Downloading...")
    await message.download(file_name=mkv_path)

    await message.reply("Converting...")
    subprocess.run(["ffmpeg", "-i", mkv_path, "-c:v", "libx264", "-c:a", "aac", mp4_path])

    await message.reply_document(mp4_path)
    os.remove(mkv_path)
    os.remove(mp4_path)

app.run()
