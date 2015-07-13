# Maintainer Danny Arnold <despair.blue at gmail dot com>
# Contributor: Andre Miranda <andreldm1989 AT gmail DOT com>
# Contributor: Tom Bu <tom.bu AT members.fsf.org>
# Contributor: John Reese <john@noswap.com>
# Upstream URL: https://github.com/atom/atom

pkgname=atom-editor-bin
pkgver=1.0.2
pkgrel=1
pkgdesc="Chrome-based text editor from Github - Precompiled binary from official repository"
arch=('x86_64')
url="https://github.com/atom/atom"
license=('MIT')
options=(!strip)
depends=('git' 'gconf' 'gtk2' 'libnotify' 'libxtst' 'nss' 'python2' 'gvfs' 'xdg-utils' 'desktop-file-utils')
conflicts=('atom-editor' 'atom-editor-git' 'atom-editor-git-tagged')
install=$pkgname.install

md5sums=('d20d52fe50e574ebf1eade928058ff94'
         'dbb685607dea46517de0a27e24085bf4')
source=("https://github.com/atom/atom/releases/download/v${pkgver}/atom-amd64.deb"
         atom-python.patch)
package() {
  bsdtar xf data.tar.gz
  patch -p1 < "${srcdir}"/atom-python.patch
  chmod -R g-w usr
  mv usr "${pkgdir}"
}
