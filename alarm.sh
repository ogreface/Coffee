#!/bin/bash

echo "1" > /sys/class/gpio/gpio17/value
sleep 10
echo "0" > /sys/class/gpio/gpio17/value
