_pkgname=butterfly
pkgname=butterfly
pkgver=3.2.5
pkgrel=4
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://github.com/paradoxxxzero/butterfly"
license=('GPLv3')
depends=('python' 'python-pyopenssl' 'python-tornado' 'tornado_systemd' 'python-setuptools')
optdepends=('python-libsass')
source=("https://files.pythonhosted.org/packages/source/b/butterfly/butterfly-${pkgver}.tar.gz" 'butterfly.service')
md5sums=('023425665c443865349201cc6316eba0'
         '37b6143ec952565987750853ec6cecd7')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  LANG=en_US.UTF-8 python3 setup.py install --root=$pkgdir --optimize=1 --skip-build
  install -Dm 0644 "${srcdir}/${pkgname}.service" \
    "$pkgdir/etc/systemd/system/${pkgname}.service"
}

# vim:set sw=2 et:
