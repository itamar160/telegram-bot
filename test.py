from time import sleep
from pyrogram import Client
import asyncio


def check_response(expected_value: str, received_value: str):
    if not received_value.startswith(expected_value):
        print("check failed: ")
    else:
        print("check passed: ")

    print(f"\tExpected: {expected_value} ")
    print(f"\tReceived: {received_value}\n")


async def run_test(application):
    # text test
    msg = await application.send_message(bot_name, "hello world")
    sleep(3)
    msg = await application.get_messages(msg.chat.id, msg.id + 1)
    check_response("error", msg.text)

    # photo test
    photo = "tal-haircut-min.jpg"
    msg = await application.send_photo(BOT_NAME, photo)
    sleep(2)
    msg = await application.get_messages(msg.chat.id, msg.id + 1)
    check_response("hash", msg.text)

    # document test
    doc = "example.txt"
    msg = await application.send_document(BOT_NAME, doc)
    sleep(2)
    msg = await application.get_messages(msg.chat.id, msg.id + 1)
    check_response("error", msg.text)

    #photo as document test
    doc = "tal-haircut-min.jpg"
    msg = await application.send_document(BOT_NAME, doc)
    sleep(2)
    msg = await application.get_messages(msg.chat.id, msg.id + 1)
    check_response("hash", msg.text)


API_ID = 12345
API_HASH = "api_hash"
PHONE_NUMBER = "972....."
BOT_NAME = "@image_hash_nso_bot"


async def main():
    async with Client("tester", API_ID, API_HASH, phone_number=PHONE_NUMBER) as app:
        await run_test(app)


asyncio.run(main())



