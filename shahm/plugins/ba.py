import asyncio
import os
import logging
from pathlib import Path
import time
from datetime import datetime

from telethon import events, functions, types
from telethon.utils import get_peer_id
from telethon.tl.types import InputPeerChannel, InputMessagesFilterDocument

from . import shahm1
from ..Config import Config
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..helpers.utils import install_pip, _reptools, _reputils, _format, parse_pre, reply_id
from ..utils import lload_module, inst_done

LOGS = logging.getLogger(__name__)
h_type = True

if Config.abbas_A:

    async def install():
        if gvarstatus("PMLOG") and gvarstatus("PMLOG") != "false":
            delgvar("PMLOG")
        if gvarstatus("GRPLOG") and gvarstatus("GRPLOG") != "false":
            delgvar("GRPLOG")
        try:
            entity = await shahm1.get_input_entity(Config.abbas_A)
            if isinstance(entity, InputPeerChannel):
                full_info = await shahm1(functions.channels.GetFullChannelRequest(
                    channel=entity
                ))
            abbas = full_info.full_chat.id
        except Exception as e:
            entity = await shahm1.get_entity(Config.abbas_A)
            full_info = await shahm1(functions.channels.GetFullChannelRequest(
                channel=entity
            ))
            abbas = full_info.full_chat.id
        documentss = await shahm1.get_messages(abbas, None, filter=InputMessagesFilterDocument)
        total = int(documentss.total)
        plgnm = 0
        for module in range(total):
            if plgnm == 22:
                break
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if plugin_name.endswith(".py"):
                if os.path.exists(f"shahm/plugins/{plugin_name}"):
                    return
                downloaded_file_name = await shahm1.download_media(
                    await shahm1.get_messages(Config.abbas_A, ids=plugin_to_install),
                    "shahm/plugins/",
                )
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                flag = True
                check = 0
                while flag:
                    try:
                        lload_module(shortname.replace(".py", ""))
                        plgnm += 1
                        break
                    except ModuleNotFoundError as e:
                        install_pip(e.name)
                        check += 1
                        if check > 5:
                            break
        print(inst_done)
        addgvar("PMLOG", h_type)
        if gvarstatus("GRPLOOG") is not None:
            addgvar("GRPLOG", h_type)

    shahm1.loop.create_task(install())
