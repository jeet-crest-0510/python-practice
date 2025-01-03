dict = {
    'name' : 'jeet',
    'age' : 21,
    'mark1' : 85,
    'mark2' : 79
}

print(f'Original Dict: {dict}')
print(f'Sorted Dict: {sorted(dict)}')
print(f'Sorted Dict by values: {sorted(dict.items(), key= lambda k: k[0])}')