from zeep import Client

URL = 'http://wsdl'

client = Client(URL)
print(client.service.sfexpressService('param1', 'param2', 'param3'))
