from setuptools import setup, find_packages

setup(
    name='workflow',
    version='0.1.0',
    description='A lightweight and flexible framework for defining and executing asynchronous workflows.',
    long_description='Python package that offers a lightweight and flexible framework for defining and executing asynchronous workflows. It allows you to compose multiple asynchronous steps into a cohesive workflow, enabling the sequential execution of tasks with support for error handling and result propagation.',
    author='Smeet Kevadiya',
    author_email='',
    url='https://github.com/kevadiyasmt/workflow',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'asyncio',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)