from setuptools import setup
from zx81p2wav import __version__

setup(
    name='zx81p2wav',
    version=__version__,
    author='Fredrik Ahlberg',
    author_email='fredrik@z80.se',
    description='Minimalistic ZX81 p-file to wav converter',
    url='https://github.com/themadinventor/zx81p2wav',
    packages=['zx81p2wav'],
    entry_points={
        'console_scripts': ['zx81p2wav = zx81p2wav.__main__:main'],
    }
)