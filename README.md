# Обрезка ссылок с помощью Bitly

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
http://bit.ly/2V4d08Z
```
Узнать количество переходов по сокращенной ссылке bit.ly/2TdQ9KE
```
iMac-Andrej:bitly anderskate$ python main.py http://bit.ly/2TdQ9KE
Количество переходов по ссылке bitly: 8
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
