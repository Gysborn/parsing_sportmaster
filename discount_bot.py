from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import json, os

from main import get_json

token = os.getenv('TOKEN')
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)



@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = "Кроссовки"  # ["Кроссовки", "Видеокарты", "Гречка"]# Создаем кнопки
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Делаем размер поменьше
    keyboard.add(start_buttons)  # Добавляем с распаковкой

    await message.answer("Товары со скидкой", reply_markup=keyboard)


@dp.message_handler(Text(equals="Кроссовки"))
async def get_discount_sneakers(message: types.Message):
    await message.answer("Please waiting...")
    res = get_json()
    if res == 200:
        with open('collect_data.json', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            card = f"{hlink(item.get('name'), item.get('link'))}\n" \
                   f"{hbold('Название: ')} {item.get('name')}\n" \
                   f"{hbold('Прайс: ')} {item.get('price')}\n" \
                   f"{hbold('Прайс со скидкой: ')} -{item.get('discount_rate')}%: {item.get('price_retail')}🔥\n" \
                   f"{hbold('Прайс: ')} {item.get('price')}"
            await message.answer(card)
    else:
        await message.answer(f"Доступ к ресурсу ограничен {res}")


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
