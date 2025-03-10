from telethon import *

from shahm import shahm

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.autopost_sql import add_post, get_all_post, is_post, remove_post
from shahm.core.logger import logging
from ..sql_helper.globals import gvarstatus
from . import BOTLOG, BOTLOG_CHATID
from . import *

plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)

SPRD = gvarstatus("R_SPRD") or "(نشر_تلقائي|نشر|تلقائي)"
OFSPRD = gvarstatus("R_OFSPRD") or "(ايقاف_النشر|ايقاف النشر|ستوب)"

abbasNSH_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝑺𝑯𝑨𝑯𝑴 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامـر النشـر التلقـائي](t.me/shahm50) 𓆪\n\n"
    "**- اضغـط ع الامـر للنسـخ** \n\n\n"
    "**⪼** `.تلقائي` \n"
    "**- الامـر + ايـدي القنـاة تستخـدم الامـر بقنـاتـك** \n\n"
    "**⪼** `.ايقاف النشر` \n"
    "**- الامـر + ايـدي القنـاة تستخـدم الامـر بقنـاتـك** \n\n"
    "🛃 سيتـم اضـافة المزيـد من تخصيص الاوامـر بالتحديثـات الجـايه\n"
    "\n𓆩 [𐇮  ✗ ¦ ↱𝐺𝑜𝑙 𝐷. 𝑅𝑜𝑔𝑒𝑟↲ ¦ ✗ 𐇮](t.me/shahm41) 𓆪"
)


async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


@shahm.rep_cmd(pattern=f"{SPRD} ?(.*)")
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**✾╎عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    trz_ = event.pattern_match.group(1)
    if str(trz_).startswith("-100"):
        zed = str(trz_).replace("-100", "")
    else:
        zed = trz_
    if not zed.isdigit():
        return await edit_or_reply(event, "**✾╎عـذراً .. قـم بوضـع ايـدي القنـاة اولاً**")
    if is_post(zed , event.chat_id):
        return await edit_or_reply(event, "**✾╎تم تفعيـل النشر التلقـائي لهـذه القنـاة هنـا .. بنجـاح ✓**")
    add_post(zed, event.chat_id)
    await edit_or_reply(event, f"**✾╎جـاري بدء النشـر التلقـائي من القنـاة ** `{trz_}`")


@shahm.rep_cmd(pattern=f"{OFSPRD} ?(.*)")
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**✾╎عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    trz_ = event.pattern_match.group(1)
    if str(trz_).startswith("-100"):
        zed = str(trz_).replace("-100", "")
    else:
        zed = trz_
    if not zed.isdigit():
        return await edit_or_reply(event, "**✾╎عـذراً .. قـم بوضـع ايـدي القنـاة اولاً**")
    if not is_post(zed, event.chat_id):
        return await edit_or_reply(event, "**✾╎تم تعطيـل النشر التلقـائي لهـذه القنـاة هنـا .. بنجـاح ✓**")
    remove_post(zed, event.chat_id)
    await edit_or_reply(event, f"**✾╎تم ايقـاف النشـر التلقـائي من** `{trz_}`")


@shahm.rep_cmd(incoming=True, forword=None)
async def _(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await shahm.send_message(int(chat), event.message)



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@shahm.rep_cmd(pattern="النشر")
async def cmd(abbas):
    await edit_or_reply(abbas, BaairNSH_cmd)

