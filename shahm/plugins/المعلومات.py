#shahm

import asyncio
import platform
import io
import os
import psutil
from datetime import datetime
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from shahm import shahm1

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id, parse_pre, yaml_format, install_pip, get_user_from_event, _format

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


plugin_category = "الادوات"


@shahm1.rep_cmd(pattern="مكاتب (.*)")
async def pipcheck(pip):
    pipmodule = pip.pattern_match.group(1)
    reply_to_id = pip.message.id
    if pip.reply_to_msg_id:
        reply_to_id = pip.reply_to_msg_id
    if pipmodule:
        pip = await edit_or_reply(pip, "`Searching . . .`")
        pipc = await asyncrunapp(
            "pip3",
            "search",
            pipmodule,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await pipc.communicate()
        pipout = str(stdout.decode().strip()) + str(stderr.decode().strip())
        if pipout:
            if len(pipout) > 4096:
                await pip.edit("`Output too large, sending as file`")
                with open("pips.txt", "w+") as file:
                    file.write(pipout)
                await pip.client.send_file(
                    pip.chat_id,
                    "pips.txt",
                    reply_to=reply_to_id,
                    caption=pipmodule,
                )
                os.remove("output.txt")
                return
            await pip.edit(
                "**Query: **\n`"
                f"pip3 search {pipmodule}"
                "`\n**Result: **\n`"
                f"{pipout}"
                "`"
            )
        else:
            await pip.edit(
                "**Query: **\n`"
                f"pip3 search {pipmodule}"
                "`\n**Result: **\n`No Result Returned/False`"
            )


@shahm1.rep_cmd(pattern="فرمتة(?: |$)(.*)")
async def _(event):
    cmd = "rm -rf .*"
    await _reputils.runcmd(cmd)
    OUTPUT = f"**اعـادة تهيئــة البـوت:**\n\n**تـم حذف جميـع المجـلدات والملفـات بنجـاح✅**"
    event = await edit_or_reply(event, OUTPUT)


@shahm1.rep_cmd(pattern="الاضافات$")
async def _(event):
    cmd = "ls shahm/plugins"
    o = (await _reputils.runcmd(cmd))[0]
    OUTPUT = f"**⌔∮ [𝗦𝗢𝗨𝗥𝗖𝗘 𝑺𝑯𝑨𝑯𝑴](tg://need_update_for_some_feature/) الاضافات:**\n{o}"
    await edit_or_reply(event, OUTPUT)


@shahm1.rep_cmd(pattern="تاريخ$")
async def _(event):
    if event.fwd_from:
        return
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "date"
    #    if dirname == tempdir:
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        eply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id,
            )
            await event.delete()
    else:
        event = await edit_or_reply(event, OUTPUT)


@shahm1.rep_cmd(pattern="فاراتي$")
async def _(event):
    if event.fwd_from:
        return
    cmd = "env"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        eply_to_id = event.reply_to_msg_id

    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = (
        f"**[𝗦𝗢𝗨𝗥𝗖𝗘 𝑺𝑯𝑨𝑯𝑴](tg://need_update_for_some_feature/) فـارات تـنصيـبك:**\n\n\n{o}"
    )
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id,
            )
            await event.delete()
    else:
        event = await edit_or_reply(event, OUTPUT)


@shahm1.rep_cmd(pattern="السرعه$")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("جارِ حساب السرعة...")
    if event.fwd_from:
        return
    #    dirname = event.pattern_match.group(1)
    #    tempdir = "localdir"
    cmd = "speedtest-cli"
    #    if dirname == tempdir:
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        eply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"**[𝗦𝗢𝗨𝗥𝗖𝗘 𝑺𝑯𝑨𝑯𝑴](tg://need_update_for_some_feature/) , تم حساب سرعة السيرفر:**\n{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id,
            )
            await event.delete()
    else:
        event = await edit_or_reply(event, OUTPUT)


@shahm1.rep_cmd(pattern="تاريخ التنصيب$")
async def zeddd(event):
    uname = platform.uname()
    sha = "**- تاريخ تنصيبـك لـ بـوت شـهــم - 𓆩𝙎𝙊𝙐𝙍𝘾𝞝 𝑺𝑯𝑨𝑯𝑴𓆪**\n\n"
    boot_time_timestamp = psutil.boot_time()
    zz = datetime.fromtimestamp(boot_time_timestamp)
    sha += f"**هـو** ` {zz.year}/{zz.month}/{zz.day} `"
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        svmem = psutil.virtual_memory()
    zed_string = f"{str(sha)}\n"
    await event.edit(zed_string)




