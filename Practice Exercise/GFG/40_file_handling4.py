with open('Practice Exercise\GFG\demo.txt') as f:
    freq = {}

    for x in f.readlines():
        text = x
        text1 = text.replace(',','').replace('.','').replace('\n','').split(' ')
        
        for t in text1:
            if t not in freq:
                freq[t] = 1
            else:
                freq[t] += 1

    maxf = max(freq.values())
    words = [k for k,v in freq.items() if v == maxf]
    print(words)