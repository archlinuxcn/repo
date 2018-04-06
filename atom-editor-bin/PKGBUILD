# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Andre Miranda <andreldm1989 AT gmail DOT com>
# Contributor: Tom Bu <tom.bu AT members.fsf.org>
# Contributor: John Reese <john@noswap.com>
# Contributor: Jordan J Klassen <forivall@gmail.com>
# Contributor: Danny Arnold <despair.blue at gmail dot com>

pkgname=atom-editor-bin
pkgver=1.25.1
pkgrel=1
pkgdesc="Atom is a hackable text editor for the 21st century built on Electron - Precompiled binary from official repository"
arch=('x86_64')
url="https://github.com/atom/atom"
license=('MIT')
provides=('atom' 'apm')
options=(!strip)
depends=('git' 'gconf' 'gtk2' 'libnotify' 'libxtst' 'nss' 'python2' 'xdg-utils' 'desktop-file-utils' 'alsa-lib' 'libgnome-keyring' 'libxss')
optdepends=('gvfs')
conflicts=('atom' 'atom-editor' 'atom-editor-git' 'atom-editor-git-tagged' 'apm' 'atom-notracking')
install=$pkgname.install
sha512sums=('e016b1576a46cfe874d40dafd61e7af4029c57500f5358f53d2eb3ccd67c8a06f717c998718744ff50879a91371b9d2023b90b0c3c7a5b36c824e7f5e42eb785'
            '66aa0c1d574def8691c0059f3b26d4b820c430a146db73c23e31a85f7d4894a3b710cef14726c3bebcc88c8c91149012d6caa4e27e62608fe7022516c10e45fe'
            '374b9f8fa1e0d2cab77d4cea9c718fb889bb6db3dbf9762ad5cbb88f3a0936023f36641012fc90e029832a772b8d4fdfe6b72f304e3950c02a7c9bf4d6d3d4ec')
source=("atom-amd64-v${pkgver}.deb::https://atom-installer.github.com/v${pkgver}/atom-amd64.deb"
         atom-python.patch
         startupwmclass.patch)

prepare() {
  # Extract data
  bsdtar xf data.tar.xz

  # Apply patches
  patch -sp1 < "${srcdir}"/atom-python.patch
  patch -sp1 < "${srcdir}"/startupwmclass.patch

  # Modify package to use python2 instead of python3
  sed -i 's|env PYTHON=python2 GTK_IM_MODULE= QT_IM_MODULE= XMODIFIERS= /usr/share/atom/atom|/usr/bin/atom|' usr/share/applications/atom.desktop
  sed -i 's|python|python2|' usr/share/atom/resources/app/apm/bin/python-interceptor.sh
}

package() {
  # Recursively remove group's write permission before moving to package directory
  chmod -R g-w usr
  mv usr "${pkgdir}"
}
