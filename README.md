Я написал программу, которая "сканирует" подключенную по SSH операционную систему.
Интерфейс реализован с помощью Django, пользователь вводит логин, пароль, порт и ip машины
![image](input.jpg)
Далее происходит подключение, получение основной информации об ОС (ОС, версия, архитектура), затем данные передаются на сервер и выводятся 
в следующем формате:
![image](results.jpg)
Все полученные данные сохраняются в базу данных - Postgresql (логи выполненных команд также приложены)
