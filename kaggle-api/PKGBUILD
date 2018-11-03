# Maintainer: asermax <asermax@gmail.com>
_branch='a3ac9a930d46d626e1f504ddeebda55129a925de'

pkgname=kaggle-api
pkgver=1.5.0
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

md5sums=('670f4c5681006d649a7634c0fb77b1a4')

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
