class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2)==0 :
            new=nums1
        elif len(nums1)==0:
            new=nums2
        else:
            flag1,flag2=0,0
            new=[]
            while flag1 != len(nums1) and flag2 != len(nums2):
                if nums1[flag1]<nums2[flag2]:
                    new.append(nums1[flag1])
                    flag1+=1
                else:
                    new.append(nums2[flag2])
                    flag2+=1
            if flag1==len(nums1):
                for i in nums2[flag2:]:
                    new.append(i)
            else:
                for i in nums1[flag1:]:
                    new.append(i)
        print(new)
        if len(new)%2==0:
            return ((new[(int)(len(new)/2-1)]+new[(int)(len(new)/2)])/2)
        else:
            return new[len(new)//2]

if __name__=="__main__":
    num1=[]
    num2=[2]
    s=Solution()
    print(s.findMedianSortedArrays(num1,num2))

