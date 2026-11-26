class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        counter = 0
        cl = word[0]
        for i in range(len(word)):
            if counter == 9:
                comp.append(f"{str(counter) + cl}")
                counter = 0
            elif word[i] != cl:
                comp.append(f"{str(counter) + cl}")
                counter = 0
            counter += 1
            cl = word[i]
        comp.append(f"{str(counter) + cl}")
        return "".join(comp)
        