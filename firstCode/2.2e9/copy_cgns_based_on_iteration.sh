#!/bin/bash

next_target=735

SOURCE_FILE="out.cgns"
MONITOR_FILE="monitor.smf"

while true; do

  sleep 1
  
  if [[ -s "$MONITOR_FILE" ]]; then
    # Extract the last line and get the iteration number
    last_line=$(tail -n 1 "$MONITOR_FILE")
    iteration=$(echo "$last_line" | awk '{print $1}')
    
    
    if [[ "$iteration" -ge "$next_target" ]]; then
    
      output_file="out-$((next_target - 2)).cgns"
      
      if [[ -f "$SOURCE_FILE" ]]; then
        cp "$SOURCE_FILE" "$output_file"
        echo "Copied to $output_file"
      else
        echo "Source file $SOURCE_FILE not found. Skipping..."
      fi
      
      next_target=$((next_target + 733))
    fi
  else
    echo "Monitor file $MONITOR_FILE not found or is empty. Retrying..."
  fi
done

