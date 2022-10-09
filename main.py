import telebot
import requests
from telebot import types


headerss = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'api.telegram.org',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
def ex_id(id):
    result = False
    file = open('users.txt', 'r')
    for line in file:
        if line.strip() == id:
            result = True
    file.close()
    return result


bot = telebot.AsyncTeleBot("5677831426:AAFpaXu2dNhS_hs5DTQBT-ID_KXiLGTWaHM")

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        id = message.from_user.id
        req = requests.get(f'https://api.telegram.org/bot5156335204:AAGw4julPGNUOY8VCE-mHRNNHQe1ovbKuNU/getChatMember?chat_id=@rickpro3&user_id={id}', headers=headerss)
        s = str(req.json()['result']['status'])
        if s == 'left':
            bot.send_message(message.chat.id, text='@rickpro3\nSubscribe to use the bot\n/start')
        else:
            idu = message.from_user.id
            f = open('users.txt', 'a')
            if (not ex_id(str(idu))):
                usern = message.from_user.username
                f.write(f"{idu}\n")
                f.close()
            bot.send_message(message.chat.id, text='''اهلا عزيزي المستخدم في بوت التواصل .
            ⌔︙ارسل رسالتك للتواصل مع المطور ...
            ⌔︙مطور البوت : @QTA_QTA''', reply_to_message_id=message.message_id)


@bot.message_handler(commands=['count'])
def count(message):
    bot.send_message(message.chat.id,text='users :'+str(len(open('users.txt', 'r').read().splitlines())))



@bot.message_handler(func=lambda message: message.chat.type=="private",content_types=['text'])
def send(message):
    bot.forward_message("1205586056", message.chat.id,message.message_id)
    bot.send_message(message.chat.id,text="تم ارسال رسالتك الى المطور .", reply_to_message_id=message.message_id)

bot.infinity_polling()
