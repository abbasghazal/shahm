import re

from telethon.utils import get_display_name

from shahm import shahm1
from ..core.managers import edit_or_reply
from ..sql_helper.filter_sql import (
    add_filter,
    get_filters,
    remove_all_filters,
    remove_filter,
)
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "العروض"


shahmWF_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝑺𝑯𝑨𝑯𝑴 - اوامـر الـردود / والتـرحيب](t.me/shahm50) 𓆪\n\n"
    "**✾╎قائـمه اوامـر الـردود 🦾 :** \n\n"
    "**⎞𝟏⎝** `.رد`\n"
    "**•• ⦇الامـر + اسـم الـرد بالـرد ع كلمـة الـرد او بالـرد ع ميديـا⦈ لـ اضـافة رد بالكـروب**\n\n"
    "**⎞𝟐⎝** `.حذف رد`\n"
    "**•• ⦇الامـر + كلمـة الـرد⦈ لـ حـذف رد محـدد**\n\n"
    "**⎞𝟑⎝** `.ردودي`\n"
    "**•• لـ عـرض قائمـة بالـردود الخـاصـه بك**\n\n"
    "**⎞𝟒⎝** `.حذف الردود`\n"
    "**•• لـ حـذف جميـع الـردود الخـاصـه بـك**\n\n"
    "**✾╎قائـمه اوامر تـرحيب المجمـوعـات 🌐:** \n\n"
    "**⎞𝟓⎝** `.ترحيب`\n"
    "**•• ⦇الامـر + نـص التـرحـيـب⦈**\n\n"
    "**⎞𝟔⎝** `.حذف الترحيب`\n"
    "**•• لـ حـذف التـرحـيـب**\n\n"
    "**⎞𝟕⎝** `.الترحيبات`\n"
    "**•• لـ جـلـب تـرحـيـبـك**\n\n"
    "**✾╎قائـمه اوامر ترحـيـب الخـاص 🌐:**\n\n"
    "**⎞𝟖⎝** `.رحب`\n"
    "**•• ⦇الامـر + نـص التـرحيـب⦈**\n\n"
    "**⎞𝟗⎝** `.حذف رحب`\n"
    "**•• لـ حـذف تـرحيـب الخـاص**\n\n"
    "**⎞𝟏𝟎⎝** `.جلب رحب`\n"
    "**•• لـ جـلب تـرحيـب الخـاص **\n\n"
    "\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝑺𝑯𝑨𝑯𝑴](t.me/shahm50) 𓆪"
)


# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@shahm1.rep_cmd(pattern="الردود")
async def cmd(abbas):
    await edit_or_reply(abbas, shahmWF_cmd)

@shahm1.rep_cmd(pattern="الترحيب")
async def cmd(roger):
    await edit_or_reply(roger, shahmWF_cmd)


@shahm1.rep_cmd(incoming=True)
async def filter_incoming_handler(event):
    name = event.raw_text
    filters = get_filters(event.chat_id)
    if not filters:
        return
    a_user = await event.get_sender()
    chat = await event.get_chat()
    me = await event.client.get_me()
    title = get_display_name(await event.get_chat()) or "هـذه الدردشــه"
    participants = await event.client.get_participants(chat)
    count = len(participants)
    mention = f"[{a_user.first_name}](tg://user?id={a_user.id})"
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    first = a_user.first_name
    last = a_user.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{a_user.username}" if a_user.username else mention
    userid = a_user.id
    my_first = me.first_name
    my_last = me.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{me.username}" if me.username else my_mention
    for trigger in filters:
        pattern = f"( |^|[^\\w]){re.escape(trigger.keyword)}( |$|[^\\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            file_media = None
            filter_msg = None
            if trigger.f_mesg_id:
                msg_o = await event.client.get_messages(
                    entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id)
                )
                file_media = msg_o.media
                filter_msg = msg_o.message
                link_preview = True
            elif trigger.reply:
                filter_msg = trigger.reply
                link_preview = False
            await event.reply(
                filter_msg.format(
                    mention=mention,
                    title=title,
                    count=count,
                    first=first,
                    last=last,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                    my_first=my_first,
                    my_last=my_last,
                    my_fullname=my_fullname,
                    my_username=my_username,
                    my_mention=my_mention,
                ),
                file=file_media,
                link_preview=link_preview,
            )


@shahm1.rep_cmd(
    pattern="رد (.*)",
    command=("رد", plugin_category),
    info={
        "header": "To save filter for the given keyword.",
        "اضـافـات الــرد": {
            "{mention}": "اضافه منشن",
            "{title}": "اضافة اسم كـروب الـرد",
            "{count}": "اضافة عدد اعضاء الكروب",
            "{first}": "اضافة الاسم الاول",
            "{last}": "اضافة الاسم الاخر",
            "{fullname}": "اضافة الاسم الكامل",
            "{userid}": "اضافة ايدي الشخص",
            "{username}": "اضافة معرف الشخص",
            "{my_first}": "اضافة اسمك الاول",
            "{my_fullname}": "اضافة اسمك الكامل",
            "{my_last}": "اضافة اسمك الاخر",
            "{my_mention}": "اضافة تاك حسابك",
            "{my_username}": "اضافة معرفك",
        },
        "الاسـتخـدام": "{tr}رد + كلمـه بالـرد ع نـص الـرد",
    },
)
async def add_new_filter(event):
    "To save the filter"
    keyword = event.pattern_match.group(1)
    string = event.text.partition(keyword)[2]
    msg = await event.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#الــردود\
            \n**⪼ ايـدي الدردشـه :**  {event.chat_id}\
            \n**⪼ الــرد :**  {keyword}\
            \n**⪼ تم حفظ الرسـالة كـرد على المستخدمين في المجموعـة المحـددة ...**",
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                event,
                "**❈╎يتطلب رد ميديـا تعيين كـروب السجـل اولاً ..**\n**❈╎لاضافـة كـروب السجـل**\n**❈╎اتبـع الشـرح ⇚**",
            )
            return
    elif msg and msg.text and not string:
        string = msg.text
    elif not string:
        return await edit_or_reply(event, "**- يجب استخدام الامر بشكل صحيح**")
    success = "**- ❝ الـرد ↫** {} **تـم {} بـ نجـاح 🎆☑️"
    if add_filter(str(event.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(event, success.format(keyword, "اضافتـه"))
    remove_filter(str(event.chat_id), keyword)
    if add_filter(str(event.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(event, success.format(keyword, "تحديثـه"))
    await edit_or_reply(event, f"**- اووبـس .. لقـد حـدث خطأ اثنـاء إعـداد الـرد** {keyword}")


@shahm1.rep_cmd(
    pattern="ردودي$",
    command=("ردودي", plugin_category),
    info={
        "header": "To list all filters in that chat.",
        "الاسـتخـدام": "{tr}ردودي",
    },
)
async def on_snip_list(event):
    "To list all filters in that chat."
    OUT_STR = "** ❈╎لاتوجـد ردود محفوظـه في هـذه الدردشـه ༗**"
    filters = get_filters(event.chat_id)
    for filt in filters:
        if OUT_STR == "** ❈╎لاتوجـد ردود محفوظـه في هـذه الدردشـه ༗**":
            OUT_STR = "𓆩 𝗦𝗼𝘂𝗿𝗰𝗲 𝑺𝑯𝑨𝑯𝑴 - قائمـة الـردود 𓆪\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n"
        OUT_STR += "👉 `{}`\n".format(filt.keyword)
    await edit_or_reply(
        event,
        OUT_STR,
        caption="**⧗╎الـردود المضـافـه في هـذه الدردشـه هـي :**",
        file_name="filters.text",
    )


@shahm1.rep_cmd(
    pattern="حذف رد ([\s\S]*)",
    command=("حذف رد", plugin_category),
    info={
        "header": "To delete that filter . so if user send that keyword bot will not reply",
        "الاسـتخـدام": "{tr}حذف رد + كلمة الرد",
    },
)
async def remove_a_filter(event):
    "Stops the specified keyword."
    filt = event.pattern_match.group(1)
    if not remove_filter(event.chat_id, filt):
        await event.edit("**- ❝ الـرد ↫** {} **غيـر موجـود ⁉️**".format(filt))
    else:
        await event.edit("**- ❝ الـرد ↫** {} **تم حذفه بنجاح ☑️**".format(filt))


@shahm1.rep_cmd(
    pattern="حذف الردود$",
    command=("حذف الردود", plugin_category),
    info={
        "header": "To delete all filters in that group.",
        "الاسـتخـدام": "{tr}حذف الردود",
    },
)
async def on_all_snip_delete(event):
    "To delete all filters in that group."
    filters = get_filters(event.chat_id)
    if filters:
        remove_all_filters(event.chat_id)
        await edit_or_reply(event, "**⪼ تم حذف جـميع الــردود المضـافـهہ هنـا .. بنجـاح☑️**")
    else:
        await edit_or_reply(event, "**⪼ لا توجـد ردود مضـافـهہ في هـذه المجموعـة**")
