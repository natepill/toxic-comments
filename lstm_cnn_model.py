"LSTM w/ CNN"
from keras.layers import GlobalMaxPooling1D

from sklearn.model_selection import cross_validate
from keras.wrappers.scikit_learn import KerasClassifier


# Grid Search model
from sklearn.model_selection import GridSearchCV
from keras.wrappers.scikit_learn import KerasClassifier

def bi_lstm_cnn():

  max_length = 150
  vocab_size = embedding_matrix.shape[0]
  embedding_size = embedding_matrix.shape[1]

  model = Sequential()
  model.add(Embedding(input_dim=vocab_size, output_dim=embedding_size,input_length=max_length, weights=[embedding_matrix], trainable=False))
  model.add(Bidirectional(LSTM(128, return_sequences=True)))
  model.add(Conv1D(128, kernel_size=3, padding='valid', kernel_initializer='glorot_uniform'))
  model.add(GlobalMaxPooling1D())

  model.add(Dense(1, activation='sigmoid'))
  model.compile(loss='binary_crossentropy', optimizer='adam', metrics=["accuracy"])
  return model




lstm_cnn_model = KerasClassifier(build_fn=bi_lstm_cnn, epochs=10, batch_size=32, verbose=1)


scores = cross_validate(lstm_cnn_model, X, y, cv=10, scoring=['precision', 'f1', 'recall'], return_estimator=True)





# epochs = [15]
# batch_size = [16]

# param_grid = dict(epochs=epochs, batch_size=batch_size)

# bi_lstm_cnn_model = KerasClassifier(build_fn=bi_lstm_cnn, verbose=1)
# grid = GridSearchCV(estimator=bi_lstm_cnn_model, param_grid=param_grid, scoring = ['precision', 'f1', 'recall'], refit='f1', cv=5, verbose=1)
# grid_result = grid.fit(X, y)
