a = int(input())  # получаем число от пользователя

# a ^ 4
ans_4 = a * a
ans_4 = ans_4 * ans_4
print(f"{ans_4}, 2")

# a ^ 6
ans_6 = a * a
prompt = ans_6 * ans_6
ans_6 = ans_6 * prompt
print(f"{ans_6}, 3")

# a ^ 7
ans_7 = a * a
prompt_2 = ans_7 * ans_7
prompt_2 = prompt_2 * ans_7
ans_7 = prompt_2 * a
print(f"{ans_7}, 4")

# a ^ 8
ans_8 = a * a
prompt_3 = ans_8 * ans_8
ans_8 = prompt_3 * prompt_3
print(f"{ans_8}, 3")

# a ^ 9
ans_9 = a * a
prompt_4 = ans_9 * ans_9
prompt_4 = prompt_4 * prompt_4
ans_9 = prompt_4 * a
print(f"{ans_9}, 4")

# a ^ 10
ans_10 = a * a
prompt_5 = ans_10 * ans_10
prompt_5 = prompt_5 * prompt_5
ans_10 = prompt_5 * ans_10
print(f"{ans_10}, 4")

# a ^ 13
ans_13 = a * a
prompt_6 = ans_13 * ans_13
prompt_6 = prompt_6 * ans_13
prompt_6 = prompt_6 * prompt_6
ans_13 = prompt_6 * a
print(f"{ans_13}, 5")

# a ^ 21
ans_21 = a * a
prompt_7 = ans_21 * ans_21
prompt_7 = prompt_7 * prompt_7
prompt_7 = prompt_7 * ans_21
prompt_7 = prompt_7 * prompt_7
ans_21 = prompt_7 * a
print(f"{ans_21}, 6")

# a ^ 28
ans_28 = a * a
prompt_8 = ans_28 * ans_28
prompt_8 = prompt_8 * ans_28
prompt_8 = prompt_8 * prompt_8
prompt_8 = prompt_8 * ans_28
ans_28 = prompt_8 * prompt_8
print(f"{ans_28}, 6")

# a ^ 64
ans_64 = a * a
prompt_9 = ans_64 * ans_64
prompt_9 = prompt_9 * prompt_9
prompt_9 = prompt_9 * prompt_9
prompt_9 = prompt_9 * prompt_9
ans_64 = prompt_9 * prompt_9
print(f"{ans_64}, 6")
