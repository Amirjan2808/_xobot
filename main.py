import settings
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters

updater = Updater(token=settings.TELEGRAM_TOKEN)
