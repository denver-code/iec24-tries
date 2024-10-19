import re

def main():
    excercises_number = int(input())

    if excercises_number > 31 and excercises_number < 1:
        return

    g = []

    for i in range(excercises_number):
        inmp = input()
        if len(inmp) > 50 and len(inmp) < 1:
            return
        g.append(inmp)

    emj_map = {
        "leg": "🦵",
        "rest": "😎",
        "arm": "💪",
        "biceps": "💪"
    }
    
    output = ""
    
    for i in g:
        word = re.findall(r'leg|rest|arm|biceps', i)

        if not word:
            output += emj_map["arm"]
        elif "rest" in word and "leg" in word:
            output += emj_map["rest"]
        else:
            output += emj_map[word[0]]
    
    output *= 31

    for week in range(1,6):
        if week == 5:
            print(f"{week} {output[week-1*week:week-1*week+3]}")
        else:
            print(f"{week} {output[week-1*week:week-1*week+7]}")

main()