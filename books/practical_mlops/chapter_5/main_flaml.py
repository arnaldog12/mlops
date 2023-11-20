from flaml import AutoML
from sklearn.datasets import load_iris

automl = AutoML()
automl_settings = dict(
    time_budget=10, # in seconds
    metric='accuracy',
    task='classification',
)

x_train, y_train = load_iris(return_X_y=True)
automl.fit(X_train=x_train, y_train=y_train, **automl_settings)

print(automl.predict_proba(x_train))
print(automl.model)
