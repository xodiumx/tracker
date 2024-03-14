# Task traker

## Принцип работы
- В поле заносится новая задача
- При нажатии на кнопку play задача перемещается на dashboard и создается в базе данных
- При нажатии на задачу, запускается таймер в формате `00 sec` - `1:00 min` - `1:00 hour`
- При каждом нажатии на задачу, время обновляется в базе данных
- На беке реализован CRUD по задачам

## Для запуска через Docker

1. Cклонируйте репозиторий
```
git clone https://github.com/xodiumx/tracker
```
2. В главной директории, создайте `.env` file:
```
SERVER_HOST=127.0.0.1
SERVER_PORT=8000

# DB_HOST=localhost
DB_HOST=db
DB_PORT=5432
DB_NAME=tracker
DB_USER=postgres
DB_PASS=admin

POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin
```
3. В директории `front` создайте `.env` file:
```
VITE_TASKS_API=http://localhost:8000/tasks
```
4. В главной директории выполните команду:
```
sudo docker-compose up -d
```

## Доступные эндпоинты

- Главный эндпоинт - `http://localhost:8080/`

## Tracker

<img width="1133" alt="tracker" src="https://github.com/xodiumx/tracker/assets/111197771/9f486fd1-fa36-47e8-8982-d4b25ff47a22">
