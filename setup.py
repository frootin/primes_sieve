from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(

    name='primes_sieve',

    version='0.0.1',

    description='A sample Python project with some functionality',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/pypa/sampleproject',  # Optional

    author='Nathalia B',

    author_email='natalyxxxgo@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development',

        'License :: OSI Approved :: MIT License',


        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],

    
    keywords='sample, prime_numbers',

    packages=find_packages(where='source'),

    python_requires='>=3.9',

    entry_points={
        'console_scripts': [
            'sieve_run=sieve:run',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
    },
)