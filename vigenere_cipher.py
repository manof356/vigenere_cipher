# from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QApplication, QMainWindow
#
# import sys
import string

# ords_of_rus_alphabet = list(range(1040, 1104)) + [1105, 1025]

# phrase = input()
# cipher_key = input()

phrase = "Порой люди, которые якобы ничего из себя не представляют совершают удивительные вещи"
cipher_key = "Тьюринг"
# phrase = "яяЯЯЯяяЯЯ"
# cipher_key = "ю"

language = "Rus"

rus_low_alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                    "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "ы", "ю", "я"]
rus_upp_alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                    'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Ы', 'Ю', 'Я']

eng_low_alphabet = string.ascii_lowercase
eng_upp_alphabet = string.ascii_uppercase

rus_eng_low_alph = {"rus": rus_low_alphabet, "eng": eng_low_alphabet}
rus_eng_upp_alph = {"rus": rus_upp_alphabet, "eng": eng_upp_alphabet}

result_alph = rus_eng_low_alph[language.lower()] + rus_eng_upp_alph[language.lower()]

l1 = "я"
l2 = "ю"
res = (rus_low_alphabet.index(l1) + rus_low_alphabet.index(l2)) % 33
print(rus_low_alphabet.index(l1), rus_low_alphabet.index(l2))
print(res)
print(rus_low_alphabet[res])


def del_all_punctuation(phrase: str):
    phrase_only_letters = ""
    for i in phrase:
        if i in result_alph:
            phrase_only_letters += i
    return phrase_only_letters


def repeat_key(key: str, phrase: str):
    new_phrase = del_all_punctuation(phrase)
    res = del_all_punctuation(key.lower())
    res *= (len(new_phrase) // len(key) + 1)
    return res[:len(new_phrase)]


def encrypt_it(phrase: str, key: str):
    new_phrase = del_all_punctuation(phrase)
    res_key = repeat_key(key, phrase)
    result = ""
    low_alph = rus_eng_low_alph[language.lower()]
    upp_alph = rus_eng_upp_alph[language.lower()]
    for i, j in zip(new_phrase, res_key):
        if i in result_alph:
            if i.islower():
                res_index = (low_alph.index(i) + 1 + low_alph.index(j) + 1) % (len(low_alph) - 1)
                result += low_alph[res_index]
            else:
                res_index = (upp_alph.index(i) + 1 + low_alph.index(j) + 1) % (len(upp_alph) - 1)
                result += upp_alph[res_index]
        else:
            result += i
    return result


def encrypt_phrase(phrase: str, key: str):
    res_phrase_only_letters = encrypt_it(phrase, key)
    result = ""
    j = 0
    for i in phrase:
        if i in result_alph:
            result += res_phrase_only_letters[j]
            j += 1
        else:
            result += i
    return result


site_res = "Вкоят щбце, ияыьунб эычою аеххль лъ нгсз ыз вмгфъагфзэоы ясфбоиилх ёажтсазюшллн пзле"

# print(del_all_punctuation(phrase))
# print(repeat_key(cipher_key, phrase))
# print(encrypt_it(phrase, cipher_key))
#
# print(encrypt_phrase(phrase, cipher_key))
# print(site_res)
# print(phrase)
# print(site_res == encrypt_phrase(phrase, cipher_key))
