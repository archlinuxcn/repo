# Contributor: Médéric Boquien <mboquien@free.fr>
# Maintainer: Médéric Boquien <mboquien@free.fr>
pkgname=python-pyerfa
pkgver=1.7.1.1
pkgrel=3
pkgdesc="Python wrapper for the ERFA library "
arch=('i686' 'x86_64')
url="https://github.com/liberfa/pyerfa"
license=('BSD')
depends=('python>=3.6' 'python-numpy>=1.16.0' 'erfa>=0.17')
makedepends=('cython' 'python-jinja' 'python-pip')
source=("https://files.pythonhosted.org/packages/3b/37/0ff81021f6405e4f6f627bb4aed32d22569fe016376dccee14e5eca947d1/pyerfa-${pkgver}.tar.gz")
sha512sums=('59c2dceed6ef5b1ece618742dd0084b729cce8eb52f903dff2aad009fa0f495defb4511688da0a5203ed5900d041a552fbe50668ddac0c3a6bb3fd6d34d089bb')

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
