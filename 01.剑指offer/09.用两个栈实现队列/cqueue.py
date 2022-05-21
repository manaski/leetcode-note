class CQueue:
    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def appendTail(self, value: int) -> None:
        self.stack_in.insert(0, value)

    def deleteHead(self) -> int:
        if len(self.stack_out) == 0:
            for v in self.stack_in:
                self.stack_out.insert(0, v)
                self.stack_in.pop(0)

        if len(self.stack_out) == 0:
            return -1

        return self.stack_out.pop(0)


if __name__ == '__main__':
    q = CQueue()
    q.appendTail(1)
    q.appendTail(2)
    q.appendTail(3)
    print(q.deleteHead())
    print(q.deleteHead())
    print(q.deleteHead())
    print(q.deleteHead())
