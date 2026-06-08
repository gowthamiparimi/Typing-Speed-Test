import tkinter as tk
import random
import time

sentences = [
    "Python is easy to learn",
    "Practice makes perfect",
    "Typing improves with practice",
    "Python is very important and essential for coding students"
]

def start():
    global start_time
    start_time = time.time()

def check(event):
    end_time = time.time()
    typed = entry.get()

    words = len(typed.split())
    wpm = (words / (end_time - start_time)) * 60

    correct = sum(1 for a, b in zip(typed, sentence) if a == b)
    accuracy = (correct / len(sentence)) * 100

    result.config(text=f"WPM: {wpm:.1f}\nAccuracy: {accuracy:.1f}%")

root = tk.Tk()
root.title("Typing Speed Test")

sentence = random.choice(sentences)

tk.Label(root, text="Type the sentence below:").pack(pady=5)
tk.Label(root, text=sentence, font=("Arial", 12)).pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

tk.Button(root, text="Start", command=start).pack()

result = tk.Label(root, text="")
result.pack(pady=10)

entry.bind("<Return>", check)

root.mainloop()