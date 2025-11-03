import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    message_text = """Hola! Bienvenidos! 

Me llamo César Gómez. Viajo mucho y ayudo a mis suscriptores a ganar dinero online: rápido, legal y con algoritmos claros, gracias a mi app. 💸

ES SENCILLO! ⚡️

La app se basa en inteligencia artificial y predice las probabilidades en el juego "Chicken Road". Gracias a ella, cientos de personas ganan entre 15.000.000 y 60.000.000 de pesos diarios conmigo. 😎

Y lo mejor de todo: ¡regalo un bot a quien lo quiera! 🙌🏻

IMPORTANTE! Solo tienes que enviarme un mensaje privado y registrarte. Solo te llevará 5 minutos. Te enseñaré a usar la app correctamente y a no perder dinero. 👌🏻

Imagínate, hoy mismo ganarás tu primer ingreso online. 💸"""

    # Create inline keyboard with button
    keyboard = [
        [InlineKeyboardButton("Consigue el hacking bot", url="https://t.me/CaesarGomezBot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send photo with caption and button
    # Replace 'photo.jpg' with the path to your image file
    try:
        with open('photo.jpg', 'rb') as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=message_text,
                reply_markup=reply_markup
            )
    except FileNotFoundError:
        # If photo not found, send text message instead
        await update.message.reply_text(
            f"⚠️ Фото не найдено! Поместите файл 'photo.jpg' в папку с ботом.\n\n{message_text}",
            reply_markup=reply_markup
        )

def main() -> None:
    """Start the bot."""
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token from @BotFather
    application = Application.builder().token("8491157719:AAFaM0-91rCEU7byIjAv9lnhOD_0GDJuU3k").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()