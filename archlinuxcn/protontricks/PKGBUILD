# Maintainer: Jason Stryker <public at jasonstryker dot com>

pkgname=protontricks
pkgver=1.3
pkgrel=2
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
sha512sums=('eb99ca9548cde2fa73705b838b7cb93c7b76460a9d96bb69aeaad772f304f37c9e0eb2481e9123145825a7379bd9d998a0fbeb52f77adf663d5c49bcff61be20')

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
