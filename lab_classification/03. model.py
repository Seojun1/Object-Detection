import tensorflow as tf

model = tf.keras.applications.MobileNet ( # 객체 검출할땐 : MobileNet-SSD / MoblieNet = 인공신경망
    input_shape=(224, 224, 3),
    include_top=False,  # MobileNet의 마지막 단계 통과안함.
    weights='imagenet' # 가중치 / imagenet = 1400만개가 넘는 이미지에 대한 Dataset
)

# model.summary()

# 학습을 시키지 않겠다 / 튜닝값(파라미터)을 설정하지 않겠다
model.trainable = False

# 만들어진 모델 활용 (커스텀)
model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalAveragePooling2D(), # 평균을 내는 역할
    tf.keras.layers.Dense(9), # 튜닝값(파라미터)을 사용해서 9로 변환 (완전 연결 신경망)
    tf.keras.layers.Softmax(), # Softmax() --> 합을 1로 맞춰주는 역할
])

model.summary()