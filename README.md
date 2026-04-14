Joseph Chammas
jchammas@oakland.edu

AI USAGE: I used ChatGPT to help debug my code and understand the algorithm

Coin Change Problem

Problem: Given coin denominations and a target amount, find the minimum number of coins needed (and which coins to use).

Time Complexity: O(amount * number of coins)
Space Complexity: O(amount) since we store arrays of size amount + 1
Dynamic programming works here because the problem has
-overlapping subproblems (we can reuse the same amounts)
-optimal substructure (the most optimal solution is built from smaller best solutions)

Solution:
We create a table dp where each index dp[amount] is the minimum number of coins needed to make each amount
Starting from dp[0] (which takes 0 coins) we build up to dp[amount+1]
For each i we try every coin, making sure it is valid (i - coin >= 0, making sure we don't go negative)
Then check if adding another coin is more optimal than the current solution for i
If it is, we update the dp and used tables to keep track of the new minimum coins and what coin was used in a separated "used" list
Then we rebuild the set of used coins and return

TEST CASES:

Coins: [1, 3, 5] Amount: 7
Minimum coins: 3
Coins used: [1, 1, 5]

Coins: [4, 2, 7] Amount: 33
Minimum coins: 6
Coins used: [4, 4, 4, 7, 7, 7]

Coins: [5, 7] Amount: 13
Minimum coins: -1
Coins used: []

Coins: [4, 9, 15] Amount: 0
Minimum coins: 0
Coins used: []

YOUTUBE LINK: https://youtu.be/mrZ_LYxMImU
