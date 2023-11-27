from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Novel translation utility using Sugoi Translator'
LONG_DESCRIPTION = 'Novel translation utility using Sugoi Translator'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="TenshiTranslator", 
        version=VERSION,
        author="Ryan4253",
        author_email="ryan.liao0305@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'selenium',
            'requests',
            'flask'
        ],

        entry_points={'console_scripts': [
            'Main = scripts:Backend:cli',
         ]},
        
        keywords=['python'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)