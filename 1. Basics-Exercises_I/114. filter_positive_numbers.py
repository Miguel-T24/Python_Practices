# 114. Write a python program to filter positive numebrs from a list

nums = [34,1,0,-23,12,-88]
print("original numbers in the list:" , nums)

new_list = list(filter(lambda x:x>0 , nums))

print(new_list)