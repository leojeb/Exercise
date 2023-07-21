s = ['a', 'b', 'c']
cbns = []
cnt = 1
for i in N:
    cnt = (N - i) * cnt

res = ['']*cnt

def add_char(s: list, idx: int):
    s1 = s.copy()
    c = s1.pop(0)
    for i in range(len(s1)):
        res[i*idx].append(c)
        add_char(s1, i)
        
        pick_one()
    
        
        
        