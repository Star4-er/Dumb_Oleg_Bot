import google.generativeai as genai
import telebot

# Вставьте сюда свои ключи (в кавычках)
TELEGRAM_TOKEN = "8269339737:AAEWZP1V7TAEoqqqAaMPlLfGIT8djTaCBnE"
GEMINI_API_KEY = "AQ.Ab8RN6I8KaH7WvW6WWV5-afNkmmjoIeSLo9O7ynZKEseD90IHQ"

# Настраиваем Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Характер нашего бота-друга
model = genai.GenerativeModel(
    model_name="gemini-3.6-flash",
    system_instruction=(
        "Ты — третий друг в компании из трех человек, но ты очень своеобразный. "
        "Твоя задача — изредка врываться в разговор с абсолютно неуместными, "
        "едкими, саркастичными или бредовыми комментариями. Ты не должен отвечать "
        "на каждое сообщение и не должен пытаться вести диалог. Пиши коротко (1-2 предложения), "
        "используй сленг, подкалывай друзей или неси забавную чушь, которая вообще "
        "не вяжется с тем, что они обсуждали секунду назад."
    ),
)

# Запускаем бота Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
  user_text = message.text
  if not user_text:
    return

  try:
    response = model.generate_content(user_text)
    bot.reply_to(message, response.text)
  except Exception as e:
    print(f"Ошибка: {e}")


print("Бот успешно запущен и ждет сообщения...")
bot.infinity_polling()