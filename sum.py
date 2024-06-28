class Solution(object):

    def twoSum(self, numbers, target):
        numbers = [1,3,4,5,7,10,11]
        target = 9

        l, r =  0, len(numbers) - 1

        while l < r :
            sums =  numbers[l] + numbers[r] 

            if sums > target:
                l += 1
            elif sums < target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return



        