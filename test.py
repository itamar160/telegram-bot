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



def get_reply(msg):
    sleep(3)
    return app.get_messages(bot_name, msg.id + 1)


async def run_test(application):
    # text test
    msg = await application.send_message(bot_name, "hello world")
    sleep(3)
    msg = await application.get_messages(msg.chat.id, msg.id + 1)
    check_response("error", msg.text)

    # photo test
    photo = "tal-haircut-min.jpg"
    msg = await application.send_photo(bot_name, photo)
    sleep(3)
    msg = await application.get_messages(msg.chat.id, msg.id + 1)
    check_response("hash", msg.text)

    # document test
    doc = "example.txt"
    msg = await application.send_document(bot_name, doc)
    sleep(3)
    msg = await application.get_messages(msg.chat.id, msg.id + 1)
    check_response("error", msg.text)

    #photo as document test
    doc = "tal-haircut-min.jpg"
    msg = await application.send_document(bot_name, doc)
    sleep(3)
    msg = await application.get_messages(msg.chat.id, msg.id + 1)
    check_response("hash", msg.text)

api_id = 19357400
api_hash = "df8be97dbdcf7c87877d25367a2f5548"
bot_name = "@image_hash_nso_bot"
CHAT_ID = 7229892701
PHONE_NUMBER = "972587755489"



async def main():
    async with Client("tester", api_id, api_hash, phone_number=PHONE_NUMBER) as app:
        await run_test(app)


asyncio.run(main())



