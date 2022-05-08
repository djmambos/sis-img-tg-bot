import config
import telebot
import image_search

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Привет!')
    bot.send_message(message.chat.id, 'Напиши команду /pic и через пробел название пикчи, которую ты хочешь найти')
    print(f'Connect new user: [username: {message.from_user.username}]')

@bot.message_handler(commands=['help'])
def welcome(message):
    bot.reply_to(message, 'Держи мои команды')
    bot.send_message(message.chat.id, '/pic название_картинки')

@bot.message_handler(commands=['pic'])
def get_pic(message):
    command = message.text
    if (len(command.split(' ')) > 1):
        pic_name = command.split(' ')[1:]
        pic_name = ' '.join(pic_name)
        print(f'[User: {message.from_user.username}] Go search pic with name: [name: {pic_name}]')

        bot.send_message(message.chat.id, f'Ищу пикчу по слову {pic_name}')
        found_picture = image_search.search_img_by_name(pic_name)

        if found_picture:
            bot.send_message(message.chat.id, found_picture)
        else:
            print(f'Nothing was found by pic name [{pic_name}]')
            bot.send_message(message.chat.id, f'По запросу "{pic_name}" ничего не было найдено')
    else:
        bot.send_message(message.chat.id, 'Вероятно вы ввели пустое имя пикчи, попробуйте еще раз')

bot.polling(none_stop=True)
