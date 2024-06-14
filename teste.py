print( A VACINAÇÃO DE CRIANÇAS CONTRA SARAMPO OCORRE A PARTIR DE 1 ANO DE IDADE,
IDENTIFIQUE QUANTOS ANOS TEM A CRIANÇA PARA INFORMAR A DATA DE VACINAÇÃO NO POSTO MAIS PRÓXIMO
DE SUA RESIDÊNCIA, A VACINA ESTA COM PRIORIDADE PARA CRIANÇAS COM 5 ANOS MOMENTÂNEAMENTE)

idade = eval (input (' qual a idade da criança?'))
if idade < 5:
 print('a criança NÃO precisa ser vacinada por enquanto')
elif idade ==5:
print ( 'a criança precisa ser vacinada, procure imediatamente um posto de saúde ')
else:
print(' crianças acima de 5 anos necessitam aguardar a chegada da vacina, retorne a ubs '
      'para melhores orientações ')


print('Obrigado ! Vacine-se')