valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("=== Conversor de Moeda ===")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print("Em dólares: U$", round(valor_dolar, 2))
print(f"Em euros: €", round(valor_euro, 2))