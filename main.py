import tkinter as tk
import random

def get_answer():
    answers = [
        "Oui, absolument !",
        "C'est certain.",
        "Peut-être...",
        "Demande plus tard.",
        "Non, vraiment pas.",
        "Mes sources disent que non.",
        "Absolument pas !",
        "C'est très probable.",
        "Signe favorable.",
        "Ne compte pas là-dessus."
    ]
    label_answer.config(text=random.choice(answers))

root = tk.Tk()
root.title("Boule de Cristal 🔮")
root.geometry("300x250")

label_question = tk.Label(root, text="Posez une question et cliquez !", pady=20)
label_question.pack()

button = tk.Button(root, text="Consulter la boule", command=get_answer)
button.pack()

label_answer = tk.Label(root, text="", pady=20, font=("Helvetica", 12, "bold"), wraplength=250)
label_answer.pack()

root.mainloop()
