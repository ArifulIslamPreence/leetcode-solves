def removeValue(self, nums:list[int], val:int):
    nums = [2, 3, 4, 5]
    val = 4
    if len(nums) != 0:
        for i in nums:
            if(nums[i] == val):
                nums.remove(val)
            
        print(nums.count())
        #return 
        