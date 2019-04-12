# Maintainer: Jason Stryker <public at jasonstryker dot com>

pkgname=protontricks
pkgver=1.2.1
pkgrel=1
pkgdesc="A simple wrapper that does winetricks things for Proton enabled games."
arch=('any')
url="https://github.com/Matoking/protontricks"
license=('GPL3')
depends=('python' 'python-vdf>=2.4' 'winetricks')
optdepends=('zenity: GUI for GNOME desktop')
makedepends=('git' 'python-setuptools')
provides=("protontricks")
conflicts=('protontricks-git')
source=("${url}/archive/${pkgver}.tar.gz")
sha512sums=('026885ba3c6c145e54292b7b806395533bf2a818a9c2a9c4a912664c5bc7f7220bf5cffbac7957985887535962672b796ec8ecddc12ad3c9c08342f67338c8e7')

build() {
  cd "${srcdir}/protontricks-${pkgver}"

  python3 setup.py build
}

package() {
  cd "${srcdir}/protontricks-${pkgver}"

  python3 setup.py install --root="$pkgdir" --optimize=1 || return 1

  install -D -m 0644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}

# vim:set ts=2 sw=2 et:
