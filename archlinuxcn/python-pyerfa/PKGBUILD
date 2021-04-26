# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-pyerfa
_name=${pkgname#python-}
pkgver=1.7.3
pkgrel=1
pkgdesc="Python wrapper for the ERFA library "
arch=('i686' 'x86_64')
url="https://github.com/liberfa/pyerfa"
license=('BSD')
depends=('python>=3.6' 'python-numpy>=1.16.0' 'erfa>=1.7.3')
makedepends=('cython' 'python-jinja' 'python-pip')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha512sums=('fe20665cfed8b921c8887e37259efe8eadd7ae34fbec4cac62a622c55afb98145deb548435c9bdbf6506c74261087234dd54188f8f02ceb446bfe9ccf4cac1f7')

build() {
  cd "${srcdir}/pyerfa-${pkgver}"

  PYERFA_USE_SYSTEM_LIBERFA=1 CONFIG_FILE=/dev/null pip wheel --no-cache-dir --no-deps --wheel-dir="${srcdir}/pyerfa-${pkgver}" .
}

package() {
  cd "${srcdir}/pyerfa-${pkgver}"

  install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}/"
  install -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}/" licenses/*
  PYERFA_USE_SYSTEM_LIBERFA=1 PIP_CONFIG_FILE=/dev/null pip install --isolated --ignore-installed --no-deps --no-warn-script-location --root="${pkgdir}" "$(ls ./*.whl 2> /dev/null)"
  rm "${pkgdir}"/usr/lib/python*/site-packages/pyerfa-"${pkgver}".dist-info/direct_url.json
}
