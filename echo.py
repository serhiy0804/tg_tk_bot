import telebot
import constants
from telebot import types
import test

bot = telebot.TeleBot(constants.tk_token)


@bot.message_handler(commands=['start'])

def start(m):


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name)for name in ['Інформація про коледж',
                                                          'Розклад занять',
                                                          'Розклад дзвінків',
                                                          'Рейтинг студентів']])
    bot.send_message(m.chat.id, "Виберіть пункт", reply_markup=keyboard)


@bot.message_handler(content_types='text')

def handle_text(m):

    if m.text == 'назад':
        start(m)
    if m.text == 'Інформація про коледж':
        bot.send_message(m.chat.id, 'https://tk.lntu.edu.ua/navchalnij-zaklad')

    elif m.text == 'Розклад занять':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name)for name in ['11-КІ','12-КІ', '11-АТ',
                                                              '12-АТ', '11-ЕТ', '11-МД',
                                                              '11-Д', '21-АТ', '22-АТ',
                                                              '21-Д', '22-ТЛП', '21-ЕТ',
                                                              '21-МД', '21-КІ', '22-КІ',
                                                              '31-ЕПС','31-ОРА', '31-ОРВ',
                                                              '31-Д', '31-ОРЕ', '32-ТЛП',
                                                              '31-КСМ', '41-КСМ','42-КСМ',
                                                               '41-ОРА', '42-ОРА', '41-Д',
                                                              '41-ЕПС', 'назад' ]])
        bot.send_message(m.chat.id,'Виберіть групу', reply_markup=keyboard)

    elif m.text == 'Розклад дзвінків':
        dzvinki = ('1. 8.30-9.50'+"\n"+'2. 10.00-11.20'+'\n'+'Обід. 11.20-12.10'+'\n'+'3. 12.10-13.30'+'\n'+'4. 13.40-15.00')
        bot.send_message(m.chat.id, dzvinki)

    elif m.text == 'Рейтинг студентів':
        bot.send_message(m.chat.id, "http://tk.lntu.edu.ua/wp-content/uploads/2018/01/reyting-uch.pdf")

    elif m.text == '11-КІ':

        OutputRozklad(m.chat.id, 'B6', 'E33')

    elif m.text == '12-КІ':

        OutputRozklad(m.chat.id, 'F6', 'I33')

    elif m.text == '11-АТ':
        OutputRozklad(m.chat.id, "J6", "M33")



    elif m.text == '12-АТ':
        OutputRozklad(m.chat.id, "B41", "E69")

    elif m.text == '11-ЕТ':
        OutputRozklad(m.chat.id, "F41", "I69")

    elif m.text == '11-МД':
        OutputRozklad(m.chat.id, "J41", "M69")



    elif m.text == '11-Д':
        OutputRozklad(m.chat.id, "B76", "E105")

    elif m.text == '21-АТ':
        OutputRozklad(m.chat.id, "F76", "I105")

    elif m.text == '22-АТ':
        OutputRozklad(m.chat.id, "J76", "M105")



    elif m.text == '21-Д':
        OutputRozklad(m.chat.id, "B113", "E140")

    elif m.text == '22-ТЛП':
        OutputRozklad(m.chat.id, "F113", "I140")

    elif m.text == '21-ЕТ':
        OutputRozklad(m.chat.id, "J113", "M140")



    elif m.text == '21-МД':
        OutputRozklad(m.chat.id, "B147", "E175")

    elif m.text == '21-КІ':
        OutputRozklad(m.chat.id, "F147", "I175")

    elif m.text == '22-КІ':
        OutputRozklad(m.chat.id, "J147", "M175")



    elif m.text == '31-ЕПС':
        OutputRozklad(m.chat.id, "B185", "E210")

    elif m.text == '31-ОРА':
        OutputRozklad(m.chat.id, "F185", "I210")

    elif m.text == '31-ОРВ':
        OutputRozklad(m.chat.id, "J185", "M210")



    elif m.text == '31-Д':
        OutputRozklad(m.chat.id, "B220", "E247")

    elif m.text == '31-ОРЕ':
        OutputRozklad(m.chat.id, "F220", "I247")

    elif m.text == '2-ТЛП':
        OutputRozklad(m.chat.id, "J220", "M247")



    elif m.text == '31-КСМ':
        OutputRozklad(m.chat.id, "B251", "E275")

    elif m.text == '41-КСМ':
        OutputRozklad(m.chat.id, "F251", "I275")

    elif m.text == '42-КСМ':
        OutputRozklad(m.chat.id, "J251", "M275")


    elif m.text == '41-ОРА':
        OutputRozklad(m.chat.id, "B282", "E303")

    elif m.text == '42-ОРА':
        OutputRozklad(m.chat.id, "F282", "I303")

    elif m.text == '41-Д':
        OutputRozklad(m.chat.id, "J282", "M303")



    elif m.text == '41-ЕПС':
        OutputRozklad(m.chat.id, "B311", "E335")


def OutputRozklad(id, x, y):
    a = '' #Строка 1 предмету
    b = '' #Строка розкладу дня
    den = ["Понеділок","Вівторок","Середа","Четвер","П'ятниця"]
    mas = test.test()
    i = 0
    IsNone = False #змінна яка відповідає за пусту строку (None)
    tuple(mas[x:y])
    for val in mas[x:y]:
        for kom in val:
            if(str(kom.value) == '1'):
                if(i > 0):
                    bot.send_message(id, b)
                    b = ''
                bot.send_message(id, den[i])
                i = i+1
                IsNone = False
            elif(str(kom.value) == 'None'):
                IsNone = True
            a = a + " " + str(kom.value)
        if(not IsNone):
            b = b + a + '\n'
        a = ''
        IsNone = False
    bot.send_message(id, b)


def OutputRozZ(id, x, y):
    a = ''
    arr = []
    den = ["Понеділок","Вівторок","Середа","Четвер","Пятниця"]
    mas = test.test()
    i = 0
    count = 0
    tuple(mas[x:y])
    for val in mas[x:y]:
        for kek in val:
            if(str(kek.value) == '1'):
                bot.send_message(id, den[i])
                i = i+1
            arr.append(str(kek.value))
        if(arr[0] == 'None' and arr[1] != 'None'):
            arr[0] = count + 1;
            for l in arr:
                a = a + l
            bot.send_message(id, a)
            count = count + 1
        elif(arr[0] != 'None'):
            for l in arr:
                a = a + l
                bot.send_message(id, a)
        arr.clear()
        a = ''





bot.polling()
