import tensorflow as tf

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    image_size=(224, 224),
    label_mode='categorical',
)

# 모의고사 하나를 통으로 가져온다.
data = train_dataset.take(1) # take() 함수 -> "몇개의 덩어리를 가져올 것이냐" 라고 해석하면 쉽다.
for images, labels in data:
    print(images, labels)

print(train_dataset.class_names)
# 원핫 인코딩
