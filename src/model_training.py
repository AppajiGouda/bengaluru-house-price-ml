from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import StackingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

def train_models(X_train, y_train):
    
    rf = RandomForestRegressor(n_estimators=100)
    knn = KNeighborsRegressor(n_neighbors=5)
    dt = DecisionTreeRegressor(max_depth=10)

    stack = StackingRegressor(
        estimators=[
            ('rf', rf),
            ('knn', knn),
            ('dt', dt)
        ],
        final_estimator=LinearRegression()
    )

    models = {
        "rf": rf,
        "knn": knn,
        "dt": dt,
        "stack": stack
    }

    for name, model in models.items():
        model.fit(X_train, y_train)

    return models


from sklearn.neural_network import MLPRegressor

def add_nn_model(X_train, y_train):
    nn = MLPRegressor(
        hidden_layer_sizes=(64, 32),
        activation='relu',
        max_iter=500
    )
    nn.fit(X_train, y_train)
    return nn