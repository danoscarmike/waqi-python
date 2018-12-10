from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='waqi-python',
    version='0.1.0',
    author='Dan O\'Meara',
    author_email='omeara.dan@gmail.com',
    description='A Python wrapper for the World Air Quality Index Project JSON API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danoscarmike/waqi-python",
    packages=['waqi-python'],
    install_requires=[
        'python-dateutil',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
    ]
)
