import sys


r,c = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(c)]
jihoon, fire, space = [], [], []
