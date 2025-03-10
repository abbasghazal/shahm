# by: t.me/Dar4k  ~ t.me/R0R77
# ported to shahm
import random

import requests
import telethon
from telethon.sync import functions
from user_agent import generate_user_agent

from shahm import shahm

a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopassdfghjklzxcvbnm1234567890"

trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "ثلاثي":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)

    elif choice == "خماسي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي حرفين":
        c = random.choices(a)
        d = random.choices(e)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي":
        c = d = random.choices(a)
        d = random.choices(e)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سداسي حرفين":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعي":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "بوتات":
        c = random.choices(a)
        d = random.choices(e)
        s = random.choices(e)
        f = [c[0], s[0], d[0]]
        username = "".join(f)
        username = username + "bot"

    elif choice == "تيست":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], d[0], d[0], c[0], c[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        raise ValueError("Invalid choice for username generation.")
    return username


abbasChecler_cmd = (
    "𓆩 [𝗦𝗼𝘂𝗿𝗰𝗲 𝑺𝑯𝑨𝑯𝑴 - اوامـر الصيـد والتشيكـر](t.me/shahm50) 𓆪\n\n"
    "**✾╎قـائمـة اوامـر تشيكـر صيـد معـرفات تيليجـرام :** \n\n"
    "**- النـوع :**\n"
    "**(** `سداسي حرفين`/`ثلاثي`/`سداسي`/`بوتات`/`خماسي حرفين`/`خماسي`/`سباعي` **)**\n\n"
    "`.صيد` + النـوع\n"
    "**⪼ لـ صيـد يـوزرات عشوائيـه على حسب النـوع**\n\n"
    "`.تثبيت` + اليوزر\n"
    "**⪼ لـ تثبيت اليـوزر بقنـاة معينـه اذا اصبح متاحـاً يتم اخـذه**\n\n"
    "`.حالة الصيد`\n"
    "**⪼ لـ معرفـة حالـة تقـدم عمليـة الصيـد**\n\n"
    "`.حالة التثبيت`\n"
    "**⪼ لـ معرفـة حالـة تقـدم التثبيت التلقـائـي**\n\n"
    "`.ايقاف الصيد`\n"
    "**⪼ لـ إيقـاف عمليـة الصيـد الجاريـه**\n\n"
    "`.ايقاف التثبيت`\n"
    "**⪼ لـ إيقـاف عمليـة التثبيت التلقـائـي**\n\n"
)


@shahm.rep_cmd(pattern="الصيد")
async def cmd(abbas):
    await edit_or_reply(abbas, abbasChecler_cmd)


@shahm.rep_cmd(pattern="صيد (.*)")
async def hunterusername(event):
    choice = str(event.pattern_match.group(1))
    await event.edit(f"**⎉╎تم بـدء الصيـد .. بنجـاح ☑️**\n**⎉╎لمعرفـة حالة تقـدم عمليـة الصيـد ارسـل (**`.حالة الصيد`**)**")

    try:
        ch = await shahm(
            functions.channels.CreateChannelRequest(
                title="⎉ صيـد شـهــم 𝑺𝑯𝑨𝑯𝑴 ⎉",
                about="This channel to hunt username by - @shahm50",
            )
        )
        ch = ch.updates[1].channel_id
    except Exception as e:
        await shahm.send_message(
            event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
        )
        sedmod = False

    isclaim.clear()
    isclaim.append("on")
    sedmod = True
    while sedmod:
        username = gen_user(choice)
        if username == "error":
            await event.edit("**- يـرجى وضـع النـوع بشكـل صحيـح ...!!**")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await shahm(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    "ᯓ 𝑺𝑯𝑨𝑯𝑴 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - صيـد شـهــم 💡\n**•────────────────────•**\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Channel ❳\n**•────────────────────•**\n- By ❲ @shahm50 ❳ ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_message(
                    ch,
                    "ᯓ 𝑺𝑯𝑨𝑯𝑴 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - صيـد شـهــم 💡\n**•────────────────────•**\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Type: {}\n- Save: ❲ Channel ❳\n**•────────────────────•**\n- By ❲ @shahm50 ❳ ".format(
                        username, trys, choice
                    ),
                )
                await event.client.send_message(
                    "@shahm41", f"- Done : @{username} !\n- By : @shahm50"
                )
                sedmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await shahm.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                sedmod = False
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                if "USERNAME_PURCHASE_AVAILABLE" in str(eee):
                    pass
                else:
                    await shahm.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    sedmod = False
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")


@shahm.rep_cmd(pattern="تثبيت (.*)")
async def _(event):
    msg = event.text.split()
    try:
        ch = str(msg[2])
        ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء التثبيت في**-  @{ch} .**")
    except:
        try:
            ch = await shahm(
                functions.channels.CreateChannelRequest(
                    title="⎉ تثبيت شـهــم 𝑺𝑯𝑨𝑯𝑴 ⎉",
                    about="This channel to hunt username by - @shahm50",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم بـدء التثبيت .. بنجـاح ☑️**")
        except Exception as e:
            await shahm.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ : {str(e)}"
            )
    isauto.clear()
    isauto.append("on")
    username = str(msg[1])

    swapmod = True
    while swapmod:
        isav = check_user(username)
        if isav == True:
            try:
                await shahm(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    ch,
                    "ᯓ 𝑺𝑯𝑨𝑯𝑴 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - صيـد شـهــم 💡\n**•────────────────────•**\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Channel ❳\n**•────────────────────•**\n- By ❲ @shahm50 ❳ ".format(
                        username, trys2
                    ),
                )
                await event.client.send_message(
                    event.chat_id,
                    "ᯓ 𝑺𝑯𝑨𝑯𝑴 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 - صيـد شـهــم 💡\n**•────────────────────•**\n- UserName: ❲ @{} ❳\n- ClickS: ❲ {} ❳\n- Save: ❲ Channel ❳\n**•────────────────────•**\n- By ❲ @shahm50 ❳ ".format(
                        username, trys2
                    ),
                )
                await event.client.send_message(
                    "@shahm41",
                    f"- Done : @{username} !\n- By : @shahm50 !\n- Hunting Log {trys2}",
                )
                swapmod = False
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(
                    event.chat_id, f"**المعرف @{username} غير صالح ؟!**"
                )
                swapmod = False
                break
            except telethon.errors.FloodError as e:
                await shahm.send_message(
                    event.chat_id, f"للاسف تبندت , مدة الباند ({e.seconds}) ثانية ."
                )
                swapmod = False
                break
            except Exception as eee:
                await shahm.send_message(
                    event.chat_id,
                    f"""خطأ مع {username} , الخطأ :{str(eee)}""",
                )
                swapmod = False
                break
        else:
            pass
        trys2[0] += 1

    isclaim.clear()
    isclaim.append("off")


@shahm.rep_cmd(pattern="حالة الصيد")
async def _(event):
    if "on" in isclaim:
        await event.edit(f"**- الصيد وصل لـ({trys[0]}) من المحـاولات**")
    elif "off" in isclaim:
        await event.edit("**- لا توجد عمليـة صيد جاريـه حاليـاً ؟!**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@shahm.rep_cmd(pattern="حالة التثبيت")
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")


@shahm.rep_cmd(pattern="حاله الصيد")
async def _(event):
    if "on" in isclaim:
        await event.edit(f"**- الصيد وصل لـ({trys[0]}) من المحـاولات**")
    elif "off" in isclaim:
        await event.edit("**- لا توجد عمليـة صيد جاريـه حاليـاً ؟!**")
    else:
        await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@shahm.rep_cmd(pattern="حاله التثبيت")
async def _(event):
    if "on" in isauto:
        await event.edit(f"**- التثبيت وصل لـ({trys2[0]}) من المحاولات**")
    elif "off" in isauto:
        await event.edit("**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        await event.edit("-لقد حدث خطأ ما وتوقف الامر لديك")


@shahm.rep_cmd(pattern="ايقاف الصيد")
async def _(event):
    if "on" in isclaim:
        isclaim.clear()
        isclaim.append("off")
        return await event.edit("**- تم إيقـاف عمليـة الصيـد .. بنجـاح ✓**")
    elif "off" in isclaim:
        return await event.edit("**- لا توجد عمليـة صيد جاريـه حاليـاً ؟!**")
    else:
        return await event.edit("**- لقد حدث خطأ ما وتوقف الامر لديك**")


@shahm.rep_cmd(pattern="ايقاف التثبيت")
async def _(event):
    if "on" in isauto:
        isauto.clear()
        isauto.append("off")
        return await event.edit("**- تم إيقـاف عمليـة التثبيت .. بنجـاح ✓**")
    elif "off" in isauto:
        return await event.edit("**- لا توجد عمليـة تثبيث جاريـه حاليـاً ؟!**")
    else:
        return await event.edit("**-لقد حدث خطأ ما وتوقف الامر لديك**")
