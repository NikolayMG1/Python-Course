class DefaultArray:
    """
    A container that behaves like a list with a maximum size (array)
    but returns a default value for missing indices.
    """

    def __init__(self, limit, default_element_func):
        self._limit = limit
        self._default_element_func = default_element_func
        self._list = [None] * limit

    def __len__(self):
        return self._limit

    def __getitem__(self, index):
        element = self._list[index]
        return self._default_element_func() if element is None else element

    def __setitem__(self, index, element):
        self._list[index] = element

    def __delitem__(self, index):
        self._list[index] = None

    def __contains__(self, item):
        return item in self._list

arr = DefaultArray(10, int)  # `int` can be viewed as a function that returns 0 upon calling

print(f"{arr[1] = }")  # __getitem__

arr[1] = 42  # __setitem__

print(f"{arr[1] = }")
print(f"{42 in arr = }")  # __contains__

del arr[1]  # __delitem__

print(f"{arr[1] = }")
print(f"{42 in arr = }")