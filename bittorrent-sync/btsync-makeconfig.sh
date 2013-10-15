#!/bin/bash
#
# Generate a default BitTorrent Sync config file for the current user.
# The config file is written to standard out.

if [[ $0 == '/bin/bash' ]]; then
    echo "It looks like you're sourcing this script."
    echo "Please execute it directly instead, lest it clutter your shell with variables and then fail."
    return 1
fi

##############################
# READ INPUT
##############################
for arg in $@; do
    case $previous in
        --device-name|--hostname)
            devicename=$arg;;
        --port)
            port=$arg;;
        --storage-path)
            storagepath=$arg;;
        --check-for-updates)
            checkupdates=$arg;;
        --upnp)
            upnp=$arg;;
        --downlimit)
            downlimit=$arg;;
        --uplimit)
            uplimit=$arg;;
        --webport)
            webport=$arg;;
        --login)
            login=$arg;;
        --pass|--password)
            password=$arg;;
    esac
    case $arg in
        -h|--help)
            cat<<EOF
Usage: source btsync-makeconfig.sh [-h|--help] | [OPTION OPTION_VALUE] ...
    -h
        Print the short version of this message and exit.
    --help
        Print the long version of this message and exit.
    (If both -h and --help appear, the first takes precedence.)

Common options:
    --device-name, --hostname
        Name to display to other clients
    --login
        WebGUI login name
    --pass, --password
        WebGUI password (WILL BE SAVED IN CLEARTEXT!)
    --webport
        WebGUI port

EOF
            # Set exit status to nonzero
            /bin/false
            ;;&
        --help)
            cat<<EOF
OPTIONS
  These options are accepted, with defaults in parentheses. If an option
  appears more than once, the last occurrence overwrites all previous
  ones.

    --device-name, --hostname (\$USER@\$HOSTNAME)
        The name of this device to show in other connected clients.

    --port (0)
        The port on which to listen for BitTorrent Sync connections. 0
        means randomize port.

    --storage-path (~/.config/btsync)
        The directory to store config files and metadata, such as folder
        keys and indices, in.

    --check-for-updates (true)
        Whether to check for updates from upstream If set to true, a
        notification will be shown in WebGUI when a newer version is
        available. Please be patient with the package maintainer. :)

    --upnp (true)
        Whether to use UPnP for port mapping

    --downlimit (0)
        Limit in kB/s on download speed. 0 means no limit.

    --uplimit (0)
        Limit in kB/s on upload speed. 0 means no limit.

    --webport (8888)
        The port on which the WebGUI will be available.

    --login (\$USER)
        The login name to use for WebGUI. You can disable authentication
        in WebGUI by manually commenting out the "login" and "password"
        rows.

    --pass, --password (password)
        The password to use for WebGUI. You can disable authentication
        in WebGUI by manually commenting out the "login" and "password"
        rows.
          WARNING: THE PASSWORD WILL BE PRESERVED IN CLEARTEXT IN THE
          GENERATED CONFIG FILE.

EOF
            # Set exit status to nonzero
            /bin/false
            ;;
    esac || exit 0 # Exit if any of the case blocks were executed
    previous=$arg
done

##############################
# DEFAULTS
##############################
devicename=${devicename:-$USER@$HOSTNAME}
port=${port:-0}
storagepath=${storagepath:-$HOME/.config/btsync}
checkupdates=${checkupdates:-true}
upnp=${upnp:-true}
downlimit=${downlimit:-0}
uplimit=${uplimit:-0}
weblisten=0.0.0.0:${webport:-8888}
login=${login:-$USER}
password=${password:-password}


##############################
# COMMENT HEADER
##############################
# Include the documentation comment from btsync.conf.doc

cat $(dirname $0)/btsync.conf.doc

##############################
# REPLACEMENT
##############################
# String parameter values in the LHS are surrounded with "s and searched for as such
# Non-string parameter values in the LHS are not quoted - use , as delimiter
btsync --dump-sample-config \
    | sed 's#"device_name" *: *"[^"]*"#"device_name" : "'$devicename'"#g' \
    | sed 's#"listening_port" *: *[^,]*#"listening_port" : '$port'#g' \
    | sed 's#"storage_path" *: *"[^"]*"#"storage_path" : "'$storagepath'"#g' \
    | sed 's#"check_for_updates" *: *[^,]*#"check_for_updates" : '$checkupdates'#g' \
    | sed 's#"use_upnp" *: *[^,]*#"use_upnp" : '$upnp'#g' \
    | sed 's#"download_limit" *: *[^,]*#"download_limit" : '$downlimit'#g' \
    | sed 's#"upload_limit" *: *[^,]*#"upload_limit" : '$uplimit'#g' \
    | sed 's#"listen" *: *[^,]*#"listen" : "'$weblisten'"#g' \
    | sed 's#"login" *: *"[^"]*"#"login" : "'$login'"#g' \
    | sed 's#"password" *: *"[^"]*"#"password" : "'$password'"#g'

# vim: ts=4:sw=4:et
