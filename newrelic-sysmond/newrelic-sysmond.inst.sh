#!/usr/bin/bash

set -u
if [ "${EUID}" -ne 0 ]; then
  echo 'Must be root!'
  exit 1
fi

_fn_install() {
  # From https://docs.newrelic.com/docs/servers/new-relic-servers-linux/installation-configuration/servers-installation-other-linux
  systemctl daemon-reload # in case the admin has edited the file
  local _RUNAS="$(sed -ne 's:^User=\(.*\)$:\1:p' '/usr/lib/systemd/system/newrelic-sysmond.service')"

  # Create the newrelic user and group
  if [ ! -z "${_RUNAS}" -a "${_RUNAS}" != 'root' ]; then
    #useradd --system -M --home / --shell '/usr/bin/nologin' "${_RUNAS}" || :
    groupadd -r "${_RUNAS}" || :
    useradd -r -g "${_RUNAS}" -d "/.${_RUNAS}" -s '/usr/bin/nologin' -c 'New Relic monitoring daemon' "${_RUNAS}" || :
    mkdir -p "/.${_RUNAS}"
    chmod 700 "/.${_RUNAS}"
    chown -R "${_RUNAS}:${_RUNAS}" "/.${_RUNAS}"
  fi
  chown -R "root:${_RUNAS}" '/etc/newrelic/'
  chown -R "root:${_RUNAS}" '/var/log/newrelic'
  #chmod 750 '/etc/newrelic/' # WTF were they thinking with chmod 600?

  # Kludge the permissions (now done in PKGBUILD)
  #mkdir -p '/var/log/newrelic'
  #chmod 1777 '/var/log/newrelic'

  local _deffile='/etc/default/newrelic-sysmond'
  local _cfgfile="$(source "${_deffile}"; echo "${cfgfile:-/etc/newrelic/nrsysmond.cfg}")"

  # This file contains nothing needing group access so it doesn't need to be chown to group any more
  #chown "root:${_RUNAS}" "${_cfgfile}"
  #chmod 640 ${_cfgfile}

  #
  # When first installing the package, the license key will not be set.
  # Instead of throwing an error, we want to whine to the user and then exit cleanly.
  #

  if sed -e '/^[ \t]*#/d' "${_cfgfile}" | grep -ql 'REPLACE_WITH_REAL_KEY'; then
    #if [ -z "${NR_SILENT}" -a -z "${SILENT}" ]; then
      #
      # WARNING - This text is duplicated from newrelic-sysmond.init
      #
      cat <<EOF
*********************************************************************
*********************************************************************
***
***  Can not start the New Relic Server Monitor until you insert a
***  valid license key in the following file:
***
***     ${_cfgfile}
***
***  You can do this by running the following command as root:
***
***     nrsysmond-config --set license_key=<your_license_key_here>
***
***  No data will be reported until the server monitor can start.
***  You can get your New Relic key from the 'Configuration' section
***  of the 'Support' menu of your New Relic account (accessible at
***  https://rpm.newrelic.com )
***
*********************************************************************
*********************************************************************

Then, enable and start your server:

    systemctl enable newrelic-sysmond.service
    systemctl start newrelic-sysmond.service
    systemctl status newrelic-sysmond.service
EOF
    #fi
  fi
}

_fn_remove() {
  # What happens if we install two New Relic packages then uninstall one?
  # We lose our user and the remaining package doesn't run, right?
  # Until someone figures out a better way we'll let an upgrade fix it.
  local _RUNAS="$(sed -ne 's:^User=\(.*\)$:\1:p' '/usr/lib/systemd/system/newrelic-sysmond.service')"
  if [ ! -z "${_RUNAS}" -a "${_RUNAS}" != 'root' ] && [ "$(id -u "${_RUNAS}")" -ge 990 ]; then
    userdel "${_RUNAS}" || :
    groupdel "${_RUNAS}" || :
  fi
}

case "${1-}" in
  install) _fn_install;;
  remove) _fn_remove;;
  *) echo "Usage $(basename "$0") remove|install";;
esac

# vim:set ts=2 sw=2 et:
