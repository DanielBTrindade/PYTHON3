import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Função para calcular alistamento
def calcular_alistamento():
    try:
        ano = int(entry_ano.get())
        ano_atual = datetime.now().year

        if not (1900 <= ano <= ano_atual):
            raise ValueError("Ano de nascimento inválido.")

        idade = ano_atual - ano
        ano_alistamento = ano + 18

        if idade < 18:
            mensagem = f"Ainda não chegou seu alistamento.\nVocê deve se alistar em {ano_alistamento}.\nFaltam {18 - idade} anos."
        elif idade == 18:
            mensagem = "Parabéns! Este é o ano do seu alistamento!"
        else:
            mensagem = f"Já passou seu alistamento.\nDeveria ter se alistado em {ano_alistamento}.\nPassaram {idade - 18} anos."

        messagebox.showinfo("Resultado", mensagem)

    except ValueError:
        messagebox.showerror("Erro", "Digite um ano válido entre 1900 e o ano atual.")

# Criando a janela principal
root = tk.Tk()
root.title("Verificador de Alistamento")
root.geometry("350x200")
root.resizable(False, False)

# Aplicando tema moderno
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Criando frame central
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Criando os elementos
ttk.Label(frame, text="Digite seu ano de nascimento:").pack(pady=5)
entry_ano = ttk.Entry(frame, width=10)
entry_ano.pack(pady=5)

ttk.Button(frame, text="Verificar", command=calcular_alistamento).pack(pady=10)

# Iniciando a interface gráfica
root.mainloop()