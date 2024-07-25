def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('TECHNOMAIN'))

print(lexicographi_sort('SALTLAKE'))
