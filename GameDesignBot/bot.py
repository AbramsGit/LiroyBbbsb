import urllib.request
import urllib.parse
import re
import wikipedia
import config
import telebot
bot = telebot.TeleBot(config.token)


@bot.message_handler(regexp="ГОЛОС!")
def voice(message):
    voice = open('/home/grandy/PycharmProjects/GameDesignBot/1.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)


@bot.message_handler(commands=['LirHelp'])
def help_desk(message):
    bot.reply_to(message,'/wiki_ru - чтобы прочесть, статью на русском(current unstable) '"                       "
''                                          '/wiki_en - to read the article in English(current unstable)'"                                         "
                 '/youtube - Search video on Youtube.(how match result you want to see [2-5]) if you want to see only 1 result dont use numbers after youtube just type /youtube GabeN for example')


@bot.message_handler(commands=['wiki_ru'])
def result(message):
    wikipedia.set_lang("ru")
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[6:99]
    #here is stupid debug. I`m not smart and i send result of wikipedia.summary to console
    print(wikipedia.summary(tj))
    #here bot send to user result of this shity magic.
    bot.reply_to(message,wikipedia.summary(tj))

@bot.message_handler(commands=['wiki_en'])
def result(message):
    wikipedia.set_lang("en")
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[6:99]
    #here is stupid debug. I`m not smart and i send result of wikipedia.summary to console
    print(wikipedia.summary(tj))
    #here bot send to user result of this shity magic.
    bot.reply_to(message,wikipedia.summary(tj))


@bot.message_handler(commands=['youtube'])
def youtuberesult(message):
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[8:120]
    query_string = urllib.parse.urlencode({"search_query" : tj})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[0])

@bot.message_handler(commands=['youtube2'])
def youtuberesult2(message):
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[8:120]
    query_string = urllib.parse.urlencode({"search_query" : tj})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[0])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[4])

@bot.message_handler(commands=['youtube3'])
def youtuberesult3(message):
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[8:120]
    query_string = urllib.parse.urlencode({"search_query" : tj})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[0])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[10])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[5])


@bot.message_handler(commands=['youtube4'])
def youtuberesult4(message):
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[8:120]
    query_string = urllib.parse.urlencode({"search_query" : tj})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[0])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[3])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[10])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[5])

@bot.message_handler(commands=['youtube5'])
def youtuberesult5(message):
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[8:120]
    query_string = urllib.parse.urlencode({"search_query" : tj})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[0])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[3])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[6])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[8])
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[12])

bot.polling()





