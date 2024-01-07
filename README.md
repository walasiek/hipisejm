# hipisejm

Process textual data from Polish Sejm.

Does the same thing as is available on https://kdp.nlp.ipipan.waw.pl/query_corpus/
but maybe someone will find those scripts useful.

Configuration
=============

Create virtualenv:

    source enter.sh

Then every time you start working you can simply type it again.

To add virtualenv from `enter.sh` to jupyter (one time):

    python -m ipykernel install --user --name=hipisejm

Testing
=======

To run all tests type (use -s for debug show of prints ;) ):

    pytest tests

To run specific test put path to the test file:

    pytest tests/t_stenparser/test_sejm_parser.py
