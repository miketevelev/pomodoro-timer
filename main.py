import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage


class PomodoroTimer():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodoro Timer")

PomodoroTimer()
