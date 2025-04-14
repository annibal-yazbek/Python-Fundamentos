# convertendo JSON para objetos python
import json

minhaStringJson = """
{
	"gerentes": [
	{
		"id":"001",
		"cidade": "São Paulo",
		"salario": "10.000"
	},
	{
		"id":"002",
		"cidade": "Rio de Janeiro",
		"salario": "7.000"
	}
	],
	"funcionario": [
	{
		"id": "999",
		"cidade": "Ribeirão",
		"cargo": "Empacotador",
		"salario": "3.000"
	}
	]
}
"""

meuObjetoPython = json.loads(minhaStringJson)
print(meuObjetoPython['gerentes'][0]['salario'])
      

