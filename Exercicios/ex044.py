# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO CONSIDERANDO SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO
#- À VISTA DINHEIRO CHEQUE 10 % DE DESCONTO
#- À VISTA CARTÃO 5% DE DESCONTO
#- EM ETÉ 2X NO CARTÃO, PREÇO NORMAL
#- 3X OU MAIS NO CARTÃO 20 % DE JUROS
try:
    while True:
        try:
            valor = float(input('Digite o preço do produto: R$ ').replace(',', '.'))
            if valor <= 0:
                print('🚨 O preço deve ser maior que zero! Tente novamente.')
                continue
            break
        except ValueError:
            print('❌ Entrada inválida! Digite um número válido.')

    while True:
        try:
            pagamento = int(input('\n📌 Escolha uma forma de pagamento:\n'
                                  '[1] À vista dinheiro/cheque - 10% de desconto\n'
                                  '[2] À vista cartão - 5% de desconto\n'
                                  '[3] Em até 2x no cartão - Preço normal\n'
                                  '[4] 3x ou mais no cartão - 20% de juros\n'
                                  '🔹 Digite sua opção: '))
            if pagamento not in [1, 2, 3, 4]:
                print('❌ Opção inválida! Escolha uma opção de 1 a 4.')
                continue
            break
        except ValueError:
            print('❌ Entrada inválida! Digite um número válido.')

    # Cálculo do pagamento
    if pagamento == 1:
        desconto = valor * 10 / 100
        total = valor - desconto
        print(f'\n✅ Você ganhou 10% de desconto. Total a pagar: R$ {total:.2f}')
    elif pagamento == 2:
        desconto = valor * 5 / 100
        total = valor - desconto
        print(f'\n✅ Você ganhou 5% de desconto. Total a pagar: R$ {total:.2f}')
    elif pagamento == 3:
        while True:
            try:
                parcelas = int(input('Quantas vezes? (1 ou 2x): '))
                if parcelas not in [1, 2]:
                    print('❌ Número de parcelas inválido! Escolha 1 ou 2.')
                    continue
                break
            except ValueError:
                print('❌ Entrada inválida! Digite um número válido.')
        if parcelas == 1:
            print(f'✅ Parabéns pela compra! Total a pagar: R$ {valor:.2f}')
        elif parcelas == 2:
            dividido = valor / parcelas
            print(f'✅ Parabéns pela compra! Total a pagar: R$ {valor:.2f} em {parcelas} parcelas de R$ {dividido:.2f}')
    elif pagamento == 4:
        while True:
            try:
                parcelas = int(input('Quantas vezes? (mínimo 3x): '))
                if parcelas < 3:
                    print('❌ Número de parcelas inválido! Escolha 3 ou mais.')
                    continue
                break
            except ValueError:
                print('❌ Entrada inválida! Digite um número válido.')
        acrescimo = valor * 20 / 100
        total = valor + acrescimo
        dividido = total / parcelas
        print(f'⚠️ Você pagará 20% de juros! Total a pagar: R$ {total:.2f} em {parcelas} parcelas de R$ {dividido:.2f}')

except ValueError as e:
    print(f'Erro! {e} Tente novamente.')
