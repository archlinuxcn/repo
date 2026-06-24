# Contributor: Pellegrino Prevete <pellegrinoprevete@gmail.com>
# Maintainer: Neko_Rikka <yjzyl9008 at gmail dot com>


_name=CustomTkinter
pkgname=python-customtkinter
pkgver=6.0.0
pkgrel=1
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
sha512sums=('eba15d66a8988958c6d6805f18260c11aeaa77d6f440d89a40fb9b0d61a656e3bc748e43b414b891be1ae42a9fc6eea3d5ee32e07ce952a1a3f66dea06b83199')

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
