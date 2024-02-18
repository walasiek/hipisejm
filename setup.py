from distutils.core import setup


setup(
    name='hipisejm',
    version=__version__,
    author='Marcin Walas',
    author_email='kontakt@marcinwalas.pl',
    packages=[
        'hipisejm',
        'hipisejm.stenparser',
    ],
    scripts=[
        'bin/parser-parse-pdf.py'
    ],
    url='https://pypi.org/project/hipisejm/',
    license='LICENSE',
    description='Parse Polish Sejm transcripts to machine readable corpus',
    long_description=open('README.md').read(),
    install_requires=[
        "pytest",
        "pdfminer.six",
    ],
)
