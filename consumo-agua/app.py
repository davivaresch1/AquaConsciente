tipo = input("Tipo do imóvel (comercial, casa ou apartamento): ").lower()
consumo = float(input("Consumo mensal em m³: "))

if tipo == "comercial":    # imóvel comercial
    print("Tarifa comercial aplicada - consulte o plano corporativo.")
elif tipo == "apartamento" and consumo < 10:      # apartamento e consumo < 10
    print("Consumo econômico - excelente controle de água!")
elif (tipo == "apartamento" or tipo == "casa") and consumo <= 25:   # apartamento ou casa, até 25
    print("Consumo moderado - dentro do padrão residencial.")
else:
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")