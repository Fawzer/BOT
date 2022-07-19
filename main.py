# install pyTelegramBotAPI

import telebot

bot = telebot.TeleBot("5562936941:AAHDpv7M92fSNk-XwR2gVGmUnteqrbVN2v8")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>Привет, я бот Fawzer, если хотите узнать, что я умею, "
                                      "то воспользуйтесь командой [ /help ]</b>", parse_mode="html")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "<b>Я могу предоставить доступ ко всем моим сотсетям"
                                      "Чтобы бот предоставил вам ссылки на мои сотсети, напишите команду [ /give ] \n "
                                      "Если тебе интересно какие проекты я создаю, то перейди на мой аккаунт в github по данной команде[ /myprojects ] </b>"
                                      "Если вам нужно связаться со мной лично, то воспользуйтесь командой [/ls]",
                     parse_mode="html")


@bot.message_handler(commands=['give'])
def give(message):
    bot.send_message(message.chat.id,
                     "<b>Telegram chat - t.me/+v5ax5E1d-t1hMjRi \n VK аккаунт - vk.com/violente1</b>",
                     parse_mode="html")


@bot.message_handler(commands=['myprojects'])
def give(message):
    bot.send_message(message.chat.id, "<b>GitHub аккаунт - https://github.com/Fawzer</b>", parse_mode="html")


@bot.message_handler(commands=['ls'])
def give(message):
    bot.send_message(message.chat.id, "<b>Перейдя по ссылке,вы можете пообщаться со мной лично- </b>", parse_mode="html")


bot.polling(none_stop=True)
