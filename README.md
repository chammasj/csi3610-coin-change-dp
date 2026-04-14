Joseph Chammas
jchammas@oakland.edu

AI USAGE: I used ChatGPT to help debug my code and understand the algorithm

Coin Change Problem

Problem: Given coin denominations and a target amount, find the minimum number of coins needed (and which coins to use).

Time Complexity: O(amount * number of coins)
Space Complexity: O(amount)
Dynamic programming works here because the problem has
-overlapping subproblems (we can reuse the same amounts)
-optimal substructure (the most optimal solution is built from smaller best solutions)

Solution:
We create a table dp where each index dp[amount] is the minimum number of coins needed to make amount
Starting from 0 we build up to amount
For each amount we try all coins and take the most optimal set (the one with the minimum number of coins required)
Also we keep track of what coins are used in a separate list

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