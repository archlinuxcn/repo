# Maintainer: asermax <asermax@gmail.com>
_branch='bd75dbfc4dbfb19a5d8538f157acf8b882249320'

pkgname=kaggle-api
pkgver=1.5.1.1
pkgrel=1
pkgdesc='Kaggle API CLI'

arch=('any')
url="http://kaggle.com/"
license=('Apache')

depends=(
  'python'
  'python-urllib3'
  'python-six'
  'python-certifi'
  'python-dateutil'
  'python-requests'
  'python-tqdm'
  'python-slugify'
)
makedepends=(
  'python-setuptools'
)

source=(
  "https://github.com/Kaggle/kaggle-api/archive/${_branch}.tar.gz"
)

md5sums=('76b306e54e4a7295d383483babb20283')

prepare() {
  cd "$srcdir"/kaggle-api-$_branch
  # remove urllib3 version restriction
  sed -e '/urllib3/d' \
      -e "s/,<.*'/'/" \
      -i setup.py
}

package() {
  cd "${pkgname}-${_branch}"

  # Python setup
  python setup.py install --root="${pkgdir}"/ --prefix=/usr --optimize=1

  # License
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE
}
