import json
import os
import re

from telethon.events import CallbackQuery
from telethon.tl.functions.users import GetUsersRequest

from shahm import shahm1
from ..sql_helper.globals import gvarstatus


@shahm1.tgbot.on(CallbackQuery(data=re.compile(b"secret_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    uzerid = gvarstatus("hmsa_id")
    ussr = int(uzerid) if uzerid.isdigit() else uzerid
    try:
        rrr = await shahm1.get_entity(ussr)
    except ValueError:
        rrr = await shahm1(GetUsersRequest(ussr))
    if os.path.exists("./shahm/secret.txt"):
        jsondata = json.load(open("./shahm/secret.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, shahm1.uid, rrr.id]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "مطـي الهمسـه مـو الك 🦓"
        except KeyError:
            reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في البوت"
    else:
        reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في البـوت"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
