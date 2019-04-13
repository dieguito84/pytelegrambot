import param    # contiene il token
import logging
from telegram.ext import Updater, CommandHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def helloworld(bot, update):
    """Send a message when the command /helloworld is issued."""
    update.message.reply_text('Hello world!')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    '''Start the bot'''
    updater = Updater(param.token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("helloworld", helloworld))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()