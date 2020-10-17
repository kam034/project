import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator

ds_train = tf.keras.preprocessing.image_dataset_from_directory(
    r'C:\Users\Admin\Desktop\data',
    labels='inferred',
    label_mode = "int",
    color_mode='rgb',
    batch_size=128,
    image_size=(640, 480),
    shuffle=True,
)

ds_validation = tf.keras.preprocessing.image_dataset_from_directory(
    r'C:\Users\Admin\Desktop\data',
    labels='inferred',
    label_mode = "int",
    color_mode='rgb',
    batch_size=128,
    image_size=(640, 480),
    shuffle=True,
)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(640,480, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(3))

model.compile(optimizer='adam',
              loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])

model.fit(ds_train, epochs=10)








