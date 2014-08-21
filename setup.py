
from distutils.core import setup

requirements = ['Flask',
                'requests']

setup(
    name='community',
    version='1.0.0a1',
    license='MIT',
    author="Ernest W. Durbin III",
    author_email='ewdurbin@gmail.com',
    description='merge together wellness checks to unify your shit',
    url='https://github.com/ewdurbin/community',
    packages=['community'],
    scripts=[],
    install_requires=requirements,
)
