import asyncio
from playwright.async_api import async_playwright

async def run(playwright):

    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()


    await page.goto("https://www.saucedemo.com/")
    await asyncio.sleep(2)

    # Авторизация
    await page.fill('#user-name', 'standard_user')
    await asyncio.sleep(2)
    await page.fill('#password', 'secret_sauce')
    await asyncio.sleep(2)
    await page.click('#login-button')
    await asyncio.sleep(2)

    # Выбор товара и добавление в корзину
    await page.click('#add-to-cart-sauce-labs-backpack')
    await asyncio.sleep(2)  # Задержка 5 секунд
    await page.click('.shopping_cart_link')
    await asyncio.sleep(2)  # Задержка 5 секунд

    #Оформление заказа
    await page.click('#checkout')
    await asyncio.sleep(2)  # Задержка 5 секунд
    await page.fill('#first-name', 'Test')
    await asyncio.sleep(2)  # Задержка 5 секунд
    await page.fill('#last-name', 'User')
    await asyncio.sleep(2)  # Задержка 5 секунд
    await page.fill('#postal-code', '12345')
    await asyncio.sleep(2)  # Задержка 5 секунд
    await page.click('#continue')
    await asyncio.sleep(2)  # Задержка 5 секунд

    # Завершение покупки
    await page.click('#finish')
    await asyncio.sleep(2)  # Задержка 5 секунд

    # Ожидание появления подтверждающего сообщения
    await page.wait_for_selector('.complete-header')
    await asyncio.sleep(2)

    # Проверка успешного завершения
    confirmation_message = await page.text_content('.complete-header')
    print(f"Confirmation message: {confirmation_message}")


    assert "thank you for your order" in confirmation_message.lower(), "Покупка не завершена успешно."


    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

# Запуск
asyncio.run(main())
