class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while (i<j):
            target1 = numbers[i]+numbers[j]
            if(target1 == target):
                return [i+1,j+1]
            elif (target1<target):
                i+=1
            elif (target1>target):
                j-=1