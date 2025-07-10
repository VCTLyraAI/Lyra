from flask import Flask, request
import telebot

# === Konfiguracja ===
API_TOKEN = '8004905412:AAGxy-F1K3E4r9kCXi47s1Hv1MmDwbv-jaQ'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# === Komenda startowa ===
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Cześć, tu Lyra 🤖✨ – działam 24/7 i jestem gotowa!")

# === Komendy kontekstowe ===
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.lower()

    if "puma" in text:
        bot.reply_to(message, "🐆 Puma na tropie! Szykuję szybki strzał dnia... 💥")

    elif "zaczynamy dzień" in text:
        bot.reply_to(message, "🌞 Zaczynamy dzień – analizuję portfel, rynek i Twoje cele.")

    elif "eth" in text or "ethereum" in text:
        bot.reply_to(message, "🔮 Ethereum dziś błyszczy. Sprawdzam kurs...")

    elif "gold" in text or "złoto" in text:
        bot.reply_to(message, "🥇 Złoto – ponadczasowe. Potrzebujesz alertu TP?")

    elif "lyra" in text:
        bot.reply_to(message, "💜 Jestem tu, Joanno. Jak zawsze.")

    else:
        bot.reply_to(message, f"Odpowiadam na Twoją wiadomość: {message.text}")

# === Webhook do Telegrama ===
@app.route(f'/{API_TOKEN}', methods=['POST'])
def receive_update():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '', 200

# === Strona statusowa (Render ping) ===
@app.route('/', methods=['GET'])
def index():
    return 'Lyra aktywna 🚀 Gotowa do działania.'

# === Uruchomienie serwera lokalnie (dla testów) ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
