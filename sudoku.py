sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
m = "---------------"

for i in sudoku:
    x=0
    while x<len(i):
        if x%2!=0:
            i.insert(x, "")
        x+=1

for t in sudoku:
    t.insert(6, "|")
    t.insert(13, "|")

x=0
while x<=len(sudoku):
    if x%4==0 or x==0:
        sudoku.insert(x, m)
    x+=1

for e in sudoku:
    print(*e)