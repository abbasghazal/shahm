# shahm - abbas
# Copyright (C) 2023 shahmArabic. All Rights Reserved
#
# This file is a part of < https://github.com/shahmArabic/shahmAr/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/shahmArabic/shahmAr/blob/master/LICENSE/>.
""" 
OpenAi & ChatGpt for shahm™ t.me/shahm50
Write file by shahm, Roger t.me/shahm41, t.me/shahm41
ها خماط بعدك تخمط مني .. ماتستحي ؟
متى راح تصير مطور وانت مقضيها خمط تعب وحقوق الناس
ههههههههههههههههههههههههههههههههههههههههههههههههههههههه
"""

import requests
import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import shahm
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "البوت"


# code by t.me/shahm41
@shahm.rep_cmd(pattern="شهم(?: |$)(.*)")
async def shahm_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@GPT4Telegrambot" #code by t.me/shahm41
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**⎉╎بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**⎉╎مثـــال :**\n`.شهم من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/shahm41
        shahm = zzz.text
    if not event.reply_to_msg_id: #code by t.me/shahm41
        shahm = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**⎉╎جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n⎉╎الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/shahm41
        try:
            await conv.send_message(shahm)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/shahm41
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            shahm = await conv.get_response()
            malath = shahm.text
            if "understanding" in shahm2.text: #code by t.me/shahm41
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {shahm}\n\n{malath}**\n\n───────────────────\n𝑺𝑯𝑨𝑯𝑴 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t𝐁𝐀𝐐𝐈𝐑 • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/shahm41
            await shahm(unblock("GPT4Telegrambot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(shahm)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/shahm41
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            shahm2 = await conv.get_response()
            malath = shahm2.text
            if "understanding" in shahm2.text: #code by t.me/shahm41
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in shahm2.text: #code by t.me/shahm41
                await asyncio.sleep(5)
                shahm2 = await conv.get_response()
                malath = shahm2.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {shahm}\n\n{malath}**\n\n───────────────────\n𝑺𝑯𝑨𝑯𝑴  𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\tˢʰᵃʰᵐ • ᴼᵖᵉⁿᴬᴵ")


# تخمــط اهينـــك Fuk-You

# code by t.me/shahm41
@shahm.rep_cmd(pattern="س(?: |$)(.*)")
async def shahm_gpt(event):
    zilzal = event.pattern_match.group(1)
    zzz = await event.get_reply_message()
    chat = "@GPT4Telegrambot" #code by t.me/shahm41
    if not zilzal and not event.reply_to_msg_id:
        return await edit_or_reply(event, "**⎉╎بالـرد ع سـؤال او باضـافة السـؤال للامـر**\n**⎉╎مثـــال :**\n`.شهم من هو مكتشف الجاذبية الارضية`")
    if not zilzal and event.reply_to_msg_id and zzz.text: #code by t.me/shahm41
        shahm = zzz.text
    if not event.reply_to_msg_id: #code by t.me/shahm41
        shahm = event.pattern_match.group(1)
    zed = await edit_or_reply(event, "**⎉╎جـارِ الاتصـال بـ الذكـاء الاصطنـاعـي\n⎉╎الرجـاء الانتظـار .. لحظـات**")
    async with borg.conversation(chat) as conv: #code by t.me/shahm41
        try:
            await conv.send_message(shahm)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/shahm41
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            shahm2 = await conv.get_response()
            malath = shahm2.text
            if "understanding" in shahm2.text: #code by t.me/shahm41
                aa = malath.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            if "Please wait a moment" in shahm2.text: #code by t.me/shahm41
                await asyncio.sleep(5)
                shahm2 = await conv.get_response()
                malath = shahm2.text
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {shahm}\n\n{malath}**\n\n───────────────────\n𝑺𝑯𝑨𝑯𝑴 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ꜱᴇʀʙᴏᴛ**\n\t\t\t\t\t\t\t\t𝐁𝐀𝐐𝐈𝐑 • ᴼᵖᵉⁿᴬᴵ")
        except YouBlockedUserError: #code by t.me/shahm41
            await shahm(unblock("GPT4Telegrambot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(shahm)
            zzzthon = await conv.get_response()
            ahmed = zzzthon.text
            if "another 8 seconds" in zzzthon.text: #code by t.me/shahm41
                aa = ahmed.replace("⏳ Please wait another 8 seconds before sending the next question . . .", "**⎉╎يُرجى الانتظار 8 ثوانٍ ⏳\n⎉╎بين ارسـال كل سـؤال والتـالي**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await asyncio.sleep(5)
            shahm2 = await conv.get_response()
            malath = shahm2.text
            if "understanding" in shahm2.text: #code by t.me/shahm41
                aa = malath.replace("I'm sorry, I'm not quite understanding the question. Could you please rephrase it?", "**- عـذراً .. لم أفهم سؤالك\n- قم بـ إعادة صياغته من فضلك؟!**") 
                await event.delete()
                return await borg.send_message(event.chat_id, aa)
            await zed.delete()
            await borg.send_message(event.chat_id, f"**س/ {shahm}\n\n{malath}**\n\n───────────────────\n𝑺𝑯𝑨𝑯𝑴 𝗨**ꜱᴇʀʙᴏᴛ** 𝗧**ᴏᴏʟꜱ**\n\t\t\t\t\t\t\t\t𝐁𝐀𝐐𝐈𝐑 • ᴼᵖᵉⁿᴬᴵ")
