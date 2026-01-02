import pandas as pd
from lstm_attention_model import build_model
data = pd.read_csv('../data/sample_kpi_data.csv')
X = data.drop('fault', axis=1).values.reshape(-1,1,6)
y = data['fault'].values
model = build_model((1,6))
model.fit(X,y,epochs=10)
model.save('model.h5')
