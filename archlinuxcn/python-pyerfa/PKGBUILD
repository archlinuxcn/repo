# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-pyerfa
_name=${pkgname#python-}
pkgver=2.0.0
pkgrel=1
pkgdesc="Python wrapper for the ERFA library "
arch=('i686' 'x86_64')
url="https://github.com/liberfa/pyerfa"
license=('BSD')
depends=('python>=3.6' 'python-numpy>=1.16.0' 'erfa>=1.7.3')
makedepends=('cython' 'python-jinja' 'python-pip')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha512sums=('5f46708c73c09760db55dcfadf7e18ae5510c5edf0ed5e9607b18d67b28509f2b62366ff19099a0008c93591bc56d85472ce19a2461fc626977c559ec6684bae')

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
