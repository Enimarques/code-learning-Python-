n = 1
par = impar = 0 #contadores
while n != 0:
    n = int(input("Digite um numero: "))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f"Okay, voce digitou {par} número(s) par(es) e {impar} numero(s) impar(es).")
