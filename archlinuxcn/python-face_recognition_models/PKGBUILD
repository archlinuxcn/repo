# Maintainer: Philip Goto <philip.goto@gmail.com>

_pkgname=face_recognition_models
pkgname=python-$_pkgname
pkgver=0.3.0
pkgrel=1
pkgdesc="Trained models for the face_recognition python library"
url="https://github.com/ageitgey/face_recognition_models"
makedepends=('python-setuptools')
license=(MIT)
arch=(any)
source=("https://files.pythonhosted.org/packages/cf/3b/4fd8c534f6c0d1b80ce0973d01331525538045084c73c153ee6df20224cf/face_recognition_models-0.3.0.tar.gz")
sha256sums=(b79bd200a88c87c9a9d446c990ae71c5a626d1f3730174e6d570157ff1d896cf)

build(){
    cd $srcdir/$_pkgname-$pkgver
    python setup.py build
}

package(){
    cd $srcdir/$_pkgname-$pkgver
    python setup.py install --skip-build --root="$pkgdir" --optimize=1
}
