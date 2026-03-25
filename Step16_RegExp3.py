# Step16_RegExp3.py


import re


logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]


# logs 에서 ERROR or WARN 로그만 찾아서 출력


# 1. Define the pattern: matches [ERROR] or [WARN]
# Note: \[ and \] are used because brackets are special characters in Regex
pattern = r"\[(ERROR|WARN)\]"


# 2. Use a list comprehension to filter and print
for log in logs:
    if re.search(pattern, log):
        print(log)
