#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modified By > @DC4_WARRIOR


from pyrogram import Client as Clinton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from plugins.help_text import help_user, start, about

@Clinton.on_callback_query()
async def button(bot, update):

    cb_data = update.data
    if "|" in cb_data:
        await youtube_dl_call_back(bot, update)
    elif "=" in cb_data:
        await ddl_call_back(bot, update)
    elif "help" in cb_data:
        await update.message.delete()
        await help_user(bot, update.message)
    elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
    elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

