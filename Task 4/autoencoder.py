import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import warnings
keras = tf.keras
mnist = tf.keras.datasets.mnist
fashion_mnist = tf.keras.datasets.fashion_mnist
Adam = tf.keras.optimizers.Adam
Model = tf.keras.Model
Input = tf.keras.layers.Input
Dense = tf.keras.layers.Dense
Flatten = tf.keras.layers.Flatten
Reshape = tf.keras.layers.Reshape
Conv2D = tf.keras.layers.Conv2D
Conv2DTranspose = tf.keras.layers.Conv2DTranspose
warnings.filterwarnings("ignore")

# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize the image data to [0, 1] range
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Checking the shape of the dataset
print("Training data shape:", train_images.shape)
print("Number of training samples:", len(train_labels))
print("Test data shape:", test_images.shape)
print("Number of test samples:", len(test_labels))

# Reshape training and test data to fit model input
train_images = train_images.reshape(-1, 28, 28)
test_images = test_images.reshape(-1, 28, 28)

def build_encoder(input_shape, encoding_dim):
    input_img = Input(shape=input_shape)
    flattened_img = Flatten()(input_img)
    encoded_output = Dense(encoding_dim, activation='relu')(flattened_img)
    return Model(input_img, encoded_output, name="encoder")

def build_decoder(encoding_dim, original_shape):
    encoded_input = Input(shape=(encoding_dim,))
    output = Dense(int(np.prod(original_shape)), activation='sigmoid')(encoded_input)
    reshaped_output = Reshape(original_shape)(output)
    return Model(encoded_input, reshaped_output, name="decoder")

def build_autoencoder(input_shape=(28, 28), encoding_dim=64):
    encoder = build_encoder(input_shape, encoding_dim)
    decoder = build_decoder(encoding_dim, input_shape)
    
    input_img = Input(shape=input_shape)
    encoded = encoder(input_img)
    decoded = decoder(encoded)
    
    autoencoder = Model(input_img, decoded, name="autoencoder")
    autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
    return autoencoder, encoder, decoder

def train_autoencoder(autoencoder, train_data, test_data, epochs=50, batch_size=256, visualize=True):
    autoencoder.fit(train_data, train_data,
                    epochs=epochs,
                    batch_size=batch_size,
                    shuffle=True,
                    validation_data=(test_data, test_data))
    if visualize:
        decoded_imgs = autoencoder.predict(test_data[:10])
        n = 10  # number of images to display
        plt.figure(figsize=(20, 4))
        for i in range(n):
            # Display original
            ax = plt.subplot(2, n, i + 1)
            plt.imshow(test_data[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

            # Display reconstruction
            ax = plt.subplot(2, n, i + 1 + n)
            plt.imshow(decoded_imgs[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        plt.show()

autoencoder, encoder, decoder = build_autoencoder()    

train_autoencoder(autoencoder, train_images, test_images) 

def visualize_compression(encoder, decoder, test_images, n=10):
    # Predict the encoded and decoded images
    encoded_imgs = encoder.predict(test_images[:n])
    decoded_imgs = decoder.predict(encoded_imgs)

    plt.figure(figsize=(20, 6))  # Wider figure to avoid squished subplots

    # Adding titles above columns once, since they share the same encoding and decoding process
    for i in range(n):
        if i == 0:
            plt.subplot(3, n, i + 1)
            plt.title("Original")
        elif i == 0 + n:
            plt.subplot(3, n, i + 1)
            plt.title("Encoded")
        elif i == 0 + 2 * n:
            plt.subplot(3, n, i + 1)
            plt.title("Decoded")

    # Plotting each category of images
    for i in range(n):
        # Original images
        ax = plt.subplot(3, n, i + 1)
        plt.imshow(test_images[i].reshape(28, 28), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Encoded representations
        ax = plt.subplot(3, n, n + i + 1)
        encoded_reshaped = encoded_imgs[i].reshape(-1, 4)  # Reshaping to a square if possible
        plt.imshow(encoded_reshaped, cmap='gray', aspect='auto')  
        plt.xlabel('Encoded Values')
        ax.get_xaxis().set_visible(True)
        ax.get_yaxis().set_visible(False)

        # Decoded images
        ax = plt.subplot(3, n, (2 * n) + i + 1)
        plt.imshow(decoded_imgs[i].reshape(28, 28), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.tight_layout()
    plt.show()

visualize_compression(encoder, decoder, test_images)

def train_and_extract_models(input_shape, encoding_dim, train_data, test_data, epochs=10, batch_size=256):
    autoencoder, encoder, decoder = build_autoencoder(input_shape=input_shape, encoding_dim=encoding_dim)
    autoencoder.fit(train_data, train_data, epochs=epochs, batch_size=batch_size, shuffle=True, validation_data=(test_data, test_data))
    return encoder, decoder

# Train autoencoders for small and large latent dimensions
small_encoder, small_decoder = train_and_extract_models((28, 28, 1), 8, train_images, test_images)
large_encoder, large_decoder = train_and_extract_models((28, 28, 1), 64, train_images, test_images)

def compare_random_generations(small_decoder, large_decoder, num_samples=10):
    # Generate random encodings for small and large latent space
    small_random_encodings = np.random.normal(size=(num_samples, 8))
    large_random_encodings = np.random.normal(size=(num_samples, 64))

    # Decode the random encodings
    small_generated_images = small_decoder.predict(small_random_encodings)
    large_generated_images = large_decoder.predict(large_random_encodings)

    plt.figure(figsize=(20, 4))
    for i in range(num_samples):
        # Display images from small latent space decoder
        ax = plt.subplot(2, num_samples, i + 1)
        plt.imshow(small_generated_images[i].reshape(28, 28))
        plt.gray()
        ax.axis('off')
        if i == 0:
            plt.title("Small Latent Space (8)")

        # Display images from large latent space decoder
        ax = plt.subplot(2, num_samples, num_samples + i + 1)
        plt.imshow(large_generated_images[i].reshape(28, 28))
        plt.gray()
        ax.axis('off')
        if i == 0:
            plt.title("Large Latent Space (64)")
    plt.show()

# Call the function with the appropriate decoders
compare_random_generations(small_decoder, large_decoder)






#TensorFlow - (batch_size,height,width,chennels)
def load_fashion_mnist():
    (x_train, _), (x_test, _) = fashion_mnist.load_data()
    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train = np.expand_dims(x_train, axis=-1)
    x_test = np.expand_dims(x_test, axis=-1)
    return x_train, x_test

def build_conv_encoder(input_shape=(28, 28, 1), filters=[32, 16], encoding_dim=64):
    input_img = Input(shape=input_shape)
    x = input_img
    for filt in filters:
        x = Conv2D(filt, (3, 3), activation='relu', padding='same')(x)
    x = Flatten()(x)
    encoded = Dense(encoding_dim, activation='relu')(x)
    return Model(input_img, encoded, name="encoder")

def build_conv_decoder(encoding_dim, output_shape=(28, 28, 1), filters=[16, 32]):
    encoded_input = Input(shape=(encoding_dim,))
    x = Dense(output_shape[0] * output_shape[1] * filters[0], activation='relu')(encoded_input)
    x = Reshape((output_shape[0], output_shape[1], filters[0]))(x)
    for filt in filters:
        x = Conv2DTranspose(filt, (3, 3), activation='relu', padding='same')(x)
    decoded = Conv2D(output_shape[2], (3, 3), activation='sigmoid', padding='same')(x)
    return Model(encoded_input, decoded, name="decoder")

def train_autoencoder(autoencoder, x_train, x_test, epochs=10, batch_size=256):
    autoencoder.fit(x_train, x_train,
                    epochs=epochs,
                    batch_size=batch_size,
                    shuffle=True,
                    validation_data=(x_test, x_test))
def visualize_compression(encoder, decoder, test_images, num_images=10):
    # Predict the encoded and decoded images
    encoded_imgs = encoder.predict(test_images[:num_images])
    decoded_imgs = decoder.predict(encoded_imgs)

    plt.figure(figsize=(20, 6))  # Wider figure to avoid squished subplots

    # Adding titles above columns once, since they share the same encoding and decoding process
    for i in range(num_images):
        if i == 0:
            plt.subplot(3, num_images, i + 1)
            plt.title("Original")
        elif i == num_images:
            plt.subplot(3, num_images, i + 1)
            plt.title("Encoded")
        elif i == 2 * num_images:
            plt.subplot(3, num_images, i + 1)
            plt.title("Decoded")

    # Plotting each category of images
    for i in range(num_images):
        # Original images
        ax = plt.subplot(3, num_images, i + 1)
        plt.imshow(test_images[i].reshape(28, 28), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Encoded representations
        ax = plt.subplot(3, num_images, num_images + i + 1)
        try:
            # Attempt to reshape to a square if possible
            sqrt_len = int(np.sqrt(len(encoded_imgs[i])))
            if sqrt_len * sqrt_len == len(encoded_imgs[i]):
                encoded_reshaped = encoded_imgs[i].reshape(sqrt_len, sqrt_len)
            else:
                raise ValueError("Cannot reshape to a square.")
        except ValueError:
            # Fallback: Use a line plot or simple reshaping if cannot be perfectly squared
            encoded_reshaped = encoded_imgs[i].reshape(1, -1)

        plt.imshow(encoded_reshaped, cmap='gray', aspect='auto')  
        plt.xlabel('Encoded Values')
        ax.get_xaxis().set_visible(True)
        ax.get_yaxis().set_visible(False)

        # Decoded images
        ax = plt.subplot(3, num_images, 2 * num_images + i + 1)
        plt.imshow(decoded_imgs[i].reshape(28, 28), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.tight_layout()
    plt.show()

def visualize_random_generation(decoder, encoding_dim, num_samples=10):
    random_encodings = np.random.normal(0, 1, (num_samples, encoding_dim))
    generated_images = decoder.predict(random_encodings)

    plt.figure(figsize=(20, 2))
    for i in range(num_samples):
        plt.subplot(1, num_samples, i + 1)
        plt.imshow(generated_images[i].reshape(28, 28), cmap='gray')
        plt.axis('off')
    plt.show()
x_train, x_test = load_fashion_mnist()

# Define different scenarios: small and large latent spaces
latent_spaces = [8, 64]  

for encoding_dim in latent_spaces:
    print(f"Training for latent space size: {encoding_dim}")
    encoder = build_conv_encoder(encoding_dim=encoding_dim)
    decoder = build_conv_decoder(encoding_dim)
    autoencoder = Model(encoder.input, decoder(encoder.output))
    autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
    train_autoencoder(autoencoder, x_train, x_test, epochs=3, batch_size=128)  
    
    print(f"Visualizing results for latent space size: {encoding_dim}")
    visualize_compression(encoder, decoder, x_test, num_images=10)
    visualize_random_generation(decoder, encoding_dim, num_samples=10)