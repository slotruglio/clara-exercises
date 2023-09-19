#!/bin/bash

USER="user"
IP="192.168.1.100"

# Date
DATE=$(date '+%F')$

# Source folder
SOURCE="/home/user"
# Destination folder, where the backup will be saved
# The backup will be saved in a folder named with the current date
# In this way, we can store multiple backups
DESTINATION="/var/backup/$DATE"

# Execute the backup
rsync -raz $SOURCE $USER@$IP:$DESTINATION


