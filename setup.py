from setuptools import setup

long_description = """
    ANN Visualizer is a great visualization python library used to work with Keras. It uses python's graphviz library to create a presentable graph of the neural network you are building.

    Usage:


from ann_visualizer.visualize import ann_viz;
#Build your model here
ann_viz(model)



Documentation:

ann_viz(model, view=True, filename="network.gv")

 model - The Keras Sequential model
 view - If True, it opens the graph preview after executed
 filename - Where to save the graph. (.gv file format)
""";


setup(
  name = 'ann_visualizer',
  packages = ['ann_visualizer'],
  version = '2.3',
  license="MIT",
  description = 'A python library for visualizing Neural Networks',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Tudor Gheorghiu',
  author_email = 'tudor.posta@live.com',
  url = 'https://github.com/Prodicode/ann-visualizer',
  download_url = '',
  keywords = ['ann', 'ai', 'visualizer', 'learning', 'artificial', 'intelligence'],
  classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Visualization',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.5',
],
)
