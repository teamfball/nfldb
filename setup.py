import codecs
from distutils.core import setup
from glob import glob
import os.path as path

cwd = path.dirname(__file__)
longdesc = codecs.open(path.join(cwd, 'longdesc.rst'), 'r', 'utf-8').read()

version = '0.0.0'
with codecs.open(path.join(cwd, 'nfldb/version.py'), 'r', 'utf-8') as f:
    exec(f.read())
    version = __version__
assert version != '0.0.0'

setup(
    name='nfldb',
    author='Andrew Gallant',
    author_email='nfldb@burntsushi.net',
    version=version,
    license='WTFPL',
    description='A library to manage and update NFL data in a relational '
                'database.',
    long_description=longdesc,
    url='https://github.com/BurntSushi/nfldb',
    classifiers=[
        'License :: Public Domain',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
    ],
    platforms='ANY',
    packages=['nfldb'],
    data_files=[('share/doc/nfldb', ['README.md', 'longdesc.rst',
                                     'COPYING', 'INSTALL']),
                ('share/doc/nfldb/doc', glob('doc/nfldb/*.html'))],
    install_requires=['nflgame', 'toml', 'psycopg2', 'enum34'],
    scripts=[]
)
