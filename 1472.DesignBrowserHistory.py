
# Solution Using Arrays

class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser_history = [homepage]
        self.cur_idx = 0
    def visit(self, url: str) -> None:
        self.browser_history = self.browser_history[:self.cur_idx + 1]
        self.browser_history.append(url)
        self.cur_idx += 1

    def back(self, steps: int) -> str:
        if self.cur_idx - steps < 0:
            self.cur_idx = 0
        else:
            self.cur_idx -= steps
        print(self.browser_history, self.cur_idx)
        return self.browser_history[self.cur_idx]

    def forward(self, steps: int) -> str:
        if steps + self.cur_idx >= len(self.browser_history):
            self.cur_idx = len(self.browser_history) - 1
        else:
            self.cur_idx += steps
        return self.browser_history[self.cur_idx]


# Solution Using Doubly LinkedList

class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next


    def back(self, steps: int) -> str:
        while (steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while (steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val
