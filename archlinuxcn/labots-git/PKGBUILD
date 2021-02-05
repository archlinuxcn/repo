_pkgname=labots
pkgname=${_pkgname}-git
pkgver=0.99.4decdc4
pkgrel=1
pkgdesc='Flexible IRC bot framework'
arch=('any')
url="https://github.com/SilverRainZ/${_pkgname}"
license=('GPL3')
makedepends=('git')
depends=('python' 'python-tornado' 'python-yaml' 'python-pydle' 'python-sqlitedict')
conflicts=('labots')
provides=('labots')
source=("git+https://github.com/SilverRainZ/${_pkgname}")
sha256sums=('SKIP')
backup=('etc/labots/default.yaml' 'var/lib/bots/bots.yaml')

pkgver() {
  cd "${srcdir}/${_pkgname}"
  echo "0.$(git rev-list --count HEAD).$(git describe --always)"
}

build() {
  cd "${srcdir}/${_pkgname}"

  python3 setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}"

  python3 setup.py install --root=${pkgdir} --optimize=1 --skip-build

  install -Dm644 "$srcdir/labots/labots.yaml" "$pkgdir/etc/labots/default.yaml"
  install -Dm644 "$srcdir/labots/scripts/labots@.service" "$pkgdir/usr/lib/systemd/system/labots@.service"
  mkdir -p "$pkgdir/var/lib/labots"
  cp -r "$srcdir/labots/bots" "$pkgdir/var/lib/labots/bots"
}
