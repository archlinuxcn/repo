# Maintainer: Kyle Sferrazza <kyle.sferrazza@gmail.com>
# Contributor: Tomasz Hamerla <tomasz.hamerla@outlook.com>

pkgname=powershell-bin
_pkgver=6.1.0
pkgver=${_pkgver/-/.}
pkgrel=1
pkgdesc='A cross-platform automation and configuration tool/framework (binary package)'
arch=('x86_64')
url='https://github.com/Powershell/Powershell'
depends=('libunwind' 'icu' 'openssl-1.0')
provides=('powershell')
conflicts=('powershell')
options=(staticlibs !strip)
install=powershell.install
md5sums=('84bddef728a72bf4873a4dd409f87b65')
source=("https://github.com/PowerShell/PowerShell/releases/download/v${_pkgver}/powershell_${_pkgver}-1.ubuntu.16.04_amd64.deb")

package() {
  bsdtar xf data.tar.gz

  mv usr "${pkgdir}"
  mv opt "${pkgdir}"

  cd "${pkgdir}"
  cp -r usr/local/share usr
  rm -rf usr/local

  chmod 755 "opt/microsoft/powershell/6/pwsh"
}
