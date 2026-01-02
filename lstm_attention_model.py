import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense, Input
from tensorflow.keras.models import Model

def build_model(input_shape):
 inputs = Input(shape=input_shape)
 lstm = LSTM(64, return_sequences=True)(inputs)
 att = Dense(1, activation='tanh')(lstm)
 att = tf.nn.softmax(att, axis=1)
 ctx = tf.reduce_sum(att * lstm, axis=1)
 out = Dense(1, activation='sigmoid')(ctx)
 model = Model(inputs, out)
 model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
 return model
