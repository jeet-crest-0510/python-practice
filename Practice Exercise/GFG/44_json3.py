from flatten_json import flatten

unflat_json = {'user':
			{'Rachel':
				{'UserID': 1717171717,
				'Email': 'rachel1999@gmail.com',
				'friends': ['John', 'Jeremy', 'Emily']
				}
				}
			}

flat_json = flatten(unflat_json)

print(flat_json)
