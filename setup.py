# setup.py

from setuptools import setup, find_packages

setup(
    name='image_processing_ajs',                # Package name
    version='0.1.2',                            # Package version
    author='Antonio José Soares',                          # Author's name
    author_email='soaresaj@terra.com.br',       # Author's email
    description='A package for image processing using Python',  # Package description
    long_description=open('README.md', encoding='utf-8').read(),  # Reads the long description from README.md
    long_description_content_type='text/markdown',  # Type of content in README
    url='https://github.com/soaresaj/image-processing-ajs-package',  # Repository URL
    packages=find_packages(),                    # Finds all packages in the directory
    classifiers=[                                # Classifiers for PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                    # Python version requirement
    install_requires=[                           # Package dependencies
        'numpy>=1.21.0',                         # Requires numpy
        'scikit-image>=0.18.0',                  # Requires scikit-image
        'matplotlib>=3.3.0',                     # Requires matplotlib
    ],
)
