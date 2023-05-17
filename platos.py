# Para cada categoria 2 primeros bits calorias, resto preferencia
# Preferencia hardcodeada por ahora con unica opcion. Mayor numero binario = mayor preferencia

# Calorias referencia
# 00 Bajo
# 01 Promedio
# 10 Alto
# 11 Excesivo

# Plato principal
# 7 bits

milanesa         = [1,0, 0,1,1,0,1]
ensalada         = [0,0, 0,0,0,1,0]
bife             = [0,1, 0,1,0,1,0]
pechuga_de_pollo = [0,0, 0,0,1,1,1]
hamburguesa      = [1,1, 0,1,1,1,1]

# Acompañamiento
# 4 bits

pure_de_papa = [0,1, 1,0]
ensalada_side     = [0,0, 0,0]
papas_fritas = [1,1, 1,1]
arroz        = [0,1, 0,0]
pan          = [0,1, 0,1]

# Bebida
# 4 bits

agua                   = [0,0, 0,1]
bebida_cola            = [1,1, 1,1]
bebida_cola_sin_azucar = [0,0, 1,0]
jugo                   = [0,1, 1,0]
bebida_energetica      = [1,1, 0,1]