#!/bin/bash

### Parameters ###
cores=4
drives="ada0 ada1 ada2 ada3 ada4"
message=''
NL=$'\n'
cpumax=50
hddmax=50
cpuhigh=0
hddhigh=0

emailto='malcolmchalmers@hotmail.com'

### CPU ###
# Get the temperature of all the cores, and then, with formatting to the message string
cores=$((cores - 1))
for core in $(seq 0 $cores)
do
    temp="$(sysctl -a | grep "cpu.${core}.temp" | cut -c24-25 | tr -d "\n")"
    message+="CPU $core: $temp $NL"
    # get the highest CPU temperature
    if [[ $temp -gt $cpuhigh ]]
    then
        cpuhigh=$temp
    fi
done

# if the highest of all the CPU temperatures is above the threshold (cpumax) send alert
if [[ $cpuhigh -gt $cpumax ]]
then
    # echo and send the whole message so we can see all CPU temperatures, not just the highest
    # echo "$message"
    echo "$message" | mail -s "CPU Temperature Alarm" $emailto
fi

# reset the message text
message=''


### Disks ###
# get the temperature of all the HDDs, and then add them to the message string
for drive in $drives
do
    serial="$(smartctl -i /dev/${drive} | grep "Serial Number" | awk '{print $3}')"
    temp="$(smartctl -A /dev/${drive} | grep "Temperature_Celsius" | awk '{print $10}')"
    message+="$drive $temp $NL"
    # get the highest of the HDD temperatures
    if [[ $temp -gt $hddhigh ]]
    then
        hddhigh=$temp
    fi
done

# if the highest of all the HDD temperatures is above the threshold (high) send alert
if [[ $hddhigh -gt $hddmax ]]
then
    # echo and send the whole message so we can see all CPU temperatures, not just the highest
    # echo "$message" 
    echo "$message" | mail -s "HDD Temperature Alarm" $emailto 
fi

