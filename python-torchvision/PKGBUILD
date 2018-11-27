# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: Jean Lucas <jean@4ray.co>
# Based on python-torchvision-git; original contributors:
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>

pkgname=python-torchvision
pkgver=0.2.1
pkgrel=2
pkgdesc='Datasets, transforms, and models specific to computer vision'
arch=(any)
url=https://pytorch.org
license=(BSD)
depends=(python-numpy python-pillow python-pytorch python-six)
makedepends=(python-setuptools)
checkdepends=(python-pytest python-scipy)
source=("torchvision-$pkgver.tar.gz"::"https://github.com/pytorch/vision/archive/v$pkgver.tar.gz"
        fix-tests.patch::https://github.com/pytorch/vision/commit/4db0398a2b02aae790013efbc868f2d795eb2ef7.patch)
sha512sums=('224a07c24b2d990a2b396a7d499975347e45eccf501fd75bf528e4d5d92bd4c8f06382b8f3012263378a5e72271d3f9df4bc40248ec7fa218d2913355ed96740'
            '624bbb9e96ccab3e7884a362015ee7ce159cb24e3fbb1d62575097658f494a7f7c21c511dc4946f808ba42143e9ba7cef9640e6aec234d36a3b48217a69d873c')

prepare() {
  cd vision-$pkgver
  patch -Np1 -i ../fix-tests.patch
}

build() {
  cd vision-$pkgver
  python setup.py build
}

check() {
  cd vision-$pkgver
  PYTHONPATH=. pytest -v test
}

package() {
  cd vision-$pkgver
  python setup.py install --root=$pkgdir --optimize=1 --skip-build
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
