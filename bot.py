import asyncio
import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

# .env ഫയലിലെ വേരിയബിളുകൾ ലോഡ് ചെയ്യുന്നു
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

app = Client(
    "my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
)


# 1. /start കമാൻഡ്
@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
  user_name = message.from_user.first_name
  welcome_text = (
      f"Hi 🛩️™**{user_name}**! I am one "
      "and only ALLU OTT Downloader Bot on Telegram.\n\n"
      "I can help you to download content "
      "from OTT Platforms\n\n"
      "You can use me to Download **DRM "
      "protected links** to **Telegram, Google "
      "Drive & GoFile**\n\n"
      "Here I support a vast number of otts "
      "from where you can download Drm or "
      "non-drm videos easily..\n\n"
      "**If You Found Any Issue Contact "
      "Support**"
  )
  keyboard = InlineKeyboardMarkup([
      [
          InlineKeyboardButton(
              "Updates Channel ↗️", url="https://t.me/AlluTvSerials"
          ),
          InlineKeyboardButton("Support ↗️", url="https://t.me/Anujith1238"),
      ],
      [
          InlineKeyboardButton("About", callback_data="about"),
          InlineKeyboardButton("Help", callback_data="help"),
          InlineKeyboardButton("Contact Us", callback_data="contact"),
      ],
      [
          InlineKeyboardButton("Usage", callback_data="usage"),
          InlineKeyboardButton("Plans", callback_data="plans"),
      ],
  ])
  await message.reply_text(
      text=welcome_text, reply_markup=keyboard, disable_web_page_preview=True
  )


# 2. /plans കമാൻഡ്
@app.on_message(filters.command("plans"))
async def plans_command(client: Client, message: Message):
  photo_url = "[YOUR_PLANS_IMAGE_URL]"
  plans_text = (
      "🚧 **Limited Time Plans** 🚧\n\n"
      "• **Plan validity cannot exceed 180 days.**\n\n"
      "⚠️ **Term and Conditions** ⚠️\n\n"
      "• **Payments are non-refundable, and we do not provide refunds.**\n"
      "• **If the service ceases to function, no compensation is provided.**\n\n"
      "🚀 Need Help / Subscription? DM: @Anujith1238\n"
      "💡 Use `/plans` to view plan details anytime."
  )
  keyboard = InlineKeyboardMarkup([
      [
          InlineKeyboardButton(
              "Updates Channel ↗️", url="https://t.me/AlluTvSerials"
          ),
          InlineKeyboardButton("Support ↗️", url="https://t.me/Anujith1238"),
      ],
      [
          InlineKeyboardButton("About", callback_data="about"),
          InlineKeyboardButton("Help", callback_data="help"),
          InlineKeyboardButton("Contact Us", callback_data="contact"),
      ],
  ])
  try:
    await message.reply_photo(
        photo=photo_url, caption=plans_text, reply_markup=keyboard
    )
  except Exception:
    await message.reply_text(
        text=plans_text, reply_markup=keyboard, disable_web_page_preview=True
    )


# 3. /myplan കമാൻഡ്
@app.on_message(filters.command("myplan"))
async def myplan_command(client: Client, message: Message):
  has_subscription = False

  if has_subscription:
    photo_url = "[YOUR_ACTIVE_PLAN_IMAGE_URL]"
    plan_details_text = (
        "✅ **Your Active Plan:**\n\n"
        "• **Plan:** 28 Days (Super Plan)\n"
        "• **Validity Remaining:** 20 Days\n"
        "• **Access:** All OTTs (43 Platforms)\n\n"
        "💡 Thank you for subscribing!"
    )
    await message.reply_photo(photo=photo_url, caption=plan_details_text)
  else:
    no_sub_text = (
        "No Subscription found...\n\ncheck `/plans` to get your subscription"
        " now..."
    )
    await message.reply_text(text=no_sub_text)


# 4. /broadcast കമാൻഡ്
@app.on_message(filters.command("broadcast") & filters.user(ADMIN_ID))
async def broadcast_command(client: Client, message: Message):
  if not message.reply_to_message:
    await message.reply_text(
        "⚠️ ദയവായി ഏത് മെസ്സേജ് ആണോ ബ്രോഡ്കാസ്റ്റ് ചെയ്യേണ്ടത്, ആ മെസ്സേജിന്"
        " മറുപടിയായി (Reply) `/broadcast` എന്ന് നൽകുക."
    )
    return

  broadcast_msg = message.reply_to_message
  sent_count = 0
  failed_count = 0

  status_msg = await message.reply_text(
      "📢 Broadcast ആരംഭിക്കുന്നു... ദയവായി കാത്തിരിക്കുക."
  )
  users_list = []

  for user_id in users_list:
    try:
      await broadcast_msg.copy(chat_id=user_id)
      sent_count += 1
    except Exception:
      failed_count += 1

  await status_msg.edit_text(
      f"✅ **Broadcast പൂർത്തിയായി!**\n\n• വിജയിച്ചത്: {sent_count}\n• പരാജയപ്പെട്ടത്:"
      f" {failed_count}"
  )


# 5. ബട്ടൺ ഹാൻഡ്‌ലർ
@app.on_callback_query()
async def button_handler(client: Client, callback_query: CallbackQuery):
  data = callback_query.data

  if data == "plans":
    await callback_query.answer()
    photo_url = "[YOUR_PLANS_IMAGE_URL]"
    plans_text = (
        "🚧 **Limited Time Plans** 🚧\n\n"
        "• **Plan validity cannot exceed 180 days.**"
    )
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "Updates Channel ↗️", url="https://t.me/AlluTvSerials"
            ),
            InlineKeyboardButton("Support ↗️", url="https://t.me/Anujith1238"),
        ],
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Contact Us", callback_data="contact"),
        ],
        [InlineKeyboardButton("« Back to Home", callback_data="back_home")],
    ])
    try:
      await callback_query.message.reply_photo(
          photo=photo_url, caption=plans_text, reply_markup=keyboard
      )
      await callback_query.message.delete()
    except Exception:
      await callback_query.message.edit_text(
          text=plans_text, reply_markup=keyboard
      )

  elif data == "about":
    await callback_query.answer()
    about_photo_url = "[https://files.catbox.moe/m42fyk.jpg]"
    about_text = (
        "🤖 **My Name** - ALLU OTT Downloader Bot\n"
        "🗂️ **Bot Version** - v7.0.0\n"
        "📝 **Language** - Python\n"
        "📚 **Library** - Pyrogram\n"
        "📡 **Hosted on** - [Linux Server]\n"
        "👨‍💻 **Developer** - Anujith\n"
        "📢 **Updates Channel** - AlluTvSerials\n"
        "🕵️ **Buy Subscription** - Anujith"
    )
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "Updates Channel ↗️", url="https://t.me/AlluTvSerials"
            ),
            InlineKeyboardButton("Support ↗️", url="https://t.me/Anujith1238"),
        ],
        [InlineKeyboardButton("« Back to Home", callback_data="back_home")],
    ])
    try:
      await callback_query.message.reply_photo(
          photo=about_photo_url, caption=about_text, reply_markup=keyboard
      )
      await callback_query.message.delete()
    except Exception:
      await callback_query.message.edit_text(
          text=about_text, reply_markup=keyboard
      )

  elif data == "contact":
    await callback_query.answer()
    contact_photo_url = "[https://files.catbox.moe/m42fyk.jpg]"
    contact_text = "📞 **Contact @Anujith1238**"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("« Back to Home", callback_data="back_home")]
    ])
    try:
      await callback_query.message.reply_photo(
          photo=contact_photo_url, caption=contact_text, reply_markup=keyboard
      )
      await callback_query.message.delete()
    except Exception:
      await callback_query.message.edit_text(
          text=contact_text, reply_markup=keyboard
      )

  elif data == "help":
    await callback_query.answer()
    help_text = "❓ **Help Menu:**\n\nSend your OTT link to start downloading."
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("« Back to Home", callback_data="back_home")]
    ])
    await callback_query.message.edit_text(
        text=help_text, reply_markup=keyboard
    )

  elif data == "usage":
    await callback_query.answer()
    usage_text = (
        "📊 **Usage Guide:**\n\n1. Send link\n2. Select destination\n3. Download"
        " file."
    )
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("« Back to Home", callback_data="back_home")]
    ])
    await callback_query.message.edit_text(
        text=usage_text, reply_markup=keyboard
    )

  elif data == "back_home":
    await callback_query.answer()
    user_name = callback_query.from_user.first_name
    welcome_text = (
        f"Hi 🛩️™**{user_name}**! I am one "
        "and only ALLU OTT Downloader Bot on Telegram.\n\n"
        "I can help you to download content "
        "from OTT Platforms"
    )
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "Updates Channel ↗️", url="https://t.me/AlluTvSerials"
            ),
            InlineKeyboardButton("Support ↗️", url="https://t.me/Anujith1238"),
        ],
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Contact Us", callback_data="contact"),
        ],
        [
            InlineKeyboardButton("Usage", callback_data="usage"),
            InlineKeyboardButton("Plans", callback_data="plans"),
        ],
    ])
    try:
      await callback_query.message.edit_text(
          text=welcome_text, reply_markup=keyboard
      )
    except Exception:
      await callback_query.message.reply_text(
          text=welcome_text, reply_markup=keyboard
      )


# സുരക്ഷിതമായി ഇവന്റ് ലൂപ്പ് കൈകാര്യം ചെയ്യാൻ
async def main():
  print("Bot is starting...")
  await app.start()
  print("Bot is running successfully!")
  await asyncio.Event().wait()


if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_loop_complete = True  # type: ignore
  asyncio.run(main())
