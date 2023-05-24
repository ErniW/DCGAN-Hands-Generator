# DCGAN-Hands-Generator
Basic Deep Convolutional Generative Adversarial Network to generate hand images. An old example from one of the courses I took.

### Model training:
You can train the GAN by using notebook and later run the Flask app (I decided to practice how to use Flask with my models, Streamlit could be an option). There are a few todos:
- Improve network architecture.
- I think feature collapse is an issue here, furthermore the generator loss increases steadily when applied some regularization techniques. The course where I done this assignment didn't cover how to improve this model. How to be an expert in AI if renowned "advanced" courses cover the basics?
- Using different loss function such as Wasserstein loss.
- Improve backend code, it looks amateurish.