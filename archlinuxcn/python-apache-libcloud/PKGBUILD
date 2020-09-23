# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Alasdair Haswell <ali at arhaswell dot co dot uk>

_name=apache-libcloud
pkgname=python-apache-libcloud
pkgver=3.2.0
pkgrel=2
pkgdesc="standard Python library that abstracts away differences among multiple cloud provider APIs"
arch=('any')
url="https://libcloud.apache.org"
license=('Apache')
depends=('python-requests')
makedepends=('python-setuptools')
optdepends=(
  'python-paramiko: alternative SSH backend'
  'libvirt-python: for libvirt compute driver'
)
checkdepends=('python-mock' 'python-pytest' 'openssh' 'python-requests-mock' 'python-pyopenssl'
              'python-paramiko' 'libvirt-python')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz{,.asc}
        $_name-issue1490.patch::https://github.com/apache/libcloud/commit/21381965241738375cc5d6d14398cae05abb6aeb.patch)
sha512sums=('5a1b7ffc3db8a315c4e5c34cf0543e04ceb4bd37356fb486b55dca07caf7544e7b304ef522b5f1a16ad3b978d50867c6cb9bad031b348c7423f2d798181b381e'
            'SKIP'
            '19303daf51e4aa5cc1111f4b86353051bf6cab3c89de1ff4c9490d56e8a532ee4bad8d59c63982f930538ac15c76c90b0baf0bc8c165e3105eeabed6056fa2df')
# possible keys: https://downloads.apache.org/libcloud/KEYS
validpgpkeys=('3ACBB4086C01F7376628088CAB4A19AE1CE85744'  # Anthony Shaw <anthonyshaw@apache.org>
              '35542BB9C0C01D5E5478BADE6A61AF8545413203'  # Quentin Pradet <quentin.pradet@gmail.com>
              '997828DC62F759CEA189D65E2C0754B2CE0692F3') # Tomaz Muraus <tomaz@apache.org>

prepare() {
  cd $_name-$pkgver
  patch -Np1 -i ../$_name-issue1490.patch
}

build() {
  cd $_name-$pkgver
  python setup.py build
}

check() {
  cd $_name-$pkgver
  cp libcloud/test/secrets.py-dist libcloud/test/secrets.py
  pytest -rs libcloud/test
  rm libcloud/test/secrets.py
}

package() {
  cd $_name-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
