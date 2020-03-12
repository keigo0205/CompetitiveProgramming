class UnionFind:
    def __init__(self, N):
        # par = parent
        self.par = [i for i in range(N)]
        return

    def root(self, x):
        if self.par[x] == x:
            return (x)
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return (self.root(x) == self.root(y))

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if (x == y):
            return False

        self.par[x] = min(x, y)
        self.par[y] = min(x, y)
        return True
