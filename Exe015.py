pr = float(input('informe o valor: '))
ds = float(input('informe o desconto: '))
desconto =( pr * ds) / 100
valor_total = pr - desconto

print('mercadoria com produto: {:.2f} '.format(valor_total))

