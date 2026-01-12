#!/bin/sh

TIMESTAMP=$(date +%F_%H-%M)
TARGETS="/output/targets.txt"
OUTPUT="/output/scan_$TIMESTAMP.txt"

nuclei -l $TARGETS -o $OUTPUT

curl -T "$OUTPUT" -u "r1jin-nextcloud:kyTfus-rawbe5-buxquz" 
