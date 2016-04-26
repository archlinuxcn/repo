# Maintainer wicastC <wicastchen at hotmail dot com>

pkgname=python-lda
_name=lda
pkgver=1.0.3
pkgrel=1
pkgdesc="Topic modeling with latent Dirichlet allocation"
arch=("i686" "x86_64")
url="https://github.com/ariddell/lda/"
license=(MPLv2)
depends=("python" "python-pbr")
makedepends=("python-setuptools")
source=("http://pypi.python.org/packages/source/l/${_name}/${_name}-${pkgver}.tar.gz")
md5sums=("17efa4f18d1aa5b08997db709d7ab068")

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py build
}

package() {
    msg "Install..."
    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py install --root="${pkgdir}" || return 1
}
