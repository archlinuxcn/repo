# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Andre Miranda <andreldm1989 AT gmail DOT com>
# Contributor: Tom Bu <tom.bu AT members.fsf.org>
# Contributor: John Reese <john@noswap.com>
# Contributor: Jordan J Klassen <forivall@gmail.com>
# Contributor: Danny Arnold <despair.blue at gmail dot com>
# Upstream URL: https://github.com/atom/atom

pkgname=atom-editor-bin
pkgver=1.14.1
pkgrel=1
pkgdesc="Chrome-based text editor from Github - Precompiled binary from official repository"
arch=('x86_64')
url="https://github.com/atom/atom"
license=('MIT')
provides=('atom' 'apm')
options=(!strip)
depends=('git' 'gconf' 'gtk2' 'libnotify' 'libxtst' 'nss' 'python2' 'xdg-utils' 'desktop-file-utils' 'alsa-lib' 'libgnome-keyring' 'libxss')
optdepends=('gvfs')
conflicts=('atom' 'atom-editor' 'atom-editor-git' 'atom-editor-git-tagged' 'apm')
install=$pkgname.install

md5sums=('32fd37f68585adc6fac2c7620e908aa1'
         '22b4763c2e8607f0ea46311ec13da9ff'
         'd472858970fc4ba6f63197729b65607c')
source=("atom-amd64-v${pkgver}.deb::https://atom-installer.github.com/v${pkgver}/atom-amd64.deb"
         atom-python.patch
         startupwmclass.patch)

package() {
  bsdtar xf data.tar.gz
  printf "Applying atom-python.patch\n"
  patch -p1 < "${srcdir}"/atom-python.patch
  printf "Applying startupwmclass.patch\n"
  patch -p1 < "${srcdir}"/startupwmclass.patch
  sed -i 's|env PYTHON=python2 GTK_IM_MODULE= QT_IM_MODULE= XMODIFIERS= /usr/share/atom/atom|/usr/bin/atom|' usr/share/applications/atom.desktop
  chmod -R g-w usr
  mv usr "${pkgdir}"
}
