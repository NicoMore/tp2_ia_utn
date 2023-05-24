import pygad
import numpy as np
from helper import *

# Las combinaciones de platos que "no tienen sentido", son penalizados
# plato-ppal
# 0000000 => 7bits
# 00xxxxx => calorias (C) => 0-3 
# xx00000 => gusto (G) => (0-31) + 32 * C
# C * 24 * factorC + G * factorG
# donde => factorC + factorG = 1
# 96/4 = 24 => lo llevamos a base 94
# 
# Acompañamiento
# 0000 => 4bits
# 00xx => calorias (C) => 0-3 
# xx00 => gusto (G) => (0-3) + 4 * C
# (C * factorC + G * factorG) * 24
# 
# Bebida
# 0000 => 4bits
# 00xx => calorias (C) => 0-3 
# xx00 => gusto (G) => (0-3) + 4 * C
# (C * factorC + G * factorG) * 24

def fitness_function(inst,solution, solution_idx):
    plato_ppal,f_plato_ppal = [solution[:7], 0.5]
    acomp,f_acom = [solution[7:11], 0.25]
    bebida,f_beb = [solution[11:], 0.25]

    f_cal = 0.5
    score_plato_ppal = get_score_plato_ppal(plato_ppal,f_cal)

    f_beb_cal = 0.5
    score_beb = get_score_bebida_acom(bebida,f_beb_cal)

    f_acom_cal = 0.5
    score_acom = get_score_bebida_acom(acomp,f_acom_cal)

    return score_plato_ppal * f_plato_ppal + score_beb * f_beb  + score_acom * f_acom


# Create the GA instance
ga_instance = pygad.GA(num_generations=300,
                       num_parents_mating=4,
                       sol_per_pop=300,
                       num_genes=15,
                       mutation_percent_genes=20,
                       mutation_type="random",
                       crossover_type="two_points",
                       parent_selection_type="sss",
                       fitness_func=fitness_function,
                       gene_space=[0,1])


ga_instance.run()
print(ga_instance.best_solution())