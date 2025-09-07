from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

def train_model(df, target='PM2.5'):
    """
    Train Random Forest to predict a pollutant.
    """
    le = LabelEncoder()
    df['City_code'] = le.fit_transform(df['City'])
    
    features = ['City_code','PM10','NO2','O3','CO','Temperature','Humidity']
    X = df[features]
    y = df[target]
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model, le
