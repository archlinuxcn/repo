# Maintainer: Jason Stryker <public at jasonstryker dot com>

pkgname=protontricks
pkgver=1.2.5
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
sha512sums=('920eeb4504aac1cdc640704b673b1014705adbacebf1ef056b69e33c464515c1d8be6b815a3305efb70396a7935affed43c04c779818e3f0693b44bfe3c4e305')

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
