
import sys
from alg_creator import *

if __name__ == '__main__':

    problem_name = "C101"
    alg_name = "PSO"

    customers_count = 30          

    max_generations = 1

    particles_pop_size = 30 # particles_pop_size = customers_size
    cognitive_acceleration = 2
    social_acceleration = 2
    speed_limit = 1.

    population_size = 1
    crossover_prob = 0.9
    mutation_prob = 0.09

    print('### GENERAL INFO ###')
    print('Problem name: ' + problem_name)
    print(f'Customer count: {customers_count}')
    print(f'Max iterations: {max_generations}')
    print('Algorithm: ' + alg_name)
    print('### ALGORITHM PARAMETERS ###')

    '''
    for mutation_prob in [0.03, 0.09]:
    for crossover_prob in [0.5, 0.7, 0.9]:
    for speed_limit in [1.5, 3]:
    for cognitive_acceleration, social_acceleration in [[2, 2], [1.5, 2.5], [2.5, 1.5]]:
    '''

    if alg_name == "PSO":
        print(f'Particles population size: {particles_pop_size}')
        print(f'Social acceleration: {social_acceleration}')
        print(f'Cognitive acceleration: {cognitive_acceleration}')
        print(f'Speed limit: {speed_limit}')
        res = run_pso(instance_name=problem_name, particle_size=particles_pop_size, pop_size=population_size,
                      max_iteration=max_generations, cognitive_coef=cognitive_acceleration,
                      social_coef=social_acceleration, s_limit=speed_limit, plot=True)

    elif alg_name == "GA":
        print(f'Population size: {population_size}')
        print(f'Crossover probability: {crossover_prob}')
        print(f'Mutation probability: {mutation_prob}')
        res = run_ga(instance_name=problem_name, individual_size=customers_count, pop_size=population_size,
                     cx_pb=crossover_prob, mut_pb=mutation_prob, n_gen=max_generations, plot=True)

    else:
        print("invalid algorithm")
        sys.exit()
