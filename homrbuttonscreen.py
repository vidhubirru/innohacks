# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:57:18 2023

@author: vidhu
"""
filename = "C:/Users/vidhu/onedrive/desktop/testqr5.py"
import kivy
from kivy.app import App
from kivy.uix.button import Button
import os
import time


class MyApp(App):
    def build(self):
        button = Button(text='Mark Your Atenndance', on_press=self.on_button_press)       
        #button = Button(text='Cry abt life', on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        print("12345")
        #os.open('qrcode.py',"1")
        os.system(f"python {filename}")


if __name__ == '__main__':
    MyApp().run()
