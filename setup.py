import os
from setuptools import setup, find_packages

DESCRIPTION = 'small learning project to visualize and document my home network'

# Funktion, um die Version aus version.py zu lesen
def read_version():
    version_file = os.path.join(os.path.dirname(__file__), 'nlist/version.py')
    with open(version_file, 'r') as f:
        exec(f.read())
        return locals()['__version__']


setup(
    name='network-listing',
    version=read_version(),
    author="Bau-steinchen",
    author_email="<mikko.ristein@gmail.com>",
    description=DESCRIPTION,
    include_package_data=True,
    python_requires='>=3.11',
    package_data={
        'btool': ['git/template.xml'],
    },
    keywords=['pip', 'python', 'network', 'kivy'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.11',
        "Operating System :: OS Independent ",
    ],
    entry_points={
        'console_scripts': [
            'nlist=nlist.networklist:main',
        ],
    },
)
