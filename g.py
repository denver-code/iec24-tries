def main():
    rk, ck = map(int, input().split())
       
    arr_k = [] 
    for line in range(rk):
        raw_line = input()
        if len(raw_line) > ck:
            return
        arr_k.append(list(map(str, raw_line)))

    rh, ch = map(int, input().split())

    arr_h = [] 
    for line in range(rh):
        raw_line = input()
        if len(raw_line) > ch:
            return
        arr_h.append(list(map(str, raw_line)))
    
    if arr_h == arr_k:
        return arr_h

    result_arr = []
    for linexxx in range(rh):
        result_arr.append(["."]*ch)

    for y, line_h in enumerate(arr_h):
        for x, item in enumerate(line_h):
            if item == arr_k[0][0]:
                if x + ck > ch or y + rk > rh:
                    break
                item = [a[x:x+ck] for a in arr_h[y:y+rk]]
                if item == arr_k:
                    for yy in range(rk):
                        for xx in range(ck):
                            result_arr[y+yy][x+xx] = arr_h[y+yy][x+xx]
    
    for linexx in result_arr:
        print("".join(linexx))

main()