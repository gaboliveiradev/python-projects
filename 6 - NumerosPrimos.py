print('')

n1 = 0
n2 = int(input("Digite a quantidade de número que deseja consultar se é primo: "))

#--------------------------Estrutura de Repetição------------------------
for i in range(n1, n2+1):
    dividiu = 0
    for divisor in range(n1+1, i+1):
        if i % divisor == 0:
            dividiu = dividiu + 1


    if dividiu == 2:
        w = open("numeros_primos.txt", "a")
        w.write("O numero {} e primo \n" .format(i))  

print("[✓] - Realizamos a consulta nos números de ", n1, " até", n2)
w.close()
#------------------------------------------------------------------------     
