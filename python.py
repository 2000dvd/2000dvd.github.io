x = input("Tipo de reserva P o N?")

bol = 0.1497
col = 0.095
crc = 0.05
sal = 0.13
gua = 0.12
hai = 0.1
hnd = 0.15
mex = 0.16
nic = 0.15
pan = 0.07
pay = 0.025
per = 0.18
rpd = 0.18
tyt = 0.125
ugy = 0.075
ven = 0.08
guy = 0.15
sur = 0.1

if x == 'p': 
    y = "PARCIALMENTE USADA"
    print(f"la reserva es {y} ")
elif x  == 'n':
    y = "NUEVA"
    print(f"la reserva es {y} ")
else :
    y = "invalida"
    print(f"la reserva es {y} ")

ant = float(input("Cuanto tiene a favor? "))
nuv = float(input("Cuanto cuesta ahora? "))
pen = float(input("Cuanto penalidad? "))

pag = nuv-ant 

pais = input("De que pais?")


if pais == 'bolivia': 
    por = bol
    
elif pais == 'colombia':
    por = col
    
elif pais == 'costa rica':
    por = crc
    
elif pais == 'salvador':
    por = sal
    
elif pais == 'guatemala':
    por = gua
    
elif pais == 'haiti':
    por = hai
    
elif pais == 'honduras':
    por = hnd
    
elif pais == 'mexico':
    por = mex
    
elif pais == 'nicaragua':
    por = nic
    
elif pais == 'panama':
    por = pan
    
elif pais == 'paraguay':
    por = pay
    
elif pais == 'peru':
    por = per
    
elif pais == 'rd':
    por = rpd
    
elif pais == 'tt':
    por = tyt
    
elif pais == 'uruguay':
    por = ugy
    
elif pais == 'venezuela':
    por = ven
    
elif pais == 'guyana':
    por = guy
    
elif pais == 'surinam':
    por = sur
    
else :
    por = 0
    
porr = por * 100

porc = pag * por

totdif= pag+porc

penimp = (pen*por)+pen 

tottot= totdif+penimp

print(f"DIFERENCIA = {pag}, PORCENTUAL DEL {porr}% = {porc}")
print(f"TOTAL DIFERENCIA = {totdif}")
print(f"PENALIDAD = {penimp}")
print(f"TOTAL A PAGAR = {tottot}")
