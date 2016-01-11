# Maintainer Danny Arnold <despair.blue at gmail dot com>
# Contributor: Andre Miranda <andreldm1989 AT gmail DOT com>
# Contributor: Tom Bu <tom.bu AT members.fsf.org>
# Contributor: John Reese <john@noswap.com>
# Contributor: Jordan J Klassen <forivall@gmail.com>
# Upstream URL: https://github.com/atom/atom

pkgname=atom-editor-bin
pkgver=1.3.3
pkgrel=1
pkgdesc="Chrome-based text editor from Github - Precompiled binary from official repository"
arch=('x86_64')
url="https://github.com/atom/atom"
license=('MIT')
options=(!strip)
depends=('git' 'gconf' 'gtk2' 'libnotify' 'libxtst' 'nss' 'python2' 'xdg-utils' 'desktop-file-utils' 'alsa-lib' 'libgnome-keyring')
optdepends=('gvfs')
conflicts=('atom-editor' 'atom-editor-git' 'atom-editor-git-tagged')
install=$pkgname.install

md5sums=('3946d7ee08a8e2190611ba2d0b0fe5ab'
         '9c752be551429c6ce5946d4fcae24464')
source=("atom-amd64-v${pkgver}.deb::https://github.com/atom/atom/releases/download/v${pkgver}/atom-amd64.deb"
         atom-python.patch)

package() {
  bsdtar xf data.tar.gz
  patch -p1 < "${srcdir}"/atom-python.patch
  chmod -R g-w usr
  mv usr "${pkgdir}"
}
