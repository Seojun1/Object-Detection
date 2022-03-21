import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    image_size=(224, 224),
    label_mode='categorical',
)

data = train_dataset.take(1)

# 0번 차트 그리기
plt.figure(0)
plt.title('data')

for images, lables in data:
    for i in range(9):
        # figure랑 비슷한 기능 -> 차트안에 또 다른 차트 그리기
        plt.subplot(3, 3, i + 1)

        # 이미지 불러오기(형변환)/matplotlib은 정수만 지원하기 때문에 정수로 형변환 해야함
        plt.imshow(images[i].numpy().astype('uint8'))

        # np.argmax() --> 배열에 들어있는 값들중에 가장 큰 값을 알아내주는 코드 (01.load_data.py 결괏값 참고)
        plt.title(train_dataset.class_names[np.argmax(lables[i])])

        # 결과 창에 x축, y축 표시X (직접 실행해보면 이해 가능.)
        plt.axis('off')

plt.show()