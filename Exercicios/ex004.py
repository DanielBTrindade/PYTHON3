# Programa que lê uma entrada do usuário e exibe seu tipo primitivo e outras informações

# Lê algo pelo teclado
a = input('Digite algo: ')

# Exibe o tipo primitivo da entrada
print('O tipo primitivo desse valor é:', type(a))

# Verifica outras informações sobre a entrada
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizado?', a.istitle())