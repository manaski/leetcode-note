class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_data = []
        self.stack_min = []

    def push(self, x: int) -> None:
        self.stack_data.insert(0, x)

        if len(self.stack_min) == 0:
            self.stack_min.insert(0, x)
        else:
            if x <= self.stack_min[0]:
                self.stack_min.insert(0, x)

    def pop(self) -> None:
        val = self.stack_data[0]
        self.stack_data.pop(0)

        if val <= self.stack_min[0]:
            self.stack_min.pop(0)


    def top(self) -> int:
        return self.stack_data[0]

    def min(self) -> int:
        return self.stack_min[0]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(5)
    print(stack.min())
    stack.push(4)
    print(stack.min())
    stack.push(3)
    print(stack.min())
    stack.push(2)
    print(stack.min())
