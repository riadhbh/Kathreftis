
from keras.callbacks import CSVLogger, ModelCheckpoint, EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator
from load_and_process import load_data
from load_and_process import treatData
from models.cnn import mini_XCEPTION
from sklearn.model_selection import train_test_split


batch_size = 32
num_epochs = 10000
input_shape = (48, 48, 1)
validation_split = .2
verbose = 1
num_labels = 7
patience = 40
base_path = 'models/'

datagen = ImageDataGenerator(
						 featurewise_center=True,
						 featurewise_std_normalization=True,
						 rotation_range=20,
						 width_shift_range=0.2,
						 height_shift_range=0.2,
						 horizontal_flip=True)


model = mini_XCEPTION(input_shape, num_labels)
model.compile(optimizer='adam', loss='categorical_crossentropy',
			  metrics=['accuracy'])
model.summary()





log_file_path = base_path + '_emotion_training.log'
csv_logger = CSVLogger(log_file_path, append=False)
early_stop = EarlyStopping('val_loss', patience=patience)
reduce_lr = ReduceLROnPlateau('val_loss', factor=0.1,patience=int(patience/4), verbose=1)
trained_models_path = base_path + '_mini_XCEPTION'
model_names = trained_models_path + '.{epoch:02d}-{val_acc:.2f}.hdf5'
model_checkpoint = ModelCheckpoint(model_names, 'val_loss', verbose=1,
													save_best_only=True)
callbacks = [model_checkpoint, early_stop, reduce_lr]


faces, emotions = load_data()
faces = treatData(faces)
num_samples, num_labels = emotions.shape
xtrain, xtest,ytrain,ytest = train_test_split(faces, emotions,test_size=0.2,shuffle=True)
model.fit_generator(datagen.flow(xtrain, ytrain,
											batch_size),
						steps_per_epoch=len(xtrain) / batch_size,
						epochs=num_epochs, verbose=1, callbacks=callbacks,
						validation_data=(xtest,ytest))
