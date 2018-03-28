from distutils.core import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'ann_visualizer',
  packages = ['ann_visualizer'],
  version = '1.2',
  license="MIT",
  description = 'A python library for visualizing Keras Artificial Neural Networks',
  long_description=long_description,
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
