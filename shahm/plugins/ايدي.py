# shahm - abbas
# Copyright (C) 2022 shahmArabic . All Rights Reserved
#
# This file is a part of < https://github.com/shahm-Arabic/shahmAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/shahm-Arabic/shahmAr/blob/web/LICENSE/>.

"""
shahm - abbas
- كتـابـة الاضـافـات
بـاقـر - @shahm41
- حقـوق شـهــم @shahm50
- تخمـط صيـر مطـور كفــوو واذكــر المصــدر لو اطشـك لـ النـاس
"""
import contextlib
import html
import shutil
import os
import base64

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest

from shahm import shahm1
from shahm.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply, edit_delete
from ..helpers import reply_id
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.echo_sql import addecho, get_all_echos, get_echos, is_echo, remove_all_echos, remove_echo, remove_echos
from . import BOTLOG, BOTLOG_CHATID, spamwatch

plugin_category = "utils"
LOGS = logging.getLogger(__name__)
#Code by T.me/shahm41
rep_dev = (1960777228, 1260465030)
rep_dev = (1960777228, 1960777228)
abbas = (6848908141, 6848908141)
RIDA = gvarstatus("R_RRID") or "Rep-Thon"

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


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "لا يـوجـد بروفـايـل"
    dc_id = "Can't get dc id"
    with contextlib.suppress(AttributeError):
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    baqqir = (await event.client.get_entity(user_id)).premium
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس له اسم أول")
    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("لا يـوجـد")
    user_bio = "لا يـوجـد" if not user_bio else user_bio
# Copyright (C) 2021 shahm . All Rights Reserved
# الـرتب الوهميـه & فارات الكليشـه & البريميـوم & عـدد الرسـائل & التفاعـل = كتـابـة الكـود - بـاقـر @shahm41 / خاصـه بسـورس - شـهــم @shahm50 فقـط
    rmsg = await bot.get_messages(event.chat_id, 0, from_user=user_id) #Code by T.me/shahm41
    rrr = rmsg.total
    if rrr < 100: #Code by T.me/shahm41
        baqr = "غير متفاعل  🗿"
    elif rrr > 200 and rrr < 500:
        baqr = "ضعيف  🗿"
    elif rrr > 500 and rrr < 700:
        baqr = "شد حيلك  🏇"
    elif rrr > 700 and rr < 1000:
        baqr = "ماشي الحال  🏄🏻‍♂"
    elif rrr > 1000 and rrr < 2000:
        baqr = "ملك التفاعل  🎖"
    elif rrr > 2000 and rrr < 3000:
        baqr = "امبراطور التفاعل  🥇"
    elif rrr > 3000 and rrr < 4000:
        baqr = "غنبله  💣"
    else:
        baqr = "نار وشرر  🏆"
################# Dev shahm #################
    if user_id in abbas: #Code by T.me/shahm41
        rotbat = "مطـور السـورس 𓄂" 
    elif user_id in rep_dev:
        rotbat = "مـطـور 𐏕" 
    elif user_id == (await event.client.get_me()).id and user_id not in rep_dev:
        rotbat = "مـالك الحساب 𓀫" 
    else:
        rotbat = "العضـو 𓅫"
################# Dev abbas ################# 
    REP_TEXT = gvarstatus("CUSTOM_ALIVE_TEXT") or "•⎚• مـعلومـات المسـتخـدم مـن بـوت شـهــم"  #Code by T.me/shahm41
    REPM = gvarstatus("CUSTOM_ALIVE_EMOJI") or "✦ " #Code by T.me/shahm41
    REPF = gvarstatus("CUSTOM_ALIVE_FONT") or "⋆─┄─┄─┄─ ᴿᴱᴾᵀᴴᴼᴺ ─┄─┄─┄─⋆" #Code by T.me/shahm41
    caption = f"<b> {REP_TEXT} </b>\n"
    caption += f"ٴ<b>{REPF}</b>\n"
    caption += f"<b>{REPM}الاسـم    ⇠ </b> "
    caption += f'<a href="tg://user?id={user_id}">{full_name}</a>'
    caption += f"\n<b>{REPM}المعـرف  ⇠  {username}</b>"
    caption += f"\n<b>{REPM}الايـدي   ⇠ </b> <code>{user_id}</code>\n"
    caption += f"<b>{REPM}الرتبـــه   ⇠ {rotbat} </b>\n" #Code by T.me/shahm41
    if baqqir == True or user_id in abbas: #Code by T.me/shahm41
        caption += f"<b>{REPM}الحسـاب ⇠  بـريميـوم 🌟</b>\n"
    caption += f"<b>{REPM}الصـور    ⇠</b>  {replied_user_profile_photos_count}\n"
    caption += f"<b>{REPM}الرسائل   ⇠</b>  {rrr}  💌\n" #Code by T.me/shahm41
    caption += f"<b>{REPM}التفاعل   ⇠</b>  {baqr}\n" #Code by T.me/shahm41
    if user_id != (await event.client.get_me()).id: #Code by T.me/shahm41
        caption += f"<b>{REPM}الـمجموعات المشتـركة ⇠  {common_chat}</b>\n"
    caption += f"<b>{REPM}البايـو     ⇠  {user_bio}</b>\n"
    caption += f"ٴ<b>{REPF}</b>"
    return photo, caption
# Copyright (C) 2021 shahmArabic . All Rights Reserved


@shahm1.rep_cmd(
    pattern="ايدي(?: |$)(.*)",
    command=("ايدي", plugin_category),
    info={
        "header": "لـ عـرض معلومـات الشخـص",
        "الاستـخـدام": " {tr}ايدي بالـرد او {tr}ايدي + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    rep = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(rep, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await rep.delete()
    except TypeError:
        await rep.edit(caption, parse_mode="html")


@shahm1.rep_cmd(
    pattern="ا(?: |$)(.*)",
    command=("ا", plugin_category),
    info={
        "header": "امـر مختصـر لـ عـرض معلومـات الشخـص",
        "الاستـخـدام": " {tr}ا بالـرد او {tr}ا + معـرف/ايـدي الشخص",
    },
)
async def who(event):
    "Gets info of an user"
    rep = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(rep, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await rep.delete()
    except TypeError:
        await rep.edit(caption, parse_mode="html")


@shahm1.rep_cmd(pattern=f"{RIDA}(?: |$)(.*)")
async def hwo(event):
    rep = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except (AttributeError, TypeError):
        return await edit_or_reply(rep, "**- لـم استطـع العثــور ع الشخــص ؟!**")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await rep.delete()
    except TypeError:
        await rep.edit(caption, parse_mode="html")


@shahm1.rep_cmd(
    pattern="صورته(?:\s|$)([\s\S]*)",
    command=("صورته", plugin_category),
    info={
        "header": "لـ جـلب بـروفـايـلات الشخـص",
        "الاستـخـدام": [
            "{tr}صورته + عدد",
            "{tr}صورته الكل",
            "{tr}صورته",
        ],
    },
)
async def potocmd(event):
    "To get user or group profile pic"
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user and user.sender:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **"
            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "الكل":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(
                    event, "**- رقـم خـاطـئ . . .**"
                )
                return
        except BaseException:
            await edit_or_reply(event, "**- رقـم خـاطـئ . . .**")
            return
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "**- لا يـوجـد هنـاك صـور لهـذا الشخـص ؟! **"
            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()
