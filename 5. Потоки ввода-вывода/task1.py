'''Откройте и прочитайте данные с файла lorum.txt, способом, который рассматривается в видео из пункта 1.'''

# Открываем файл 'lorum.txt' в режиме чтения ('r') с использованием кодировки UTF-8
file = open('lorum.txt', mode='r', encoding='utf-8')
# Читаем содержимое файла и выводим его на экран
print(file.read())
# Закрываем файл, чтобы освободить системные ресурсы
file.close()

# Используем контекстный менеджер 'with' для открытия файла, который автоматически закроет файл после выхода из блока
with open('lorum.txt', mode='r', encoding='utf-8') as f:
    # Читаем и выводим содержимое файла на экран
    print(f.read())
# После выхода из блока 'with' файл уже закрыт, и мы выводим слово 'end' на экран
print('end')

