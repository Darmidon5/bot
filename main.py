from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import date

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    print(1/0)
    update.message.reply_text('Здравствуй, пользователь')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def planet_pos(update, context):
    planet = update.message.text.split()[1]
    cur_date = date.today()

    planets = {
        "jupiter": ephem.Jupiter,
        "moon": ephem.Moon,
        "saturn": ephem.Saturn,
        'uranus': ephem.Uranus,
        'mars': ephem.Mars,
        'mercury': ephem.Mercury,
        'venus': ephem.Venus,
        'sun': ephem.Sun,
        'pluto': ephem.Pluto,
        'neptune': ephem.Neptune
    }
    const = ephem.constellation(planets[planet.lower()](cur_date))
    print(const[1])
    update.message.reply_text(const[1])

def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_pos))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()