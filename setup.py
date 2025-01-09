from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='rfm_scoring_model',
    version='0.2.1',
    author='Heath Thapa',
    author_email='htmagar.university@gmail.com',
    description='A Python package for scoring Customer ID based ON RFM Analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/singularity-htmagarh/rfm_modeling',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.19.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
