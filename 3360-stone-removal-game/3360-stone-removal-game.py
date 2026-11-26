class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = True
        x = 10
        while n >= 0:
            n -= x
            alice = not alice
            x -= 1
        return alice