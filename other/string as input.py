import io
import sys

user = """2
3
4
"""

sys.stdin = io.StringIO(user)

for _ in range (int(input())):
    n = int(input())
    print(n**n)