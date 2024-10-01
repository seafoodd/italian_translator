from setuptools import setup, find_packages

setup(
    name='italian_translator',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'italian-translator=italian_translator.main:main',
            'ita=italian_translator.main:main',
        ],
    },
    author='seafood',
    author_email='mail.seafood@proton.me',
    description='A command-line tool for translating Italian words using Reverso Context.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seafoodd/italian_translator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)