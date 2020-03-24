import tensorflow as tf
from keras.preprocessing import text, sequence
from keras.models import load_model
import pickle


# Start TF graph session
graph = tf.get_default_graph()

# load classifier
model = load_model('lstm_cnn_split_5.h5')


def get_score(text):

    # Constants
    max_features=100000
    max_len=150
    embed_size=300

    # Unpickling the trained tokenizer to one hot encode our text
    pickled_file = open('text_tokenizer.pickle', 'rb')
    keras_tokenizer = pickle.load(pickled_file)
    pickled_file.close()

    # One hot encode
    tokenized_text = keras_tokenizer.texts_to_sequences(text)

    # Pad sequences to accomadate 150 unique vocab
    padded_text = sequence.pad_sequences(tokenized_text, maxlen = max_len)

    # use model to predict toxic score
    # with graph.as_default():
    # print(len(padded_text))
    toxicity_score = model.predict(padded_text)
    # print(sum(toxicity_score)/len(toxicity_score))
    toxicity_score = sum(toxicity_score)/len(toxicity_score)

    return toxicity_score
