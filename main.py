import pygad
import numpy as np

def fitness_function(inst,solution, solution_idx):
    cal_plato,pref_plato,cal_acom,pref_acom = solution
    return pref_plato * 10 + pref_acom * 9 + cal_plato * -5 + cal_acom * -5

# Create the GA instance
ga_instance = pygad.GA(num_generations=10,
                       num_parents_mating=2,
                       sol_per_pop=3,
                       num_genes=4,
                       fitness_func=fitness_function,
                       mutation_type="random",
                       mutation_percent_genes=25,
                       gene_space=[0,1])


ga_instance.run()
print(ga_instance.initial_population)
print(ga_instance.population)
print(ga_instance.best_solution())