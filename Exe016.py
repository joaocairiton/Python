salario_atual = float(input('informe o salario: '))
desc = float(input('informe o desconto: '))

vl_desc = (salario_atual * desc) / 100
total_salario = salario_atual + vl_desc

print('O novo salario: {}'.format(total_salario))
