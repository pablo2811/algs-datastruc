# Common interface for Segment binary tree.
# Can be used to find min, max, sum on any given [a..b] in logarithmic time.
# Bulit on python list,when boolean arguments sum, min, max set to True,
# trees of according type are bulit.

import math,copy

class STree:

    def __init__(self,arr,sum=True,min=True,max=True):

        i = len(arr)
        self.upper = i - 1
        while not math.log(i,2).is_integer():
            i += 1
        self.height = int(math.log(i,2)) + 1
        if not sum and not min and not max:
            raise Exception("At least one from sum/min/max.")
        if sum:
            arr2 = copy.deepcopy(arr)
            arr2 += [0]*(i-len(arr))
            self.tree_sum = self.set_tree(arr2,1)
        if min:
            arr2 = copy.deepcopy(arr)
            arr2 += [float("Inf")]*(i-len(arr))
            self.tree_min = self.set_tree(arr2,2)
        if max:
            arr2 = copy.deepcopy(arr)
            arr2 += [float("-Inf")]*(i-len(arr))
            self.tree_max = self.set_tree(arr2,3)
        self.s = sum
        self.mi = min
        self.ma = max


    def set_tree(self,arr,a):

        T = [[0 for i in range(2**(j))] for j in range(self.height)]
        T[-1] = arr
        for i in range(self.height-1,0,-1):
            j = 0
            while j < len(T[i]):
                if a == 1:
                    T[i-1][j//2] = T[i][j] + T[i][j+1]
                elif a == 2:
                    T[i - 1][j // 2] = min(T[i][j],T[i][j + 1])
                elif a == 3:
                    T[i - 1][j // 2] = max(T[i][j],T[i][j + 1])
                j += 2
        return T

    def processing(self,a,b,q):
        assert (a >= 0, b <= self.upper)
        if q == 1:
            sx = 0
        else:
            sx = []
        l = self.height - 1
        while a <= b:
            if a % 2 == 1:
                if q == 1:
                    sx += self.tree_sum[l][a]
                elif q == 2:
                    sx.append(self.tree_min[l][a])
                else:
                    sx.append(self.tree_max[l][a])
                a += 1
            if b % 2 == 0:
                if q == 1:
                    sx += self.tree_sum[l][b]
                elif q == 2:
                    sx.append(self.tree_min[l][b])
                else:
                    sx.append(self.tree_max[l][b])
                b -= 1
            if a <= b :
                l -= 1
                a //= 2
                b //= 2
        if q == 1 :
            return sx
        elif q == 2 :
            return min(sx)
        else:
            return max(sx)

    def sum(self,a,b):
        return self.processing(a,b,q=1)

    def min(self,a,b):
        return self.processing(a,b,q=2)

    def max(self,a,b):
        return self.processing(a,b,q=3)

    def update(self,i,val):
        assert(self.upper >= i >= 0)
        if self.s:
            prev = self.tree_sum[-1][i]
            self.tree_sum[-1][i] = val
        if self.mi:
            prev = self.tree_min[-1][i]
            self.tree_min[-1][i] = val
        if self.ma:
            prev = self.tree_max[-1][i]
            self.tree_max[-1][i] = val

        for l in range(self.height-2,-1,-1):

            i //= 2
            if self.s:
                self.tree_sum[l][i] += val - prev
            if self.mi:
                self.tree_min[l][i] = min(self.tree_min[l+1][2*i],self.tree_min[l+1][2*i+1])
            if self.ma:
                self.tree_max[l][i] = max(self.tree_max[l + 1][2 * i], self.tree_max[l + 1][2 * i + 1])


def main():

    q = [5,8,6,3,2,7,2,6,10,12]
    s = STree(q,sum=True,min=True,max=True)
    s.update(3,10)
    print(s.sum(4,6))
    print(s.min(1,3))
    print(s.max(0,7))

if __name__ == "__main__":
    main()


