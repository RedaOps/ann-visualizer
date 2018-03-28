![photo](https://i.imgur.com/DrZJOzy.png)
![photo](https://i.imgur.com/EHIoNoR.png)

# ANN Visualizer
[![PyPI version](https://badge.fury.io/py/ann_visualizer.svg)](https://badge.fury.io/py/ann_visualizer)

A great visualization python library used to work with Keras. It uses python's graphviz library to create a presentable graph of the neural network you are building.

## Installation
### From Github
1. Download the `ann_visualizer` folder from the github repository.
2. Place the `ann_visualizer` folder in the same directory as your main python script.

### From pip
Use the following command:

```bash
pip install ann_visualizer
```

## Usage

```python

from ann_visualizer.visualize import ann_viz;
#Build your model here
ann_viz(model)
```

## Documentation

### ann_viz(model, view=True, filename="network.gv")
* `model` - The Keras Sequential model
* `view` - If True, it opens the graph preview after executed
* `filename` - Where to save the graph. (.gv file format)

## Example
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

ann_viz(network);
```

This will output:
![photo](https://i.imgur.com/ngThGlk.png)

## Contributions
This library is still unstable. Please report all bug to the issues section. It is currently tested with `python3.5`, but it should run just fine on any python3.
