from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# This is a fork of Kyubyong/g2p, published under its own name because PyPI
# rejects a distribution whose metadata points at a git repository. See
# FORK_NOTICE.md for what differs from upstream and why. The import name stays
# g2p_en, so nothing downstream changes except which distribution provides it.
fork_notice = """
**This is an unofficial republication of**
`Kyubyong/g2p <https://github.com/Kyubyong/g2p>`_ **maintained by the ESPnet
project. It is not affiliated with, nor endorsed by, the original authors.**
It exists because upstream's last release (2.1.0, December 2019) asks NLTK for
``averaged_perceptron_tagger``, which NLTK 3.8.2 renamed to
``averaged_perceptron_tagger_eng``, so ``import g2p_en`` fails on any current
NLTK. The import name is unchanged. See ``FORK_NOTICE.md``.

"""

setup(
  name = 'espnet-g2p-en',
  packages = ['g2p_en'],  # the import name, deliberately unchanged
  version = '2.1.0.post1',
  description = 'A Simple Python Module for English Grapheme To Phoneme Conversion (ESPnet fork)',
  long_description=fork_notice + long_description,
  long_description_content_type='text/x-rst',
  author = 'Kyubyong Park & Jongseok Kim',
  author_email = 'kbpark.linguist@gmail.com',
  maintainer = 'ESPnet Developers',
  url = 'https://github.com/Kyubyong/g2p',  # the original project
  project_urls = {
    'Original project': 'https://github.com/Kyubyong/g2p',
    'Source (this fork)': 'https://github.com/espnet/g2p',
    'Fork notice': 'https://github.com/espnet/g2p/blob/master/FORK_NOTICE.md',
  },
  keywords = ['g2p','g2p_en'],
  classifiers = [],
  install_requires = [
    'numpy>=1.13.1',
    # 3.8.2 is where averaged_perceptron_tagger_eng appears, and this fork asks
    # for that resource by name, so an older NLTK would fail the lookup.
    'nltk>=3.8.2',
    'inflect>=0.3.1',
    'distance>=0.1.3',
  ],
  license='Apache Software License',
  include_package_data=True
)
