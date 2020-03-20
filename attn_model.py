import numpy as np
import pandas as pd
from keras.layers import Dense, Input, LSTM, Bidirectional, Conv1D
from keras.layers import Dropout, Embedding
from keras.preprocessing import text, sequence
from keras.models import Model
from keras.models import Sequential
import numpy as np
import pandas as pd
from keras.layers import Dense, Input, LSTM, Bidirectional, Conv1D, MaxPooling1D, GlobalMaxPooling1D
from keras.layers import Dropout, Embedding, concatenate
from keras.preprocessing import text, sequence

from keras.models import Model



from keras.layers import Input, Flatten, Activation, multiply, TimeDistributed, RepeatVector, Permute, Lambda
from keras import backend as K

from sklearn.model_selection import cross_validate
from keras.wrappers.scikit_learn import KerasClassifier

"""
  Bi-LSTM w/ Attn and K-fold cross validation
"""

def create_attn_lstm():


  units = 32
  max_length = 150
  vocab_size = embedding_matrix.shape[0]
  embedding_size = embedding_matrix.shape[1]


  _input = Input(shape=[max_length], dtype='int32')

  # get the embedding layer
  embedded = Embedding(
          input_dim=vocab_size,
          output_dim=embedding_size,
          input_length=max_length,
          trainable=False,
          weights=[embedding_matrix]
      )(_input)

  # Bidirectional(LSTM(128, return_sequences=True))
  # activations = LSTM(units, return_sequences=True)(embedded)
  # Bidirectional(LSTM(64, return_sequences=True))
  activations = Bidirectional(LSTM(32, return_sequences=True))(embedded)


  # compute importance for each step
  attention = TimeDistributed(Dense(1, activation='tanh'))(activations)
  attention = Flatten()(attention)
  attention = Activation('softmax')(attention)
  # adjusting vector shapes for multiplication
  attention = RepeatVector(64)(attention)
  attention = Permute([2, 1])(attention)

  # apply the attention
  sent_representation = multiply([activations, attention])

  sent_representation = Lambda(lambda xin: K.sum(xin, axis=1))(sent_representation)

  probabilities = Dense(1, activation='sigmoid')(sent_representation)

  model = Model(input=_input, output=probabilities)
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

  return model


attn_lstm_model = KerasClassifier(build_fn=create_attn_lstm, epochs=10, batch_size=32, verbose=1)

scores = cross_validate(attn_lstm_model, X, y, cv=10, scoring=['precision', 'f1', 'recall'],return_estimator=True)


print(scores)
