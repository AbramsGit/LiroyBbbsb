import telebot
import urllib.request
import urllib.parse
import re


bot = telebot.TeleBot("193284640:AAFFjVWBhbsciXZ0ZmG1C4reiFZ8W03L6Hg")

f = open('Much_text.txt', 'a')

import re
import urllib.request



@bot.message_handler(regexp="ГОЛОС!")
def voice(message):
    voice = open('1.ogg', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Hello,  i`m a Leeroy. My master, decided to make the neural network, which is the ability to understand your message. "
                          "If you want to teach me, please enter the following command [/t] + type some text with your opinion of something"
                          "or  if you want to watch some fun videos on youtube, please type [/y] + all of you want to watch"
                          "or you can type [/c] and read funny comics from xkcd.com")

@bot.message_handler(commands=['y'])
def youtuberesult(message):
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[2:120]
    query_string = urllib.parse.urlencode({"search_query" : tj})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    bot.reply_to(message,"http://www.youtube.com/watch?v=" + search_results[0])


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'str: %s' % self.name

    def __repr__(self):
        return 'repr: %s' % self.namecharm



@bot.message_handler(commands=['t'])
def teachresult(message):
    #here we get message from user
    ij = message.text
    #here we say that ij is string
    string = ij
    #here i`ll say for python "Don`t read fucking command /wiki, and read all latter from 6 to 99 "
    tj = string[2:120]
    bot.reply_to(message,message.text + " i`ll try to understand it")
    writer = open('C:\\Users\Abrams\PycharmProjects\MicroBrain\main_folder\Much_text.cvs', 'a')
    writer.write(tj)
    writer.write('\n'+'\n')
    writer.close()

#_______________________________________________________________________________________________________________________
#
# That commented part of code work not corrected for now/
# Recently it works perfect, but now he get a wrong link to image.
# Maybe, soon i`ll fix it.
#                                                       (...*hey*...)
# I`m so lazy ? i don`t wanna do that))
#
#_______________________________________________________________________________________________________________________

#get some fucking comics
#def GetURL(url):
#    s = 'error'
#    try:
#        f = urllib.request.urlopen(url)
#        s = f.read()
#    except urllib.error.HTTPError:
#        s = 'connect error'
#    except urllib.error.URLError:
#        s = 'url error'
#    return s
#Site = GetURL('http://c.xkcd.com/random/comic/')
#SiteFind = re.findall('img .*? src="(.*?)"', str(Site))


#Send some fucking comics.
#def GetURL(url):
#    s = 'error'
#    try:
#        f = urllib.request.urlopen(url)
#        s = f.read()
#    except urllib.error.HTTPError:
#        s = 'connect error'
#    except urllib.error.URLError:
#        s = 'url error'
#    return s

#def GetIamage(self):
#    Site = GetURL('http://c.xkcd.com/random/comic/')
#    SiteFind = re.findall('img .*? src="(.*?)"', str(Site))



#def GetIamage(self):
#    Site = GetURL('http://c.xkcd.com/random/comic/')
#    SiteFind = re.findall('img .*? src="(.*?)"', str(Site))
#    return SiteFind[0]


#@bot.message_handler(commands=['c'])
#def comixresult(message):
#    bot.send_message(message.chat.id, "http:" + GetIamage(3))

bot.polling(none_stop=True)