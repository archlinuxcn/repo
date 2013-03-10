# Maintainer: abf <zouxiaoming@gmail.com>

pkgname=auto-complete
pkgver=1.3.1
pkgrel=1
pkgdesc="A plugin for emacs that allows to auto-complete.Auto Complete Mode is the most intelligent auto-completion extension for GNU Emacs."
arch=('any')
url="http://cx4a.org/software/auto-complete/"
license=('GPL3')
install=$pkgname.install
depends=()
optdepends=('emacs')
source=(http://cx4a.org/pub/auto-complete/$pkgname-$pkgver.tar.bz2)
md5sums=('0ffdc1223d40b8ebc57495e33708ceea')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p $pkgdir/usr/share/$pkgname
  mkdir -p $pkgdir/usr/share/emacs/site-lisp/
  make DIR="$pkgdir/usr/share/$pkgname" install 
  ln -s /usr/share/$pkgname $pkgdir/usr/share/emacs/site-lisp/$pkgname
}

# vim:set ts=2 sw=2 et:
