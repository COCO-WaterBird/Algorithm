from collections import deque

class RecentCounter:
    def __init__(self):
        self.Q = deque()

    def ping(self, t: int) -> int:
        self.Q.append(t)
        while self.Q and self.Q[0] < t - 3000:
            self.Q.popleft()
        return len(self.Q)
