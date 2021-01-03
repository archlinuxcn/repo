# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Alasdair Haswell <ali at arhaswell dot co dot uk>

_name=apache-libcloud
pkgname=python-apache-libcloud
pkgver=3.3.0
pkgrel=1
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
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz{,.asc})
sha512sums=('051827f37e80b4481b9270db66b1875f408d10a2600025c0431998dc87d4e177c734e4ddc7951914dc21b4b5e520f4c1c84d9fdd005bc98162af58985be52366'
            'SKIP')
# possible keys: https://downloads.apache.org/libcloud/KEYS
validpgpkeys=('3ACBB4086C01F7376628088CAB4A19AE1CE85744'  # Anthony Shaw <anthonyshaw@apache.org>
              '35542BB9C0C01D5E5478BADE6A61AF8545413203'  # Quentin Pradet <quentin.pradet@gmail.com>
              '997828DC62F759CEA189D65E2C0754B2CE0692F3') # Tomaz Muraus <tomaz@apache.org>

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
