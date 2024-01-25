"""Функція normalize:

приймає на вхід рядок та повертає рядок;
проводить транслітерацію кириличних символів на латиницю;
замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
великі літери залишаються великими, а маленькі — маленькими після транслітерації."""


import re

CYRILLIC_SYMBOLS = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
TRANSLATION = ("a", "b", "v", "h", "g", "d", "e", "ye", "j", "z", "i", "y", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "kh", "ts", "ch", "sh", "sch", "", "yu", "ya")


TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name

