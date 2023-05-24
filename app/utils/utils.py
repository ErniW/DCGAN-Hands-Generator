import tensorflow as tf

@tf.keras.utils.register_keras_serializable()
class SpectralNormalization(tf.keras.layers.Wrapper):
    def __init__(self, layer, iteration=1,**kwargs):
        super(SpectralNormalization, self).__init__(layer, **kwargs)
        self.iteration = iteration

    def build(self, input_shape):
        super(SpectralNormalization, self).build(input_shape)
        self.w = self.layer.kernel
        self.w_shape = self.w.shape.as_list()
        self.u = self.add_weight(shape=(1, self.w_shape[-1]),
                                 initializer=tf.initializers.RandomNormal(),
                                 trainable=False,
                                 
                                 dtype=tf.float32)

    def call(self, inputs):
        self.normalize_weights()
        output = self.layer(inputs)
        return output

    def normalize_weights(self):
        w = tf.reshape(self.w, [-1, self.w_shape[-1]])
        u_hat = self.u
        v_hat = None

        for _ in range(self.iteration):
            v_ = tf.matmul(u_hat, tf.transpose(w))
            v_hat = tf.nn.l2_normalize(v_)

            u_ = tf.matmul(v_hat, w)
            u_hat = tf.nn.l2_normalize(u_)

        sigma = tf.matmul(tf.matmul(v_hat, w), tf.transpose(u_hat))
        self.u.assign(u_hat)

        self.layer.kernel = self.w / sigma


def generate_images(generator):
    images_amount = 6
    random_normal_dimensions = 32
    noise = tf.random.normal(shape=[images_amount, random_normal_dimensions])
    images = generator(noise)
    return images


def load_generator(filepath):
    model = tf.keras.models.load_model(filepath,  custom_objects={'SpectralNormalization': SpectralNormalization})
    model.summary()
    generator = model.get_layer('Generator')
    generator.summary()
    return generator


def save_as_png(image, index):
    file_name = f"static/images/prediction_{index}.png"
    tf.keras.preprocessing.image.save_img(file_name, image)
    return file_name


def generate_images_paths(images):
    image_paths = []

    for i, image in enumerate(images):
        file_path = save_as_png(image, i)
        image_paths.append(file_path)

    return image_paths