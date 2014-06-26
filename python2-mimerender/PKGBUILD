# Maintainer: Felix Yan <felixonmars@gmail.com>

pkgname=python2-mimerender
_pkgname=mimerender
pkgver=0.5.4
pkgrel=1
pkgdesc="Transparently select a render function for an HTTP request handler's result"
arch=('any')
url="https://github.com/martinblech/mimerender"
license=('MIT')
depends=('python2' 'python2-mimeparse>=0.1.4')
conflicts=()
replaces=()
source=("https://github.com/martinblech/$_pkgname/archive/v$pkgver.tar.gz")

package() {
  cd "${srcdir}/$_pkgname-$pkgver"
  python2 setup.py install -O1 --root "${pkgdir}"
}

sha512sums=('4665eeb1a8f6e80183e51c72cd03187eb7de96c66e9967736a7f5e7054da7c499b2865e120343646fd6ac5b3964a32f296f9de1ed191b4ab6f946ab2b4bdb9f7')
sha512sums=('4616569bb73772ad02b481edfb90cdc1eb46b888241efed1726b1f6edcbaa6a9145d51450b2170e01121a20fa5407e9f5f415e0d5620875baddae17da60f0252')
