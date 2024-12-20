#!/usr/bin/env python3

# We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:
# Colombian pesos
# Peruvian soles
# Brazilian reais
# Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.
# Make sure to Google the current exchange rates!

pesos = float(input('What do you have left in pesos ? '))
soles = float(input('What do you have left in soles ? '))
reais = float(input('What do you have left in reais ? '))

usd = (pesos * 0.04) + (soles * 0.26761) + (reais * 0.16)

print(usd)
