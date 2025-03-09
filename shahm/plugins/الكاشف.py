#𝑺𝑯𝑨𝑯𝑴 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @shahm41 خاص بسـورس ⤶ 𝑺𝑯𝑨𝑯𝑴
#الملف مرفـوع ع استضـافتـي مهمـا خمطت راح تطلـع حقـــوقــي بســورســـك
#هههههههههههههههههه


import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from shahm import shahm1

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


abbasPH_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝑺𝑯𝑨𝑯𝑴 𝗖𝗼𝗻𝗳𝗶𝗴 📲 - كـاشـف الارقـام العربيــة](t.me/shahm50) 𓆪\n\n"
    "**⪼ الامــر ↵**\n\n"
    "⪼ `.كاشف` + اسـم الدولـة + الـرقـم بـدون مفتـاح الـدولة\n\n"
    "**⪼ الوصـف :**\n"
    "**- لجـلب معلـومـات عـن رقـم هـاتف معيـن**\n\n"
    "**⪼ مثـال :**\n\n"
    "`.كاشف اليمن 777887798` \n\n"
    "`.كاشف السعوديه 555542317` \n\n"
    "`.كاشف الامارات 43171234` \n\n"
    "**الامـر يدعـم الـدول التـاليـة ↵** 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 \n\n"
    "🛃 سيتـم اضـافة المزيـد من الدول قريبـاً\n\n"
    "\n𓆩 [𐇮 ✗ ¦ ↱𝐺𝑜𝑙 𝐷. 𝑅𝑜𝑔𝑒𝑟↲ ¦ ✗  𐇮](t.me/shahm41) 𓆪"
)


@shahm1.rep_cmd(
    pattern="كاشف ?(.*)",
    command=("كاشف", plugin_category),
    info={
        "header": "لـ جـلب معلـومـات عـن رقـم هـاتف معيـن .. الامـر يدعـم الـدول التـاليـة ↵ 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 .. سيـتم اضـافـة بقيـة الـدول العـربيـة قريبـاً",
        "الاستـخـدام": "{tr}كاشف + اسـم الدولـة + الـرقـم بـدون مفتـاح الـدولة",
    },
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . كـاشف الاࢪقـام الـ؏ـࢪبيـة 📲.. اࢪسـل** `.الكاشف` **للتعليـمات 𓅫╰**"
        )
    chat = "@shahmybot"
    shahm41 = await edit_or_reply(event, "**╮•⎚ جـارِ الكـشف ؏ــن الـرقـم  📲 ⌭ . . .**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1194140165)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await shahm41.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @shahmybot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await shahm41.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await shahm41.delete()
            await event.client.send_message(event.chat_id, response.message)



# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@shahm1.rep_cmd(pattern="الكاشف")
async def cmd(abbas):
    await edit_or_reply(abbas, abbasPH_cmd)

