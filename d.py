
def main():
    q = int(input())
    if q < 1 or q > 100000:
        return 
    
    for line in range(q):
        p, r, y = map(int, input().split())
        if p < -1 or r < -1 or y < -1 or p > 1 or r > 1 or y > 1:
            return
        


    # n e s w
    w = e-p
    e = p + w 

        
