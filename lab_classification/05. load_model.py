import tensorflow as tf

# 모델 불러오기
model = tf.keras.models.load_model('../models/mymodel.h5')
model.summary()