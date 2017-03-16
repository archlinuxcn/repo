# Maintainer: roger rogerduran at gmail

pkgname=qtile
pkgver=0.10.7
pkgrel=1
pkgdesc="A full-featured, pure-Python tiling window manager."
arch=('any')
url="http://www.qtile.org"
license=('MIT')
depends=('python' 'pango' 'python-xcffib>=0.5.1' 'python-cairocffi>=0.8.0')
makedepends=('python-distribute')
optdepends=('python-setproctitle: change the process name to qtile')
conflicts=('qtile-git')
install=${pkgname}.install
source=("https://github.com/qtile/qtile/archive/v${pkgver}.tar.gz")
sha256sums=('cbde17f5afdf2af7c80dd47c0f0ed5f8d716e3c87082c091b38e0d241ba39753')

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
