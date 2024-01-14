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

Here is the human readable description of the format:

!!! TODO tutaj trzeba dać prawilny opis XML - na razie to jest notatka dla mnie, abym wiedział do czego zmierzam :)

  <meta>
     <!-- metadata about given event -->
     <date>YYYY-MM-DD</date> <!-- date of the event -->
  </meta>

  <speakers>
     <!-- list of speakers, including interruptions -->
     <speaker id="{id only valid in one file}>
       <raw_name>
     </speaker>

  </speakers>

  <transcript>
    <utter speaker_raw_name="{raw name as extracted from PDF}" speaker_id="{reference to speakers}">
       <!-- Here is the text of the given utterance -->
       Lorem ipsum lorem ipsum lorem ipsum
       <interruption speaker_raw_name="{raw name as extracted from PDF}" speaker_id="{}">
       </interruption>
       Lorem ipsum lorem ipsum lorem ipsum
       <reaction name="" raw_name="{raw name extracted from transcript file}" />
       Lorem ipsum lorem ipsum lorem ipsum
    </utter>
    <utter>
       ...
    </utter>
  </transcript>
