import tkinter as tk
import string as s
import random

root = tk.Tk()
root.title("Password Generator")
root.geometry("250x200")

#Colors
dark_bg = "#2D2D2D"
light_text = "#2D2D2D"
highlight_color = "#444444"
light_text_button = "#f4f4f4"

root.configure(bg=dark_bg)

#Add label
label = tk.Label(root, text="Hello!",
                 font=("Zain", 14), bg=dark_bg, fg=light_text)
label.pack(pady=10)

#Add frame for the password display and copy button
password_frame = tk.Frame(root, bg=dark_bg)
password_frame.pack(pady=5)

password_display = tk.Entry(password_frame, font=("Zain", 12), bd=0, relief=tk.FLAT, bg=highlight_color,
        fg=light_text,
        selectbackground="#555555",
        selectforeground=light_text,
        width=20,
        justify='center')
password_display.pack(side=tk.LEFT, padx=(0, 5))
password_display.config(state='readonly')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_display.get())
    # Flash the entry to show it was copied
    password_display.config(bg="#5D5D5D")
    password_display.after(100, lambda: password_display.config(bg=highlight_color))

copy_button = tk.Button(password_frame, text="Copy", command=copy_to_clipboard, bg=highlight_color,
       fg=light_text_button,
       activebackground=dark_bg,
       activeforeground=light_text,
       bd=0)
copy_button.pack(side=tk.LEFT)

icon_path = "assets/lock.png"
try:
    icon = tk.PhotoImage(file=icon_path)
    root.iconphoto(False, icon)
except Exception as e:
    print("Error loading icon:", e)

def on_button_click():
    s1 = list(s.ascii_lowercase)
    s2 = list(s.ascii_uppercase)
    s3 = list(s.digits)
    s4 = list(s.punctuation)

    characters_number = 12  # Specify password length

    #Shuffle the character lists
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    #Determine proportions for each character type
    part_1 = round(characters_number * (30 / 100))
    part_2 = round(characters_number * (20 / 100))

    password = []

    for i in range(part_1):
        password.append(s1[i])
        password.append(s2[i])
    for i in range(part_2):
        password.append(s3[i])
        password.append(s4[i])

    #Shuffle the final password list
    random.shuffle(password)
    password = "".join(password[:characters_number])

    #Update the label and display
    label.config(text="Your password is:")
    password_display.config(state='normal')
    password_display.delete(0, tk.END)
    password_display.insert(0, password)
    password_display.config(state='readonly')

#Add the button to the window
button = tk.Button(root, text="Generate Password", command=on_button_click,
        bg=highlight_color, fg=light_text_button, activebackground=dark_bg, activeforeground=light_text)
button.pack(pady=10)


root.mainloop()