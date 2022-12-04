# from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QApplication, QMainWindow
#
# import sys

import string

main_phrase = "How many Children do you have?"
cipher_key = "I have five kids, thanks for you queStion"

language = "Eng"
encrypt_or_decrypt = True

rus_low_alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с",
                    "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

rus_upp_alphabet = list(map(lambda x: x.upper(), rus_low_alphabet))

eng_low_alphabet = string.ascii_lowercase
eng_upp_alphabet = string.ascii_uppercase

rus_eng_low_alph = {"rus": rus_low_alphabet, "eng": eng_low_alphabet}
rus_eng_upp_alph = {"rus": rus_upp_alphabet, "eng": eng_upp_alphabet}

low_alph = rus_eng_low_alph[language.lower()]
upp_alph = rus_eng_upp_alph[language.lower()]
result_alph = low_alph + upp_alph


def del_all_punctuation(phrase: str):
    """
    deletes all punctuations in phrase
    :param phrase: phrase to encrypt or decrypt
    :return: phase without any punctuations
    """
    phrase_only_letters = ""
    for i in phrase:
        if i in result_alph:
            phrase_only_letters += i
    return phrase_only_letters


def repeat_key(key: str, phrase: str):
    """
    loops key as many times as length phrase
    :param key: encryption key
    :param phrase: phrase to encrypt or decrypt. it is needed to count its length
    :return: looped key
    """
    new_phrase = del_all_punctuation(phrase)
    res = del_all_punctuation(key.lower())
    res *= (len(new_phrase) // len(key) + 1)
    return res[:len(new_phrase)]


def en_or_de_crypt_it(phrase: str, key: str, en_or_de: bool = True):
    """
    encrypts or decrypts phase with key without any punctuations
    :param phrase: phrase to encrypt or decrypt
    :param key: encryption key
    :param en_or_de: encrypt = True, decrypt = False
    :return: encrypted/decrypted phrase without any punctuations
    """
    new_phrase = del_all_punctuation(phrase)
    res_key = repeat_key(key, phrase)
    result = ""
    for i, j in zip(new_phrase, res_key):
        if i in result_alph:
            if i.islower():
                res_index = (low_alph.index(i) + [-1, 1][en_or_de] * low_alph.index(j)) % (len(low_alph))
                result += low_alph[res_index]
            else:
                res_index = (upp_alph.index(i) + [-1, 1][en_or_de] * low_alph.index(j)) % (len(upp_alph))
                result += upp_alph[res_index]
        else:
            result += i
    return result


def encrypt_phrase(phrase: str, key: str, en_or_de: bool = True):
    """
    encrypts or decrypts phase with key and with punctuation according to entry phrase
    :param phrase: phrase to encrypt or decrypt
    :param key: encryption key
    :return: phrase with punctuation according to entry phrase
    """
    res_phrase_only_letters = en_or_de_crypt_it(phrase, key, en_or_de)
    result = ""
    j = 0
    for i in phrase:
        if i in result_alph:
            result += res_phrase_only_letters[j]
            j += 1
        else:
            result += i
    return result


print(encrypt_phrase(main_phrase, cipher_key, encrypt_or_decrypt))
