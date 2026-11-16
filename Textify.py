
import tkinter as tk
from tkinter import messagebox, filedialog
from collections import Counter

# ================= WINDOW =================

root = tk.Tk()
root.title("String Studio Pro")
root.geometry("1050x720")
root.minsize(750, 550)
root.configure(bg="#F3F6FC")

# ================= COLORS =================

BG = "#F3F6FC"
WHITE = "#FFFFFF"
PURPLE = "#635BDB"
LIGHT_PURPLE = "#EEEDFF"
BLUE = "#EAF3FF"
TEXT = "#252B42"
GREY = "#8490A5"
GREEN = "#16A085"
RED = "#E85D75"

current_result = ""

# ================= SIDEBAR =================

sidebar = tk.Frame(root, bg=WHITE, width=200)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

tk.Label(
    sidebar,
    text="✦ STRING\n   STUDIO",
    font=("Arial", 21, "bold"),
    fg=PURPLE,
    bg=WHITE,
    justify="left"
).pack(anchor="w", padx=20, pady=30)

tk.Label(
    sidebar,
    text="TEXT TOOLS",
    font=("Arial", 10, "bold"),
    fg=GREY,
    bg=WHITE
).pack(anchor="w", padx=20, pady=10)

# ================= SCROLLABLE CONTENT =================

container = tk.Frame(root, bg=BG)
container.pack(side="left", fill="both", expand=True)

canvas = tk.Canvas(
    container,
    bg=BG,
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    container,
    orient="vertical",
    command=canvas.yview
)

main = tk.Frame(canvas, bg=BG)

window_id = canvas.create_window(
    (0, 0),
    window=main,
    anchor="nw"
)

def update_scroll(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

def resize_main(event):
    canvas.itemconfigure(window_id, width=event.width)

main.bind("<Configure>", update_scroll)
canvas.bind("<Configure>", resize_main)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Mouse wheel scrolling
def mouse_scroll(event):
    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )

canvas.bind_all("<MouseWheel>", mouse_scroll)

# ================= FUNCTIONS =================

def get_word():
    return word_entry.get()

def display_result(title, result):
    global current_result

    current_result = str(result)

    result_title.config(text=title)

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", current_result)
    result_text.config(state="disabled")

    result_text.update_idletasks()

def uppercase():
    display_result("UPPERCASE", get_word().upper())

def lowercase():
    display_result("LOWERCASE", get_word().lower())

def reverse():
    display_result("REVERSED WORD", get_word()[::-1])

def length():
    word = get_word()

    display_result(
        "STRING LENGTH",
        f"Characters: {len(word)}\n"
        f"Characters without spaces: {len(word.replace(' ', ''))}"
    )

def word_count():
    word = get_word()
    display_result("WORD COUNT", f"Total Words: {len(word.split())}")

def title_case():
    display_result("TITLE CASE", get_word().title())

def count_vowels():
    word = get_word().lower()

    vowels = sum(c in "aeiou" for c in word)
    consonants = sum(
        c.isalpha() and c not in "aeiou"
        for c in word
    )
    digits = sum(c.isdigit() for c in word)

    display_result(
        "TEXT ANALYSIS",
        f"Vowels: {vowels}\n"
        f"Consonants: {consonants}\n"
        f"Digits: {digits}\n"
        f"Spaces: {word.count(' ')}"
    )

def palindrome():
    word = get_word()

    cleaned = ''.join(
        c.lower() for c in word if c.isalnum()
    )

    if cleaned and cleaned == cleaned[::-1]:
        display_result("PALINDROME CHECK", "Yes! This is a Palindrome.")
    else:
        display_result("PALINDROME CHECK", "No! This is not a Palindrome.")

def remove_spaces():
    display_result("REMOVE SPACES", get_word().replace(" ", ""))

def duplicate_letters():
    word = get_word()
    result = ''.join(dict.fromkeys(word))
    display_result("REMOVE DUPLICATES", result)

def frequency():
    word = get_word()
    counts = Counter(word)

    result = "\n".join(
        f"{repr(char)} : {count}"
        for char, count in counts.items()
    )

    display_result("CHARACTER FREQUENCY", result or "No characters")

def update_word():
    new_word = new_entry.get()

    if not new_word:
        messagebox.showwarning("Warning", "Enter a new word!")
        return

    word_entry.delete(0, tk.END)
    word_entry.insert(0, new_word)

    display_result("UPDATED WORD", new_word)

def combine():
    first = get_word()
    second = new_entry.get()

    display_result("COMBINED WORD", first + second)

def find_replace():
    word = get_word()
    old = old_entry.get()
    new = replace_entry.get()

    if not old:
        messagebox.showwarning("Warning", "Enter text to find!")
        return

    display_result("FIND & REPLACE", word.replace(old, new))

def copy_result():
    if current_result:
        root.clipboard_clear()
        root.clipboard_append(current_result)
        messagebox.showinfo("Success", "Result copied!")

def save_result():
    if not current_result:
        messagebox.showwarning("Warning", "No result to save!")
        return

    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if path:
        with open(path, "w", encoding="utf-8") as file:
            file.write(current_result)

        messagebox.showinfo("Saved", "File saved successfully!")

def clear_all():
    word_entry.delete(0, tk.END)
    new_entry.delete(0, tk.END)
    old_entry.delete(0, tk.END)
    replace_entry.delete(0, tk.END)

    display_result("YOUR RESULT", "Your result will appear here...")

# ================= HEADER =================

header = tk.Frame(main, bg=BG)
header.pack(fill="x", padx=30, pady=25)

tk.Label(
    header,
    text="Welcome to String Studio",
    font=("Arial", 22, "bold"),
    fg=TEXT,
    bg=BG
).pack(anchor="w")

tk.Label(
    header,
    text="Your smart text manipulation workspace",
    font=("Arial", 11),
    fg=GREY,
    bg=BG
).pack(anchor="w", pady=5)

# ================= ENTRY DESIGN =================

def create_label(parent, text):
    tk.Label(
        parent,
        text=text,
        font=("Arial", 10, "bold"),
        fg=TEXT,
        bg=WHITE
    ).pack(anchor="w", pady=(5, 7))

def create_entry(parent):
    entry = tk.Entry(
        parent,
        font=("Arial", 12),
        bg="#F5F7FC",
        fg=TEXT,
        relief="flat",
        insertbackground=PURPLE
    )
    entry.pack(fill="x", ipady=9, pady=(0, 12))
    return entry

# ================= INPUT CARD =================

input_card = tk.Frame(main, bg=WHITE, padx=20, pady=18)
input_card.pack(fill="x", padx=30, pady=8)

create_label(input_card, "Enter Your Word")
word_entry = create_entry(input_card)

create_label(input_card, "New / Second Word")
new_entry = create_entry(input_card)

# ================= OPERATIONS CARD =================

operations_card = tk.Frame(main, bg=WHITE, padx=20, pady=15)
operations_card.pack(fill="x", padx=30, pady=8)

tk.Label(
    operations_card,
    text="Text Operations",
    font=("Arial", 14, "bold"),
    fg=TEXT,
    bg=WHITE
).pack(anchor="w", pady=(0, 12))

button_frame = tk.Frame(operations_card, bg=WHITE)
button_frame.pack(fill="x")

operations = [
    ("ABC Uppercase", uppercase),
    ("abc Lowercase", lowercase),
    ("Reverse", reverse),
    ("Length", length),
    ("Word Count", word_count),
    ("Title Case", title_case),
    ("Vowels & Consonants", count_vowels),
    ("Palindrome", palindrome),
    ("Remove Spaces", remove_spaces),
    ("Remove Duplicates", duplicate_letters),
    ("Character Frequency", frequency),
    ("Update Word", update_word),
    ("Combine Words", combine),
]

for i, (name, command) in enumerate(operations):
    tk.Button(
        button_frame,
        text=name,
        command=command,
        font=("Arial", 9, "bold"),
        bg=LIGHT_PURPLE if i % 2 == 0 else BLUE,
        fg=PURPLE,
        activebackground=PURPLE,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        pady=10
    ).grid(
        row=i // 3,
        column=i % 3,
        sticky="ew",
        padx=5,
        pady=5
    )

for i in range(3):
    button_frame.columnconfigure(i, weight=1)

# ================= FIND & REPLACE =================

replace_card = tk.Frame(main, bg=WHITE, padx=20, pady=15)
replace_card.pack(fill="x", padx=30, pady=8)

tk.Label(
    replace_card,
    text="Find & Replace",
    font=("Arial", 13, "bold"),
    fg=TEXT,
    bg=WHITE
).pack(anchor="w", pady=(0, 8))

create_label(replace_card, "Find Text")
old_entry = create_entry(replace_card)

create_label(replace_card, "Replace With")
replace_entry = create_entry(replace_card)

tk.Button(
    replace_card,
    text="Find & Replace",
    command=find_replace,
    bg=PURPLE,
    fg=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    pady=9
).pack(fill="x")

# ================= RESULT CARD =================

result_card = tk.Frame(main, bg=WHITE, padx=20, pady=15)
result_card.pack(fill="both", expand=True, padx=30, pady=8)

result_title = tk.Label(
    result_card,
    text="YOUR RESULT",
    font=("Arial", 12, "bold"),
    fg=PURPLE,
    bg=WHITE
)
result_title.pack(anchor="w", pady=(0, 10))

result_text = tk.Text(
    result_card,
    height=7,
    font=("Consolas", 12),
    bg="#F5F7FC",
    fg=GREEN,
    relief="flat",
    wrap="word",
    padx=12,
    pady=12
)
result_text.pack(fill="both", expand=True)

result_text.insert("1.0", "Your result will appear here...")
result_text.config(state="disabled")

# ================= FOOTER =================

footer = tk.Frame(result_card, bg=WHITE)
footer.pack(fill="x", pady=(12, 0))

def footer_button(name, command, color):
    tk.Button(
        footer,
        text=name,
        command=command,
        bg=color,
        fg=WHITE,
        font=("Arial", 9, "bold"),
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=9
    ).pack(side="left", padx=(0, 8))

footer_button("Copy Result", copy_result, GREEN)
footer_button("Save TXT", save_result, PURPLE)
footer_button("Clear All", clear_all, RED)

# ================= RUN =================

display_result("YOUR RESULT", "Your result will appear here...")

root.mainloop()
