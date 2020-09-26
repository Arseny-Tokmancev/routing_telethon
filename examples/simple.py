from telethon_routing import Bot
from telethon_routing.utils import wrap_keyboard, wrap_inline
import asyncio
import random
import time

phrases = [
    'A blessing in disguise',
    'A dime a dozen',
    'Beat around the bush',
    'Better late than never',
    'Bite the bullet',
    'Break a leg',
    'Call it a day'
]

bot = Bot()

say_name = 'Say my name'
say_some = 'Say something'

@bot.on(command='/start')
async def start(event, data):
    await event.respond('hello!')
    await data.change_step('menu')
    await event.respond(
        'you are on menu',
        buttons = wrap_keyboard([say_name, say_some])
    )


@bot.on(step='menu', command=say_name)
async def say_my_name(event, data):
    user = await event.get_sender()
    await event.respond(f'your name is {user.first_name} {user.last_name}')


@bot.on(step='menu', command=say_some)
async def say_something(event, data):
    phrase = random.choice(phrases)
    await event.respond(
        phrase,
        buttons = wrap_inline([[('Another phrase', 'another')]])
    )


@bot.on(callback='another')
async def another_phrase(event, data, arguments):
    phrase = random.choice(phrases)
    await event.edit(
        phrase,
        buttons = wrap_inline([[('Another phrase', 'another')]])
    )


async def main(api_id, api_hash, bot_token):
    random.seed(time.time())
    await bot.connect(api_id, api_hash, bot_token)
    await bot.run_forever()


if __name__=='__main__':
    asyncio.run(main(1, 'asdfghjk','1:asdfghjk'))
