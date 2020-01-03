import sys

currencies = [1,3,10,25]

def greedy_min_coin(n, curreny):
    coin = 0
    for curreny in range(currencies.index(curreny),-1,-1):
        curreny = currencies[curreny]
        coin = coin + int(n/curreny)
        n = n%curreny
        if n == 0:
            break
    return coin

def min_coins(n):
    min = n
    for coin in currencies:
        greedy_min = greedy_min_coin(n, coin)
        if greedy_min < min:
            min = greedy_min
    return min

# m is size of coins array (number of  
# different coins) 
def minCoins(coins, m, V): 
      
    # table[i] will be storing the minimum  
    # number of coins required for i value.  
    # So table[V] will have result 
    table = [0 for i in range(V + 1)] 
  
    # Base case (If given value V is 0) 
    table[0] = 0
  
    # Initialize all table values as Infinite 
    for i in range(1, V + 1): 
        table[i] = sys.maxsize 
  
    # Compute minimum coins required  
    # for all values from 1 to V 
    for i in range(1, V + 1): 
          
        # Go through all coins smaller than i 
        for j in range(m): 
            if (coins[j] <= i): 
                sub_res = table[i - coins[j]] 
                if (sub_res != sys.maxsize and 
                    sub_res + 1 < table[i]): 
                    table[i] = sub_res + 1
    return table[V]

for i in range(1,90):
    print(i,min_coins(i), minCoins(currencies,len(currencies),i))