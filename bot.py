from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

async def start(update: Update, context):
    # Создаем кнопку с мини-приложением
    keyboard = [[InlineKeyboardButton("Открыть мини-приложение", web_app={"url": "https://t.me/MiniAppbroBot/justmyfirstminiapp"})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажми на кнопку ниже, чтобы открыть мини-приложение:", reply_markup=reply_markup)

# Запуск бота
application = ApplicationBuilder().token("7610308197:AAGH_dbH405Jv2jHADHXldsJcMoCsfFNXrwKEN").build()
application.add_handler(CommandHandler("start", start))
application.run_polling()