import tkinter as tk

# Função para atualizar a entrada quando um botão é pressionado
def press(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Erro")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Cria a janela principal
window = tk.Tk()
window.title("Calculadora")

# Cria a entrada de texto
entry = tk.Entry(window, font=("Arial", 20))
entry.pack(fill=tk.BOTH, expand=True)

# Cria os botões
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    '.', '/'
]

button_frame = tk.Frame(window)
button_frame.pack()

row, col = 1, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Arial", 20), width=3, height=1)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", press)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Inicia a interface gráfica
window.mainloop()
