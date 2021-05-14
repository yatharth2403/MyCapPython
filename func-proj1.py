def frequency(str):
    d1 = {}
    d2 = {}
    for i in str:
        if i in d1.keys():
            d1[i] += 1
        else:
            d1[i] = 1
    d2 = sorted(d1.items(), key=lambda k:k[1], reverse = True)
    print(d2)

word = input("Enter the word: ")
frequency(word)
