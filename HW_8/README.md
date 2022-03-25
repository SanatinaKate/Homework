Скрипт logs_parser.py предназначен для обработки лог-файлов с информацией о HTTP-запросах и выдачи статистики по каждому обработанному файлу Статистика включает в себя:

общее количество выполненных запросов
количество выполненных запросов для каждого HTTP-метода
топ-3 IP адресов, с которых были сделаны запросы
топ-3 самых долгих запросов
Формат запуска скрипта: python logs_parser.py -p <путь к лог-файлу или к директории с лог-файлами>

Лог-файлы - это файлы с расширением .log Если указан путь к конкретному лог-файлу, то обрабатывается только этот конкретный лог-файл Если указан путь к директории, то по очереди обрабатываются все лог-файлы, находящиеся в этой директории Статистика по каждому обработанному лог-файлу выводится в формате JSON в терминал, а также в файл <имя лог-файла>.log.json

Пример запуска скрипта: python logs_parser.py -p logs2/ Statistics for file logs2/access2.log: {
"HTTP REQUESTS": 1000,
"GET": 573,
"HEAD": 1,
"POST": 426,
"PUT": 0,
"PATCH": 0,
"DELETE": 0,
"CONNECT": 0,
"OPTIONS": 0,
"TRACE": 0,
"TOP-3 IP ADDRESSES BY SENT REQUESTS": [ { "IP ADDRESS": "191.182.199.16", "SENT REQUESTS": 37 }, { "IP ADDRESS": "188.45.108.168", "SENT REQUESTS": 31 }, { "IP ADDRESS": "37.1.206.196", "SENT REQUESTS": 18 } ], "TOP-3 REQUESTS BY DURATION": [ { "METHOD": "POST", "URL": "http://almhuette-raith.at/administrator/", "IP ADDRESS": "201.79.97.230", "DURATION": 9996, "DATE & TIME": "12/Dec/2015 23:54:27 +0100" }, { "METHOD": "POST", "URL": "http://almhuette-raith.at/administrator/", "IP ADDRESS": "189.13.146.143", "DURATION": 9989, "DATE & TIME": "12/Dec/2015 20:06:43 +0100" }, { "METHOD": "GET", "URL": "http://almhuette-raith.at/", "IP ADDRESS": "191.182.199.16", "DURATION": 9963, "DATE & TIME": "12/Dec/2015 19:02:40 +0100" } ] } Statistics is also saved into file logs2/access2.log.json