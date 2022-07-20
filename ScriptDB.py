import random

j = 0
j_gambiarra = 6216

## Função para gerar Nomes e Definir um Gênero
def gerar_nome_genero():
    global chance
    numeros = [1, 2]
    chance = random.choice(numeros)

    nome_do_meio = ['Baroni','Bottelho','Akynatom','Martins','Botura','Right','Rodrigues','Faccin','Tesser','Tavares','Nunes','Proenca','Sales','Bentes','Noah','Viella','Bezerra','Muniz','Dantas','Flora','Varoa','Varao','Pimenta','Salomao','Aquilante','Domingos','Do Pneu','Nobrega','Do Berrante','Flores','Gama','Breia','Batata','Varejao','Fanizzi','Luzzeti','Oliveira','Gino','Filho','Frasson','Morais','Aguiar','Cacador','Neto','Paulo','Muzy','Gotas','Peixe','Polonio','Pignatti','Otavio','Nascibem','Borges','Albino','Fonscesa','Silva','Dito','Perez','Bregaz','Bras','Tom','Brasil','Pereira','De Paula','Androcioli','Cabeludo','Pericles','Pinto']
    nome_m = ['Diego','Denilson','Camilo','Iago','Julio','Ezequiel','Alexandro','Valdir','Yuri','Danilo','Ryan','Ricardo','Carlos','Eduardo','Antonio','Alberto','Edgar','Gabriel','Edvaldo','Thiago','Andre','Joao','Mario','Marcos','Renato','Jose','Lorenzo','Deolindo','Miguel','Felipe','Osvaldo','Osmar','Eder']
    nome_f = ['Kaliany','Hilary','Victor','Poliana','Elsa','Riana','Melody','Rita','Raissa','Leandra','Berenice','Solange','Melinda','Josiane','Nara','Nayara','Carla','Eduarda','Maria','Lais','Taina','Isabela','Bianca','Laura','Fatima','Andrea','Telma','Dalva','Olinda','Benedita','Mariane','Marina','Gabriela','Agata','Jennifer']
    sobrenomes = ['Baroni','Bottelho','Akynatom','Martins','Botura','Right','Rodrigues','Faccin','Tesser','Tavares','Nunes','Proenca','Sales','Bentes','Noah','Viella','Bezerra','Muniz','Dantas','Flora','Varoa','Varao','Pimenta','Salomao','Aquilante','Domingos','Do Pneu','Nobrega','Do Berrante','Flores','Gama','Breia','Batata','Varejao','Fanizzi','Luzzeti','Oliveira','Gino','Filho','Frasson','Morais','Aguiar','Cacador','Neto','Paulo','Muzy','Gotas','Peixe','Polonio','Pignatti','Otavio','Nascibem','Borges','Albino','Fonscesa','Silva','Dito','Perez','Bregaz','Bras','Tom','Brasil','Pereira','De Paula','Androcioli','Cabeludo','Pericles','Pinto']

    if(chance == 1):
        escolher_nome_m = random.choice(nome_m)
        escolher_sobrenome_m = random.choice(sobrenomes)
        escolher_nome_meio_m = random.choice(nome_do_meio)
        nome_completo = escolher_nome_m + " " + escolher_nome_meio_m + " " + escolher_sobrenome_m 
        return nome_completo
    else:
        escolher_nome_f = random.choice(nome_f)
        escolher_sobrenome_f = random.choice(sobrenomes)
        escolher_nome_meio_f = random.choice(nome_do_meio)
        nome_completo = escolher_nome_f + " " + escolher_nome_meio_f + " " + escolher_sobrenome_f
        return nome_completo

## Função para gerar endereços
def gerar_nome_endereco():
    numeros = [1,2]
    chance = random.choice(numeros)
    start = ''

    if(chance == 1):
        start = "Rua"
    else:
        start = "Avenida"
    
    nome1 = ['Diego','Denilson','Camilo','Iago','Julio','Ezequiel','Alexandro','Valdir','Yuri','Danilo','Ryan','Ricardo','Carlos','Eduardo','Antonio','Alberto','Edgar','Gabriel','Edvaldo','Thiago','Andre','Joao','Mario','Marcos','Renato','Jose','Lorenzo','Deolindo','Miguel','Felipe','Osvaldo','Osmar','Eder']
    nome2 = ['Baroni','Bottelho','Akynatom','Martins','Botura','Right','Rodrigues','Faccin','Tesser','Tavares','Nunes','Proenca','Sales','Bentes','Noah','Viella','Bezerra','Muniz','Dantas','Flora','Varoa','Varao','Pimenta','Salomao','Aquilante','Domingos','Do Pneu','Nobrega','Do Berrante','Flores','Gama','Breia','Batata','Varejao','Fanizzi','Luzzeti','Oliveira','Gino','Filho','Frasson','Morais','Aguiar','Cacador','Neto','Paulo','Muzy','Gotas','Peixe','Polonio','Pignatti','Otavio','Nascibem','Borges','Albino','Fonscesa','Silva','Dito','Perez','Bregaz','Bras','Tom','Brasil','Pereira','De Paula','Androcioli','Cabeludo','Pericles','Pinto']
    p1 = random.choice(nome1)
    p2 = random.choice(nome2)
    p3 = random.choice(nome2)

    endereco = start+" "+p1+" "+p2+" "+p3
    return endereco

## Função para gerar números de Telefones
def gerar_tel():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # NÚMERO DE CELULAR TEM 9 DIGITOS

    num4 = random.choice(numeros)
    num5 = random.choice(numeros)
    num6 = random.choice(numeros)
    num7 = random.choice(numeros)
    num8 = random.choice(numeros)
    num9 = random.choice(numeros)
    tel = '981'+num4+num5+num6+num7+num8+num9
    return tel

## Função para gerar números de CPF
def gerar_cpf():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # CPF TEM 11 DIGITOS
    num1 = random.choice(numeros)
    num2 = random.choice(numeros)
    num3 = random.choice(numeros)
    num4 = random.choice(numeros)
    num5 = random.choice(numeros)
    num6 = random.choice(numeros)
    num7 = random.choice(numeros)
    num8 = random.choice(numeros)
    num9 = random.choice(numeros)
    num10 = random.choice(numeros)
    num11 = random.choice(numeros)
    cpf = num1+num2+num3+num4+num5+num6+num7+num8+num9+num10+num11
    return cpf

## Funções para gerar números de RG
def gerar_rg():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # RG TEM 9 DIGITOS
    num1 = random.choice(numeros)
    num2 = random.choice(numeros)
    num3 = random.choice(numeros)
    num4 = random.choice(numeros)
    num5 = random.choice(numeros)
    num6 = random.choice(numeros)
    num7 = random.choice(numeros)
    num8 = random.choice(numeros)
    num9 = random.choice(numeros)
    rg = num1+num2+num3+num4+num5+num6+num7+num8+num9
    return rg

## Função para gerar número de CNPJ
def gerar_cnpj():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    num1 = random.choice(numeros)
    num2 = random.choice(numeros)
    num3 = random.choice(numeros)
    num4 = random.choice(numeros)
    num5 = random.choice(numeros)
    num6 = random.choice(numeros)
    num7 = random.choice(numeros)
    num8 = random.choice(numeros)
    num9 = random.choice(numeros)
    num10 = random.choice(numeros)
    num11 = random.choice(numeros)
    cnpj = num1+num2+num3+num4+num5+num6+num7+num8+'000'+num9+num10+num11
    return cnpj

## Funções para gerar números de CEP
def gerar_cep():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    num1 = random.choice(numeros)
    num2 = random.choice(numeros)
    num3 = random.choice(numeros)
    num4 = random.choice(numeros)
    num5 = random.choice(numeros)
    num6 = random.choice(numeros)
    num7 = random.choice(numeros)
    num8 = random.choice(numeros)
    cep = num1+num2+num3+num4+num5+num6+num7+num8
    return cep

## Funções para gerar número de casa
def gerar_numero_casa():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    num1 = random.choice(numeros)
    num2 = random.choice(numeros)
    num3 = random.choice(numeros)

    numero_casa = num1+num2+num3
    return numero_casa

## Funções para gerar nomes de cidades
def gerar_cidade():
    cidades = ['Iacanga', 'Rio De Janeiro', 'Petropoles', 'Niteroi', 'Parana', 'Minas-Gerais', 'Brazilia', 'Amazonas', 'Roraima', 'Acre', 'Tocantins', 'Bahia', 'Mato Grosso do Sul', 'Mato Grosso', 'Santa Catarina', 'Natal', 'Belem', 'São Miguel', 'Bariri','Jaú','Eroza','Potunduva','Pindamonhagava','Bauru','Perderneiras','Itapui','Lins','Marilia','Itaju','Boraceia',]
    escolher_cidade = random.choice(cidades)
    return escolher_cidade

## Funções para gerar data de nascimento
def gerar_data_nasc():
    dias = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
    meses = ['01','02','03','04','05','06','07','08','09','10','11','12']
    ano = ['1972','1974','1978','1981','1988','1985','1983','1987','1991','1992','1993','1995','1997']
    escolher_dia = random.choice(dias)
    escolher_mes = random.choice(meses)
    escolher_ano = random.choice(ano)
    data_completa = escolher_dia+'/'+escolher_mes+'/'+escolher_ano
    return data_completa

## Função para gerar bairros de cidades
def gerar_bairros():
    bairros = ['Nova Fanizzi', 'Jardim Nova Era Frasson', 'Jardim Tiagotas', 'Jardim Oeste', 'Maria Luiza 2', 'Maria Luiza 1', 'Nova Esperanca', 'Jardim Dos Supremos', 'Parque Do Eder', 'Jardim Eder Coxas', 'Centro Marcao Souza', 'Parque Courte CouBen', 'Jardim Edilson', 'Nova Junin 2', 'Nova Junin 1', 'Jardim Gama','Jardim Paulista','Jardim Das Explanadas','Nova Cidade','Jardim Porto','Bela Vista','Vista Nova','Centro','Parafuso','Vila','Jardim Garotinho','Parque Dos Ipes']
    escolher_bairros = random.choice(bairros)
    return escolher_bairros

## Funções para gerar cargo para o funcionário
def gerar_cargo():
    cargos = ['Gerente de Vendas', 'Supervisor de Vendas', 'Auxiliar Administrativos de Vendas', 'Vendedor', 'Vendedor', 'Vendedor', 'Vendedor', 'Vendedor']
    escolher_cargo = random.choice(cargos)
    return escolher_cargo

def gerar_email():
    nome1 = ['Diego','Denilson','Camilo','Iago','Julio','Ezequiel','Alexandro','Valdir','Yuri','Danilo','Ryan','Ricardo','Carlos','Eduardo','Antonio','Alberto','Edgar','Gabriel','Edvaldo','Thiago','Andre','Joao','Mario','Marcos','Renato','Jose','Lorenzo','Deolindo','Miguel','Felipe','Osvaldo','Osmar','Eder']
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']
    escolher_nome = random.choice(nome1)
    l1 = random.choice(letras)
    l2 = random.choice(letras)
    l3 = random.choice(letras)
    l4 = random.choice(letras)
    l5 = random.choice(letras)
    email = escolher_nome+l1+l2+l3+l4+l5+"@gmail.com"
    return email

def gerar_valor_total():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    n1 = random.choice(numeros)
    n2 = random.choice(numeros)
    n3 = random.choice(numeros)
    n4 = random.choice(numeros)
    n5 = random.choice(numeros)
    valor_total = n1+n2+n3+"."+n4+n5
    return valor_total

def gerar_qnt_produto():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    qnt = random.choice(numeros)
    return qnt

tabela = input("Digite qual o nome tabela que você deseja preencher: ")
num_registros = int(input("Digite a quantidade de registros que você deseja: "))

if (tabela == "compra" or tabela == "Compra"):
    insert_model = "INSERT INTO Venda(valor, quantidade, id_fornecedor, id_produto) VALUES"
    w = open("insert_compra.sql", "a")
    for i in range(num_registros):
        valor_total = gerar_valor_total()
        qnt = gerar_qnt_produto()
        id_produto = random.randint(1, 30)
        id_fornecedor = random.randint(1, 50)
        w.write(insert_model+"({}, {}, {}, {}) \n".format(valor_total, qnt, id_fornecedor, id_produto))

    print("[✓] - Foram criados ", num_registros, " registros com sucesso!")
    w.close()

if (tabela == "venda" or tabela == "Venda"):
    insert_model = "INSERT INTO Venda(quantidade_produto, valor_total, id_cliente, id_produto, id_funcionario) VALUES"
    w = open("insert_venda.sql", "a")
    for i in range(num_registros):
        qnt = gerar_qnt_produto()
        valor_total = gerar_valor_total()
        id_cliente = random.randint(1, 5000)
        id_produto = random.randint(1, 30)
        id_funcionario = random.randint(1, 500)
        w.write(insert_model+"({}, {}, {}, {}, {}) \n".format(qnt, valor_total, id_cliente, id_produto, id_funcionario))

    print("[✓] - Foram criados ", num_registros, " registros com sucesso!")
    w.close()

if (tabela == 'fornecedor' or tabela == 'Fornecedor'):
    insert_model = "INSERT INTO Fornecedor(nome, cnpj, email, telefone, id_endereco) VALUES"
    w = open("insert_fornecedor.sql", "a")
    for i in range(num_registros):
        j_gambiarra += 1
        nome = gerar_nome_genero()
        email = gerar_email()
        cnpj = gerar_cnpj()
        telefone = gerar_tel()
        w.write(insert_model+"('"+nome+"','"+cnpj+"','"+email+"','"+telefone+"',{}); \n".format(j_gambiarra))

    print("[✓] - Foram criados ", num_registros, " registros com sucesso!")
    w.close()

if (tabela == 'funcionario' or tabela == 'Funcionario'):
    insert_model = "INSERT INTO Funcionario(nome, genero, telefone, cpf, cargo, id_endereco) VALUES"
    w = open("insert_funcionario.sql", "a")
    for i in range(num_registros):
        nome = gerar_nome_genero()
        tel = gerar_tel()
        cpf = gerar_cpf()
        cargo = gerar_cargo()
        if (chance == 1):
            genero = "Homem"
        else:
            genero = "Mulher"
        #print(insert_model+"('"+nome+"','"+genero+"','"+tel+"','"+cpf+"','"+cargo+"');")
        w.write(insert_model+"('"+nome+"','"+genero+"','"+tel+"','"+cpf+"','"+cargo+"'); \n")

    print("[✓] - Foram criados ", num_registros, " registros com sucesso!")
    w.close()

elif (tabela == 'endereco' or tabela == 'Endereco'):
    insert_model = "INSERT INTO Endereco(nome_endereco, cep, bairro, cidade, numero) VALUES"
    w = open("insert_endereco.sql", "a")

    for i in range(num_registros):
        j += 1
        nome_endereco = gerar_nome_endereco()
        cep = gerar_cep()
        bairro = gerar_bairros()
        cidade = gerar_cidade()
        numero = gerar_numero_casa()
        w.write(insert_model+"('"+nome_endereco+"','"+cep+"','"+bairro+"','"+cidade+"','"+numero+"'); \n")
    
    print("[✓] - Foram criados ", num_registros, " registros com sucesso!")
    w.close()

elif (tabela == 'cliente' or tabela == 'Cliente'):
    insert_model = "INSERT INTO Cliente(nome, rg, cpf, data_nasc, genero, id_endereco) VALUES"
    w = open("insert_cliente.sql", "a")
    for i in range(num_registros):
        j += 1
        nome = gerar_nome_genero()
        cpf = gerar_cpf()
        rg = gerar_rg()
        data_nasc = gerar_data_nasc()
        if (chance == 1):
            genero = "Homem"
        else:
            genero = "Mulher"
        #print(insert_model+"("+nome+"','"+rg+"','"+cpf+"','"+data_nasc+"','"+genero+"');")
        w.write(insert_model+"('"+nome+"','"+rg+"','"+cpf+"','"+data_nasc+"','"+genero+"',{}); \n".format(j))
    
    print("[✓] - Foram criados ", num_registros, " registros com sucesso!")
    w.close()