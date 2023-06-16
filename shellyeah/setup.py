from setuptools import setup, find_packages

setup(
    name="shellyeah",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'shellyeah=shellyeah.shellyeah:main',
        ],
    },
)