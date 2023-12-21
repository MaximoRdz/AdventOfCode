# # some practice on dynamic programming
# # and on memoization


# coins = {1, 4, 5}


# def nan_min(number_a, number_b):
#     if number_a is None:
#         return number_b
#     if number_b is None:
#         return number_a
    
#     return min(number_a ,number_b)

# memo = {}
# def minimum_coins(m, coins):
#     if m in memo:
#         return memo[m]
#     if m == 0: 
#         return 0
#     else:
#         ans = None
#         for coin in coins: 
#             subproblem = m - coin
#             if subproblem < 0:
#                 continue
#             ans = nan_min(ans, minimum_coins(m-coin, coins) + 1)
#     memo[m] = ans
#     return ans

# print("Min Coins for 150: ", minimum_coins(150, coins))


# # how many ways to have a given sum
# memo = {}
# def ways(m, coins):
#     if m in memo:
#         return memo[m]
#     if m == 0: 
#         return 1
#     else:
#         ans = 0
#         for coin in coins:
#             subproblem = m-coin
#             if subproblem < 0: 
#                 continue
#             ans += ways(m-coin, coins)
#     memo[m] = ans
#     return ans

# print("ways to sum 87: ", ways(87, [1, 4, 5, 8]))


# # write a recursive function that given an input n sums all nonegative integers
# # up to n

# def sum(n):
#     if n == 0:
#         return 0
    
#     result = n
#     if n > 0:
#         result +=  sum(n-1)
#     return result

# print(sum(3))

# Write a function that takes tow inputs n and m and outpts the number of unique paths
# from the top left corner to bottom right corner of a n x m grid, you can only move d 
# or r one unit at a time


def paths(n, m, i, j):
    # base cases, bottom and right bordes
    if i == n-1 or j == m-1:
        return 0
    
    result = 0
    
    
