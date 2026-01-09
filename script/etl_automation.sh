#!/bin/bash

#---------------------------------------------------------

# ETL Automation Script 

#---------------------------------------------------------

set -euo pipefail


#Define project paths
PROJECT_DIR="/mnt/c/Users/User/Desktop/Volts/week 12/ETL_Pipeline_spotify_playlist"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/etl_$(date +%Y%m%d).log"
PYTHON=$(which python3 || which python)


# Make sure log directory exists
mkdir -p "$LOG_DIR"

echo "----- ETL Job Started at $(date) -----" >> "$LOG_FILE"

#  Step 1 - Ingestion
echo "$(date): Running ingestion..." >> "$LOG_FILE"
"$PYTHON" "$PROJECT_DIR/script/ingest.py" >> "$LOG_FILE" 2>&1

# Step 2 - Transformation
echo "$(date): Running transformation..." >> "$LOG_FILE"
"$PYTHON" "$PROJECT_DIR/script/transform.py" >> "$LOG_FILE" 2>&1


#Step 3 -- Load
echo "$(date): Running Load..." >> "$LOG_FILE" 2>&1
"$PYTHON" "$PROJECT_DIR/script/load.py" >> "$LOG_FILE" 2>&1


echo "ETL Completed Successfully at $(date)" >> "$LOG_FILE"
echo "-------------------------------------" >> "$LOG_FILE"
