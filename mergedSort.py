class Merge:

    def mergedSort(self, num1, num2, m, n):
        num1 = [1, 2, 3, 0, 0, 0]
        num2 = [ 2, 3, 4 ]
        m = 3
        n = 3
        
        sortedNum = {}

        for i in num1: 
            if (num1[i] != 0):
                sortedNum.append(num1[i])
        sortedNum.append(num2)
        sortedNum.sort()

        print(sortedNum)

        return
            
