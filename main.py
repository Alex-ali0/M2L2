import telebot 
from config import token
from random import randint
from logic import Pokemon, Wizard, Fighter
bot = telebot.TeleBot(token) 


@bot.message_handler(commands=['start'])
def start(message):
        bot.reply_to(message,"Привет, это бот который будет кидать вам рандомных покемонов")
        bot.reply_to(message,"все команды тут ---> /infor")

@bot.message_handler(commands=['infor'])
def info(message):
        if message.from_user.username in Pokemon.pokemons.keys():
            bot.reply_to(message,"/plus_age - вырастить покемона\n/info - посмотреть информацию о покемоне")
        else:
            bot.reply_to(message,"вы ещё не создали покемона поэтому доступна только одна команда\n/go - создать покемона")

@bot.message_handler(commands=['info'])
def info_pokemon(message):
        if message.from_user.username in Pokemon.pokemons.keys():
                    pokemon = Pokemon(message.from_user.username)
                    bot.send_message(message.chat.id, pokemon.info())
        else:
            bot.reply_to(message,"вы ещё не создали покемона\n/go - создать покемона")

# @bot.message_handler(commands=['go'])
# def go(message):
#     pokemon = Pokemon(message.from_user.username)
#     bot.send_message(message.chat.id, pokemon.info())
#     bot.send_photo(message.chat.id, pokemon.show_img())

@bot.message_handler(commands=['go'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def feed_pok(message):
      if message.from_user.username in Pokemon.pokemons.keys():
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.feed()
            bot.send_message(message.chat.id, res)
      else:
            bot.send_message(message.chat.id, "Нельзя кормить покемона которого нет ❌")

@bot.message_handler(commands=['plus_age'])
def age(message):
        if message.from_user.username not in Pokemon.pokemons.keys():
                pokemon = Pokemon(message.from_user.username)
                bot.send_message(message.chat.id, pokemon.plus_age())
        else:
                pokemon = Pokemon(message.from_user.username)
                bot.send_message(message.chat.id, pokemon.plus_age())


@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "❌Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "❌Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")


bot.infinity_polling(none_stop=True)



