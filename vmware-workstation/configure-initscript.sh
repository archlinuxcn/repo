#!/bin/bash

action="$1" # add, remove, or status
serviceName="$2"
startLevel="$3"
stopLevel="$4"

# Notes:
# This package does not need a vmware service to make VMware usable, so this script says that vmware service is always started.
# vmware-workstation-server service is named vmware-hostd in this package.

case "$serviceName" in
   vmware-workstation-server)
      serviceName="vmware-hostd"
      ;;
esac

#echo $serviceName && exit # DEBUG

addService() {
   if [ "$serviceName" != "vmware" ]; then
      systemctl start $serviceName.service
      systemctl enable $serviceName.service
   fi
}

removeService() {
   if [ "$serviceName" != "vmware" ]; then
      systemctl stop $serviceName.service
      systemctl disable $serviceName.service
   fi
}

# Check to see whether a program is set to start on boot.
checkService() {
   if [ "$serviceName" = "vmware" ]; then
      retval=0
   else
      systemctl is-active $serviceName.service > /dev/null
      retval=$?
   fi

   if [ "$retval" = "0" ]; then
      echo 'on'
      exit 5
   else
      echo 'off'
      exit 6
   fi
}

usage() {
      echo "Syntax for this script is as follows:"
      echo ""
      echo " $0 <action> <serviceName>"
      echo ""
      echo " action      - add or remove"
      echo " serviceName - The name of the service"
      echo ""
      echo ""
      echo " $0 status <serviceName>"
      echo " serviceName - The name of the service"
      echo ""
}



case $action in
   add)
      # Don't allow any empty arguments for add
      if [ "$1" = "" ] || [ "$2" = "" ] || [ "$3" = "" ] || [ "$4" = "" ]; then
         usage
         exit 1
      fi
      addService
      ;;
   remove)
      # Don't allow any empty arguments for remove
      if [ "$1" = "" ] || [ "$2" = "" ] || [ "$3" = "" ] || [ "$4" = "" ]; then
         usage
         exit 1
      fi
      removeService
      ;;
   status)
      # We only need the serviceName to check status
      if [ "$1" = "" ] || [ "$2" = "" ]; then
         usage
         exit 1
      fi
      checkService
      ;;
   *)
      usage
      exit 1
      ;;
esac
