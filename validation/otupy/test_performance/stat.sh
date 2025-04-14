#!/bin/bash
# Run the simulation and got statistics

# Remove existing log files
rm -rf controller.log server.log
# Clean server log file
echo "" > ../../examples/server.log

# Run the simulation (change the number of trials: NUM_TESTS)
./controller.py

# Collect log file from the server
cp ../../examples/server.log .

# Collect statistics
awk -f server.awk server.log  | gawk -f stat-server.awk > server.txt
awk -f controller.awk controller.log  | gawk -f stat-controller.awk > controller.txt
