salario = float( input ('Digite seu salario:    ' ))
if salario <= 3000:
    print (' voce é junior')
elif salario >=3000 and salario <=6000:
    print ('você é intermediario')
elif salario >=6000 and salario <=15000:
    print ('senior')
else: print('gerente de programação')
