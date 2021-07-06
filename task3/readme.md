# Порядок установки

Настройте необходимые разрешения для доступа к Xserver из Docker

```
$ sudo xhost +local:root
```

Соберите образ из Dockerfile

```
$ sudo docker build -t myfirefox .
```

Запустите образ с указанными параметры сети и GUI

```
$ sudo docker run -it --env="DISPLAY" --net=host myfirefox
```

