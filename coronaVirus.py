def helper():
    mat = []
    for i in range(9):
        mat.append(input())
    print()

    matrix = []
    total = 0
    for i in range(8, -1, -1):
        matrix.append(mat[i])
    for i in matrix:
        for j in i:
            if j == 'a' or j == 'c':
                total += 1
    trajectory = [(0, 0)]

    def traverse(i, j, count, infected):

        if count == 2:
            return infected

        prev = trajectory[-1]
        trajectory.append((i, j))
        print(j, i)

        if matrix[i][j] == 'a':
            infected += 1
            if prev[0] > i and prev[1] > j:
                i -= 1
                j += 1
            elif prev[0] < i and prev[1] < j:
                i += 1
                j -= 1
            elif prev[0] > i and prev[1] < j:
                i += 1
                j += 1
            else:
                i -= 1
                j -= 1

        elif matrix[i][j] == 'c':
            infected += 1
            if prev[0] > i and prev[1] > j:
                i += 1
                j -= 1
            elif prev[0] < i and prev[1] < j:
                i -= 1
                j += 1
            elif prev[0] > i and prev[1] < j:
                i -= 1
                j -= 1
            else:
                i += 1
                j += 1

        elif matrix[i][j] == '.':
            if prev[0] < i and prev[1] < j:
                i += 1
                j += 1
            elif prev[0] > i and prev[1] > j:
                i -= 1
                j -= 1
            elif prev[0] > i and prev[1] < j:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1
        else:
            count += 1
            if i == 0 or i == 8:
                i = prev[0]
                if prev[1] < j:
                    j += 1
                else:
                    j -= 1
            else:
                j = prev[1]
                if prev[0] < i:
                    i += 1
                else:
                    i -= 1

        return traverse(i, j, count, infected)
    infected = traverse(1, 1, 0, 0)
    trajectory = trajectory[1:]

    answer = []

    for i in range(8, -1, -1):
        s = ''
        for j in range(20):
            if (matrix[i][j] == 'a' or matrix[i][j] == 'c') and (i, j) in trajectory:
                s += '-'
            else:
                s += matrix[i][j]
        answer.append(s)

    for i in answer:
        for j in i:
            print(j, end='')
        print()

    print("safe={}".format(total-infected))
    print("infected={}".format(infected))


helper()
