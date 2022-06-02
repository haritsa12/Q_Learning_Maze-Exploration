import randomz
alpha = 0.5
gamma = 0.9
Q_table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0][0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0][0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0][0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


for i in range(80):
    for j in range(4):   
       Q_table[i][j] = random.random()
       
       
def print_Qtable(Q_table):
    print("\nState\t\tRight\t\t\tUp\t\t\tLeft\t\t\tDown")
    print("-----\t\t-----\t\t\t-----\t\t\t-----\t\t\t-----")

    for s in range(80):
        if(Q_table[s][0] >= 90):	
            print(s+1, "\t", Q_table[s][0], "\t\t\t", Q_table[s][1], "\t", Q_table[s][2], "\t", Q_table[s][3])
        else:
            print(s+1, "\t", Q_table[s][0], "\t", Q_table[s][1], "\t", Q_table[s][2], "\t", Q_table[s][3])
    s += 1

    print(s+1, "\t", Q_table[s][0], "\t\t\t", Q_table[s][1], "\t\t\t", Q_table[s][2], "\t\t\t", Q_table[s][3], "\n")

def Search_Location(maze):
    for i in range(3):
        for j in range(3):
			for k in range(3):
				for l in range(3):
					if maze[i][j][k][l] == 1:
					
						#return (5 * (i) + j + 1), i + 1, j + 1
					
						return (27 * (i) + 9*(j) + 3 * (k) + l + 1), i + 1, j + 1, k + 1,l + 1

def Action(mazes, Q_tables, epsilons):
    out = 0

    while out == 0:
        state, state_i, state_j, state_j, state_k = Search_Location(mazes)

        rdm = random.random()

        if epsilons <= rdm:
            max_value = max(Q_tables[state-1][0], Q_tables[state-1][1], Q_table[state-1][2], Q_table[state-1][3])
            
            for j in range(4):
                if max_value == Q_tables[state-1][j]:
                    act = j+1
        
        else:
            random_value = random.random()

            if random_value <= 0.25:
                act = 1
            elif random_value <= 0.5:
                act = 2
            elif random_value <= 0.25:
                act = 3
            else:
                act = 4

        if act == 1:
            state_i=state_i-1
            if counter_j % 2 = 0:
                state_j = state_j + 1
            else:
                state_j = state_j
            if counter_k % 2 = 0:
                state_k = state_k + 1
            else:
                state_k = state_k
            if counter_l % 2 = 0:
                state_l = state_l + 1
            else:
                state_l = state_l
        elif act == 2:
            state_j=state_j-1
            if counter_i % 2 = 0:
                state_i = state_i + 1
            else:
                state_i = state_i
            if counter_k % 2 = 0:
                state_k = state_k + 1
            else:
                state_k = state_k
            if counter_l % 2 = 0:
                state_l = state_l + 1
            else:
                state_l = state_l 
        elif act == 3:
            state_k=state_k-1
            if counter_j % 2 = 0:
                state_j = state_j + 1
            else:
                state_j = state_j
            if counter_i % 2 = 0:
                state_i = state_i + 1
            else:
                state_i = state_i
            if counter_l % 2 = 0:
                state_l = state_l + 1
            else:
                state_l = state_l 
        else:
            state_i=state_i-1
            if counter_j % 2 = 0:
                state_j = state_j + 1
            else:
                state_j = state_j
            if counter_k % 2 = 0:
                state_k = state_k + 1
            else:
                state_k = state_k
            if counter_i % 2 = 0:
                state_i = state_i + 1
            else:
                state_i = state_i

        # if state_i == 0:
            # out = 0 
        # elif state_j == 0:
            # out = 0
        # elif state_i == 6:
            # out = 0
        # elif state_j == 6:
            # out = 0
        # else:
            # out = out + 1

    new_mazes = [[[[0 for i in range (3)] for j in range (3)] for k in range (3)] for l in range (3)]
    new_mazes[state_i - 1][state_j - 1][state_k - 1][state_l - 1] = 1
    return act, new_mazes

def Routing(Q_table):
    print("Route")
    s = 1

    for i in range(1,82):

        print("S",  s, end=" ")

        M = max(Q_table[s-1][0], Q_table[s-1][1], Q_table[s-1][2], Q_table[s-1][3])
        I = 0
        while Q_table[s-1][I] != M:
            I += 1
        I += 1

        if I == 1:
		
			state_i=state_i-1
            if counter_j % 2 = 0:
                state_j = state_j + 1
            else:
                state_j = state_j
            if counter_k % 2 = 0:
                state_k = state_k + 1
            else:
                state_k = state_k
            if counter_l % 2 = 0:
                state_l = state_l + 1
            else:
                state_l = state_l
                
                break
         if I == 2:
			state_j=state_j-1
            if counter_i % 2 = 0:
                state_i = state_i + 1
            else:
                state_i = state_i
            if counter_k % 2 = 0:
                state_k = state_k + 1
            else:
                state_k = state_k
            if counter_l % 2 = 0:
                state_l = state_l + 1
            else:
                state_l = state_l
                
                break
         if I == 3:
			state_k=state_k-1
            if counter_j % 2 = 0:
                state_j = state_j + 1
            else:
                state_j = state_j
            if counter_i % 2 = 0:
                state_i = state_i + 1
            else:
                state_i = state_i
            if counter_l % 2 = 0:
                state_l = state_l + 1
            else:
                state_l = state_l
                
                break
          if I == 4:
			state_i=state_i-1
            if counter_j % 2 = 0:
                state_j = state_j + 1
            else:
                state_j = state_j
            if counter_k % 2 = 0:
                state_k = state_k + 1
            else:
                state_k = state_k
            if counter_i % 2 = 0:
                state_i = state_i + 1
            else:
                state_i = state_i
                
                break
        
    if i == 25:
        print("error")

def update_Qvalue(states, new_states, Q_tabless, acts, alphas, gammas, t):
    if new_state_i == 3 AND I=1:
        reward = 50
    elif new_state_j == 3 AND I=2:
        reward = 50
    elif new_state_k == 3 AND I=3:
        reward = 50
    elif new_state_l == 3 AND I=4:
        reward = 50
        
    elif new_state_i == 3 AND (I=2 OR I=3 OR I=4):
        reward = -50
    elif new_state_j == 3 AND (I=1 OR I=3 OR I=4):
        reward = -50
    elif new_state_k == 3 AND (I=2 OR I=1 OR I=4):
        reward = -50
    elif new_state_l == 3 AND (I=2 OR I=3 OR I=1):
        reward = -50
    
    if new_state_i == 1 AND I=1:
        reward = -50
    elif t == 15:     
        reward = -50 
    elif new_state_j == 1 AND I=2:
        reward = -50
    elif new_state_k == 1 AND I=3:
        reward = -50
    elif new_state_l == 1 AND I=4:
        reward = -50
        
    elif new_state_i == 1 AND (I=2 OR I=3 OR I=4):
        reward = 50
    elif new_state_j == 1 AND (I=1 OR I=3 OR I=4):
        reward = 50
    elif new_state_k == 1 AND (I=2 OR I=1 OR I=4):
        reward = 50
    elif new_state_l == 1 AND (I=2 OR I=3 OR I=1):
        reward = 50
    else:
        reward = 0 
    
    Q_tabless[states - 1][acts - 1] = (1 - alphas) * Q_tabless[states - 1][acts - 1] + alphas * (reward + gammas * max(Q_tabless[new_states - 1][0], Q_tabless[new_states - 1][1], Q_tabless[new_states - 1][2], Q_tabless[new_states - 1][3]))
    
    return Q_tabless, new_states

print("\nQ-Table and route before learning")
print_Qtable(Q_table)
Routing(Q_table)

for Episode in range(1, 301):
    maze = [[[[0 for i in range (3)] for j in range (3)] for k in range (3)] for l in range (3)]
	maze[0][0][0][0]=1
    epsilon = 1 - (Episode / 301)

    for i in range(1, 16):
        state, state_i, state_j = Search_Location(maze)
        
        if state == 81:
            break
        
        actss, new_maze = Action(maze, Q_table, epsilon)

        new_state, new_state_i, new_state_j = Search_Location(new_maze)
        
        Q_table, new_state = update_Qvalue(state, new_state, Q_table, actss, alpha, gamma, i)

        maze = new_maze

print("\nQ-Table and route after learning")
print_Qtable(Q_table)
Routing(Q_table)


