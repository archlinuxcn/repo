# Maintainer: roger rogerduran at gmail

pkgname=qtile
pkgver=0.10.0
pkgrel=1
pkgdesc="A full-featured, pure-Python tiling window manager."
arch=('any')
url="http://www.qtile.org"
license=('MIT')
depends=('python' 'pango' 'python-xcffib>=0.3.2' 'python-cairocffi>=0.7')
makedepends=('python-distribute')
optdepends=('python-setproctitle: change the process name to qtile')
conflicts=('qtile-git')
install=${pkgname}.install
source=("https://github.com/qtile/qtile/archive/v${pkgver}.tar.gz")
md5sums=('fb95960b4d495f6637da83c9d54c2c6a')

package() {
  cd "$srcdir/$pkgname-$pkgver/"
  # license
  msg "Copying license..."
  install -D -m 644 LICENSE $pkgdir/usr/share/licenses/$pkgname/LICENSE

  msg "Copying default config..."
  install -D -m 644 libqtile/resources/default_config.py $pkgdir/usr/share/doc/$pkgname/default_config.py

  msg "Copying desktop file..."
  install -D -m 644 resources/qtile.desktop $pkgdir/usr/share/xsessions/qtile.desktop

  # install
  msg "Running setup.py"
  python setup.py install --root=${pkgdir} --prefix=/usr
}
