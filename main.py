from flask import Flask, request
import telebot

API_TOKEN = '8004905412:AAGxy-F1K3E4r9kCXi47s1Hv1MmDwbv-jaQ'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Cześć, tu Lyra 🤖✨ – działam 24/7!")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.lower()
    if "puma" in text:
        bot.reply_to(message, "🐆 Puma na tropie! Szybki strzał nadchodzi.")
    elif "zaczynamy dzień" in text:
        bot.reply_to(message, "🌞 Zaczynamy dzień – analizuję rynek.")
    else:
        bot.reply_to(message, f"Odpowiadam na Twoją wiadomość: {message.text}")

@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

@app.route('/', methods=['GET'])
def index():
    return 'Lyra online! 🧠'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
