import shlex
command = "CREATE_LISTING user1 'Black shoes' 'Training shoes' 100 'Sports'"
qq = "CREATE_LISTING user1 'Black shoes' 'Training shoes' 100 'Sports'"
parts = shlex.split(qq)
action = parts[0]

# 取得原始輸入，確保帶有引號
raw_input = command[len(action) + len(parts[1]) + 2:]  # 跳過 "CREATE_LISTING user1 "
raw_parts = shlex.split(raw_input, posix=True)

print(raw_parts)