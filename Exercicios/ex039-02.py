import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


# Função para calcular alistamento
def calcular_alistamento():
    try:
        ano = entry_ano.get().strip()
        sexo = combo_sexo.get()

        # Validação do ano
        if not ano.isdigit() or not (1900 <= int(ano) <= datetime.now().year):
            raise ValueError("Ano de nascimento inválido. Digite um ano entre 1900 e o ano atual.")

        ano = int(ano)
        idade = datetime.now().year - ano
        ano_alistamento = ano + 18

        if sexo == "Feminino":
            mensagem = "O alistamento militar não é obrigatório para mulheres.\nVocê pode ingressar nas forças armadas por concurso público."
        elif sexo == "Masculino":
            if idade < 18:
                mensagem = f"Você ainda não precisa se alistar.\nSeu alistamento será em {ano_alistamento}.\nFaltam {18 - idade} anos."
            elif idade == 18:
                mensagem = "Parabéns! Este é o ano do seu alistamento!"
            else:
                mensagem = f"Seu período de alistamento já passou.\nVocê deveria ter se alistado em {ano_alistamento}.\nJá se passaram {idade - 18} anos."
        else:
            raise ValueError("Escolha uma opção válida para o sexo.")

        messagebox.showinfo("Resultado", mensagem)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))


# Criando a janela principal
root = tk.Tk()
root.title("Verificador de Alistamento")
root.geometry("400x280")
root.configure(bg="#F0F0F0")  # Cor de fundo suave

# Criando um frame para organizar os elementos
frame = ttk.LabelFrame(root, text="Insira seus dados", padding=20)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Elementos da interface com mais espaçamento e fonte ajustada
ttk.Label(frame, text="Digite seu ano de nascimento:", font=("Arial", 12)).pack(pady=5)
entry_ano = ttk.Entry(frame, width=10, font=("Arial", 12))
entry_ano.pack(pady=5)

ttk.Label(frame, text="Selecione seu sexo:", font=("Arial", 12)).pack(pady=5)
combo_sexo = ttk.Combobox(frame, values=["Masculino", "Feminino"], state="readonly", font=("Arial", 12))
combo_sexo.pack(pady=5)

# Botão com texto corrigido e ajuste de largura
btn_verificar = ttk.Button(frame, text="Verificar Alistamento", command=calcular_alistamento)
btn_verificar.pack(pady=12, ipady=5)  # ipady aumenta o tamanho do botão para melhor legibilidade

# Iniciando a interface gráfica
root.mainloop()