import pygad as pg
from platos import *

def switch_calos(calorias) -> int:

    if calorias == [1,1]:
        return 0
    else:
        if calorias == [1,0]:
            return 34
        else:
             if calorias == [0,1]:
                return 67
             else:
                 if calorias == [0,0]:
                     return 100

    return -100
def caloria_calculator(principal, acomp, bebida) -> int:
    calos_principal = principal[:1]
    calos_acomp = acomp[:1]
    calos_bebida = bebida[:1]

    return round((switch_calos(calos_principal) + switch_calos(calos_acomp) + switch_calos(calos_bebida)) / 3) # Tope de 100

def gusto_calculator(principal, acomp, bebida) -> int:
    gusto_principal = principal[2:]
    gusto_acomp = acomp[2:]
    gusto_bebida = bebida[2:]

    gusto_p = int("".join(str(i) for i in gusto_principal), 2)
    gusto_a = int("".join(str(i) for i in gusto_acomp), 2)
    gusto_b = int("".join(str(i) for i in gusto_bebida), 2)

    return round((gusto_p + gusto_a + gusto_b) * 3 * 100 / 111)

# Donde solution es el plato, requiere ese nombre x Pygad
def fitness_func(ga_instance, solution, solution_idx):
    principal = int(solution[0])
    acomp = int(solution[1])
    bebida = int(solution[2])


    principal_s = str(principal)
    principal_s = principal_s[1:]
    principal_s = " ".join(char for char in principal_s)
    acomp_s = str(acomp)
    acomp_s = acomp_s[1:]
    acomp_s = " ".join(char for char in acomp_s)
    bebida_s = str(bebida)
    bebida_s = bebida_s[1:]
    bebida_s = " ".join(char for char in bebida_s)

    principal_lista = [int(num) for num in principal_s.split()]
    acomp_lista = [int(num) for num in acomp_s.split()]
    bebida_lista = [int(num) for num in bebida_s.split()]

    return round((caloria_calculator(principal_lista, acomp_lista, bebida_lista) + gusto_calculator(principal_lista, acomp_lista, bebida_lista)) / 2)

def main():
    num_generations = 50
    num_parents_mating = 3

    parent_selection_type = "sss"
    keep_parents = 1

    crossover_type = "single_point"

    mutation_type = "random"
    mutation_num_genes = 2

    # Poblacion inicial para limitar genes
    initial_population = [
        [milanesa, papas_fritas, agua],
        [ensalada, arroz, bebida_cola],
        [bife, pan, jugo]
    ]

    gene_space = [[milanesa, ensalada, bife, pechuga_de_pollo, hamburguesa],
                  [pure_de_papa, ensalada_side, papas_fritas, arroz, pan],
                  [agua, bebida_cola, bebida_cola_sin_azucar, jugo, bebida_energetica]]

    # Creo clase de Pygad con parametros
    ga_instance = pg.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type= mutation_type,
                       mutation_num_genes=mutation_num_genes,
                       initial_population=initial_population,
                       gene_space = gene_space)

    ga_instance.run()

    print(ga_instance.best_solution())

if __name__=="__main__":
    main()