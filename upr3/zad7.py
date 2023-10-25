class Stack:
    def __init__(self, *args):
        self.stack = list(args)
    
    @property
    def top(self):
        if self.stack != []:
            return self.stack[-1]
        return None

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def __len__(self):
        return len(self.stack)

# Тестове
assert Stack().top is None
assert Stack("a").top == "a"
assert Stack(1, 2, 3, 4, 5).top == 5
assert Stack(*list(range(1000)).top)== 999

# Тестове за pop
s = Stack("a", "b", "c", "d")
s.pop()
assert s.top == "c"
s.pop()
s.pop()
assert s.top == "a"
s.pop()
assert s.top is None

# Тестове за push
s.push("X")
assert s.top == "X"
s.push("X")
s.push("X")
assert s.top == "X"

# Тестове за len
assert len(s) == 3
s.pop(); s.pop(); s.pop()
assert len(s) == 0
