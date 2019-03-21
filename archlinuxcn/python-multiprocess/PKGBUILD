pkgname=python-multiprocess
pkgver=0.70.7
pkgrel=1
pkgdesc="better multiprocessing and multithreading in python"
url="http://trac.mystic.cacr.caltech.edu/project/pathos/wiki.html"
arch=('i686' 'x86_64')
license=('BSD')
makedepends=('python-setuptools')
depends=('python-dill')
source=("https://github.com/uqfoundation/multiprocess/archive/multiprocess-${pkgver}.tar.gz")
sha256sums=('225526007f02469eb8d0baabcd397058c6a68cf33ba231fd3ded9de3c43941fd')

build() {
  cd "${srcdir}"/multiprocess-multiprocess-$pkgver
  python setup.py build
}

package() {
  cd "${srcdir}/multiprocess-multiprocess-$pkgver"
  python setup.py install --root=${pkgdir} --optimize=1
}


