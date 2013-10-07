#!/bin/bash
# Author: Emil Lundberg <lundberg.emil@gmail.com>
#
# Wraps the btsync executable and creates config file if necessary.
#
# This script will create a default BitTorrent Sync configuration file
# at $configPath, if it does not already exist. $configPath is the value
# of the --config option if it is given, and
# ~/.config/btsync/btsync.conf if it is not given. If the --config
# argument appears but is not followed by another argument, then the
# script behaves as if the --config option is not given.
#
# The script /usr/share/bittorrent-sync/btsync-makeconfig.sh will be
# used to create the config file. No arguments will be given to the
# btsync-makeconfig.sh script.
#
# After and creating a config file as necessary, the script runs the
# /usr/share/bittorrent-sync/btsync executable with all arguments
# preserved. If the --config option is not given, then
# "--config ~/.config/btsync/btsync.conf" is appended to the arguments.
#
# If creation of the config file fails, the script exits immediately
# with nonzero exit code, and does not run the btsync executable.
#
# Exit codes:
#   0 The script was executed successfully.
#   1 The config file did not exist and the script failed to create its
#     directory
#   2 The config file did not exist, its directory did exist, and the
#     script failed to create the file.
#

configArgumentAppears=false
configPath=~/.config/btsync/btsync.conf

# Parse arguments
previous=''
for arg in $@; do
    if [[ $previous == '--config' ]]; then
        configPath=$arg
        configArgumentAppears=true
        break
    fi
    previous=$arg
done

if [[ $configArgumentAppears == true ]]; then
    logger " --config option is given"
else
    logger " --config option is not given - using default"
fi

logger "Using config file path: $configPath"

# Create config file if necessary
if [[ ! -f $configPath ]]; then
    logger "Config file does not exist - will create it"

    if mkdir -p $(dirname $configPath); then
        if /usr/share/bittorrent-sync/btsync-makeconfig.sh > $configPath; then
            logger "Config successfully created at $configPath"
        else
            logger "Could not create config at $configPath -
exiting"
            exit 2
        fi
    else
        logger "Could not create directory $(dirname $configPath)
- exiting"
        exit 1
    fi
else
    logger "Config file already exists"
fi

# Execute the btsync executable
if [[ $configArgumentAppears == true ]]; then
    exec /usr/bin/btsync $@
else
    exec /usr/bin/btsync $@ --config $configPath
fi
