option = int(input("Введите 1 для ввода данных из терминала / введите 2 для ввода данных из файла\n"))
if option == 1:
    n, s, f = map(int,
                  input("Введите через пробел количество вершин графа, начальную вершину, конечную вершину: ").split())
    matrix = [0] * (n + 1)
    for row in range(1, n + 1):
        matrix[row] = [(i, int(j)) for i, j in
                       enumerate(input("Введите следующую строку матрицы смежности графа: ").split(), 1) if
                       int(j) != 0 and int(j) != -1]
else:
    path = input("Укажите путь к файлу: ")
    with open(path, "r") as file:
        n, s, f = map(int, file.readline().split())
        matrix = [0] * (n + 1)
        for row in range(1, n + 1):
            matrix[row] = [(i, int(j)) for i, j in
                           enumerate(file.readline().split(), 1) if
                           int(j) != 0 and int(j) != -1]

visited = [0] * (n + 1)
dist = [1000] * (n + 1)
dist[s] = 0

prev = [0] * (n + 1)


# выбираем минимум из непомеченных
def find_min_index():
    min_v = 1000
    for i in range(1, n + 1):
        if visited[i] == 0 and dist[i] < min_v:
            min_v = dist[i]
            index_r = i
    if min_v == 1000:
        index_r = -1
    return index_r


for i in range(1, n + 1):
    index = find_min_index()
    if index == -1:
        break
    elif visited[index] == 0:
        visited[index] = 1
        for value in matrix[index]:
            v, e = value[0], value[1]
            if dist[index] + e < dist[v]:
                dist[v] = dist[index] + e
                prev[v] = index

if dist[f] == 1000:
    print(-1)
else:
    current_graph = f
    path_ = []
    while prev[current_graph] != 0:
        if dist[current_graph] == 1000:
            break
        else:
            path_.append(current_graph)
            current_graph = prev[current_graph]
    path_.append(current_graph)
    print(*path_[::-1])