from telegram import Bot
import cv2


async def send_message(text, uid, token):
    if len(text) == 0 or len(uid) == 0 or len(token) == 0:
        return
    bot = Bot(token)
    async with bot:
        try:
            await bot.send_message(uid, text)
        except:
            print('Error sending telegram message')


async def send_image(path, text, uid, token, crop=False):
    if len(path) == 0 or len(uid) == 0 or len(token) == 0:
        return
    if crop:
        img = cv2.imread(path)
        cropped_img = img[260:1150, 20:880]
        path = 'last_purchase.png'
        cv2.imwrite(path, cropped_img)
    bot = Bot(token)
    async with bot:
        if len(text) == 0:
            try:
                await bot.send_photo(chat_id=uid, photo=path)
            except:
                print('Error sending telegram message')
        else:
            try:
                await bot.send_photo(chat_id=uid, photo=path, caption=text)
            except:
                print('Error sending telegram message')
