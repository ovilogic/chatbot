from telegram.ext import Updater, MessageHandler, Filters
def echo(update, context):
    update.message.reply_text(update.message.text)
updater = Updater('TOKEN', use_context=True)
#registering a handler to handle input text messages
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
#starting polling updates from the messenger
updater.start_polling()
updater.idle()