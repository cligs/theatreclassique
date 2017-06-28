#!/bin/bash


FILENAME=$1
IDS_DECLARED=`xpath $FILENAME '//role/@xml:id' 2> /dev/null | sed -E 's/xml:id="([a-zA-Z0-9-]+)"/\1/g' | tr ' ' '\n' | sort | uniq`
IDS_USED=`xpath $FILENAME //sp/@who 2> /dev/null | sed -E 's/who="([a-zA-Z0-9-]*)"/\1/g' | tr ' ' '\n' | sort | uniq `
echo "IDs used and not declared:"
comm -3 -2  <(echo "$IDS_USED" ) <(echo "$IDS_DECLARED")

echo "IDs declared and not used:"
comm -3 -1  <(echo "$IDS_USED" ) <(echo "$IDS_DECLARED")
