class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        if not self.stack:
            self.stack.append((price, 1))
            return 1
            
        elif price < self.stack[-1][0]:
            self.stack.append((price, 1)) 

        elif price >= self.stack[-1][0]:
            while self.stack and self.stack[-1][0] <= price:
                top, span = self.stack.pop()
                count += span
            self.stack.append((price, count))

        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)