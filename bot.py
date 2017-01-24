import config
import telebot
import utils
from encrypt import enctypt,decrypt,get_key

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['code'])
def markup_code(message):
    '''Выбор шифрование/дешифрование при вводе команды "/code"'''
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add('Зашифровать')
    markup.add('Расшифровать')
    bot.send_message(message.chat.id,'Действие',reply_markup=markup)
    utils.set_active_user(message.chat.id,'active_command')

@bot.message_handler(content_types=["text"])
def active_caesar(message):
    answer = utils.get_active_for_user(message.chat.id)
    if not answer:
        bot.send_message(message.chat.id,'Необходимо ввести команду',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text == 'Зашифровать':
            utils.finish_active_comand(message.chat.id)
            utils.set_active_user(message.chat.id, 'Зашифровать')
            bot.send_message(message.chat.id, 'Введите слово для шифрования',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
    elif message.text=='Расшифровать':
        utils.finish_active_comand(message.chat.id)
        utils.set_active_user(message.chat.id, 'Расшифровать')
        bot.send_message(message.chat.id, 'Введите слово для шифрования',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        comm = utils.get_active_for_user(message.chat.id)
        if not comm:
            bot.send_message(message.chat.id, 'Ошибка!')
        elif comm=='Зашифровать':
            bot.send_message(message.chat.id, enctypt(message))
        elif comm=='Расшифровать':
            bot.send_message(message.chat.id, decrypt(message))
        utils.finish_active_comand(message.chat.id)

if __name__ == '__main__':
    bot.polling(none_stop=True)
