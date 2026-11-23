import tensorflow as tf
import cv2
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
 
model=tf.keras.models.load_model('pic_num_reader.keras')

loss, accuracy = model.evaluate(x_test, y_test)

print('Loss:', loss)
print('Accuracy:', accuracy)