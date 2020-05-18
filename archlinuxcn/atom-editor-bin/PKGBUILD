# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Andre Miranda <andreldm1989 AT gmail DOT com>
# Contributor: Tom Bu <tom.bu AT members.fsf.org>
# Contributor: John Reese <john@noswap.com>
# Contributor: Jordan J Klassen <forivall@gmail.com>
# Contributor: Danny Arnold <despair.blue at gmail dot com>

pkgname=atom-editor-bin
pkgver=1.46.0
pkgrel=1
pkgdesc="Hackable text editor built on Electron (official precompiled binary)"
arch=('x86_64')
url="https://github.com/atom/atom"
license=('MIT')
provides=('atom' 'apm')
options=(!strip !emptydirs)
depends=('git' 'gtk3' 'libnotify' 'libxtst' 'nss' 'python2' 'xdg-utils' 'desktop-file-utils' 'alsa-lib' 'libgnome-keyring' 'libxss' 'libxkbfile' 'ripgrep')
optdepends=('gvfs')
conflicts=('atom' 'atom-editor' 'atom-editor-git' 'atom-editor-git-tagged' 'apm' 'atom-notracking')
install=$pkgname.install
source=("atom-amd64-v${pkgver}.deb::https://atom-installer.github.com/v${pkgver}/atom-amd64.deb"
         "LICENSE::https://raw.githubusercontent.com/atom/atom/v${pkgver}/LICENSE.md"
         atom-editor-bin.install
         atom-python.patch
         startupwmclass.patch)
sha512sums=('2fddd676ad35758fc8e0bb3e34de5d03e347b174f6ff42042924321dbd887d929f20c9ee479a71b8032d7c3e94f86d90c1878551b2e4fc17a3a02e505aa35137'
            'c8fdd1d51313c078d20ab4c127db78d71d94e1987b78ce04fb1b6b47e875b047c5722092892ac0b6ec6640c7428b4e03a22f71f29d9d67082cd22cadf604b7fc'
            'e30f7e4812898b80c079ba419e0cb37522c2e154ef7fdd6dda3da06dcbcaadc42016dd3d3b8caf206b842a2b9e3b954e537626d72337c56f05365a733627ce6c'
            '37e33402ff1a21c27debc56ac909279992c6a3aa9f2d8dd49fb13fc02cc3fb91a373531be92df9cc81089e167827ca7b36f967e4f7e482b1173d358a8b29cb98'
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
