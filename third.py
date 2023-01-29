n = int(input())
ans = [["1"]]
maxim = 1
for i in range(n):
    prompt = ["0"] * (len(ans[i]) + 1)
    prompt[0], prompt[-1] = "1", "1"
    for j in range(1, len(prompt) - 1, 1):
        prompt[j] = str(int(ans[i][j - 1]) + int(ans[i][j]))
        maxim = max(maxim, len(prompt[j]))
    ans.append(prompt)

# for i in range(len(ans)):
#     for el in range(len(ans[i])):
#         if len(ans[i][el]) < maxim:
#             if not maxim % 2:
#                 ans[i][el] = ans[i][el] + (" " * (maxim // 2))
#             else:
#                 ans[i][el] = (" " * (maxim // 2 - 1)) + ans[i][el] + (" " * (maxim // 2 - 1))
#         else:
#             ans[i][el] = ans[i][el] + " "

for i in range(len(ans)):
    print(" " * (len(ans[-1]) - i) + " ".join(ans[i]))
