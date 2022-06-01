# Maintainer: Andreas Radke <andyrtr@archlinux.org>
# Maintainer: Jan de Groot <jgc@archlinux.org>

_pkgname=xdg-utils
pkgname=$_pkgname-lxqt
# https://gitlab.freedesktop.org/xdg/xdg-utils/commits/master
_commit=1a58bc28f6844898532daf9ee1bf6da7764955a9 # master # 2021-08-05
pkgver=1.1.3+21+g1a58bc2
pkgrel=1
pkgdesc="Command line tools that assist applications with a variety of desktop integration tasks"
arch=('any')
url="https://www.freedesktop.org/wiki/Software/xdg-utils/"
license=('MIT')
depends=('sh' 'which' 'file' 'xorg-xset' 'xorg-xprop') # xset + xprop needed inside xdg-screensaver
makedepends=('docbook-xsl' 'lynx' 'xmlto' 'git')
optdepends=('kde-cli-tools: for KDE Plasma5 support in xdg-open'
            'exo: for Xfce support in xdg-open'
            'pcmanfm: for LXDE support in xdg-open'
            'perl-file-mimeinfo: for generic support in xdg-open'
            'perl-net-dbus: Perl extension to dbus used in xdg-screensaver'
            'perl-x11-protocol: Perl X11 protocol used in xdg-screensaver')
source=("git+https://gitlab.freedesktop.org/xdg/xdg-utils.git#commit=$_commit")
sha256sums=('SKIP')
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")

pkgver() {
  cd $_pkgname
  git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
  cd $_pkgname
  # https://gitlab.freedesktop.org/xdg/xdg-utils/-/merge_requests/48
  git cherry-pick -n ba6d7dee165aaf2dc01305f53b9229985bc7cb0a
}

build() {
  cd $_pkgname
  ./configure --prefix=/usr --mandir=/usr/share/man
  make
}

package() {
  cd $_pkgname
  make DESTDIR="${pkgdir}" install
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # install empty directory to prevent xdg-desktop-menu install *.desktop to fail, see FS#33316
  install -dm755 "$pkgdir"/usr/share/desktop-directories
}
