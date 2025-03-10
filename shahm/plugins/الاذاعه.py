from telethon import events

from shahm import shahm

from ..core.managers import edit_or_reply
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البوت"
from . import * 

REP_BLACKLIST = [
    -1001236815136,
    -1001614012587,
    ]

REP_BBLACKLIST = [
    777000,
    ]
#

abbas_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝑺𝑯𝑨𝑯𝑴 𝗖𝗼𝗻𝗳𝗶𝗴 - اوامـر الاذا؏ـــة](t.me/shahm50) 𓆪\n\n"
    "**⎞𝟏⎝** `.للمجموعات`\n"
    "**بالـرد ؏ــلى رسـالة او وسائـط او كتابـة رسـالة مع الامـࢪ**\n"
    "**- لـ اذاعـة رسـالة او ميديـا لكـل المجموعـات اللي انت موجود فيهـا . .**\n\n\n"
    "**⎞𝟐⎝** `.للخاص`\n"
    "**بالـرد ؏ــلى رسـالة او وسائـط او كتابـة رسـالة مع الامـࢪ**\n"
    "**- لـ اذاعـة رسـالة او ميديـا لكـل الاشخـاص اللي موجـودين عنـدك خـاص . .**\n\n\n"
    "**⎞𝟑⎝** `.خاص`\n"
    "**الامـر + معرف الشخص + الرسـاله . .**\n"
    " **- ارسـال رسـاله الى الشخص المحدد بدون الدخول للخاص وقراءة الرسـائل . .**\n\n"
    "\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝑺𝑯𝑨𝑯𝑴](t.me/shahm50) 𓆪"
)


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@shahm.rep_cmd(pattern="الاذاعه")
async def cmd(abbas):
    await edit_or_reply(abbas, abbas_cmd)


@shahm.rep_cmd(pattern=f"للمجموعات(?: |$)(.*)")
async def gcast(event):
    shahm = event.pattern_match.group(1)
    if shahm:
        msg = shahm
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**✾╎بالـرد ؏ــلى رسـالة او وسائـط او كتابـة رسـالة مع الامـࢪ**")
        return
    roz = await edit_or_reply(event, "**✾╎ جـاري الاذاعـه في المجموعـات ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in REP_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**✾╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من المجموعـات ، خطـأ في الارسـال الـى ** `{er}` **من المجموعـات**"
    )
    
@shahm.rep_cmd(pattern=f"للخاص(?: |$)(.*)")
async def gucast(event):
    shahm = event.pattern_match.group(1)
    if shahm:
        msg = shahm
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await edit_or_reply(event, "**✾╎بالـرد ؏ــلى رسـالة او وسائـط او كتابـة رسـالة مع الامـࢪ**")
        return
    roz = await edit_or_reply(event, "**✾╎ جـاري الاذاعـه في الخـاص ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in REP_BBLACKLIST:
                    done += 1
                    await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await roz.edit(
        f"**✾╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من الخـاص ، خطـأ في الارسـال الـى ** `{er}` **من الخـاص**"
    )
    

@shahm.rep_cmd(pattern="خاص ?(.*)")
async def pmto(event):
    r = event.pattern_match.group(1)
    p = r.split(" ")
    chat_id = p[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = ""
    for i in p[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await shahm.send_message(chat_id, msg)
        await event.edit("**✾╎تـم ارسال الرسـالة الـى الشخـص بـدون الدخـول للخـاص .. بنجـاح ✓**")
    except BaseException:
        await event.edit("**✾╎اووبس .. لقـد حدث خطـأ مـا .. اعـد المحـاوله**")

