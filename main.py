import tkinter as tk
from tkinter import filedialog, IntVar, StringVar
from os.path import expanduser


# Okno glowne
window = tk.Tk()
window.title("Traffic Intensity Calculation Methods Visualization")
window.geometry("720x720")
window.resizable(False, False)
window.configure(bg="#606166")


#funkcje

def browse_input_file():
    input_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("TXT files", "*.txt")], initialdir=expanduser("~") + "/Desktop/")
    if input_file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, input_file_path)
#Funkcja generate
def generate_chart():
    input_data = entry_file_path.get()
    with open(input_data, "r") as myfile:
        for el in myfile:
            print(el)





# Wybieranie metody liczenia
button_frame = tk.Frame(window, width=720, height=720)
button_frame.configure(bg="#606166")
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


# Wybieranie metody uploadowania danych
# input_label_data = tk.Label(window, text="Choose ")
input_button = tk.Button(button_frame, text="Input your data")
input_button.grid(row=2, padx=20, pady=5, columnspan=3)
file_button = tk.Button(button_frame, text="Choose from file", command = browse_input_file)
file_button.grid(row=3, column=1, padx=20, pady=5)

text = StringVar(button_frame)
file_path = StringVar(button_frame)

# Wpisywanie sciezki pliku
entry_file_path = tk.Entry(button_frame, textvariable=file_path)
entry_file_path.grid(row=3, column=2)

#zakres
input_range = tk.Entry(button_frame, textvariable=text)
input_range.grid(row = 4, columnspan=3)

#generator
generate_button = tk.Button(button_frame, text="Generate Chart", command=generate_chart)
generate_button.grid(row=5, columnspan=1, pady=20)


window.mainloop()
