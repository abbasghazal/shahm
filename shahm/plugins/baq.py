# shahmArabic
# Copyright (C) 2023 shahmArabic. All Rights Reserved
#
# This file is a part of < https://github.com/shahmArabic/shahm/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/shahmArabic/shahm/blob/master/LICENSE/>.
"""سـورس شـهــم™
So تخمـط الملـف اهينك واطشك للناس خماط واوثق عليك
Copyright (C) 2023 shahmArabic. All Rights Reserved
Credit: https://github.com/shahmArabic/shahm
Devloper: https://telegram.dog/shahm41"""
"""import json
import math
import asyncio
import os
import random
import re
import time
from pathlib import Path
from uuid import uuid4

from telethon import Button, types
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery
from telethon.tl.functions.users import GetUsersRequest

from . import shahm1
from ..Config import Config
from ..helpers import reply_id
from ..sql_helper.globals import gvarstatus
from ..core.logger import logging
from ..helpers.utils import _format
from . import mention

LOGS = logging.getLogger(__name__)
tr = Config.COMMAND_HAND_LER

# Copyright (C) 2023 abbas . All Rights Reserved
@shahm1.tgbot.on(InlineQuery)
async def inline_handler(event):
    from .baq import ttt, ddd, bbb, hmm, ymm, fmm, dss, hss, nmm, mnn, bmm, scc
    builder = event.builder
    result = None
    query = event.text
    string = query.lower()
    query.split(" ", 2)
    str_y = query.split(" ", 1)
    string.split()
    query_user_id = event.query.user_id
    user_id = gvarstatus("hmsa_id")
    full_name = gvarstatus("hmsa_name")
    username = gvarstatus("hmsa_user")
    if username.startswith("@"):
        abbas = gvarstatus("hmsa_user")
    else:
        abbas = f"[{full_name}](tg://user?id={user_id})"
    if query_user_id == Config.OWNER_ID or query_user_id in Config.SUDO_USERS:  # Code by T.me/shahm41
        taibaid = Config.OWNER_ID
    elif query_user_id == user_id or query_user_id == int(user_id):
        taibaid = user_id
    if query_user_id == Config.OWNER_ID or query_user_id == user_id or query_user_id == int(user_id) or query_user_id in Config.SUDO_USERS:  # Code by T.me/shahm41
        inf = re.compile("secret (.*) (.*)")
        match2 = re.findall(inf, query)
        if match2:
            user_list = []
            baqqir = ""
            query = query[7:]
            info_type = [hmm, ymm, fmm]
            if "|" in query:
                iris, query = query.replace(" |", "|").replace("| ", "|").split("|")
                users = iris.split(" ")
            else:
                user, query = query.split(" ", 1)
                users = [user]
            for user in users:
                usr = int(user) if user.isdigit() else user
                try:
                    u = await shahm1.get_entity(usr)
                except ValueError:
                    u = await shahm1(GetUsersRequest(usr))
                if u.username:
                    baqqir += f"@{u.username}"
                else:
                    baqqir += f"[{u.first_name}](tg://user?id={u.id})"
                user_list.append(u.id)
                baqqir += " "
            baqqir = baqqir[:-1]
            old_msg = os.path.join("./shahm", f"{scc}.txt")
            try:
                jsondata = json.load(open(old_msg))
            except Exception:
                jsondata = False
            timestamp = int(time.time() * 2)
            new_msg = {
                str(timestamp): {"userid": user_list, "text": query}
            }  # Code by T.me/shahm41
            buttons = [[Button.inline(info_type[2], data=f"{scc}_{timestamp}")],[Button.switch_inline(bmm, query=f"secret {malathid} \nهلو", same_peer=True)]]
            result = builder.article(
                title=f"{hmm} {baqqir}",
                description=f"{dss}",
                text=f"{hss} {baqqir} \n**{dss}**",
                buttons=buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(new_msg)
                json.dump(jsondata, open(old_msg, "w"))
            else:
                json.dump(new_msg, open(old_msg, "w"))
        elif string == "abbas":
            results = []
            results.append(
                builder.article(
                    title=f"{nmm}",
                    description=f"{mnn}",
                    text=f"**{ttt}** {abbas} **{ddd}**",
                    buttons=bbb,
                    link_preview=False,
                ),
            )
            await event.answer(results)
"""
