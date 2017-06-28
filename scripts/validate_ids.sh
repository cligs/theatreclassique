#!/bin/bash


FILENAME=$1
IDS_DECLARED=`xpath $FILENAME '//role/@xml:id' 2> /dev/null | LC_ALL=C sed -E 's/xml:id="([^"]+)"/\1/g' | LC_ALL=C tr ' ' '\n' | LC_ALL=C sort | LC_ALL=C uniq`
IDS_USED=`xpath $FILENAME //sp/@who 2> /dev/null | LC_ALL=C sed -E 's/who="([^"]*)"/\1/g' | LC_ALL=C tr ' ' '\n' | LC_ALL=C sort | LC_ALL=C uniq`
echo "IDs used and not declared:"
LC_ALL=C comm -3 -2  <(echo "$IDS_USED" ) <(echo "$IDS_DECLARED")

echo "IDs declared and not used:"
LC_ALL=C comm -3 -1  <(echo "$IDS_USED" ) <(echo "$IDS_DECLARED")
