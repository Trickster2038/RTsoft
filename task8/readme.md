# OpenCV + Rest

## Архитектура

- основная программа (main.py)
- промежуточный http-сервер (server.py)
- управляющая программа (remote.py)

## Порядок запуская

- установить необходимые библиотеки через pip
- запустить программы в следующем порядке
```
$ python3 server.py
$ python3 remote.py
$ python3 main.py
```
По умолчанию видео находится в режиме play,  для преключения режимов следуйте подсказкам remote.py

## Скриншоты

GUI основной программы (main.py)

![](screens/screen1.png)

Лог основной программы (main.py)

![](screens/screen2.png)

Лог http-сервера (server.py)

![](screens/screen4.png)

Интерактивная консоль управляющей программы (remote.py)

![](screens/screen3.png)