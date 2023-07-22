import base64
import tkinter as tk
from tkinter import filedialog

def html_to_shtml(html_file_path, shtml_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    encoded_content = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    with open(shtml_file_path, 'w', encoding='utf-8') as shtml_file:
        shtml_file.write(encoded_content)

def shtml_to_html(shtml_file_path, html_file_path):
    with open(shtml_file_path, 'r', encoding='utf-8') as shtml_file:
        encoded_content = shtml_file.read()
    decoded_content = base64.b64decode(encoded_content).decode('utf-8')
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(decoded_content)

def choose_input_file():
    input_file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html"), ("SHTML Files", "*.shtml")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_file_path)

def choose_output_file():
    output_file_path = filedialog.asksaveasfilename(defaultextension=".shtml", filetypes=[("SHTML Files", "*.shtml")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_file_path)

def convert_file():
    input_file = input_entry.get()
    output_file = output_entry.get()
    if choice_var.get() == 1:
        html_to_shtml(input_file, output_file)
        status_label.config(text="Conversion completed: HTML to SHTML")
    elif choice_var.get() == 2:
        shtml_to_html(input_file, output_file)
        status_label.config(text="Conversion completed: SHTML to HTML")

# Create the main application window
app = tk.Tk()
app.title("HTML-SHTML File Converter")

# Create the choice variable to track the selected operation
choice_var = tk.IntVar()

# Create radio buttons for choosing the conversion type
html_to_shtml_radio = tk.Radiobutton(app, text="HTML to SHTML", variable=choice_var, value=1)
shtml_to_html_radio = tk.Radiobutton(app, text="SHTML to HTML", variable=choice_var, value=2)

# Create labels and buttons for file selection and conversion
input_label = tk.Label(app, text="Input File:")
input_entry = tk.Entry(app, width=40)
input_button = tk.Button(app, text="Browse", command=choose_input_file)

output_label = tk.Label(app, text="Output File:")
output_entry = tk.Entry(app, width=40)
output_button = tk.Button(app, text="Browse", command=choose_output_file)

convert_button = tk.Button(app, text="Convert", command=convert_file)

status_label = tk.Label(app, text="", fg="green")

# Pack GUI elements into the window
html_to_shtml_radio.pack(anchor="w")
shtml_to_html_radio.pack(anchor="w")

input_label.pack(anchor="w")
input_entry.pack(side="left")
input_button.pack(side="right")

output_label.pack(anchor="w")
output_entry.pack(side="left")
output_button.pack(side="right")

convert_button.pack(pady=10)
status_label.pack()

# Start the main event loop
app.mainloop()