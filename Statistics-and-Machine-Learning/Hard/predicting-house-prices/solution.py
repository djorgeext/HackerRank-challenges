import sys
from sklearn.linear_model import LinearRegression

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Extract F (features) and N (rows/houses)
    F = int(input_data[0])
    N = int(input_data[1])

    X_train = []
    y_train = []
    
    idx = 2
    
    # Extract the training data
    for _ in range(N):
        # The first F elements are features, the last is the price
        features = [float(x) for x in input_data[idx : idx+F]]
        price = float(input_data[idx+F])
        
        X_train.append(features)
        y_train.append(price)
        
        idx += (F + 1)

    # Extract T (number of test cases)
    T = int(input_data[idx])
    idx += 1

    X_test = []
    
    # Extract the test data (features only)
    for _ in range(T):
        features = [float(x) for x in input_data[idx : idx+F]]
        X_test.append(features)
        idx += F

    # Initialize and train the Multiple Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict the prices for the test data
    predictions = model.predict(X_test)

    # Print each prediction on a new line
    for p in predictions:
        print(f"{p:.2f}")

if __name__ == '__main__':
    solve()