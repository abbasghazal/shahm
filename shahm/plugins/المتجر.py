"""Fetch App Details from Playstore.
.app <app_name> to fetch app details.
.appr <app_name>  to fetch app details with Xpl0iter request link.
  ©REP™ - @shahm41 """

import bs4
import requests

from . import ALIVE_NAME, shahm1, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "shahm"

plugin_category = "البحث"


@shahm1.rep_cmd(
    pattern="app ([\s\S]*)",
    command=("app", plugin_category),
    info={
        "header": "To search any app in playstore",
        "الاستـخـدام": "{tr}app <name>",
    },
)
async def apk(event):
    app_name = event.pattern_match.group(1)
    event = await edit_or_reply(event, "**⌔╎جـارِ البحث ؏ـن التطبيق ⇱...**")
    try:
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += "<b>𓆰 " + app_name + " 𓆪</b>"
        app_details += (
            "\n\n<code>⌔╎المطور :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>⌔╎تقييم التطبيق :</code> " + app_rating.replace(
            "صـنفت ", "⭐ "
        ).replace(" out of ", "/").replace(" الـنجوم", "", 1).replace(
            " الـنجوم", "⭐ "
        ).replace(
            "خـمس", "5"
        )
        app_details += (
            "\n<code>⌔╎للتفاصيـل :</code> <a href='"
            + app_link
            + "'>لتحميلها من سوق بلي</a>"
        )
        app_details += f"\n\n    𓍹 {Name} 𓍻"
        await event.edit(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await event.edit("** لم يتم العثور على نتائج البحث يرجى وضع اسم تطبيق متوفر ❕**")
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))


@shahm1.rep_cmd(
    pattern="متجر ([\s\S]*)",
    command=("متجر", plugin_category),
    info={
        "header": "لـ البحـث عـن التطبيقـات على جـوجـل بـلاي وجـلب رابـط تحميـل مباشــر",
        "الاستـخـدام": "{tr}متجر <اسم التطبيق>",
    },
)
async def apkr(event):
    app_name = event.pattern_match.group(1)
    event = await edit_or_reply(event, "**╮ جـارِي البحـث ؏ــن التـطبيـٓق... 📲╰**")
    try:
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>⌔╎المطور :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>⌔╎تقييم التطبيق :</code> " + app_rating.replace(
            "التصنيف ", "⭐ "
        ).replace(" out of ", "/").replace(" النجوم", "", 1).replace(
            " النجوم", "⭐ "
        ).replace(
            "خمس", "5"
        )
        app_details += (
            "\n<code>⌔╎للتفاصيـل :</code> <a href='"
            + app_link
            + "'>رابـط التطبيـق ع جوجل بـلاي</a>"
        )
        app_details += "\n\n<b>زلــزال الهيبــه : </b> <a href='https://t.me/shahm41'>لــ الاستفسـار</a>"
        app_details += "\n\n===> 𝙕𝙚𝙙𝙏𝙝𝙤𝙣 - @shahm2 ® <==="
        await event.edit(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await event.edit("**عـذراً .. لا يـوجد نتائـج اكتـب الاسـم الصحيـح للتطبيـق وعـاود البحث مـرة اخـرى**")
    except Exception as err:
        await event.edit("Exception Occured:- " + str(err))


#𝑺𝑯𝑨𝑯𝑴 ®
# الملـف حقـوق روجـــــــر - بـاقـر ⤶ @shahm41 خاص بسـورس ⤶ 𝑺𝑯𝑨𝑯𝑴
# الملف متعوب عليه So تخمط وماتذكـر المصـدر == اهينـك

@shahm1.rep_cmd(
    pattern="تطبيق ([\s\S]*)",
    command=("تطبيق", plugin_category),
    info={
        "header": "To search any app in playstore",
        "الاستـخـدام": "{tr}تطبيق + اسم",
    },
)
async def zed(event):
    if event.fwd_from:
        return
    zedr = event.pattern_match.group(1)
    shahm = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(shahm, zedr)
    await tap[0].click(event.chat_id)
    await event.delete()


@shahm1.rep_cmd(
    pattern="فلم ([\s\S]*)",
    command=("فلم", plugin_category),
    info={
        "header": "لـ البحـث عـن الافـلام",
        "الاستـخـدام": "{tr}فلم + اسم",
    },
)
async def zed(event):
    if event.fwd_from:
        return
    zedr = event.pattern_match.group(1)
    shahm = "@TGFilmBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(shahm, zedr)
    await tap[0].click(event.chat_id)
    await event.delete()
