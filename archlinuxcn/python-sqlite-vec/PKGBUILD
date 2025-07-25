# Maintainer: Mohamed Amine Zghal (medaminezghal) <medaminezghal at outlook dot com>

_name=sqlite-vec
pkgname=python-${_name}
pkgver=0.1.6
pkgrel=1
pkgdesc=''
arch=(any)
url='https://pypi.org/project/sqlite-vec/'
license=('MIT OR Apache-2.0')
source_x86_64=("https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/${_name//-/_}-$pkgver-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux1_x86_64.whl")
source_aarch64=("https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/${_name//-/_}-$pkgver-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl")
sha256sums_x86_64=('823b0493add80d7fe82ab0fe25df7c0703f4752941aee1c7b2b02cec9656cb24')
sha256sums_aarch64=('7b0519d9cd96164cd2e08e8eed225197f9cd2f0be82cb04567692a0a4be02da3')
depends=('python' 'glibc')
makedepends=('python-installer')

package() {
  python -m installer --destdir="$pkgdir" *.whl
}
