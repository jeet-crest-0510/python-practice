def overlapping_substring(string, pattern):
    result = []
    for i in range(len(string) - len(pattern) + 1):
        if string[i: i + len(pattern)] == pattern:
            result.append(i)
    return result

string1 = 'geeksforgeeksforgeeks'
pattern1 = 'geeksforgeeks'

string2 = 'barfoobarfoobarfoobarfoobarfoo'
pattern2 = 'foobarfoo'

print(overlapping_substring(string1, pattern1))
print(overlapping_substring(string2, pattern2))
