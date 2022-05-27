# Classification using Tensor flow on MNIST cloth dataset
#import libraries
import tensorflow as tf
# access the dataset
fashion_mnist=tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data( )
# print the training and test dataset
train_images.shape

train_images [0]

train_labels

test_images.shape

test_labels.shape

# visualization of training data
import matplotlib.pyplot as plt
# plot the first train_image
plt.imshow(train_images[0])
plt.show()

# plot multiple images and its label
class_names = ['T-shirt/ top' , 'Trouser' , ' Pullover' , 'Dress ' , 'Coat ' , 'Sandal' , ' Shirt ' , 'Sneaker','Bag','Ankle boot']
plt.figure(figsize=(15,15))
for i in range(25):
plt.subplot(5,5,i+1)
plt.imshow(train_images[i])
plt.xlabel(class_names[train_labels[i]])
plt.xticks([])
plt.yticks([])
pass

plt.show()

# scale images to a range of 0 to 1
train_images=train_images/255.0
test_images=test_images/255.0
# see the train_image[0] after scaling
train_images[0]

# create model
model=tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add (tf.keras.layers.Dense(128,activation='relu'))
model.add(tf.keras.layers.Dense(10))
model.compile(optimizer= 'adam' ,
loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
metrics=['accuracy'])
# model summary
model.summary()

# Train the Model
history=model.fit(train_images,train_labels,epochs=10)

loss=history.history['loss']
acc=history.history['accuracy']
epochs_range=range(10)
plt.plot(epochs_range,loss,label= 'Training Loss')
plt.plot(epochs_range,acc,label= 'Training Accuracy')
plt.legend(loc='lower right')
plt.title('Training Loss and Accuracy')

# Evaluate the accuracy
test_loss, test_acc=model.evaluate(test_images, test_labels, verbose=2)
print( ' \Test accuracy: ' , test_acc)

# Predict
probability_model=tf.keras.Sequential([model,tf.keras.layers.Softmax()])
predictions=probability_model.predict(test_images)
predictions[0]

# view prediction
import numpy as np
np.argmax(predictions[0])

#verify predictions
def plot_image(i, predictions_array, true_label, img) :
true_label, img=true_label [i] , img[i]
plt.grid(False)
plt.xticks([])
plt.yticks([])
plt.imshow(img)
predicted_label = np.argmax(predictions_array)
if predicted_label == true_label:
color = 'blue'
else:
color = 'red'

plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
100*np.max(predictions_array),
class_names[true_label]),
color=color)
pass
def plot_value_array(i, predictions_array, true_label):
true_label = true_label[i]
plt.grid(False)
plt.xticks(range(10))
plt.yticks([])
thisplot = plt.bar(range(10), predictions_array, color="#777777")
plt.ylim([0,1])
predicted_label = np.argmax(predictions_array)
thisplot[predicted_label].set_color('red')
thisplot[true_label].set_color('blue')
pass
# Verify the 0th image prediction
i=0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i,predictions[i],test_labels,test_images)
plt.subplot(1,2,2)
plot_value_array(i,predictions[i],test_labels)
plt.show()

# plot images with their predictions
num_rows = 5
num_cols = 3
num_images = num_rows * num_cols
plt.figure(figsize=(10,10))
for i in range(num_images):
plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()
