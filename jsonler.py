from datetime import datetime
import json
from json.decoder import JSONDecodeError
import locale
from estatistica import Estatistica

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
lista=[]
produtos={10:"Leite",15:"Iogurte",20:"Manteiga"}
precos={10:1,15:2,20:3}
formato="%d/%m/%Y %H:%M:%S"
valorTotal=0.0
registros = []
try:
    with open('saida.json','r') as arq:
        lista=json.load(arq)
    
    for venda in lista:
        nome_produto=produtos[venda['mercadoria']]
        preco_produto=precos[venda['mercadoria']]
        data=datetime.strptime(venda['data'],formato)
        quantidade=locale.format_string('%.2f',venda['quantidade'])
        valor = float(preco_produto) * float(quantidade.replace(',', '.'))

        contemLista = False
        for i,item in enumerate(registros):
            if item.id==venda['mercadoria']:
                registros[i].valor= item.valor + valor
                contemLista = True
                break
        if not contemLista:
            registro : Estatistica = Estatistica(venda['mercadoria'],valor)
            registros.append(registro)
        
        valorTotal = valorTotal + float(valor)
        print('Cliente: {}, Produto: {}, Data: {}, Quantidade: {}'.format(
            venda['cliente'],nome_produto,data,quantidade)
        )
    
    print('O valor total obtido com os produtos foi: {}  '.format(
        locale.format_string('%.2f',valorTotal)))
    
    registroMaior : Estatistica = registros[0]
    for i,reg in enumerate(registros, start= 1):
        if registroMaior.valor < reg.valor:
            registroMaior = reg;

    print ('O produto que gerou maior faturamento foi: {} , R$ {}  '.format(
        produtos.get(registroMaior.id), locale.format_string('%.2f', registroMaior.valor)))

except JSONDecodeError:
    print('O arquivo de movimento está inválido!')