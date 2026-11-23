import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
model=tf.keras.models.load_model('pic_num_reader.keras')
i=1
while os.path.exists(f'digit{i}.png'):
    img = cv2.imread(f'digit{i}.png')[:,:,0]
    img = np.invert(np.array([img]))
    p=model.predict(img)
    print("The number is probably a ", np.argmax(p))
    plt.imshow(img[0], cmap=plt.cm.binary)
    plt.show()
    i+=1