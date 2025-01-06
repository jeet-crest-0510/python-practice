# txt = 'BACDGABCDA'
# pat = 'ABCD'

txt =  "AAABABAA" 
pat = "AABA"

def search_anagram(pat, txt):
    indexes = []

    n = len(pat)
    m = len(txt)

    dictP = {}

    for p in pat:
        if p not in dictP:
            dictP[p] = 1
        else:
            dictP[p] += 1

    dictT = {}
    i=j=0

    for j in range(m):
        if txt[j] not in dictT:
            dictT[txt[j]] = 1
        else:
            dictT[txt[j]] += 1

        if j-i+1 == n:
            if dictT == dictP:
                # print(i)
                # print(dictP)
                # print(dictT)
                indexes.append(i)
            
            dictT[txt[i]] -= 1
            if dictT[txt[i]] == 0:
                del dictT[txt[i]]
            # print(f'DictT: {dictT}')
            i += 1
        j += 1


    return indexes

indexes = search_anagram(pat, txt)
print(indexes)