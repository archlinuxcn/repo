# Maintainer: Olivier Biesmans <olivier at biesmans dot fr>
# Maintainer: Peter Cai <peter at typeblog dot net>
pkgname=butterfly
pkgver=2.0.1
pkgrel=2
pkgdesc="A sleek web based terminal emulator"
arch=('any')
url="https://pypi.python.org/pypi/butterfly"
license=('GPL')
groups=()
depends=('python' 'python-tornado' 'python-pyopenssl' 'tornado_systemd')
makedepends=('python-setuptools')
optdepends=('python-libsass: theming support')
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=("https://pypi.python.org/packages/source/b/butterfly/butterfly-${pkgver}.tar.gz" "butterfly.service")
sha256sums=('93ecdef71b62e1809a48a706ac2ae86fdbeea6d722970cda99969bccad8ba7ef'
            '2e4fe822908270db8648bcdb492025ab4b972007860a92393b4d4313d6598dbe')

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm 0644 "${srcdir}/${pkgname}.service" \
    "$pkgdir/etc/systemd/system/${pkgname}.service"
}

# vim:set ts=2 sw=2 et:
