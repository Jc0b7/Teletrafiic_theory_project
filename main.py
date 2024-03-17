import tkinter as tk
from tkinter import *


# Okno glowne
window = tk.Tk()
window.title("Traffic Intensity Calculation Methods Visualization")
window.geometry("720x720")
window.resizable(False, False)
window.configure(bg="#606166")

# Wybieranie metody liczenia



#Kontener
button_frame = tk.Frame(window, width=720, height=720)
button_frame.configure(bg="#606166", highlightbackground="red", highlightthickness="1")
button_frame.pack(pady = 50, padx=30)

input_label_methods = tk.Label(button_frame, text="Pick the calculation method")
input_label_methods.grid(row=0, column=0, columnspan=3, pady=10)

v = IntVar(button_frame)

method1_button = tk.Radiobutton(button_frame, text="Metoda 1", variable=v, value=1)
method1_button.grid(row=1, column=0, padx=20, pady=5)
method2_button = tk.Radiobutton(button_frame, text="Metoda 2", variable=v, value=2)
method2_button.grid(row=1, column=1, padx=20, pady=5)
method3_button = tk.Radiobutton(button_frame, text="Metoda 3", variable=v, value=3)
method3_button.grid(row=1, column=2, padx=20, pady=5)

#Wybieranie zakresu danych



# Wybieranie metody uploadowania danych
# input_label_data = tk.Label(window, text="Choose ")
input_button = tk.Button(button_frame, text="Input your data")
input_button.grid(row=2, padx=20, pady=5, columnspan=3)
file_button = tk.Button(button_frame, text="Choose from file")
file_button.grid(row=3, column=1, padx=20, pady=5)

window.mainloop()
