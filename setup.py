from setuptools import setup, find_packages

setup(
    name='pyai',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyai=pyai.main:main',
        ],
    },
)
