import requests

from acesso_CEP import BuscaEndereco
cep = "63902290"
objeto_cep = BuscaEndereco(cep)


a = objeto_cep.acessa_via_cep()
print(a)
