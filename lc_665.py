nums = [3,4,2,3]
nums1 = nums[:]
nums2 = nums[:]
for i in range(1,len(nums)):
	if nums[i] - nums[i-1] < 0:
		nums1[i] = nums1[i-1]
		nums2[i-1] = nums2[i]
		break

if nums1 == sorted(nums1) or nums2 == sorted(nums2):
	print(True)
else:
	print(False)
