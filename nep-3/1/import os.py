import os
import itertools

def split_file(filename, parts):
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    part_length = len(lines) // parts
    for i in range(parts):
        start = i * part_length
        end = None if i+1 == parts else (i+1) * part_length
        with open(f'{filename}_{i}', 'w') as f:
            f.writelines(lines[start:end])

# Split 'test.xyz' into 5 parts
#split_file('test.xyz', 5)

# Split 'force_test.out' into 2 parts
split_file('force_test.out', 2)