# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Maintainer:  Paul Severance <paulseverance+aur@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Preston <pentie [at] gmail.com>

# Install: https://docs.newrelic.com/docs/servers/new-relic-servers-linux/installation-configuration/servers-installation-other-linux
# source PKGBUILD
# Edit PKGBUILD.local and set your RUNAS user
# makepkg -scCfi
# Watch screen for Install instructions.

# UnInstall cleanup: (as root)
#    systemctl status newrelic-sysmond.service
#    systemctl stop newrelic-sysmond.service
#    systemctl disable newrelic-sysmond.service
#    pacman -R newrelic-sysmond
# Sub in the username you picked into the following
#    rm -rf '/var/log/newrelic' '/etc/newrelic' '/.newrelic'

set -u
pkgname='newrelic-sysmond'
pkgver='2.1.0.124'
pkgrel='1'
pkgdesc='collect, monitor, and analyze critical server load metrics including CPU, memory, network, process, disk utilization and capacity'
arch=('i686' 'x86_64')
url='http://newrelic.com/'
license=('custom')
depends=('glibc' 'bash' 'grep' 'sed' 'awk' 'systemd')
makedepends=('binutils')
backup=('etc/newrelic/nrsysmond.cfg')
install="${pkgname}.install"
source=("http://download.newrelic.com/server_monitor/archive/${pkgver}/${pkgname}-${pkgver}-linux.tar.gz"
        "${pkgname}.logrotate"
        "${pkgname}.inst.sh"
        "${pkgname}.service")

sha256sums=('052e42d156e20f77e78f82372123eadf069ef2e5758a1184725a906ead551d9b'
            '02d70a783e30a7b6f8c438b1bae5a57d37d2204d112ccca38eada2b9044a5ebe'
            'bcce083629dcd0827f86247872ee4b42dec2c51349b4cc10c0ce7619f94faf9f'
            '58fade9de4793e22cda75816a74c52d5d9b831ab68bc7b8225aa1bb294b3b31b')

package() {
  set -u
  cd "${srcdir}/${pkgname}-${pkgver}-linux"

  install -dm770 "${pkgdir}/var/log/newrelic" # For some reason the daemon writes files with umask 000

  case "${CARCH}" in
  'i686') install -Dpm755 'daemon/nrsysmond.x86' "${pkgdir}/usr/bin/nrsysmond";;
  'x86_64') install -Dpm755 'daemon/nrsysmond.x64' "${pkgdir}/usr/bin/nrsysmond";;
  *)echo "${}";;
  esac

  install -Dpm755 "${srcdir}/newrelic-sysmond.inst.sh" "${pkgdir}/usr/bin/newrelic-sysmond-inst"

  # The installer makes this file chmod 640. Anything in this file can be found
  # with ps -ef, ls -l /etc/default, or cat newrelic-sysmond.service by any
  # user so there's no reason to go through all the chmod hassle for a file
  # that has nothing to hide.
  install -dm750 "${pkgdir}/etc/newrelic" # The New Relic instructions say 600 but this is clearly wrong.
  install -Dpm640 'nrsysmond.cfg' -t "${pkgdir}/etc/newrelic/"
  sed -i -e '# Forward location of this setting' \
         -e 's:^#pidfile=.*$'":&\n# In Arch Linux this setting is found in /usr/lib/systemd/system/${pkgname}.service:g" \
    "${pkgdir}/etc/newrelic/nrsysmond.cfg"
  install -Dpm755 'scripts/nrsysmond-config' -t "${pkgdir}/usr/bin/"
  sed -i -e '# Our sed recognizes tab escape sequences' \
         -e 's:\t\]:\\t]:g' \
    "${pkgdir}/usr/bin/nrsysmond-config"
  install -Dpm644 "scripts/${pkgname}.default.debian" "${pkgdir}/etc/default/${pkgname}"
  sed -i -e "# Disable a setting we don't use" \
         -e 's;^nrdaemon=.*$'";# The nrdaemon is set by the Arch Linux package installer and cannot be changed here.\n#&;g" \
         -e '# Provide change requirements for RUNAS' \
         -e 's;^RUNAS=.*$'";#&\n# In Arch Linux the RUNAS setting is found in /usr/lib/systemd/system/${pkgname}.service as User=;g" \
     "${pkgdir}/etc/default/${pkgname}"
  install -Dpm644 'INSTALL.txt' 'LICENSE.txt' -t "${pkgdir}/usr/share/doc/newrelic/"
  install -Dpm644 "${srcdir}/${pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system/"
  sed -i -e "# Apply user group info" \
         -e "s;NEWRELIC_USER;${_opt_ASUSER};g" \
     "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
  install -Dpm644 "${srcdir}/${pkgname}.logrotate" "${pkgdir}/etc/logrotate.d/${pkgname}"

  # Ensure there are no forbidden paths. Place at the end of package() and comment out as you find or need exceptions. (git-aurcheck)
  ! test -d "${pkgdir}/sbin" || { echo "Forbidden: /sbin"; echo "${}"; }
  ! test -d "${pkgdir}/usr/sbin" || { echo "Forbidden: /usr/sbin"; echo "${}"; }
  ! test -d "${pkgdir}/usr/local" || { echo "Forbidden: /usr/local"; echo "${}"; }
  #! grep -lr "/sbin" "${pkgdir}" || { echo "Forbidden: /sbin"; echo "${}"; }
  ! grep -lr "/usr/tmp" "${pkgdir}" || { echo "Forbidden: /usr/tmp"; echo "${}"; }
  #! grep -lr "/usr/local" "${pkgdir}" || { echo "Forbidden: /usr/local"; echo "${}"; }
  ! pcregrep -lr "(?<!/usr)/bin" "${pkgdir}" || { echo "Forbidden: /bin"; echo "${}"; }
  set +u
}

[ ! -s 'PKGBUILD.local' ] && cat > 'PKGBUILD.local' << EOF
# Set your RUNAS user here
# root is insecure and unnecesary
# Default: newrelic
_opt_ASUSER='newrelic'
EOF
source 'PKGBUILD.local'

set +u
