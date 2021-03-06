import itertools

def sequential_group_by(iterable, key):
    
    groups = []
    for group_key, group in itertools.groupby(iterable, lambda item: item.get(key, 'None')) :
        groups.append((group_key, list(group)))

    return groups
