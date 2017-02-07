import telebot
from jinja2 import Template
from new_insert import Pizza


TOKEN = '321211996:AAHVErTVde46F-yx7nOkE3DfLWy5oFpD8-0'

if not TOKEN:
    raise Exception('BOT_TOKEN should be specified')

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
