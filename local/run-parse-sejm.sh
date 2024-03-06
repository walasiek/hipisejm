#!/bin/bash -e

INDIR=resources/raw-data/sejm
OUTDIR=resources/parsed-data/sejm

if [[ -d $OUTDIR ]]; then
    mkdir -p $OUTDIR
fi

for filepath in `ls $INDIR/*.pdf`
do
    IN_FILENAME=`basename "$filepath"`
    OUT_FP=`echo "$OUTDIR/$IN_FILENAME" | sed -r 's/.pdf$/.xml/;'`

    if [[ ! -e $OUT_FP ]]; then
        echo "Processing $filepath -> $OUT_FP"
        # TODO
        python bin/parser-parse-pdf.py -i $filepath -o $OUT_FP
    else
        echo "$OUT_FP already exists... not processing!"
    fi
done
