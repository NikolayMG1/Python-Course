def merge(d1, d2):
    for i in d2.keys():
        d1[i]=d2[i]
    return d1


assert merge({"name": "Pesho", "year": 1999}, {"groups": ["A", "B"]}) == {"name": "Pesho", "year": 1999, "groups": ["A", "B"]}
assert merge({}, {}) == {}