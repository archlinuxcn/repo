# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=python2-newrelic
pkgver=2.56.0.42
pkgrel=1
pkgdesc="Python agent for the New Relic web application performance monitoring service."
arch=('i686' 'x86_64')
url="http://newrelic.com/docs/python/new-relic-for-python"
license=("custom")
depends=('python2')
makedepends=('python2-setuptools')
source=("http://download.newrelic.com/python_agent/release/newrelic-${pkgver}.tar.gz"
        LICENSE)
sha512sums=('5a535b76619c54c4345ba9d7cd17a70fec7330b19ecbeaf736ddbde169777b227823eb6eefe5c50570fd0b9bac18c3bb0cdd2f12e7dbfc65e6a48d7b77e85f31'
            'a9d8e4cf71c6bbb372aeb62fca5ced760ea00f406938d28cff57b9d9097abff1580649585f760e0131d59ff764aa2f5249b0ef19233981800211ede66633402b')

package() {
  cd newrelic-$pkgver
  python2 setup.py install -O1 --root="$pkgdir"
  install -Dm644 "$srcdir/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
