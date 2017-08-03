# Telegram Bot for Pizzeria

# Что это

Телеграм бот для пиццерии. С помощью команды "/menu" в чате бот отображает меню пиццерии. С помощью панели администратора можно изменять меню заведения.

# Как пользоваться

1. Регистрируем бота с помощью [@BotFather](https://telegram.me/botfather)
2. Устанавливаем путь к бд в переменной окружения
```
$ export db_uri="your_path"
```

3. Создаём и заполняем базу данных

```
$ python create_db.py
$ python fill_db.py

```
4. Запускаем телегра-бота
```
$ token="your_token" python bot.py
```
5. Для редактирования меню запускаем панель администратора (указываем юзернейм и пароль для ограничения доступа к панели администратора)
```
$ username="admin" password="secret" python server.py
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
