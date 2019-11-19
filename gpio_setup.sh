#!/bin/bash

# Pin 19: OUT + HIGH
gpio -g mode 19 out
gpio -g write 19 1
