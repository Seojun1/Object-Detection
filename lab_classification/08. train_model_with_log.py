import tensorflow as tf
import os

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224, 224),
    label_mode='categorical'
)

model = tf.keras.models.load_model('../models/mymodel.h5')

if not os.path.exists('../logs'):
    os.mkdir('../logs')

# tensorboard 변수에 기능을 만들어놓은 것
tensorboard = tf.keras.callbacks.TensorBoard(log_dir='../logs')

learning_rate = 0.001 # 0.001 --> Right Learning rage (적정 치수)
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=learning_rate),
    metrics=['accuracy']
)

model.fit(train_dataset, epochs=5, callbacks=[tensorboard])

if not os.path.exists('../models'):
    os.mkdir('../models')

model.save('../models/classification_model_trained.h5')