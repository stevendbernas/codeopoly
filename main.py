import tkinter as tk
from io import StringIO
from tkinter import scrolledtext
from tkinter import *
from PIL import ImageTk, Image
from interpreter import interpreter as GAME_PIECE
from interpreter3 import interpreter as interpreter3
from interpreter2 import interpreter as interpreter2

def interpret_program():
    program = code_editor.get("1.0", tk.END)
    interpreter = interpreter_selection.get()
    
    sys.stdout = output_buffer = StringIO()
    
    if interpreter == "GAME PIECE":
        GAME_PIECE(program)
    elif interpreter == "COLLECT PASS GO":
        interpreter3(program)
    elif interpreter == "WIN OR LOSE":
        interpreter2(program)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output_buffer.getvalue().upper()) 
    sys.stdout = sys.__stdout__

def open_help_file():
    with open("help.txt", "r") as file:
        help_content = file.read()
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, help_content.upper())  

def open_sample_programs_file():

    file = open("sample_programs.txt", "r")
    

    sample_programs_content = file.read()    

    output_text.delete("1.0", tk.END)
    
    output_text.insert(tk.END, sample_programs_content.upper())



root = tk.Tk()
root.title("CODEOPOLY - CODING MONOPOLY PHRASES")

font_style = ("Mulish", 16, "bold")  


font_colors = {
    "label": "blue",
    "button1": "orange",
    "button2": "red",
    "button3": "green",
    "dropdown": "purple"  
}

opened_image = Image.open("codeopoly.png")
resized_image = opened_image.resize((250, 250))
logo_image = ImageTk.PhotoImage(resized_image)
logo_label = tk.Label(root, image=logo_image)
logo_label.pack()

code_frame = tk.Frame(root)
code_frame.pack(pady=5)

code_label = tk.Label(code_frame, text="READY TO PLAY! \n\n INPUT: ".upper(), font=font_style, fg=font_colors["label"])
code_label.pack()

code_editor = scrolledtext.ScrolledText(code_frame, width=75, height=7, font=font_style)
code_editor.pack()

interpreter_frame = tk.Frame(root)
interpreter_frame.pack(pady=5)

interpreter_label = tk.Label(interpreter_frame, text="SELECT A PROGRAM".upper(), font=font_style, fg=font_colors["label"])
interpreter_label.pack(side=tk.LEFT)

interpreters = ["GAME PIECE", "COLLECT PASS GO", "WIN OR LOSE"]
interpreter_selection = tk.StringVar(root)
interpreter_selection.set(interpreters[0])
interpreter_dropdown = tk.OptionMenu(interpreter_frame, interpreter_selection, *interpreters)
interpreter_dropdown.config(font=font_style, fg=font_colors["dropdown"], bg="white")
interpreter_dropdown["menu"].config(font=font_style)
interpreter_dropdown.pack(side=tk.LEFT)

interpret_button = tk.Button(
    root,
    text="RUN PROGRAM".upper(),
    command=interpret_program,
    font=font_style,
    fg=font_colors["button1"],
    bg="white"
)

interpret_button.pack(pady=5)

help_button = tk.Button(
    root,
    text="HELP".upper(),
    command=open_help_file,
    font=font_style,
    fg=font_colors["button2"],
    bg="white"
)

help_button.pack(pady=5)

sample_programs_button = tk.Button(
    root,
    text="SAMPLE PROGRAMS".upper(),
    command=open_sample_programs_file,
    font=font_style,
    fg=font_colors["button3"],
    bg="white"
)

sample_programs_button.pack(pady=5)

output_frame = tk.Frame(root)
output_frame.pack(pady=5)

output_label = tk.Label(output_frame, text="Output:".upper(), font=font_style, fg=font_colors["label"])
output_label.pack()

output_text = scrolledtext.ScrolledText(output_frame, width=75, height=10, font=font_style)
output_text.pack()

root.mainloop()
