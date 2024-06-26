from pyrogram import filters
from pyrogram.types import Message

from InflexMusic import app
from InflexMusic.misc import SUDOERS
from InflexMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>example :</b>\n\n/autoend [enable | disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» auto end stream enanled.\n\nasisstants will automatically leave the videochat after few mins when no one is listening."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» auto end stream disabled.")
    else:
        await message.reply_text(usage)
