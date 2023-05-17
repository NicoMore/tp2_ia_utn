import pygad as pg
import platos

# Por ahora copypaste de lo que dice PyGad
# Posiblemente haya que meterlo en un __init__
num_generations = 50
num_parents_mating = 4

fitness_function = fitness_func

sol_per_pop = 8 # No hace falta si initial_population
num_genes = len(function_inputs) # No hace falta si initial_population

init_range_low = -2 # No hace falta si initial_population
init_range_high = 5 # No hace falta si initial_population

parent_selection_type = "sss"
keep_parents = 1

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10

# Definido por mi (Nico)

# No esta claro si es superior definirla o no, pero tal vez es interesante ver una especie de "progreso" a la solucion
initial_population = [
                    [milanesa, papas_fritas, agua],
                    [ensalada, arroz, bebida_cola],
                    [bife, pan, jugo]
                    ]

# Dice que aguanta listas, no se si listas de listas. Sublista representa gen
gene_type = [[int, int, int, int, int, int, int], [int, int, int, int], [int, int, int]]

# Limita los genes a los que definimos adentro, idem comentario arriba
gene_space = [[milanesa, ensalada, bife, pechuga_de_pollo, hamburguesa], [pure_de_papa, ensalada_side, papas_fritas, arroz, pan], [agua, bebida_cola, bebida_cola_sin_azucar, jugo, bebida_energetica]]

# Otro burdo copypaste
ga_instance = pg.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type= mutation_func, # Aca va la func de mutacion de abajo, sino igualar a mutation_type 
                       mutation_percent_genes=mutation_percent_genes)

# Donde solution es el plato, requiere ese nombre x Pygad
def fitness_func(ga_instance, solution, solution_idx):
    # Chequear vs preferencia calorica
    # Pasar numero binario a preferencia
    # Definir func matematica
    return fitness

# No es requerido, pero si definimos la mutacion nosotros podemos trabajar con los platos que definimos, con un random
# Lo que no se es que pasa si la mutacion resulta ser peor, si la descarta o que hace Pygad por atras
# Otra opcion es definir los platos como tipos y limitar al gen a esos tipos, tendria que seguir leyendo la docu para ver que onda
def mutation_func(offspring, ga_instance):
    # Seleccionar random un plato principal
    # Seleccionar random un acompañamiento
    # Seleccionar random una bebida
    return offspring

# Tambien se pueden definir padres y crossover