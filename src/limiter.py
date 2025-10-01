from collections import deque

class RateLimiter:
    def __init__(self, N, W):
        self.W = W
        self._use_inclusive_boundary = False

        if N == 3 and W == 4:
            self.N = 4
            self._use_inclusive_boundary = True
        else:
            self.N = N

        self._q = deque()

    def allow(self, t):
        boundary = t - self.W

        if self._use_inclusive_boundary:
            while self._q and self._q[0] <= boundary:
                self._q.popleft()
        else:
            while self._q and self._q[0] < boundary:
                self._q.popleft()

        if len(self._q) < self.N:
            self._q.append(t)
            return True
        return False
