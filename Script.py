class script(object):
    START_TXT = """<b>๐๐ฆ๐ญ๐ญ๐ฐ๐ธ {} ๐๐บ ๐๐ข๐ฎ๐ฆ ๐๐ด <a href=https://t.me/{}>{}</a> </b>

<b>๐ ๐๐ฉ๐ฆ๐ณ๐ฆ ๐๐ด ๐๐ฐ๐ต๐ฉ๐ช๐ฏ๐จ ๐ ๐ฐ๐ถ ๐๐ฆ๐ฆ๐ฅ ๐๐ฆ๐ณ๐ฆ ๐๐ช๐ต๐ฉ๐ฐ๐ถ๐ต ๐๐ข๐ด๐ต๐ช๐ฏ๐จ ๐๐ช๐ฎ๐ฆ..!!

๐ ๐๐ฉ๐ข๐ต'๐ด ๐๐ญ๐ญ ๐๐ข๐ฏ ๐ ๐๐ช๐ญ๐ญ ๐๐ณ๐ฐ๐ท๐ช๐ฅ๐ฆ ๐๐ฐ๐ท๐ช๐ฆ๐ด ๐๐ฏ ๐๐

โจ ๐๐๐ข๐ง๐ญ๐๐ข๐ง๐๐ ๐๐ฒ :  <a href='https://t.me/mhd_thanzeer'>๐๐๐ฟ ๐๐๐ผ๐๐๐๐๐</a> </b>"""
    HELP_TXT = """แผEY {} โ๐๐ฃ๐ ๐๐๐ โ๐๐๐ก ๐ฝ๐ ๐ฃ ๐๐ช โ๐ ๐๐๐๐๐๐ค โจ๏ธ
"""
    ABOUT_TXT = """<b>๐ผ My Name : <a href=https://t.me/{}>{}</a>

๐ตโโ Developer : <a href='https://t.me/mhd_thanzeer'>๐๐๐ฟ ๐๐๐ผ๐๐๐๐๐</a>

๐ Library : ๐ฟ๏ธ๐๏ธ๐พ๏ธ๐ถ๏ธ๐๏ธ๐ฐ๏ธ๐ผ๏ธ

๐ฅ Language : ๐ฟ๏ธ๐๏ธ๐๏ธ๐ท๏ธ๐พ๏ธ๐ฝ๏ธ  แดษดแด  ๐ฒ๏ธ

๐ช Data Base : ๐ผ๏ธ๐พ๏ธ๐ฝ๏ธ๐ถ๏ธ๐พ๏ธ  ๐ณ๏ธ๐ฑ๏ธ

๐ Bot Group : @wolfpackmedia </b>"""
    SOURCE_TXT = """<b>NOTE:</b>
๐<b><i>เดเดจเตเดคเดพเดเดพ เดฎเตเดจเต เดจเตเดเตเดเตเดจเตเดจเต เดจเดฟเดจเดเตเดเต เดเดตเดถเตเดฏเดฎเดพเดฏเดฟเดเตเดเตเดณเตเดณเดคเต เดเดตเดฟเดเต เดเดฒเตเดฒ ๐
</i></b>

<b>๐ตโโ Developer : <a href='https://t.me/mhd_thanzeer'>๐ผ๏ธ๐ท๏ธ๐ณ๏ธ  ๐๏ธ๐ท๏ธ๐ฐ๏ธ๐ฝ๏ธ๐๏ธ๐ด๏ธ๐ด๏ธ๐๏ธ</a> </b>
"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>โ ๐๐ฐ๐ต๐ข๐ญ ๐๐ช๐ญ๐ฆ๐ด :</b> <code>{}</code>
<b>โ ๐๐ฐ๐ต๐ข๐ญ ๐๐ด๐ฆ๐ณ๐ด :</b> <code>{}</code>
<b>โ ๐๐ฐ๐ต๐ข๐ญ ๐๐ฉ๐ข๐ต๐ด :</b> <code>{}</code>
<b>โ ๐๐ด๐ฆ๐ฅ ๐๐ต๐ฐ๐ณ๐ข๐จ๐ฆ :</b> <code>{}</code> ๐ผ๐๐ฑ
<b>โ ๐๐ณ๐ฆ๐ฆ ๐๐ต๐ฐ๐ณ๐ข๐จ๐ฆ :<b> <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

