def main():
    input_1 = input()
    input_2 = input()

    if len(input_1 + input_2) < 2:
        return

    if input_1 == input_2:
        print(input_1)
        return
    
    input1_map = {}
    input2_map = {}


    for i in input_1:
        if i not in input1_map:
            input1_map[i] = 1
        else:
            input1_map[i] += 1

    for i in input_2:
        if i not in input2_map:
            input2_map[i] = 1
        else:
            input2_map[i] += 1

    final_hasmap = {}

    letters = set(list(input1_map.keys()) + list(input2_map.keys()))

    for letter in letters:
        l1 = input1_map.get(letter, 0)
        l2 = input2_map.get(letter, 0)

        final_hasmap[letter] = l1 if l1 > l2 else l2
    
    sequence = ""


    for letter, count in final_hasmap.items():
        sequence += letter * count 

    print(sequence)
    
main()
