


def start(update, context):
    ...
    return 'ORDERING'
def intent_ext(update, context):
    ...
    if context.user_data.has_key('intent'):
        return 'ADD_INFO'
    else:
        update.message.reply_text('Please rephrase your request.')
        return 'ORDERING'
def add_info(update, context):
    ...
    return ConversationHandler.END
def cancel(update, context):
    ...
    return ConversationHandler.END
...
def main():
    ...
    disp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            'ORDERING': [MessageHandler(Filters.text,
                intent_ext)],
            'ADD_INFO': [MessageHandler(Filters.text,
                add_info)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dip.add_handler(conv_handler)
...