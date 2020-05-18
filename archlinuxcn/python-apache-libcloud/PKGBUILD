# Maintainer:
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Daniel Wallace <danielwallace at gtmanfred dot com>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Alasdair Haswell <ali at arhaswell dot co dot uk>

_name=apache-libcloud
pkgname=python-apache-libcloud
pkgver=3.0.0
pkgrel=1
pkgdesc="standard Python library that abstracts away differences among multiple cloud provider APIs"
arch=('any')
url="https://libcloud.apache.org"
license=('Apache')
depends=('python-requests')
makedepends=('python-setuptools')
checkdepends=('python-mock' 'python-pytest-runner' 'openssh' 'python-requests-mock' 'python-pyopenssl')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz{,.asc})
sha512sums=('c04e55e0b7b8943250fd3b291d7aa5e2aa67c4460405f8cb7f527a2c95e045dcd4ce3785ad83fe8284e49d761c84c3f243f491e59c94de463e2079d77da09332'
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
  python setup.py test
  rm libcloud/test/secrets.py
}

package() {
  cd $_name-$pkgver
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
