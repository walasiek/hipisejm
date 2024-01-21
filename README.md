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

    python -m pytest tests

To run specific test put path to the test file:

    python -m pytest tests/t_stenparser/test_sejm_parser.py

Format
======

We use XML-alike format to store parsed data.
Each day is stored in the separate file (so in general one PDF transcription will create one XML file).

You will find XSD schema for the corpus output file in resources/hipisejm-transcript-schema.xsd

You can find example of the parsed file in resources/hipisejm-transcript-example.xml

Hint, to validate your XML file:

    xmllint --schema resources/hipisejm-transcript-schema.xsd resources/hipisejm-transcript-example.xml --noout
