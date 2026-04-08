#!/bin/bash

LOG_FILE="sample.log"
KEYWORDS=("error" "failed" "critical" "timeout")
THRESHOLD=3

count=0

echo "Scanning logs..."

for keyword in "${KEYWORDS[@]}"; do
    matches=$(grep -i "$keyword" "$LOG_FILE" | wc -l)
    count=$((count + matches))
done

echo "Total issues found: $count"

if [ "$count" -ge "$THRESHOLD" ]; then
    echo "ALERT: High number of errors detected!"
else
    echo "System looks healthy."
fi