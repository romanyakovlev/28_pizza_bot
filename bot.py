import telebot
import os
from jinja2 import Template
from models import Pizza


try:
    TOKEN = os.environ['token']
except KeyError:
    print("KeyError: 'token' is not defined")


bot = telebot.TeleBot(TOKEN)

with open('templates/catalog.md', 'r') as catalog_file:
    catalog_tmpl = Template(catalog_file.read())

with open('templates/greetings.md', 'r') as greetings_file:
    greetings_tmpl = Template(greetings_file.read())


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_tmpl.render())


@bot.message_handler(commands=['menu'])
def show_catalog(message):
    bot.send_message(message.chat.id, catalog_tmpl.render(
        catalog=Pizza.query.all()), parse_mode='Markdown'
    )


if __name__ == '__main__':
    bot.polling(none_stop=True)
