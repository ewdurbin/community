
import os
from distutils.core import setup

requirements = ['Flask',
                'requests']

def read(fname):
    try:
        path = os.path.join(os.path.dirname(__file__), fname)
        return open(path).read()
    except IOError:
        return ""

setup(
    name='community',
    version='1.0.0b1',
    license='MIT',
    author="Ernest W. Durbin III",
    author_email='ewdurbin@gmail.com',
    description='merge together wellness checks to unify your shit',
    long_description=read('README.rst'),
    url='https://github.com/ewdurbin/community',
    packages=['community'],
    scripts=[],
    install_requires=requirements,
)
