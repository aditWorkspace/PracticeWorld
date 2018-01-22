celsius = [0,35.67,2323]
#Change celsius in to whatever you want to...so later we can convert that into farenheit
farenheit = [(temp*(9/5) + 32) for temp in celsius]
print (farenheit)