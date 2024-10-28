from datetime import datetime
from dateutil.relativedelta import relativedelta

def idade():

    data_nascimento_input = input("Digite a data de nascimento (diamesano): ")
    data_nascimento = datetime.strptime(data_nascimento_input, '%d%m%Y')

    data_atual = datetime.now()

    diferenca = relativedelta(data_atual, data_nascimento)

    print(f"{diferenca.years}")
    
    return data_atual

data_atual = idade()

c = data_atual.strftime("%d/%m/%Y")
print(c)

