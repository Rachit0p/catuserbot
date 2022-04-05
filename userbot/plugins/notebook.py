# \\ Created by-@Jisan7509 -- Github.com/Jisan09 //
#  \\   https://github.com/TgCatUB/catuserbot   //
#   \\       Plugin for @catuserbot            // 
#    ```````````````````````````````````````````

import os
import urllib

from . import BOTLOG, BOTLOG_CHATID, catub, reply_id
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import deEmojify,higlighted_text
from ..sql_helper.globals import addgvar, gvarstatus
from telethon.tl.functions.users import GetFullUserRequest


plugin_category = "tools"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pages = {
    "Note Book":"note",
    "Raugh Book":"rough",
    "Spiral Book":"spiral",
    "White Book":"white",
    "Notepad":"notepad",
    "A4 Page":"a4",
}
 
Fonts = ["BrownBag","Caveat","HomemadeApple","JottFLF","LiuJian","WriteSong"]

Colors = ['black', 'brown', 'crimson', 'darkblue', 'darkcyan', 'darkgreen', 'darkmagenta', 'darkred', 'darkslateblue', 'darkslategray', 'darkviolet', 'indigo', 'magenta', 'maroon', 'mediumblue', 'midnightblue', 'navy', 'orangered', 'purple', 'red', 'teal']
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def notebook_values(page,font):
    if page == "a4":
        position=(75, 10)
        lines = 28
        if font == "BrownBag":
            text_wrap=1.1
            font_size=55
            linespace="-64"
            lines = 26
        elif font == "HomemadeApple":
            text_wrap=1.1
            font_size=30
            linespace="-64"
            lines = 26
        elif font == "JottFLF":
            text_wrap=0.9
            font_size=40
            linespace="-38"
        elif font == "LiuJian":
            text_wrap=0.7
            font_size=30
            linespace="-35"
        elif font == "WriteSong":
            text_wrap=0.5
            font_size=30
            linespace="-15"
        elif font == "Caveat":
            text_wrap=0.666
            font_size=35
            linespace="-35"
    elif page == "spiral":
        position=(130, 10)
        lines = 26
        if font == "BrownBag":
            text_wrap=1.1
            font_size=55
            linespace="-64"
        elif font == "HomemadeApple":
            text_wrap=1.1
            font_size=30
            linespace="-64"
        elif font == "JottFLF":
            text_wrap=0.9
            font_size=40
            linespace="-38"
            lines = 28
        elif font == "LiuJian":
            text_wrap=0.7
            font_size=30
            linespace="-35"
            lines = 30
        elif font == "WriteSong":
            text_wrap=0.5
            font_size=30
            linespace="-15"
        elif font == "Caveat":
            text_wrap=0.666
            font_size=35
            linespace="-35"
            lines = 28
    elif page == "white":
        position=(130, 35)
        if font == "BrownBag":
            text_wrap=1.1
            font_size=50
            linespace="-57"
            lines = 26
        elif font == "HomemadeApple":
            text_wrap=1.1
            font_size=28
            linespace="-60"
            lines = 28
        elif font == "JottFLF":
            text_wrap=0.9
            font_size=35
            linespace="-30"
        elif font == "LiuJian":
            text_wrap=0.7
            font_size=30
            linespace="-35"
            lines = 30
        elif font == "WriteSong":
            text_wrap=0.6
            font_size=30
            linespace="-20"
            lines = 30
        elif font == "Caveat":
            text_wrap=0.75
            font_size=35
            linespace="-35"
            lines = 27
    elif page == "notepad":
        position=(80, 100)
        lines = 25
        if font == "BrownBag":
            text_wrap=1
            font_size=50
            linespace="-57"
        elif font == "HomemadeApple":
            text_wrap=0.9
            font_size=28
            linespace="-60"
        elif font == "JottFLF":
            text_wrap=0.8
            font_size=35
            linespace="-30"
        elif font == "LiuJian":
            text_wrap=0.666
            font_size=30
            linespace="-35"
        elif font == "WriteSong":
            text_wrap=0.6
            font_size=30
            linespace="-23"
            lines = 30
        elif font == "Caveat":
            text_wrap=0.666
            font_size=35
            linespace="-35"
            lines = 24
    elif page == "note":
        position=(80, 123)
        lines = 22
        if font == "BrownBag":
            text_wrap=1
            font_size=50
            linespace="-54"
            position=(80, 100)
        elif font == "HomemadeApple":
            text_wrap=0.9
            font_size=28
            linespace="-57"
            position=(80, 115)
        elif font == "JottFLF":
            text_wrap=0.8
            font_size=36
            linespace="-30"
        elif font == "LiuJian":
            text_wrap=0.666
            font_size=30
            linespace="-33"
        elif font == "WriteSong":
            text_wrap=0.6
            font_size=30
            linespace="-14"
        elif font == "Caveat":
            text_wrap=0.6
            font_size=35
            linespace="-33"
            position=(80, 115)
    elif page == "rough":
        position=(120, 55)
        lines = 25
        if font == "BrownBag":
            text_wrap=0.9
            font_size=50
            linespace="-56"
        elif font == "HomemadeApple":
            text_wrap=0.9
            font_size=27
            linespace="-55"
        elif font == "JottFLF":
            text_wrap=0.65
            font_size=36
            linespace="-31"
            position=(120, 60)
        elif font == "LiuJian":
            text_wrap=0.6
            font_size=30
            linespace="-31"
            position=(120, 65)
        elif font == "WriteSong":
            text_wrap=0.45
            font_size=30
            linespace="-16"
            position=(120, 65)
        elif font == "Caveat":
            text_wrap=0.6
            font_size=35
            linespace="-35"
            position=(120, 60)
    return lines,text_wrap,font_size,linespace,position
    

@catub.cat_cmd(
    pattern="(write|notebook)(?:\s|$)([\s\S]*)",
    command=("write", plugin_category),
    info={
        "header": "To write down your text in notebook.",
        "description": "Give text to it or reply to msg, it will write that in notebook.",
        "usage": "{tr}write <Reply/Text>",
    },
)
async def write_page(event):
    """Write down your text in notebook."""
    cmd = event.pattern_match.group(1)
    font = gvarstatus("NOTEBOOK_FONT") or "Caveat"
    page = gvarstatus("NOTEBOOK_PAGE") or "spiral"
    log = gvarstatus("NOTEBOOK_LOG") or "Off"
    foreground = gvarstatus("NOTEBOOK_PEN_COLOR") or "black"
    if cmd == "write":
        text = event.pattern_match.group(2)
        rtext = await event.get_reply_message()
        if not text and rtext:
            text = rtext.message
        if not text:
            return await edit_delete(event, "**ಠ∀ಠ Gimmi text to write**")
        cap = "**🖋️ Written Using :-** [CatUserbot](https://t.me/catuserbot_support)"
        pass
    if cmd == "notebook":
        text = ((await catub(GetFullUserRequest(catub.uid))).full_user).about or "This is just a Sample text\n              -by Catuserbot"
        cap = f"**NoteBook Configs :-**\n\n**Font:** `{font}`\n**Page:** `{list(Pages.keys())[list(Pages.values()).index(page)]}`\n**Color:** `{foreground.title()}`\n**Log:**  `{log}`"
        pass
    reply_to_id = await reply_id(event)
    text = deEmojify(text)
    catevent = await edit_or_reply(event, "**Processing....**")
    temp_name = "./temp/nbpage.jpg"
    font_name = "./temp/nbfont.ttf"
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    if not os.path.exists(temp_name):
        urllib.request.urlretrieve(f"https://github.com/TgCatUB/CatUserbot-Resources/raw/master/Resources/Notebook/Images/{page}.jpg", temp_name)
    if not os.path.exists(font_name):
        urllib.request.urlretrieve(f"https://github.com/TgCatUB/CatUserbot-Resources/blob/master/Resources/Notebook/Fonts/{font}.ttf?raw=true", font_name)
    lines,text_wrap,font_size,linespace,position = notebook_values(page,font)
    image = higlighted_text(
        temp_name,
        text,
        text_wrap=text_wrap,
        font_name=font_name,
        font_size=font_size,
        linespace=linespace,
        position=position,
        foreground=foreground,
        lines = lines,
        align="left",
        transparency=0,
        album = True)
    await event.client.send_file(event.chat_id, image, caption=cap, reply_to=reply_to_id)
    await catevent.delete()
    if log == "On" and cmd != "notebook" and BOTLOG_CHATID != event.chat_id:
        await event.client.send_file(BOTLOG_CHATID, image, caption=f"#NOTE_BOOK\n\n{cap}")
    for i in image:
        os.remove(i)


@catub.cat_cmd(
    pattern="notebook$",
    command=("notebook", plugin_category),
    info={
        "header": "To show your notebook configs.",
        "description": "Shows current notebook configs like font, color, page...",
        "usage": "{tr}notebook",
    },
)
async def notebook(event):
    """Shows your notebook configs."""



@catub.cat_cmd(
    pattern="nb(page|font|pen|log)(?:\s|$)([\s\S]*)",
    command=("nb", plugin_category),
    info={
        "header": "Change configuration of notebook",
        "description": "Customise Notebook font, page, pen color, log .... to full list of avilable options you have to use the cmd without input.",
        "flags": {
            "font": "To change font for notebook",
            "page": "To change page for notebook",
            "pen": "To change color of text for notebook",
            "log": "Save your notes in your botlogger.",
        },
        "usage": [
            "{tr}nbfont <font name>",
            "{tr}nbpage <page name>",
            "{tr}nbpen <font color>",
            "{tr}nblog <On/Off>",
        ],
        "examples": [
            "{tr}nbfont BrownBag",
            "{tr}nbpage Note Book",
            "{tr}nbpen darkblue",
            "{tr}nblog On",
        ],
    },
)
async def notebook_conf(event):
    """Change settings for notebook"""
    cmd = event.pattern_match.group(1).lower()
    input_str = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if cmd == "page":
        cap = "**Available Notebook Pages are here:-**\n\n"  
        for i, each in enumerate(Pages.keys(), start=1):
            cap += f"**{i}.**  `{each}`\n"
        if input_str and input_str in Pages.keys():
            addgvar("NOTEBOOK_PAGE", Pages[input_str])
            if os.path.exists("temp/nbpage.jpg"):
                os.remove("temp/nbpage.jpg")
            return await edit_delete(event,f"**Notebook page successfully changed to : **`{input_str}`",20)
        temp_page = "Pages"
        pass
    elif cmd == "font":
        cap = "**Available Notebook Fonts are here:-**\n\n"  
        for i, each in enumerate(Fonts, start=1):
            cap += f"**{i}.**  `{each}`\n"
        if input_str and input_str in Fonts:
            addgvar("NOTEBOOK_FONT",input_str)
            if os.path.exists("temp/nbfont.ttf"):
                os.remove("temp/nbfont.ttf")
            return await edit_delete(event,f"**Notebook font successfully changed to : **`{input_str}`",20)
        temp_page = "Fonts"
        pass
    elif cmd == "pen":
        cap = "**Available Pen Color are here:-**\n\n"  
        for i, each in enumerate(Colors, start=1):
            cap += f"**{i}.**  `{each}`\n"
        if input_str and input_str in Colors:
            addgvar("NOTEBOOK_PEN_COLOR",input_str) 
            if os.path.exists("temp/nbfont.ttf"):
                os.remove("temp/nbfont.ttf")
            return await edit_delete(event,f"**Notebook pen color Successfully changed to : **`{input_str}`",20)
        temp_page = "Colors"
        pass
    elif cmd == "log":
        if not BOTLOG:
            return await edit_delete(event,"You need to set `PRIVATE_GROUP_BOT_API_ID` in your config.",20)
        cap = "**Available log option are:-**\n\n1. `On`\n2. `Off`"  
        if input_str and input_str in ["On","Off"]:
            addgvar("NOTEBOOK_LOG",input_str)
            return await edit_delete(event,f"**Notebook pen color Successfully changed to : **`{input_str}`",50)
        return await edit_delete(event,cap)
    await event.delete()
    file = f"{temp_page}.jpg"
    urllib.request.urlretrieve(f"https://github.com/TgCatUB/CatUserbot-Resources/raw/master/Resources/Notebook/Images/{temp_page}.jpg",file)
    await event.client.send_file(event.chat_id,file,caption=cap,reply_to=reply_to_id)
    os.remove(file)