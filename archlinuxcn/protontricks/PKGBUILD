# Maintainer: Jason Stryker <public at jasonstryker dot com>

pkgname=protontricks
pkgver=1.10.1
pkgrel=1
pkgdesc="A simple wrapper that does winetricks things for Proton enabled games."
arch=('any')
url="https://github.com/Matoking/protontricks"
license=('GPL3')
depends=('python' 'python-vdf' 'winetricks' 'python-setuptools')
optdepends=(
  'yad: GUI for game selection', 
  'zenity: GUI for winetricks'
)
makedepends=('git' 'python-setuptools-scm')
provides=("protontricks")
conflicts=('protontricks-git')
source=("git+${url}.git#tag=${pkgver}")
sha512sums=('SKIP')

build() {
  cd "${srcdir}/${pkgname}"

  python3 setup.py build
}

package() {
  cd "${srcdir}/${pkgname}"

  python3 setup.py install --root="$pkgdir" --optimize=1 || return 1

  install -D -m 0644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}

# vim:set ts=2 sw=2 et:
