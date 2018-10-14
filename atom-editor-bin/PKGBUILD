# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Andre Miranda <andreldm1989 AT gmail DOT com>
# Contributor: Tom Bu <tom.bu AT members.fsf.org>
# Contributor: John Reese <john@noswap.com>
# Contributor: Jordan J Klassen <forivall@gmail.com>
# Contributor: Danny Arnold <despair.blue at gmail dot com>

pkgname=atom-editor-bin
pkgver=1.31.2
pkgrel=1
pkgdesc="Hackable text editor built on Electron (official precompiled binary)"
arch=('x86_64')
url="https://github.com/atom/atom"
license=('MIT')
provides=('atom' 'apm')
options=(!strip !emptydirs)
depends=('git' 'gconf' 'gtk2' 'libnotify' 'libxtst' 'nss' 'python2' 'xdg-utils' 'desktop-file-utils' 'alsa-lib' 'libgnome-keyring' 'libxss')
optdepends=('gvfs')
conflicts=('atom' 'atom-editor' 'atom-editor-git' 'atom-editor-git-tagged' 'apm' 'atom-notracking')
install=$pkgname.install
source=("atom-amd64-v${pkgver}.deb::https://atom-installer.github.com/v${pkgver}/atom-amd64.deb"
         "LICENSE::https://raw.githubusercontent.com/atom/atom/v${pkgver}/LICENSE.md"
         atom-editor-bin.install
         atom-python.patch
         startupwmclass.patch)
sha512sums=('73974d0a3baec8222a1c5074e6ae1ffb8c890c89ffabe12c94387ab83c04abc344d7c9a19d7c6e336e8904a5096178d58524d416ec5d819196a45c61463d2827'
            '4946629b14a57a57a3849fc3ff7f43779b55e1883383949212ccb6cb7bb4867edffb927f9d85cb2717b932c4f5162140d421e19df031edc7ea384ee93d93b2a4'
            'e30f7e4812898b80c079ba419e0cb37522c2e154ef7fdd6dda3da06dcbcaadc42016dd3d3b8caf206b842a2b9e3b954e537626d72337c56f05365a733627ce6c'
            '66aa0c1d574def8691c0059f3b26d4b820c430a146db73c23e31a85f7d4894a3b710cef14726c3bebcc88c8c91149012d6caa4e27e62608fe7022516c10e45fe'
            '374b9f8fa1e0d2cab77d4cea9c718fb889bb6db3dbf9762ad5cbb88f3a0936023f36641012fc90e029832a772b8d4fdfe6b72f304e3950c02a7c9bf4d6d3d4ec')

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

  # Add LICENSE
  install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
}
