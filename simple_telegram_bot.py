# Description: A simple Telegram bot that sends the Restopolis balance at 8pm CET every day

import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import logging
import asyncio

from restopolis_balance_provider import get_restopolis_balance

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(chat_id)
    if str(chat_id) == os.environ['PREDEFINED_CHAT_ID']:
        while True:
            # Get the Restopolis balance and send it in a Telegram message
            balance = get_restopolis_balance(os.environ['RESTOPOLIS_USERNAME'],
                                             os.environ['RESTOPOLIS_PASSWORD'])
            message = f"Your Restopolis balance is {balance}."
            await context.bot.send_message(chat_id=chat_id,
                                           text=message,
                                           disable_notification=True)
            # Sleep until 8pm CET of next day
            await asyncio.sleep(60 * 60 * 24 - time.time() % (60 * 60 * 24) +
                                60 * 60 * 19)
    else:
        await context.bot.send_message(
            chat_id=chat_id,
            text="You are not authorized to receive the balance information.")


def main():
    application = ApplicationBuilder().token(
        os.environ['TELEGRAM_API_KEY']).build()

    start_handler = CommandHandler('start', start, block=False)
    application.add_handler(start_handler)

    application.run_polling()


if __name__ == '__main__':
    main()