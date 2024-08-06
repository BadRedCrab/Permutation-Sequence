#optimized code

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        mask1 = [i for i in range(1, n+1)]
        busy = []

        mask2 = [1] * n
        for i in range(1, n):
            mask2[i] = mask2[i - 1] * i

        mask2 = mask2[::-1]

        for i in range(n-1):
            n = mask1[(((k - 1) // mask2[i] + 1)-1)%len(mask1)]
            busy.append(n)
            mask1.remove(n)
        busy.append(mask1[0])

        return ''.join(map(str, busy))


print(Solution().getPermutation(5,9))