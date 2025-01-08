from setuptools import setup, find_packages

setup(
    name='rfm_analysis',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python package for RFM analysis and scoring of CRM datasets.',
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
