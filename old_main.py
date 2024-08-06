#not optimized code
#first answer

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def find_num(c, busy):
            while c>0:
                for i in mask1:
                    if i in busy:
                        continue
                    if c==1:
                        return i
                    c -= 1
            raise AttributeError('перебрал весь mask1, нихуя не нашел')

        mask1 = [i for i in range(1, n+1)]
        mask2 = [0, 1]
        busy = []
        s = ''

        for i in range(1, n-1):
            mask2.append(mask2[i]*mask1[i])
        mask2 = mask2[::-1]
        #print(mask1, mask2)

        for i in range(n-1):
            #print((k-1), mask2[i], end=" ")
            #print('-mask1(x)-=',mask1[(k-1)//mask2[i]], end=' ')
            #print('//=', (k-1)//mask2[i], end=' ')
            #busy.append(find_num(mask1[(k-1)//mask2[i]], busy))
            busy.append(find_num((k - 1) // mask2[i] + 1, busy))
            #print(busy)
        busy.append(find_num(1 , busy))

        for i in busy:
            s +=str(i)
        return s
