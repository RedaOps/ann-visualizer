![photo](https://i.imgur.com/DrZJOzy.png)
![photo](https://i.imgur.com/EHIoNoR.png)

# ANN Visualizer
[![PyPI version](https://badge.fury.io/py/ann_visualizer.svg)](https://badge.fury.io/py/ann_visualizer) [![Build Status](https://travis-ci.org/Prodicode/ann-visualizer.svg?branch=master)](https://travis-ci.org/Prodicode/ann-visualizer) [![Donate](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/Prodicode/donate)

A great visualization python library used to work with Keras. It uses python's graphviz library to create a presentable graph of the neural network you are building.

## Version 2.0 is Out!

Version 2.0 of the ann_visualizer is now released! The community demanded a CNN visualizer, so we updated our module. You can check out an example of a CNN visualization below!

Happy visualizing!

## Installation
### From Github
1. Download the `ann_visualizer` folder from the github repository.
2. Place the `ann_visualizer` folder in the same directory as your main python script.

### From pip
Use the following command:

```bash
pip3 install ann_visualizer
```

Make sure you have graphviz installed. Install it using:

```bash
sudo apt-get install graphviz && pip3 install graphviz
```

## Usage

```python

from ann_visualizer.visualize import ann_viz;
#Build your model here
ann_viz(model)
```

## Documentation

### ann_viz(model, view=True, filename="network.gv", title="MyNeural Network")
* `model` - The Keras Sequential model
* `view` - If True, it opens the graph preview after executed
* `filename` - Where to save the graph. (.gv file format)
* `title` - A title for the graph

## Example ANN
```python
import keras;
from keras.models import Sequential;
from keras.layers import Dense;

network = Sequential();
        #Hidden Layer#1
network.add(Dense(units=6,
                  activation='relu',
                  kernel_initializer='uniform',
                  input_dim=11));

        #Hidden Layer#2
network.add(Dense(units=6,
                  activation='relu',
                  kernel_initializer='uniform'));

        #Exit Layer
network.add(Dense(units=1,
                  activation='sigmoid',
                  kernel_initializer='uniform'));

from ann_visualizer.visualize import ann_viz;

ann_viz(network, title="");
```

This will output:
![photo](https://i.imgur.com/ngThGlk.png)

## Example CNN
```python
import keras;
from keras.models import Sequential;
from keras.layers import Dense;
from ann_visualizer.visualize import ann_viz
model = build_cnn_model()
ann_viz(model, title="")

def build_cnn_model():
  model = keras.models.Sequential()

  model.add(
      Conv2D(
          32, (3, 3),
          padding="same",
          input_shape=(32, 32, 3),
          activation="relu"))
  model.add(Dropout(0.2))

  model.add(
      Conv2D(
          32, (3, 3),
          padding="same",
          input_shape=(32, 32, 3),
          activation="relu"))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.2))

  model.add(
      Conv2D(
          64, (3, 3),
          padding="same",
          input_shape=(32, 32, 3),
          activation="relu"))
  model.add(Dropout(0.2))

  model.add(
      Conv2D(
          64, (3, 3),
          padding="same",
          input_shape=(32, 32, 3),
          activation="relu"))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.2))

  model.add(Flatten())
  model.add(Dense(512, activation="relu"))
  model.add(Dropout(0.2))

  model.add(Dense(10, activation="softmax"))

  return model
```

This will output:
![photo](https://i.imgur.com/v3QpACl.png)

## Contributions
This library is still unstable. Please report all bug to the issues section. It is currently tested with `python3.5` and `python3.6`, but it should run just fine on any python3.
