from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='flapo',
      description='A simple wsgi web framework',
      long_description=long_description,
      version='0.1',
      url='https://github.com/gjergjk71/flapo',
      author='Gjergj Kadriu',
      author_email='gjergjk71@gmail.com',
      license='Apache2',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
      packages=['flapo'],
      install_requires=[
          'PyYAML>=3.11',
          'sh>=1.11'
      ]
)