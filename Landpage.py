from customtkinter import *
from PIL import Image
# from stack_test import StackVisualizer

set_appearance_mode("light")

app = CTk()
app.title("Simulation Draft")
app.geometry("{}x{}".format(1000,600))
app.grid_rowconfigure((0,1,2,3), weight=1)
app.grid_columnconfigure((0,1,2,3,4,5), weight=1)

#Programs
def open_program_a():
    new_window = CTkToplevel(app)
    new_window.title("Program A")
    CTkLabel(new_window, text="This is Program A").pack()
    # Add specific widgets and logic for Program A here


# TOP FRAME
top = CTkFrame(app, height=50, fg_color="lightgrey")
top.grid(rowspan = 2, columnspan = 6, sticky='nsew', ipadx=5)
label1 = CTkLabel(top, text="Home", font=("Arial", 20))
label1.grid(row=0, column=0, padx=20, pady=20, sticky='w')

canvas = CTkCanvas(top, width=50, height=50, bg="lightgrey")
canvas.grid(row=1, column=0, padx=30, pady=10, sticky='e')
label2 = CTkLabel(top, text="Username", font=("Arial", 14))
label2.grid(row=1, column=1, sticky='w')

# BOTTOM FRAME
bottom = CTkFrame(app, height=500, fg_color="white")
bottom.grid(rowspan=5, columnspan=6, sticky='nsew', ipady=55, ipadx=5)
label3 = CTkLabel(bottom, text="Recommended for you", font=("Arial", 16))
label3.grid(row=0, column=0, padx=20, pady=20, sticky='w')
bottom.grid_rowconfigure(1, weight=1)
bottom.grid_columnconfigure((0,1,2,3,4), weight=1)

buttons_data = [
    ("Img/Stacks.png", "Stacks", open_program_a),
    ("Img/Queues.png", "Queues", open_program_a),
    ("Img/Xiao.png", "Binary Tree", open_program_a),
    ("Img/Xiao2.png", "Binary Search Tree", open_program_a),
    ("Img/Xiao.png", "Recursion", open_program_a),
]

for i, (img_file, text, cmd) in enumerate(buttons_data):
    pil_image = Image.open(img_file)
    tk_image = CTkImage(pil_image, size=(150, 150))

    btn = CTkButton(
        bottom,
        image=tk_image,
        compound=TOP,
        text=text,
        text_color="black",
        font=("Arial", 14),
        anchor='s',
        command=cmd,
        fg_color="white",
        border_width=0
    )

    btn.image = tk_image  # Prevent garbage collection
    btn.grid(row=1, column=i, padx=10, sticky='ne')




app.mainloop()

