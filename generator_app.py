from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from generatorlib import GeneratorLib
import sys
import os
import pyperclip
import settings
from validator import Validate


class NewGrid(GridLayout):

    def __init__(self, **kwargs):
        super(NewGrid, self).__init__(**kwargs)
        self.hash_algo_index = 1

    def set_hash_algo(self, instance):
        self.ids.sha256btn.background_color = "#928E85"
        self.ids.sha384btn.background_color = "#928E85"
        self.ids.sha512btn.background_color = "#928E85"
        # instance.color = "#000000"
        instance.background_color = "#94e5ff"
        self.hash_algo_index = 1 if instance.value == "" else int(instance.value)

    def copy_to_clipboard(self, instance):
        pyperclip.copy(self.ids.pwdresulttxtbox.text)

    def invoke(self, instance):
        self.ids.passlentxtbox.value = pwd_len = (
            settings.PASSWORD_MAX_LENGTH) if not Validate.validate_pwd_length(self.ids.passlentxtbox.text)\
            else int(self.ids.passlentxtbox.text)
        genlib = GeneratorLib(self.ids.usertxtbox.text, pwd_len, self.hash_algo_index)
        self.ids.pwdresulttxtbox.text = pwd_result = genlib.getpassword()
        print(pwd_result)


class MyApp(App):
    def build(self):
        return NewGrid()


def resourcePath():
    """
    Returns path containing content - either locally or in pyinstaller tmp file
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)

    return os.path.join(os.path.abspath("."))


if __name__ == "__main__":
    MyApp().run()
