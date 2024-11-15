import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

class MarathonModel:
    def trainModel(self, dataPath, modelPath):
        data = pd.read_csv(dataPath)
        X = data[['km4week', 'sp4week', 'Category']]
        y = data['MarathonTime']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(), ['Category'])
            ],
            remainder='passthrough'
        )
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', RandomForestRegressor(random_state=42))
        ])
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"Model performance:\n - MAE: {mae:.4f}\n - R^2: {r2:.4f}")
        joblib.dump(model, modelPath)
        print(f"Model saved at {modelPath}")

    def predict(self, modelPath, inputData):
        model = joblib.load(modelPath)
        return model.predict(inputData)
