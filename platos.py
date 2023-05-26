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

milanesa             = 91010111
ensalada             = 90000111
bife                 = 90101010
pechuga_de_pollo     = 90001011
hamburguesa          = 91110101
fideos               = 90110000
tacos                = 91010100
empanadas            = 91001100
pizza                = 91111000
salmon_grille        = 90111111
filet_de_merluza     = 90010001
bondiola_a_la_mostaza= 91110101
conejo_hervido       = 90000000
guiso                = 91011010



# Acompañamiento
# 4 bits

pure_de_papa  = 90110
ensalada_side = 90000
papas_fritas  = 91111
arroz         = 90100
pan           = 90101
vegetales     = 90001

# Bebida
# 4 bits

agua                   = 90001
bebida_cola            = 91110
bebida_cola_sin_azucar = 90010
jugo                   = 90110
bebida_energetica      = 91101
te                     = 90001
vino                   = 90110
cerveza                = 91111

principales = [milanesa, ensalada, bife, pechuga_de_pollo, hamburguesa, salmon_grille, filet_de_merluza, bondiola_a_la_mostaza, conejo_hervido, guiso]
acomps = [pure_de_papa, ensalada_side, papas_fritas, arroz, pan]
bebidas = [agua, bebida_cola, bebida_cola_sin_azucar, jugo, bebida_energetica]

combinacionesPlatoprincipalAcompañamiento = {
    milanesa:[pure_de_papa,papas_fritas],
    ensalada:[ensalada_side, pan], 
    bife:[ensalada_side,papas_fritas,pure_de_papa,arroz], 
    pechuga_de_pollo:[ensalada_side,arroz], 
    hamburguesa:[papas_fritas], 
    fideos:[],
    tacos:[],
    empanadas:[],
    pizza:[],
    salmon_grille:[ensalada_side,arroz], 
    filet_de_merluza:[pure_de_papa], 
    bondiola_a_la_mostaza:[pan], 
    conejo_hervido:[arroz,pure_de_papa], 
    guiso:[pan],
}