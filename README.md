# Обрезка ссылок с помощью Битли

Данный проект - это простая утилита для сокращения ссылок, взаимодействующая с API Bitly. Поможет сформировать короткую ссылку, а также посмотреть статистику переходов по ней.

### Как установить

Для взаимодействия с API Bitly, необходим токен. Для этого зарегистрируйтесь на сайте Bitly по ссылке (https://bitly.com/a/oauth_apps). Далее перейдите в раздел "Generic Access Token" и сгенерируйте токен по кнопке "GENERATE TOKEN". Токен будет выглядеть, как строка наподобие следующей: 
```
"17c09e20ad155405123ac1977542fecf00231da7"
```

Далее нужно создать файл .env в папке проекта и прописать токен, вот так:
```
TOKEN=17c09e20ad155405123ac1977542fecf00231da7
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Простой пример использования

Сокращение ссылки proglib.io/p/let-us-learn-program/
```
iMac-Andrej:bitly anderskate$ python main.py https://proglib.io/p/let-us-learn-program/
{'created_at': '1970-01-01T00:00:00+0000', 'id': 'bit.ly/2V4d08Z', 'link': 'http://bit.ly/2V4d08Z', 'custom_bitlinks': [], 'long_url': 'https://proglib.io/p/let-us-learn-program/', 'archived': False, 'tags': [], 'deeplinks': [], 'references': {'group': 'https://api-ssl.bitly.com/v4/groups/Bj2mlFawUJC'}}
```
Узнать количество переходов по сокращенной ссылке bit.ly/2TdQ9KE
```
iMac-Andrej:bitly anderskate$ python main.py http://bit.ly/2TdQ9KE
{"unit_reference":"2019-03-31T17:11:37+0000","total_clicks":8,"units":-1,"unit":"day"}
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
