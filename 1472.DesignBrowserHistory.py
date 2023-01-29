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


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
