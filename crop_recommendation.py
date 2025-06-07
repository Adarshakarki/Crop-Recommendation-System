import pickle
import numpy as np

model = pickle.load(open('models/RandomForest.pkl', 'rb'))

def recommend_crop(N, P, K, temp, humidity, ph, rainfall):
    data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(data)
    return prediction[0]
