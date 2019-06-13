#!/bin/bash

hostname -I | awk '{print $1}' > /var/www/html/input.txt
