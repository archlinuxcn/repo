# Maintainer: Tobias Bachmann <tobachmann@gmx.de>
pkgname=python-opengl-accelerate
pkgver=3.1.9
pkgrel=1
pkgdesc="This is the Cython-coded accelerator module for PyOpenGL 3.x"
_name=PyOpenGL-accelerate
__name=pyopengl_accelerate
arch=('any')
url=""
license=('BSD')
groups=()
depends=('python' 'python-opengl' 'cython')
makedepends=(python-build python-installer python-wheel)
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
#source=("https://github.com/mcfletch/${_name}/archive/${_commit}.tar.gz")
source=($pkgname-$pkgver.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$__name-$pkgver.tar.gz)
sha256sums=('85957c7c76975818ff759ec9243f9dc7091ef6f373ea37a2eb50c320fd9a86f3')

build() {
  cd "$srcdir/${__name}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/${__name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}

# vim:set ts=2 sw=2 et:
