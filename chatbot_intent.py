def extract_intent(doc):
    for token in doc:
        if token.dep_ == 'dobj':
            verb = token.head.text
            dobj = token.text
        # create a list of tuples for possible verb synonyms
        verbList = [('order', 'want', 'give', 'make'), ('show', 'find')]
        # find the tuple containing the transitive verb extracted from the sample
        verbSyns = [item for item in verbList if verb in item]
        # create a list of tuples for possible direct object synonyms
        dobjList = [('pizza', 'pie', 'dish'), ('cola', 'soda')]
        # find the tuple containing the direct object extracted from the sample
        dobjSyns = [item for item in dobjList if dobj in item]
        # replace the transitive verb and the direct object with synonyms supported by the application and compose the string that represents the intent
        intent = verbSyns[0][0] + dobjSyns[0][0].capitalize()
        
        def utterance(update, context):
            msg = update.message.text
            nlp = spacy.load('en')
            doc = nlp(msg)
            for token in doc:
                if token.dep_ == 'dobj':
                    intent = extract_intent(doc)
                    if intent == 'orderPizza':
                        update.message.reply_text('We need some more information to place your order.')
                    elif intent == 'showPizza':
                        update.message.reply_text('Would you like to look at our menu?')
                    else:
                        update.message.reply_text('Your intent is not recongnised.')
                    return
                update.message.reply_text('Please rephrase your request. Be as specific as possible!')
                        