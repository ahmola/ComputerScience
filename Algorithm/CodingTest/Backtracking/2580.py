from itertools import combinations, permutations

def define_square(seudoku, square):
    for i in range(9):
        for j in range(9):
            square[(i//3)*3 + j//3].append(seudoku[i][j])

def validate_moc(moc):
    for i in range(9):
        row = [1,2,3,4,5,6,7,8,9]
        for j in range(9):
            if moc[i][j] in row or moc[i][j] == 0:
                if moc[i][j] != 0:
                    row.remove(moc[i][j])
            else:
                return False

    for j in range(9):
        col = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            if moc[i][j] in col or moc[i][j] == 0:
                if moc[i][j] != 0:
                    col.remove(moc[i][j])
            else:
                return False

    square = [[] for _ in range(9)]
    define_square(moc, square)
    for s in square:
        squa = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            if s[i] in squa or s[i] == 0:
                if s[i] != 0:
                    squa.remove(s[i])
            else:
                return False
    
    return True
    
def is_not_validate(seudoku):
    for i in range(9):
        for j in range(9):
            if seudoku[i][j] == 0:
                return True

    return False

def solution(seudoku):
    # square = [[] for _ in range(9)]

    while is_not_validate(seudoku):
        for i in range(9):
            row_sum = 0
            zero_count = 0
            zero_coordinate = []
            row = [1,2,3,4,5,6,7,8,9]

            for j in range(9):
                if seudoku[i][j] == 0:
                    zero_coordinate.append([i, j])
                    zero_count += 1
                else:
                    row.remove(seudoku[i][j])
                row_sum += seudoku[i][j]
            
            row_sum = 45-row_sum
            if row_sum == 0:
                continue
            
            for comb in combinations(row, zero_count):
                for per in permutations(comb):
                    per = list(per)
                    moc_seudoku = [row[:] for row in seudoku]
                    for i in range(len(per)):
                        moc_seudoku[zero_coordinate[i][0]][zero_coordinate[i][1]] = per[i]
                        if validate_moc(moc_seudoku):
                            seudoku = moc_seudoku
    
    for i in range(9):
        for j in range(9):
            print(seudoku[i][j], end=" ")
        print()
    print()

seudoku = [list(map(int, input().split(" "))) for _ in range(9)]
solution(seudoku)