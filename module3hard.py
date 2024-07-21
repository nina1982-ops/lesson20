def calculate_structure_sum(data_structure):
    if isinstance(data_structure, int):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, dict):
        summ = 0
        for key, value in data_structure.items():
            summ += calculate_structure_sum(value)
            summ += calculate_structure_sum(key)
        return summ
    elif hasattr(data_structure, '__iter__'):
        summ = 0
        for i in data_structure:
            summ += calculate_structure_sum(i)
        return summ
result = calculate_structure_sum([
     [1, 2, 3],
     {'a': 4, 'b': 5},
     (6, {'cube': 7, 'drum': 8}),
     "Hello",
     ((), [{(2, 'Urban', ('Urban2', 35))}])
    ])
print(result)
