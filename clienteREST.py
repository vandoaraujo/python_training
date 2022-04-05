import requests


print("1) Tentando pegar a conta 100 inexistente:")
url = 'http://localhost:8080/accounts/100'
res = requests.get(url)
print(res.content)


#adiciona o usuario 1
print("\n2) Adicionando a conta 6:")
url = 'http://localhost:8080/accounts'
dados = { "user_id":"6", "username":"Fulano Teste", "password":"abc12323", "email":"fulano@gmail.com"}
res2 = requests.post(url, json=dados)
print(res2.status_code, res2.headers)

#tenta pegar a conta 1 novamente
print("\n3) Pegando novamente a conta 6:")
url = 'http://localhost:8080/accounts/6'
res3 = requests.get(url)
print(res3.json())

#tenta adicionar novamente a conta 6
print("\n4) Adicionando novamente a conta 6:")
url = 'http://localhost:8080/accounts'
dados = { "user_id":"6", "username":"Fulano Teste", "password":"abc12323", "email":"fulano@gmail.com"}
res4 = requests.post(url, json=dados)
print(res4.status_code, res4.json())

#altera email da conta 1
print("\n5) Alterando o email da conta 1:")
url = 'http://localhost:8080/accounts/1'
dados = { "user_id":"1", "username":"Vando Ribeiro", "password":"abc12344", "email":"vando.araujo@gmail.com"}
res5 = requests.put(url, json=dados)
print(res5.status_code)

# tenta alterar email do usuario 2
print("\n6) Tentando alterar o email do usuario 20 (inexistente):")
url = 'http://localhost:8080/accounts/20'
dados = { "user_id":"1", "username":"Vando Ribeiro", "password":"abc12344", "email":"vando.araujo@gmail.com"}
res6 = requests.put(url, json=dados)
print(res6.status_code, res6.json())

#apaga usuario 1
print("\n7) Apagando o usuario 1:")
url = 'http://localhost:8080/accounts/1'
res7 = requests.delete(url)
print(res7.status_code)

#tenta pegar o usuario 1 novamente (inexistente)
print("\n8) Pegando novamente a conta 1 (inexistente):")
url = 'http://localhost:8080/accounts/1'
res8 = requests.get(url)
print(res8.json())