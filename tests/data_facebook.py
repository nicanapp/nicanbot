import re
from datetime import date, timedelta


mapameses = {
    'janeiro':'01','fevereiro':'02','março':'03',
    'abril':'04','maio':'05','junho':'06',
    'julho':'07','agosto':'08','setembro':'09',
    'outubro':'10','novembro':'11','dezembro':'12'
}


def _transform_els_data(num:str, var:str, ano:str):

    hoje  = date.today()

    if var in ["min", "h"]:
        return hoje
    
    if var == "d":
        return date.today() - timedelta(days=int(num))

    dia = "0"+num if len(num) == 1 else num
    if var in mapameses.keys():
        return f"{ano}-{mapameses[var]}-{dia}"

    return hoje


def _transform_data(value:str) -> str:

    # ((\d+)(\sde)?\s([A-z]+)(\sde\s(\d+))?) 
    # se nao entrar nesse regex, é porque é HOJE! - foda-se

    values = re.search("((\d+)(\sde)?\s([A-z]+)(\sde\s(\d+))?)", value)
    hoje = date.today()
    
    if values == None: 
        return hoje

    value = _transform_els_data(values.group(2), values.group(4), values.group(6) if values.group(6) != None else hoje.year)

    return value


data1 = "2 de outubro às 12:48"
data2 = "5 d"
data3 = "22 h"
data4 = "2 de outubro de 2021"


print(_transform_data(data1))
print(_transform_data(data2))
print(_transform_data(data3))
print(_transform_data(data4))

