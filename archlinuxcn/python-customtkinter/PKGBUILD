# Contributor: Pellegrino Prevete <pellegrinoprevete@gmail.com>
# Maintainer: Neko_Rikka <yjzyl9008 at gmail dot com>


_name=CustomTkinter
pkgname=python-customtkinter
pkgver=5.2.2
pkgrel=2
pkgdesc="A modern and customizable python UI-library based on Tkinter"
arch=('any')
url="https://github.com/TomSchimansky/CustomTkinter"
license=('MIT')
depends=('python'
         'python-darkdetect' 
         'python-packaging' 
         'python-pillow' 
         'python-typing_extensions'
         'tk')
provides=('python-customtkinter')
conflicts=('python-customtkinter-git')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('310010366d2c6fba53045cccc45117b4bdfaeaebaa090fed2e4fc99db805a05ea99c9f4f7d32b5129694036c77b6f442b43ef5a79b7d5fa0de19f8ffbb6fb646')

build() {
  cd "${_name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm0644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm0644 Readme.md "${pkgdir}/usr/share/doc/${pkgname}/README" 
}

# vim:set sw=2 ts=2 et:
