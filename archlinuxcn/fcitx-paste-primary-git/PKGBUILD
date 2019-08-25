# Maintainer: lilydjwg <lilydjwg@gmail.com>

pkgname=fcitx-paste-primary-git
_gitname=fcitx-paste-primary
pkgver=0.11.ca5e4ca
pkgrel=1
pkgdesc="Paste-primary module for fcitx, paste primary selection with keyboard shortcut."
arch=('i686' 'x86_64')
url="https://github.com/lilydjwg/fcitx-paste-primary"
license=('GPL')
depends=('fcitx>=4.2.7')
makedepends=('cmake' 'git')
source=('git+https://github.com/lilydjwg/fcitx-paste-primary.git')
_gitname=fcitx-paste-primary
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$_gitname"
  echo "0.$(git rev-list --count HEAD).$(git describe --always)"
}

build() {
  cd "$srcdir/$_gitname"
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo .
  make
}

package() {
  cd "$srcdir/$_gitname"
  make DESTDIR="${pkgdir}" install
}

