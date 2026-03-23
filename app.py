# Entrada de dados 
nome_aparelho = input("Digite o nome do aparelho:").strip()
potencia = float(input("Digite a potência do aparelho em watts(W):").strip())
horas_dia = float(input("Qual o tempo médio de uso diário?(horas:)").strip())
preco_kWh = float(input("Digite o preço do Kwh cobrado (R$):)".strip().replace(',','.')))

# Cálculos 
consumo_mensal = (potencia * horas_dia * 30)/1000
custo_mensal = consumo_mensal * preco_kWh

# Saída dos resultados 
print(f"\nO aparelho cadastrado foi:{nome_aparelho}")
print(f"O Consumo Mensal estimado é de:{consumo_mensal:.2f} kWh/mês")
print(f"O Custo estimado é de: R$ {custo_mensal:.2f}/mês")