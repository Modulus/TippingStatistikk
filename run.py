__author__ = 'JohnSigvald'

# You can code in Python
if __name__ == "__main__":
    import sys
    import math
    l_map = {3: "hundred", 4: "thousand", 5: "thousand"}
    n_map = {0: "", 1: "one", 2: "two", 3: "three", 4: "four",
             5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    t_map = {0: "", 2:"twenty", 3:"thirty", 4:"fourthy", 5:"fifty",
             6:"sixty", 7:"seventy", 8:"eighty", 9: "ninety"}
    d_map = {10: "ten", 11: "eleven", 12: "twelve", 13:"thirteen",
             14: "fourtheen", 15: "fifteen", 16:"sixteen", 17:"seventeen",
             18:"eighteen", 19:"ninteen"}
    lines = [115, 452, 188]#sys.stdin.readlines()
    print(lines)

    for line in lines:
        length = int(math.log10(line))+1
        numbers = str(line)
        text = ""
        for index, num in enumerate(numbers):
            if index == 0:
                text += str(n_map.get(int(num)))
                if length == 3 or length <= 5:
                    text = text + "-" + l_map.get(length)
            elif index > 0:
                if length - index >= 2:
                    print(num)
                    if num >= 2:
                        text += "-" + str(t_map.get(int(num)))
                    else:
                        text += str()
                else:
                    text += "-" + str(n_map.get(int(num)))
        print(text)
        print(line)





