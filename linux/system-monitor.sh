#!/bin/bash

# Define function to calculate percentage
calc_percent() {
  awk "BEGIN { pc=100*${1}/${2}; i=int(pc); print (pc-i<0.5)?i:i+1 }"
}

# Loop indefinitely
while true; do
  # Get CPU usage
  cpu=$(top -bn1 | grep "Cpu(s)" | awk '{print $2+$4}')
  cpu_percent=$(calc_percent $cpu $(nproc))

  # Get memory usage
  mem_used=$(free -m | awk 'NR==2{printf "%.2f\n", $3/1024}')
  mem_total=$(free -m | awk 'NR==2{printf "%.2f\n", $2/1024}')
  mem_percent=$(calc_percent $mem_used $mem_total)

  # Get disk usage
  disk_used=$(df -h / | awk 'NR==2{print $3}')
  disk_total=$(df -h / | awk 'NR==2{print $2}')
  disk_percent=$(df -h / | awk 'NR==2{print $5}')

  # Clear screen and display stats
  clear
  echo "System Monitor"
  echo "----------------"
  echo "CPU Usage  : $cpu_percent%"
  echo "Memory     : $mem_used / $mem_total GB ($mem_percent%)"
  echo "Disk Usage : $disk_used / $disk_total ($disk_percent)"
  
  # Sleep for 1 second
  sleep 1
done
