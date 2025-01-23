import logging
import requests
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters

class AyushiChatBot:
    def __init__(self, token, api_url, model_name):
        """Initialize the bot with Telegram token, LM Studio API URL, and model name."""
        self.token = token
        self.api_url = api_url
        self.model_name = model_name
        self.chat_history = [
            {"role": "system", "content": "You are a helpful and concise AI assistant."}
        ]
        self.setup_logging()

    def setup_logging(self):
        """Set up logging for the bot."""
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

    def build_application(self):
        """Build and return the Telegram application."""
        app = Application.builder().token(self.token).build()
        app.add_handler(CommandHandler("start", self.start_command))
        app.add_handler(CommandHandler("help", self.help_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_user_message))
        return app

    async def start_command(self, update: Update, context) -> None:
        """Handle the /start command."""
        user = update.effective_user
        welcome_message = (
            f"Hello {user.first_name}! I’m Ayushi your personal assistant bot created by Ayushi Jaimani. "
            "Feel free to chat with me!"
        )
        await update.message.reply_html(welcome_message, reply_markup=ForceReply(selective=True))

    async def help_command(self, update: Update, context) -> None:
        """Handle the /help command."""
        help_message = (
            "I’m here to assist you with your queries. Just type a message, and I’ll respond!"
        )
        await update.message.reply_text(help_message)

    async def handle_user_message(self, update: Update, context) -> None:
        """Handle user messages by sending them to the AI model and returning the response."""
        user_message = update.message.text.strip()
        if not user_message:
            await update.message.reply_text("I’m listening! Please send a message.")
            return

        self.logger.info("Received message from user: %s", user_message)
        self.chat_history.append({"role": "user", "content": user_message})

        try:
            ai_response = self.get_ai_response(user_message)
            await update.message.reply_text(ai_response)
        except Exception as e:
            self.logger.error("Error occurred: %s", e)
            await update.message.reply_text("Sorry, something went wrong on my end.")

    def get_ai_response(self, user_message: str) -> str:
        """Send the user message to LM Studio and return the AI response."""
        try:
            response = requests.post(
                f"{self.api_url}/chat/completions",
                headers={"Content-Type": "application/json"},
                json={
                    "model": self.model_name,
                    "messages": self.chat_history,
                    "temperature": 0.5,
                    "max_tokens": 200,
                },
            )

            if response.status_code == 200:
                data = response.json()
                ai_reply = data["choices"][0]["message"]["content"].strip()
                self.chat_history.append({"role": "assistant", "content": ai_reply})
                return ai_reply
            else:
                self.logger.error(
                    "Failed to fetch response from LM Studio: %s - %s",
                    response.status_code,
                    response.text,
                )
                return "I’m having trouble understanding. Please try again."
        except requests.RequestException as e:
            self.logger.error("Request to LM Studio failed: %s", e)
            raise

    def run(self):
        """Run the Telegram bot."""
        self.logger.info("Starting Ayushi's ChatBot...")
        app = self.build_application()
        app.run_polling()


if __name__ == "__main__":
    TELEGRAM_TOKEN = "7682858071:AAG2qDtJEuVFTsahYs1RwDY4FOECodJMdGY"
    LM_STUDIO_API_URL = "http://191.278.0.64:1234/v1"
    MODEL_NAME = "tinyllama_-_tinyllama-1.1b-chat-v1.0"

    bot = AyushiChatBot(TELEGRAM_TOKEN, LM_STUDIO_API_URL, MODEL_NAME)
    bot.run()