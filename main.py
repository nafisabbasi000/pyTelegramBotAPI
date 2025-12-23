import telebot
import os

# 1. Yahan apna Token dalein (Jo BotFather se mila hai)
BOT_TOKEN = "APNA_BOT_TOKEN_HERE"

bot = telebot.TeleBot(BOT_TOKEN)

# Start Command ka reply
@bot.message_handler(commands=['start'])
def welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"Hello {user_name}! Main aapka naya Python bot hoon. Bataiye main aapki kya madad kar sakta hoon?")

# Help Command
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Aap mujhe koi bhi message bhej sakte hain, main use repeat karunga!")

# Normal messages ko handle karna (Echo Bot)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Aapne kaha: {message.text}")

# Bot ko chalu rakhne ke liye
print("Bot is running...")
bot.infinity_polling()
