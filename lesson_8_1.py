"""
Напишите регулярное выражение, извлекающее e-mail адрес из текста
"""
import re

re_email = re.compile(r'[^\s]+[@]\w+[.][rucom]{2,3}')
text = 'My email xxfox.o@yandex.ru. Another one email: fox@gmail.com If you wanna write to my dog, use this email emmadog@bk.ru'
address = 'foxana@yandex.ru'
print(re_email.findall(text))
print(re_email.match(address))