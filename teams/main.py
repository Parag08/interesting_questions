input = [[1,1,1,0,1],
         [0,1,0,0,0],
         [1,0,0,0,1],
         [0,0,0,1,1],
         [1,0,0,0,0]]

checked = []

def check_matrix(i,j):
    check = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1, j-1],[i+1, j],[i+1, j+1]]
    return_array = []
    for elem in check:
        if (elem[0] in range(0,len(input))) and (elem[1] in range(0, len(input[0]))):
            return_array.append(elem)
    return return_array

def iterate(i,j):
    elem_to_check = check_matrix(i,j)
    team_member = 1
    checked.append([i,j])
    while True:
        pos = elem_to_check[-1]
        if (input[pos[0]][pos[1]] == 1) and (pos not in checked):
            team_member = team_member + 1
            elem_to_check.pop()
            elem_to_check = elem_to_check + check_matrix(pos[0], pos[1])
        else:
            elem_to_check.pop() 
        checked.append(pos)
        if len(elem_to_check) == 0:
            break
    return team_member

teams = []

for i in range(len(input)):
    for j in range(len(input)):
        if ([i,j] not in checked) and (input[i][j] == 1):
            teams.append(iterate(i,j))

print(teams)