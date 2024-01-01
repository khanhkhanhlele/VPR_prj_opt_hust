# import numpy as np
# import random
# def read_data():
#     N, K = list(map(int, input().split()))
#     d = [0]
#     d.extend(list(map(int, input().split())))
#     t = []
#     for i in range(N+1):
#         t.append(list(map(int, input().split())))
#     return N, K, d, t


# def cal_time_employee(segment, d, t):
#     if len(segment) == 0:
#         return 0
#     time_work = 0
#     time_work += t[0][segment[0]]
#     for i in range(len(segment) - 1):
#         time_work += t[segment[i]][segment[i+1]] + d[segment[i]]
#     time_work += t[segment[-1]][0] + d[segment[-1]]
#     return time_work

# def split_segment(chromosome, N):
#     segment = []
#     segment_employee = []
#     for i in range(len(chromosome)):
#         if chromosome[i] > N:
#             segment.append(segment_employee)
#             segment_employee = []
#         else:
#             segment_employee.append(chromosome[i])
#     segment.append(segment_employee)
#     return segment
        


# N, K, d, t = read_data()
# POP_SIZE = 100
# MAX_GEN = 100
# crossover_parameter = 0.8
# mutation_parameter = 0.1

# class Individual:
#     def __init__(self):
#         self.chromosome = list(np.zeros(N + K - 1, dtype = int))
#         self.fitness = None
    
#     def cal_fitness(self):
#         segment = split_segment(self.chromosome, N)
#         max_time = 0
#         for i in range (K):
#             max_time = max(max_time, cal_time_employee(segment[i], d, t))
#         self.fitness = max_time
        
#     def gen_random(self):
#         number_list = list(range(1, N+K))
#         self.chromosome = list(random.sample(number_list, len(number_list)))
#         self.cal_fitness()

# def order_crossover(parent1, parent2):
#     indi1 = Individual()
#     indi2 = Individual()
    
#     start = random.randint(0, N + K - 3)
#     end = random.randint(start, N + K -2)
#     for i in range(start, end + 1):
#         indi1.chromosome[i] = parent1.chromosome[i]
#         indi2.chromosome[i] = parent2.chromosome[i]
    
#     indi1_index = end + 1
#     indi1_i = 0
#     while indi1_index < N + K - 1:
#         if parent2.chromosome[indi1_i] not in indi1.chromosome:
#             indi1.chromosome[indi1_index] = parent2.chromosome[indi1_i]
#             indi1_index += 1
#         indi1_i += 1
#     indi1_index = 0
#     while indi1_index < start:
#         if parent2.chromosome[indi1_i] not in indi1.chromosome:
#             indi1.chromosome[indi1_index] = parent2.chromosome[indi1_i]
#             indi1_index += 1
#         indi1_i += 1
    
#     indi2_index = end + 1
#     indi2_i = 0
#     while indi2_index < N + K - 1:
#         if parent1.chromosome[indi2_i] not in indi2.chromosome:
#             indi2.chromosome[indi2_index] = parent1.chromosome[indi2_i]
#             indi2_index += 1
#         indi2_i += 1
    
#     indi2_index = 0
#     while indi2_index < start:
#         if parent1.chromosome[indi2_i] not in indi2.chromosome:
#             indi2.chromosome[indi2_index] = parent1.chromosome[indi2_i]
#             indi2_index += 1
#         indi2_i += 1
    
#     indi1.cal_fitness()
#     indi2.cal_fitness()
#     return indi1, indi2

# def mutation(parent):
#     indi = Individual()
#     index1 = random.randint(0, N + K -2)
#     index2 = random.randint(0, N + K -2)
#     while index1 == index2:
#         index2 = random.randint(0, N + K -2)
    
#     indi.chromosome = parent.chromosome.copy()
#     indi.chromosome[index1], indi.chromosome[index2] = indi.chromosome[index2], indi.chromosome[index1]
#     indi.cal_fitness()
#     return indi
    
    
    
# class Population:
#     def __init__(self):
#         self.indivs = []
    
#     def gen_pop(self):
#         for i in range(POP_SIZE):
#             indi = Individual()
#             indi.gen_random()
#             self.indivs.append(indi)
        
#     def evolve(self):
#         for i in range(MAX_GEN):
#             for j in range(POP_SIZE):
#                 if random.random() < crossover_parameter:
#                     parent1_index = random.randint(0, POP_SIZE - 1)
#                     parent2_index = random.randint(0, POP_SIZE - 1)
#                     while parent1_index == parent2_index:
#                         parent2_index = random.randint(0, POP_SIZE - 1)
#                     parent1 = self.indivs[parent1_index]
#                     parent2 = self.indivs[parent2_index]
                    
#                     indi1, indi2 = order_crossover(parent1, parent2)
#                     if random.random() < mutation_parameter:
#                         indi1 = mutation(indi1)
#                         indi2 = mutation(indi2)
#                     self.indivs.append(indi1)
#                     self.indivs.append(indi2)
#             self.indivs.sort(key = lambda x: x.fitness)
#             self.indivs = self.indivs[:POP_SIZE]
#         return self.indivs[0].fitness, self.indivs[0].chromosome

# pop = Population()
# pop.gen_pop()
# fitness, chromosome = pop.evolve()
# segment = split_segment(chromosome, N)
# print(K)
# for se in segment:
#     print(len(se) + 2)
#     print(0, end = ' ')
#     for pos in se:
#         print(pos, end = ' ')
#     print(0)
import numpy as np
def read_data():
    N, K = list(map(int, input().split()))
    d = [0]
    d.extend(list(map(int, input().split())))
    t = []
    for i in range(N+1):
        t.append(list(map(int, input().split())))
    return N, K, d, t

def creat_cost(N, d, t):
    cost_matrix = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(N + 1):
            if i != j:
                cost_matrix[i][j] = d[j] + t[i][j]

    return cost_matrix

def cal_cost(router, t, d):
    cost = [0 for i in range(len(router))]
    for i in range(len(router)):
        for j in range(len(router[i]) - 1):
            cost[i] += t[router[i][j]][router[i][j + 1]] + d[router[i][j + 1]]
    return cost

def local_search_greedy2():
    N, K, d, t = read_data()
    cost_matrix = creat_cost(N, d, t)

    router = [[0] for i in range(K)]
    cost = [0 for i in range(K)]
    tuple_dis_depot = []
    for i in range(1, N + 1):
        tuple_dis_depot.append((i, cost_matrix[0][i]))
    tuple_dis_depot.sort(key = lambda x: x[1])

    while len(tuple_dis_depot) > 0:
        # lay phan tu dau tien trong tuple_dis_depot
        first = tuple_dis_depot[0][0]
        # xoa phan tu dau tien trong tuple_dis_depot
        tuple_dis_depot.pop(0)
        # Them vao router lam tang it chi phi nhat

        cost_value = [cost[i] + cost_matrix[router[i][-1]][first] for i in range(K)]
        min_cost = min(cost_value)

        index_list = [index for index, value in enumerate(cost_value) if value == min_cost]

        router_selected = index_list[0]
        for index in index_list[1:]:
            if cost[index] < cost[router_selected]:
                router_selected = index
        
        router[router_selected].append(first)
        cost[router_selected] += cost_matrix[router[router_selected][-2]][first]

    for i in range(K):
        router[i].append(0)
        cost[i] += cost_matrix[router[i][-2]][0]
    history_count = 0
    while True:
        max_cost = max(cost)
        max_index = [i for i, j in enumerate(cost) if j == max_cost]
        router_neighborhood = []

        swap1 = np.random.choice(max_index)
        swap2 = np.random.randint(0, K)
        while swap2 == swap1:
            swap2 = np.random.randint(0, K)
        
        if len(router[swap1]) == 3:
            a1 = 1
            b1 = 2
        else:
        #a1 != b1
            a1 = np.random.randint(1, len(router[swap1]) - 2)
            b1 = np.random.randint(a1 + 1, len(router[swap1]) - 1)

        if len(router[swap2]) == 3:
            a2 = 1
            b2 = 2
        else:
            a2 = np.random.randint(1, len(router[swap2]) - 2)
            b2 = np.random.randint(a2 + 1, len(router[swap2]) - 1)

        new_router1 = router[swap1][:a1] + router[swap2][a2:b2] + router[swap1][b1:]
        new_router2 = router[swap2][:a2] + router[swap1][a1:b1] + router[swap2][b2:]

        for i in range(K):
            if i == swap1:
                router_neighborhood.append(new_router1)
            elif i == swap2:
                router_neighborhood.append(new_router2)
            else:
                router_neighborhood.append(router[i])
        
        cost_neighborhood = cal_cost(router_neighborhood, t, d)
        new_max_cost = max(cost_neighborhood)
        if new_max_cost < max_cost:
            router = router_neighborhood
            cost = cost_neighborhood
            history_count = 0
        else:
            history_count += 1
        if history_count == 1000:
            break
        

    print(K)
    for sub in router:
        print(len(sub))
        for pos in sub:
            print(pos, end = ' ')
        print()
    return router, cost, K

router, cost, K = local_search_greedy2()


# import numpy as np

# def cal_cost(router, t, d):
#     cost = [0 for i in range(len(router))]
#     for i in range(len(router)):
#         for j in range(len(router[i]) - 1):
#             cost[i] += t[router[i][j]][router[i][j + 1]] + d[router[i][j + 1]]
#     return cost

# def UCV(visited):
#         unvisited = []
#         for pos in range(len(visited)):
#             if visited[pos] == 0:
#                 unvisited.append(pos)
#         return unvisited

# def local_search_greedy1():
#     N, K, d, t = read_data()
#     router = []
#     for i in range(K):
#         router.append([0])

#     visited = np.zeros(N + 1, dtype = int)
#     visited[0] = 1      
        
#     k = 0
#     while sum(visited) != N + 1:
#         start = router[k][-1]
#         next_pos = 0
#         next_time = 1000000
#         unvisited = UCV(visited)
#         for pos in unvisited:
#             if t[start][pos] + d[pos] < next_time:
#                 next_time = t[start][pos] + d[pos]
#                 next_pos = pos
#         router[k].append(next_pos)
#         visited[next_pos] = 1
#         k = (k + 1) % K
    
#     for i in range(K):
#         router[i].append(0)
#     cost = [0 for i in range(K)]
#     for i in range(K):
#         for j in range(len(router[i]) - 1):
#             cost[i] += t[router[i][j]][router[i][j + 1]] + d[router[i][j + 1]]
#     history_count = 0
#     while True:
#         max_cost = max(cost)
#         max_index = [i for i, j in enumerate(cost) if j == max_cost]
#         router_neighborhood = []

#         swap1 = np.random.choice(max_index)
#         swap2 = np.random.randint(0, K)
#         while swap2 == swap1:
#             swap2 = np.random.randint(0, K)
        
#         #a1 != b1
#         a1 = np.random.randint(1, len(router[swap1]) - 2)
#         b1 = np.random.randint(a1 + 1, len(router[swap1]) - 1)

#         a2 = np.random.randint(1, len(router[swap2]) - 2)
#         b2 = np.random.randint(a2 + 1, len(router[swap2]) - 1)

#         new_router1 = router[swap1][:a1] + router[swap2][a2:b2] + router[swap1][b1:]
#         new_router2 = router[swap2][:a2] + router[swap1][a1:b1] + router[swap2][b2:]

#         for i in range(K):
#             if i == swap1:
#                 router_neighborhood.append(new_router1)
#             elif i == swap2:
#                 router_neighborhood.append(new_router2)
#             else:
#                 router_neighborhood.append(router[i])
        
#         cost_neighborhood = cal_cost(router_neighborhood, t, d)
#         new_max_cost = max(cost_neighborhood)
#         if new_max_cost < max_cost:
#             router = router_neighborhood
#             cost = cost_neighborhood
#             history_count = 0
#         else:
#             history_count += 1
#         if history_count == 100:
#             break
        

#     print(K)
#     for sub in router:
#         print(len(sub))
#         for pos in sub:
#             print(pos, end = ' ')
#         print()
#     return router, cost

# router, cost = local_search_greedy1()





        



