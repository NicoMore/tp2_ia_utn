# Para cada categoria 2 primeros bits calorias, resto preferencia
# Preferencia hardcodeada por ahora con unica opcion. Mayor numero binario = mayor preferencia

# Calorias referencia
# 00 Bajo
# 01 Promedio
# 10 Alto
# 11 Excesivo

# ARRANCO CON 9 PARA QUE NO ME TOME OCTAL, LO CORTO EN FITNESS

# Plato principal
# 7 bits

milanesa         = 91010111
ensalada         = 90000111
bife             = 90101010
pechuga_de_pollo = 90001011
hamburguesa      = 91101110


# Acompañamiento
# 4 bits

pure_de_papa  = 90110
ensalada_side = 90000
papas_fritas  = 91111
arroz         = 90100
pan           = 90101

# Bebida
# 4 bits

agua                   = 90001
bebida_cola            = 91111
bebida_cola_sin_azucar = 90010
jugo                   = 90110
bebida_energetica      = 91101

principales = [milanesa, ensalada, bife, pechuga_de_pollo, hamburguesa]
acomps = [pure_de_papa, ensalada_side, papas_fritas, arroz, pan]
bebidas = [agua, bebida_cola, bebida_cola_sin_azucar, jugo, bebida_energetica]