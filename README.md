# PhoneNotes
Программа реализует записную книжку для телефонов. Можно выводить записи постранично (за страницу считается 3 строчки, легко поменять через константу line_in_page). Когда записи закончаться выведет сообщение об этом и закончит чтение
Через функцию add_line реализуется добавление записей по введенной информации, а через функцию edit_line редактирование, функция search реализует поиск по введенной информацмм.
Путь к файлу указан в константе PHONEBOOK. Выбор опции происходит в начале с помощью консоли с текстовым меню с описанием возможных опций.
Также используется namedtuple, который можно заменить обычным кортежем, но в данном случае просто удобнее обращаться по имени. 