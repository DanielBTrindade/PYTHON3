nome = str(input("Qual é o seu nome?"))
if nome in ['Daniel', 'Gabrieli']:
    print(f'{nome} é um nome bonito!')
elif nome in ['Pedro', 'Maria', 'João']:
    print("Seu nome é bem popular no Brasil!")
else:
    print("Seu nome é bem normal!")