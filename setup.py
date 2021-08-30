# Reference :  Setup script documentation
# https://setuptools.readthedocs.io/en/latest/setuptools.html

from setuptools import setup, find_packages

def get_requirements(filename):
    with open(filename) as f:
        requirements = f.read().splitlines()
    return requirements

setup(name='testing',
      setup_requires=['pytest-runner', 'pytest-pylint'],
      tests_require=['pytest', 'pylint'],
      version='1.0',
      description='Software Engineering Homework 2b',
      author='Gaolin Zhang',
      author_email='gzhang26@ncsu.edu',
      license="MIT",
      packages=find_packages(),
      python_requires=">=3.5",
      install_requires=get_requirements("requirements.txt"),
)