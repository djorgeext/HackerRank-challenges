import sys
from solution import solve



input_data = 'predicting-house-prices/predicting-house-prices-testcases/input/input00.txt'
with open(input_data, 'r') as f:
    sys.stdin = f
    solve()