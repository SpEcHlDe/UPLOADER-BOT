#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation
from pyrogram import filters
from database.adduser import AddUser
from pyrogram import Client as Clinton
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ForceReply


@Clinton.on_message(filters.private & filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Source ⚡", url="https://github.com/Clinton-Abraham/UPLOADER-BOT"),
                    InlineKeyboardButton("Channel 👨🏻‍💻", url="https://t.me/Space_X_bots"),
                    InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/clinton_abraham_bot"),
                ],
                [
                    InlineKeyboardButton("🏡Home", callback_data="start"),
                    InlineKeyboardButton("♻️About", callback_data="about")
                ],
            ]
        ),
        reply_to_message_id=update.message_id
    )


@Clinton.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    await AddUser(bot, update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Source ⚡", url="https://github.com/Clinton-Abraham/UPLOADER-BOT"),
                    InlineKeyboardButton("Channel 👨🏻‍💻", url="https://t.me/Space_X_bots"),
                    InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/clinton_abraham_bot"),
                ],
                [
                    InlineKeyboardButton("⚙️Help", callback_data="help"),
                    InlineKeyboardButton("♻️About", callback_data="about")
                ],
            ]
        ),
        reply_to_message_id=update.message_id
    )
    
@Clinton.on_message(filters.private & filters.command(["about"]))
def about(bot, update):
    
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Source ⚡", url="https://github.com/Clinton-Abraham/UPLOADER-BOT"),
                    InlineKeyboardButton("Channel 👨🏻‍💻", url="https://t.me/Space_X_bots"),
                    InlineKeyboardButton("Developer 👨‍⚖️", url="https://t.me/clinton_abraham_bot"),
                ],
                [
                    InlineKeyboardButton("🏡Home", callback_data="start"),
                    InlineKeyboardButton("⚙️Help", callback_data="help")
                ],
            ]
        ),
    )

@Clinton.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)
        
Clinton.run()
