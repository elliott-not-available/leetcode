from sentence_similarity_3_1813 import Solution

# True
inp1 = ["My name is Haley", "My Haley"]
out1 = Solution().areSentencesSimilar(inp1[0], inp1[1])
print(f"output: {out1}")

# True
inp2 = ["Eating right now", "Eating"]
out2 = Solution().areSentencesSimilar(inp2[0], inp2[1])
print(f"output: {out2}")

# False
inp3 = ["of", "A lot of words"]
out3 = Solution().areSentencesSimilar(inp3[0], inp3[1])
print(f"output: {out3}")

# False
inp4 = ["qbaVXO Msgr aEWD v ekcb", "Msgr aEWD ekcb"]
out4 = Solution().areSentencesSimilar(inp4[0], inp4[1])
print(f"output: {out4}")

# # False
inp5 = ["B", "ByI BMyQIqce b bARkkMaABi vlR RLHhqjNzCN oXvyK zRXR q ff B yHS OD KkvJA P JdWksnH"]
out5 = Solution().areSentencesSimilar(inp5[0], inp5[1])
print(f"output: {out5}")

# False
inp6 = ["pp ZM ZJ lE B", "ZM"]
out6 = Solution().areSentencesSimilar(inp6[0], inp6[1])
print(f"output: {out6}")

# False
inp7 = ["A A", "A aA"]
out7 = Solution().areSentencesSimilar(inp7[0], inp7[1])
print(f"output: {out7}")