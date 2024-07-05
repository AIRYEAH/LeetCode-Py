# hash_table = {}
# hash_table[1] = 1
# hash_table[2] = 3
# print(hash_table)
# print(hash_table[2])      #打印key对应的值
# print(hash_table.get(2))      #打印key对应的值
# if (2 in hash_table):
#     print(True)

# a = [1, 2, 3]


# def func(val: list):
#     yield val


# def Ifunc(val: list):
#     yield from val


# for i in func(a):  # �ɵ�������
#     print(i)

# for i in Ifunc(a):  # ���ɵ�������
#     print(i)

# a = list(1, 2, 3)
# print(a)

# table = {
#     "I": 1,
#     "IV": 4,
#     "V": 5,
#     "IX": 9,
#     "X": 10,
#     "XL": 40,
#     "L": 50,
#     "XC": 90,
#     "C": 100,
#     "CD": 400,
#     "D": 500,
#     "CM": 900,
#     "M": 1000,
# }

# key = "I"
# val = table[key]
# print(key)
# print(val)

# for i, j in zip(range(0, 10), range(5, 9)):
#     print(i, j)

# 多元素list定义
# a = ["" for i in range(3)]

# # 对元素内的每个字符遍历做字符串拼接
# for i in range(0, len(a)):
#     a[i] += 'a'

# # 使用一个字符拼接一个list内的所有字符元素
# b = "".join(a)
# print(b)

# a = [1 for i in range(3)]
# print(a)

# a = "acb"
# b = sorted(a)
# print(b)

# table = {}
# table["ab"] = [1]
# table["bc"] = [2]
# b = table.values()
# print(b)

# a = set([1, 2, 3, 4])  # 集合
# print(True if 3 in a else False)
# a.add(5)
# a.remove(1)
# print(a)

# a = set("abcd")
# b = set("adbc")
# print(a)
# a.add('a')
# print(a)
# print(b)

# 螺旋数字矩阵

# import math

# a = [9, 4]
# dic = {}
# r = math.ceil(a[0]/a[1])  # 总列数
# c = a[1]  # 总行数

# # 定义坐标
# x = 0
# y = 0
# movedir = 0  # 移动方向,0-左，1-下，2-右，3-上
# for i in range(0, a[0]+1):
#     dic[i] = [x, y]
#     if (movedir == 0):
#         # 列数填满，移动向下
#         if (x == r):
#             movedir = 1
#         else:
#             x += 1

#     if (movedir == 1):
#         # 行数填满，移动向右
#         if (y == c):
#             movedir = 2
#         else:
#             y += 1

#     if (movedir == 2):
#         # 列数填满，移动向左
#         if (x == 0):
#             movedir = 0
#         else:
#             x -= 1

#     if (movedir == 3):
#         # 行数填满，移动向上
#         if (y == c-1):
#             movedir = 3
#             c -= 1
#             r -= 1
#         else:
#             y -= 1

# print(dic)


# nums = list(map(int, input().split()))
# n = len(nums)
# stack = list()
# # 初始化答案列表为nums的一个拷贝
# # 这样对于数组中的最小值就不用额外考虑了
# ans = nums.copy()
# # 正序遍历下标
# # 范围从0开始，到2*n-1结束
# for i in range(2*n):
#     # i对n求余，得到数字在nums中的真实下标
#     idx = i % n
#     num = nums[idx]
#     while stack and nums[stack[-1]] > num:
#         # 如果此时栈不为空，则栈顶元素top_idx索引右侧的下一个更小元素是nums[idx]
#         # 因此ans[top_idx]为两者相加；否则只为nums[top_idx]
#         top_idx = stack.pop()
#         ans[top_idx] = num + nums[top_idx]
#     stack.append(idx)

# # # 用解包的方式输出答案
# # print(*ans)

line = "3 14 15 6 5"
nums = list(map(int, line.split()))
length = len(nums)
res = []
# l = 0
r = 0
for i in range(0, length):
    # l = i-1
    r = i+1
    # l_min = 0  # 左侧小于num[i]的数
    r_min = 0  # 右侧小于num[i]的数
    addprice = 0
    # while (l >= 0 and l < length):
    #     if (nums[l] < nums[i]):
    #         l_min = nums[l]
    #         break
    #     else:
    #         l -= 1

    while (r >= 0 and r < length):
        if (nums[r] < nums[i]):
            r_min = nums[r]
            break
        else:
            r += 1

    addprice = max(nums[0], r_min)

    if (addprice != nums[i]):
        res.append(str(nums[i]+addprice))
    else:
        res.append(str(nums[i]))

print(" ".join(res))
