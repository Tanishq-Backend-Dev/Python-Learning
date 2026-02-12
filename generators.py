def topTenSquares():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n = n + 1
        
values = topTenSquares()
print(values.__next__())
print(values.__next__())
# for i in values:
#     print(i)