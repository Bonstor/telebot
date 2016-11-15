import config
import init
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)

customer = init.Customer('None', [], [])


def restart(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for s in customer.services:
        markup.add(s)
    msg = bot.send_message(message.chat.id, 'Что нибудь еще?', reply_markup=markup)
    bot.register_next_step_handler(msg, control)


@bot.message_handler(commands=['test'])
def test(mes):
    bot.send_message(mes.chat.id, customer.name)




@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Привет!\nЯ тестовый бот.\n1 - Юрий\n2 - Глеб')
    bot.register_next_step_handler(msg, auth)


def auth(message):
    identifer = message.text
    if not identifer.isdigit():
        msg = bot.reply_to(message, 'Id это цифра, попробуйте еще раз')
        bot.register_next_step_handler(msg, auth)
        return
    else:
        global customer
        customer = init.customers.get(int(identifer),init.Customer('None', [], []))
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        if customer.name == 'None':
            msg = bot.send_message(message.chat.id, 'Пользователь не найден, попробуйте еще раз')
            bot.register_next_step_handler(msg, auth)
        else:
            bot.send_message(message.chat.id, 'Приветствую тебя, ' + customer.name)
            for s in customer.services:
                markup.add(s)
            msg = bot.send_message(message.chat.id, 'Чем хотите управлять?', reply_markup=markup)
            bot.register_next_step_handler(msg, control)


def control(message):
    if message.text == 'Управление стажировкой':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Конечно', 'Естественно')
        msg = bot.send_message(message.chat.id, 'Хотите нанять Глеба на стажировку?', reply_markup=markup)
        bot.register_next_step_handler(msg, probation)
    elif message.text == 'Умный дом':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        for s in customer.smd:
            markup.add(s)
        msg = bot.send_message(message.chat.id, 'Сейчас у вас подключенны следующие устройства', reply_markup=markup)
        bot.register_next_step_handler(msg, smart_house)
    elif message.text == 'Интернет':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Сделать быстрее', 'Сделать дешевле')
        msg = bot.send_message(message.chat.id, 'Что нужно сделать с интернетом?', reply_markup=markup)
        bot.register_next_step_handler(msg, internet)
    elif message.text == 'Интернет Yota':
        msg = bot.send_message(message.chat.id, 'Тут наука бессильна')
        restart(message)


def internet(message):
    if message.text == 'Сделать быстрее':
        msg = bot.send_message(message.chat.id, 'Теперь он стоит 10000$ в месяц')
        restart(message)
    if message.text == 'Сделать дешевле':
        bot.send_message(message.chat.id, 'time out error')
        msg = bot.send_message(message.chat.id, 'Ладно ладно, шутка это')
        restart(message)

def smart_house(message):
    if message.text == 'Термостат':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Сделать жарко', 'Давай похолоднее')
        msg = bot.send_message(message.chat.id, 'Что прикажете?', reply_markup=markup)
        bot.register_next_step_handler(msg, thermo)
    if message.text == 'Свет':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ярче', 'Темнее')
        msg = bot.send_message(message.chat.id, 'Что прикажете?', reply_markup=markup)
        bot.register_next_step_handler(msg, light)


def thermo(message):
    if message.text == 'Сделать жарко':
        msg = bot.send_message(message.chat.id, 'Теперь дома тепло')
        restart(message)
    elif message.text == 'Давай похолоднее':
        msg = bot.send_message(message.chat.id, 'Дома арктическая свежесть и прохлада')
        restart(message)
    else:
        bot.send_message(message.chat.id, 'Где то ошибка((')
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Сделать жарко', 'Давай похолоднее')
        msg = bot.send_message(message.chat.id, 'Что прикажете?', reply_markup=markup)
        bot.register_next_step_handler(msg, thermo)


def light(message):
    if message.text == 'Ярче':
        bot.send_message(message.chat.id, 'Свет включен')
        msg = bot.send_message(message.chat.id, 'Но вообще я пока не умею этого')
        restart(message)
    elif message.text == 'Темнее':
        msg = bot.send_message(message.chat.id, 'Готово!')
        restart(message)
    else:
        bot.send_message(message.chat.id, 'Где то ошибка((')
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ярче', 'Темнее')
        msg = bot.send_message(message.chat.id, 'Что прикажете?', reply_markup=markup)
        bot.register_next_step_handler(msg, light)





def probation(message):
    msg = bot.send_message(message.chat.id, 'Спасибо!)')
    restart(message)

try:
    bot.polling(none_stop=True)
except Exception:
    print('e')
