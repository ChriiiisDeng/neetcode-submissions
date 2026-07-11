
class MinStack:    
    def __init__(self):
        self.num_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.num_stack.append(val)
        min_val = val
        if len(self.min_stack) > 0:
            min_val = min(val, self.min_stack[-1])
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.num_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.num_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]