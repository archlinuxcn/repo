# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgbase=python-qiniu
pkgname=(python-qiniu python2-qiniu)
_pkgname=qiniu
pkgver=7.0.3
pkgrel=1
pkgdesc="Qiniu Resource Storage SDK for Python"
arch=('any')
url='https://github.com/qiniu/python-sdk'
license=('MIT')
makedepends=('python-setuptools' 'python2-setuptools')
source=("https://pypi.python.org/packages/source/q/qiniu/qiniu-$pkgver.tar.gz"
        LICENSE)
sha512sums=('9a0f8bc71617579880cb8946d999a3188094470746dcc42791f8cbd5d1e1436d5bd32fbadab649d42d6757fac85695e5ddc8e34fa4d5e10ea69bc06c537ccfc6'
            '4fbb1090b3ee0d230d40b45db7bcd164873872d1860bd83b51197ed5d03e9d4be7785a400f1d314d6e3c0a6fcba7e1afdf3fdab04ae9970df59f96b18862c529')

prepare() {
  cp -a ${_pkgname}-$pkgver{,-py2}
}

package_python-qiniu() {
  depends=('python-requests')

  cd ${_pkgname}-$pkgver
  python setup.py install -O1 --root "${pkgdir}"

  install -Dm644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_python2-qiniu() {
  depends=('python2-requests')

  cd ${_pkgname}-$pkgver-py2
  python2 setup.py install -O1 --root "${pkgdir}"

  install -Dm644 ../LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # Don't conflict with python 3.x version
  mv "$pkgdir"/usr/bin/qiniupy{,2}
}
