class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        k = len(s1)

        c1 = Counter(s1)
        c2 = Counter(s2[:k])

        def compare():
            found = True
            if len(c1) == len(c2):
                for c in c1:
                    if c1[c] != c2[c]:
                        found = False
                        break
            else:
                found = False

            return found

        # First k
        if compare(): return True

        # Rest
        for i in range(k, len(s2)):
            left = s2[i - k]
            right = s2[i]
            
            if left != right:

                # Decrement / Delete left
                if c2[left] > 1:
                    c2[left] -= 1
                else:
                    del c2[left]

                # Increment / Add right
                c2[right] = 1 + c2.get(right, 0)

                # Compare both counter
                if compare(): return True

        return False




        