import socket
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

Toplevel.resizable(True,True)