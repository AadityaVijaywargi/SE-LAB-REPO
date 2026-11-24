from flask import Flask, request
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app2 = Flask(__name__)

# Dataset
X = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
y = [8, 10, 12, 14, 16, 18, 20]

# Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=7
)

# Create and train the model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Calculate model accuracy
accuracy = reg.score(X_test, y_test) * 100


def page(prediction=None, last_val='', error=None):

    result = ''

    if prediction is not None:
        result = f'''
        <p>
            Prediction for {last_val}:
            <strong>{prediction:.2f}</strong>
        </p>
        '''

    if error:
        result = f'''
        <p style="color: red;">
            {error}
        </p>
        '''

    return f'''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <title>ML Prediction</title>
    </head>

    <body>

        <h1>Linear Regression Prediction</h1>

        <p>
            Model accuracy:
            <strong>{accuracy:.2f}%</strong>
        </p>

        <form method="POST" action="/predict">

            <label for="val">
                Enter a value:
            </label>

            <input
                id="val"
                name="val"
                type="number"
                step="any"
                required
                value="{last_val}"
            >

            <button type="submit">
                Predict
            </button>

        </form>

        {result}

    </body>

    </html>
    '''


# Home page
@app2.route('/')
def index():
    return page()


# Prediction endpoint
@app2.route('/predict', methods=['GET', 'POST'])
def predict():

    # If user opens /predict directly
    if request.method == 'GET':
        return page()

    try:
        user_input = float(request.form['val'])

    except (KeyError, TypeError, ValueError):
        return page(
            error='Please enter a valid number.'
        ), 400

    # Make prediction
    prediction = reg.predict([[user_input]])[0]

    # Return result
    return page(
        prediction=prediction,
        last_val=user_input
    )


if __name__ == '__main__':
    app2.run(debug=True, port=8000)