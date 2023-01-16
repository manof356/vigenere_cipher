from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow
import sys, string


class MainWindow(QMainWindow):
    """
    Main window class
    """

    def __init__(self):
        """
        Constructor of main window
        """
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi('cipher Vigenere.ui', baseinstance=self)

        self.textEdit_phrase = self.findChild(QtWidgets.QTextEdit, 'textEdit_phrase')
        self.textEdit_key = self.findChild(QtWidgets.QTextEdit, 'textEdit_key')

        self.textBrowser_res = self.findChild(QtWidgets.QTextBrowser, 'textBrowser_res')
        self.radioButton_ENC = self.findChild(QtWidgets.QRadioButton, "radioButton_ENC")

        self.radioButton_RUS = self.findChild(QtWidgets.QRadioButton, "radioButton_RUS")
        self.pushButton_get_res = self.findChild(QtWidgets.QPushButton, 'pushButton_get_res')

        self.pushButton_get_res.clicked.connect(self.show_result)

    def show_result(self):
        main_phrase = self.textEdit_phrase.toPlainText()
        cipher_key = self.textEdit_key.toPlainText()
        encrypt_or_decrypt = self.radioButton_ENC.isChecked()
        language = self.radioButton_RUS.isChecked()
        self.textBrowser_res.setText(encrypt_phrase(main_phrase, cipher_key, language, encrypt_or_decrypt))


RUS_low_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

RUS_upp_alphabet = RUS_low_alphabet.upper()

ENG_low_alphabet = string.ascii_lowercase
ENG_upp_alphabet = string.ascii_uppercase

RUS_ENG_low_alph = [ENG_low_alphabet, RUS_low_alphabet]
RUS_ENG_upp_alph = [ENG_upp_alphabet, RUS_upp_alphabet]


def result_alph(lang: bool):
    global low_alph, upp_alph
    low_alph = RUS_ENG_low_alph[lang]
    upp_alph = RUS_ENG_upp_alph[lang]
    return low_alph + upp_alph


def del_all_punctuation(phrase: str, language: bool):
    """
    deletes all punctuations in phrase
    :param phrase: phrase to encrypt or decrypt
    :return: phase without any punctuations
    """
    res_alph = result_alph(language)
    phrase_only_letters = ""
    for i in phrase:
        if i in res_alph:
            phrase_only_letters += i
    return phrase_only_letters


def repeat_key(key: str, phrase: str, language: bool):
    """
    loops key as many times as length phrase
    :param key: encryption key
    :param phrase: phrase to encrypt or decrypt. it is needed to count its length
    :return: looped key
    """
    new_phrase = del_all_punctuation(phrase, language)
    new_key = del_all_punctuation(key, language)
    res = del_all_punctuation(key.lower(), language)
    res *= (len(new_phrase) // len(new_key) + 1)
    return res[:len(new_phrase)]


def en_or_de_crypt_it(phrase: str, key: str, language: bool, en_or_de: bool = True):
    """
    encrypts or decrypts phase with key without any punctuations
    :param phrase: phrase to encrypt or decrypt
    :param key: encryption key
    :param en_or_de: encrypt = True, decrypt = False
    :return: encrypted/decrypted phrase without any punctuations
    """
    new_phrase = del_all_punctuation(phrase, language)
    res_key = repeat_key(key, phrase, language)
    res_alph = result_alph(language)
    result = ""
    for i, j in zip(new_phrase, res_key):
        if i in res_alph:
            if i.islower():
                res_index = (low_alph.index(i) + [-1, 1][en_or_de] * low_alph.index(j)) % len(low_alph)
                result += low_alph[res_index]
            else:
                res_index = (upp_alph.index(i) + [-1, 1][en_or_de] * low_alph.index(j)) % len(upp_alph)
                result += upp_alph[res_index]
        else:
            result += i
    return result


def encrypt_phrase(phrase: str, key: str, language: bool, en_or_de: bool = True):
    """
    encrypts or decrypts phase with key and with punctuation according to entry phrase
    :param phrase: phrase to encrypt or decrypt
    :param key: encryption key
    :return: phrase with punctuation according to entry phrase
    """
    res_phrase_only_letters = en_or_de_crypt_it(phrase, key, language, en_or_de)
    res_alph = result_alph(language)
    result = ""
    j = 0
    for i in phrase:
        if i in res_alph:
            result += res_phrase_only_letters[j]
            j += 1
        else:
            result += i
    return result


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
