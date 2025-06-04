from datetime import datetime

try:
    ano_atual = datetime.now().year

    # Solicita o ano e já valida se é um número correto
    ano = input("Digite seu ano de nascimento: ")

    if not ano.isdigit() or not (1900 <= int(ano) <= ano_atual):
        raise ValueError("Ano de nascimento inválido. Digite um ano entre 1900 e o ano atual.")

    ano = int(ano)

    # Só pergunta o sexo se o ano for válido
    sexo = input("[1] Masculino\n[2] Feminino\nEscolha uma opção: ")

    if sexo not in ["1", "2"]:
        raise ValueError("Opção inválida. Escolha [1] para Masculino ou [2] para Feminino.")

    idade = ano_atual - ano
    ano_alistamento = ano + 18

    if sexo == "2":
        print("O alistamento militar não é obrigatório para mulheres. \nNo entanto, é possível ingressar nas forças armadas por meio de concurso público.")
    elif sexo == "1":
        if idade < 18:
            print(f"Você ainda não precisa se alistar.\nSeu alistamento será em {ano_alistamento}. \nFaltam {18 - idade} anos.")
        elif idade == 18:
            print("Parabéns! Este é o ano do seu alistamento.")
        else:
            print(f"Seu período de alistamento já passou.\nVocê deveria ter se alistado em {ano_alistamento}. \nJá se passaram {idade - 18} anos.")

except ValueError as e:
    print(f"Erro! {e}")