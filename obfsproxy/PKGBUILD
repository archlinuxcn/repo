# Maintainer: mutantmonkey <aur@mutantmonkey.in>
# Contributor: Techlive Zheng <techlivezheng@gmail.com>
pkgname=obfsproxy
pkgver=0.2.13
pkgrel=1
pkgdesc="A pluggable transport proxy written in Python"
arch=('any')
url="https://pypi.python.org/pypi/obfsproxy"
license=('BSD')
depends=('python2>=2.7' 'python2-crypto' 'python2-pyptlib>=0.0.6' 'twisted'
         'python2-yaml' 'python2-setuptools')
optdepends=('python2-gmpy2: speed up some cryptographic operations')
conflicts=('pyobfsproxy' 'obfsproxy-git')
options=(!emptydirs)
source=("https://pypi.python.org/packages/source/o/obfsproxy/obfsproxy-${pkgver}.tar.gz"{,.asc})
sha256sums=('1e26c2faef1cfcf856ddf60e9647058a7c78fb0d47f05b58a0f847ed7cc41a66'
            'SKIP')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"

  # argparse is part of python 2.7+, so we can remove it from install_requires
  sed -i "/'argparse',/d" setup.py
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
