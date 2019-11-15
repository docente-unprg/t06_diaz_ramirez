# Programa 01
import os

cliente=os.sys.argv[1]
precio=float(os.sys.argv[2])

# COndicion simple
# SI precio supera los 100 soles, mostrar mensaje de oferta
if ( precio > 100):
    print("Oferta del dia: Lleve 1 producto mas por 5 soles")
if (precio > 90 and precio < 100):
    print("Precio entre 90 y 100")
if (precio > 50 and precio < 90):
    print("Precio entre 50 y 90")
