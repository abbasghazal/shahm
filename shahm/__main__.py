import sys, asyncio
import shahm
from shahm import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import shahm
from .utils import mybot, saves, autoname
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup
from .sql_helper.globals import addgvar, delgvar, gvarstatus

LOGS = logging.getLogger("𝐑𝐞𝐩𝐭𝐡𝐨𝐧")
cmdhr = Config.COMMAND_HAND_LER

if gvarstatus("ALIVE_NAME") is None: #Code by T.me/shahm41
    try:
        LOGS.info("⌭ بـدء إضافة الاسـم التلقـائـي ⌭")
        shahm.loop.run_until_complete(autoname())
        LOGS.info("✓ تـم إضافة فار الاسـم .. بـنجـاح ✓")
    except Exception as e:
        LOGS.error(f"- The AutoName {e}")

try:
    LOGS.info("⌭ بـدء تنزيـل شـهــم ⌭")
    shahm.loop.run_until_complete(setup_bot())
    LOGS.info("✓ تـم تنزيـل شـهــم .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

class RPCheck:
    def __init__(self):
        self.sucess = True
RPcheck = RPCheck()

try:
    LOGS.info("⌭ بـدء إنشـاء البـوت التلقـائـي ⌭")
    shahm.loop.run_until_complete(mybot())
    LOGS.info("✓ تـم إنشـاء البـوت .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")

try:
    LOGS.info("⌭ جـارِ تفعيـل الاشتـراك ⌭")
    shahm.loop.create_task(saves())
    LOGS.info("✓ تـم تفعيـل الاشتـراك .. بنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    LOGS.info(f"⌔ تـم تنصيـب شـهــم . . بنجـاح ✓ \n⌔ لـ إظهـار الاوامـر ارسـل (.الاوامر)")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    RPcheck.sucess = True
    return


shahm.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    shahm.disconnect()
elif not RPcheck.sucess:
    try:
        shahm.run_until_disconnected()
    except ConnectionError:
        pass
else:
    try:
        shahm.run_until_disconnected()
    except ConnectionError:
        pass
