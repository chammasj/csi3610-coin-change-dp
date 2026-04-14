import sys

def coin_change(coins, amount):
    # Store minimum number of coins needed for each amount
    dp = [float("inf")] * (amount + 1)

    # 0 coins needed to reach amount 0
    dp[0] = 0

    # Track which coins are used
    used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        # Iterate over the list of coins and check if it can be used
        for coin in coins:
            # If the coin value is at most equal to i we can use it
            # Since we already know how to use i - coin (stored in dp[i - coin])
            # We can add 1 coin and check if the solution is more optimal
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                # Track the new minimum number of coins
                dp[i] = dp[i - coin] + 1

                # Add the coin to our used list to rebuild answer later
                used[i] = coin

    # No valid combination was found
    if dp[amount] == float("inf"):
        return -1, []

    # Reconstruct coins used
    result = []
    while amount > 0:
        coin = used[amount]
        result.append(coin)
        amount -= coin

    return dp[-1], result
    
def main():
    coins = [2, 4, 7]
    amount = 22

    min_coins, used_coins = coin_change(coins, amount)

    print("Coins:", coins, "Amount:", amount)
    print("Minimum coins:", min_coins)
    print("Coins used:", used_coins)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        print("Usage: coin_change.py")