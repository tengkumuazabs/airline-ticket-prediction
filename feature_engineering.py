from sklearn.base import BaseEstimator, TransformerMixin
from datetime import timedelta
import pandas as pd

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        # Convert times to datetime (without date)
        X['dep_time_dt'] = pd.to_datetime(X['dep_time'], format='%H:%M')
        X['arr_time_dt'] = pd.to_datetime(X['arrival_time'], format='%H:%M')

        # Compute duration
        def compute_duration(row):
            dep_time = row['dep_time_dt']
            arr_time = row['arr_time_dt']
            if arr_time < dep_time:
                arr_time += timedelta(days=1)

            total_seconds = (arr_time - dep_time).total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            return pd.Series([hours, minutes])

        X[['duration_hour', 'duration_minute']] = X.apply(compute_duration, axis=1)

        # Categorize departure time
        def categorize_dep_time(dep_time):
            hour = dep_time.hour
            if 0 <= hour < 6:
                return 'Early Morning'
            elif 6 <= hour < 12:
                return 'Morning'
            elif 12 <= hour < 17:
                return 'Afternoon'
            elif 17 <= hour < 21:
                return 'Evening'
            else:
                return 'Night'

        X['dep_time_category'] = X['dep_time_dt'].apply(categorize_dep_time)

        # Drop original and helper columns
        X.drop(['dep_time', 'arrival_time', 'dep_time_dt', 'arr_time_dt'], axis=1, inplace=True)

        return X
