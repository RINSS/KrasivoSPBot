from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler

from config import token

import re


def krasivo(data):
    text = str(data.group(0))
    return '`' + ' '.join(sym for sym in text if sym.isalnum()).upper() + '`'


def inlinequery(bot, update):
    query = update.inline_query.query

    if not query:
        return

    result = re.sub(r'{(.*?)}', krasivo, query)

    if result == query:
        return

    print('Username: ', update.inline_query.from_user.username)
    print('Input: ' + query)
    print('Result: ' + result)
    print('')

    content = InputTextMessageContent(result, parse_mode=ParseMode.MARKDOWN)
    results = [InlineQueryResultArticle(id=uuid4(), title='𝓚𝓹𝓪𝓬𝓾𝓫𝓸', description=result, input_message_content=content)]
    bot.answerInlineQuery(update.inline_query.id, results=results)


def main():
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
