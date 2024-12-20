from distutils.core import setup
import hipisejm


setup(
    name='hipisejm',
    version=hipisejm.__version__,
    author='Marcin Walas',
    author_email='kontakt@marcinwalas.pl',
    packages=[
        'hipisejm',
        'hipisejm.stenparser',
        'hipisejm.utils',
    ],
    scripts=[
        'bin/hipisejm-parse-pdf.py'
    ],
    url='https://pypi.org/project/hipisejm/',
    license='LICENSE',
    description='Parse Polish Sejm transcripts to machine readable corpus',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "pytest",
        "pdfminer.six",
    ],
)
