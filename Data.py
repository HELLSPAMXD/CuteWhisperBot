from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}

I am the Master of Whisperers (like Varys in Game of Thrones).

You can use me to send whispers to your friend in groups and channels (even if I'm not there).
Only that friend and you will be able to read the message even though others are in same group. 

To see how to use me press 'How to Use' below.

By @StarkBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ channel ♥", url="https://t.me/WAJAH_U_HO")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/ACTIVE_24X7_CHATS")],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

@CUTEWHISPERRBOT your_message friend_username/id`
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @I_LOVE_Y0U_MY_HEARTBEET

Source Code : [Click Here](https://t.me/ACTIVE_24X7_CHATS)

Inspired By : nnbbot

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @I_LOVE_Y0U_MY_HEARTBEET
    """
