import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
yourkey = os.getenv("key")
bot_id = os.getenv("botkey")

bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

row = []
@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    chat_id = message.chat.id
    bot.reply_to(message, 'Getting movie info...')
    string_ = message.text
    moviename = string_.split()
    moviename_ = ""
    for i in moviename:
        if i != "/movie":
            moviename_ = moviename_+i+" "
    response_ = requests.get(f"http://www.omdbapi.com/?apikey={yourkey}&t={moviename_}",)
    json_ = response_.json()
    print(json.dumps(json_,indent = 3))
    send_ = f"Movie Name: {json_['Title']}\nYear: {json_['Year']}\nReleased: {json_['Released']}\nimdbRating: {json_['imdbRating']}"
    link = json_['Poster']
    response = requests.get(link,allow_redirects=True)
    if response.status_code:
        open('image.png','wb').write(response.content)
    photo = open('/home/wreck/Desktop/cinebot/task-04/image.png', 'rb')
    bot.send_photo(chat_id, photo)
    photo.close()
    bot.reply_to(message, send_)
    row.append([json_['Title'],json_['Year'],json_['Released'],json_['imdbRating']])
    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    chat_id = message.chat.id
    with open('data_file.csv','w') as data_file:
        csv_writer = csv.writer(data_file)
        count = 0
        if count == 0:
            header = ['Movie Name','Year','Released','imdbRating']
        csv_writer.writerow(header)
        count = count + 1
        for i in row:
            csv_writer.writerow(i)
    
    with open('data_file.csv','r') as read_file:
        csv_reader = csv.reader(read_file)
        bot.send_document(chat_id, read_file)

    #TODO: 2.2 Send downlodable CSV file to telegram chat

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
