# Maintainer: Jason Stryker <public at jasonstryker dot com>
# Maintainer: Konstantin Liberty <jon9097 at gmail dot com>

pkgname=protontricks
pkgver=1.11.1
pkgrel=1
pkgdesc="A simple wrapper that does winetricks things for Proton enabled games."
arch=('any')
url="https://github.com/Matoking/protontricks"
license=('GPL-3.0-or-later')
depends=('python' 'python-vdf' 'winetricks' 'python-setuptools' 'python-pillow')
optdepends=(
  'yad: GUI for game selection', 
  'zenity: GUI for winetricks'
)
makedepends=('git' 'python-setuptools-scm' 'python-build' 'python-installer' 'python-wheel')
provides=("protontricks")
conflicts=('protontricks-git')
source=("git+${url}.git#tag=${pkgver}")
sha512sums=('SKIP')

build() {
  cd "${srcdir}/${pkgname}"

  python -m build --wheel
}

package() {
  cd "${srcdir}/${pkgname}"

  python -m installer --destdir="$pkgdir" dist/*.whl

  install -D -m 0644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}

# vim:set ts=2 sw=2 et:
