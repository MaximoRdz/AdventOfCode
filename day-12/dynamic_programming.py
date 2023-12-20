# some practice on dynamic programming
# and on memoization


coins = {1, 4, 5}


def nan_min(number_a, number_b):
    if number_a is None:
        return number_b
    if number_b is None:
        return number_a
    
    return min(number_a ,number_b)

memo = {}
def minimum_coins(m, coins):
    if m in memo:
        return memo[m]
    if m == 0: 
        return 0
    else:
        ans = None
        for coin in coins: 
            subproblem = m - coin
            if subproblem < 0:
                continue
            ans = nan_min(ans, minimum_coins(m-coin, coins) + 1)
    memo[m] = ans
    return ans

print("Min Coins for 150: ", minimum_coins(150, coins))


# how many ways to have a given sum
memo = {}
def ways(m, coins):
    if m in memo:
        return memo[m]
    if m == 0: 
        return 1
    else:
        ans = 0
        for coin in coins:
            subproblem = m-coin
            if subproblem < 0: 
                continue
            ans += ways(m-coin, coins)
    memo[m] = ans
    return ans

print("ways to sum 5: ", ways(87, [1, 4, 5, 8]))
