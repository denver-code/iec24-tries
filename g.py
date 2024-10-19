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

    result_x_y = []

    for y, line_h in enumerate(arr_h):
        for x, item in enumerate(line_h):
            if item == arr_k[0][0]:
                
                if x + ck > ch or y + rk > rh:
                    break
                print(x, y)
                item = [a[x:x+ck] for a in arr_h[y:y+rk]]
                if item == arr_k:
                    for yy in range(rk):
                        for xx in range(ck):
                            result_arr[yy][xx] = arr_h[x]
                
                break
                # err_status = 0
                # tmp_arr = []
                # if x + ck > ch or y + rk > rh:
                #     break
                # for letter_k_x in range(ck):
                #     for letter_k_y in range(rk):
                #         if arr_k[letter_k_y][letter_k_x] != arr_h[y+letter_k_y][x+letter_k_x]:
                #             err_status = 1
                #             break
                #         else:
                #             tmp_arr.append([y+letter_k_y,x+letter_k_x])
                # if not err_status:
                #     result_x_y.append(tmp_arr)
    
    # for word in result_x_y:
    #     for letter in word:
    #         result_arr[letter[0]][letter[1]] = arr_h[letter[0]][letter[1]]

    
    # for linexx in result_arr:
    #     print("".join(linexx))

main()