import sys
from sklearn.linear_model import LinearRegression

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    F = int(input_data[0])
    N = int(input_data[1])
    
    X_train = []
    y_train = []
    
    for _ in range(N):