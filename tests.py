nums = [-1,-2,-3,-4,-5]
target = -8
outlist = []
for x in nums:
    y = nums.index(x)
    for xx in nums:
        if y < len(nums) - 1:
            y += 1
        if x + nums[y] == target:
            if nums.index(x) not in outlist:
                outlist.append(nums.index(x))
            if y not in outlist:
                outlist.append(y)


print(outlist)

# name = input('Представься:\n')
#
#
# def lovely(func):
#     def wrap(name):
#         print('Всем привет!')
#         func(name)
#         print('Я очень дружелюбная и веселая')
#     return wrap
#
# def angry(func):
#     def wrap(name):
#         print('Пошли все нахуй!')
#         func(name)
#         print('Рот ваш ебала')
#     return wrap
#
#
#
#
#
#
#
#
#
#
# @angry
# def print_name(name):
#     print(f'Меня зовут {name}')
#
# print_name(name)
