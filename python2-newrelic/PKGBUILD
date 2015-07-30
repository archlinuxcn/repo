# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=python2-newrelic
pkgver=2.54.0.41
pkgrel=1
pkgdesc="Python agent for the New Relic web application performance monitoring service."
arch=('i686' 'x86_64')
url="http://newrelic.com/docs/python/new-relic-for-python"
license=("custom")
depends=('python2')
makedepends=('python2-setuptools')
source=("http://download.newrelic.com/python_agent/release/newrelic-${pkgver}.tar.gz"
        LICENSE)
sha512sums=('3293410cb5b4306db93ad10bc3b88ac42fc771164aaac491c56817c97ded7119bac0aff45d1fa2813f3f3736f9879c054849e8912d5c999b7e1f18a0ab4e38be'
            'a9d8e4cf71c6bbb372aeb62fca5ced760ea00f406938d28cff57b9d9097abff1580649585f760e0131d59ff764aa2f5249b0ef19233981800211ede66633402b')

package() {
  cd newrelic-$pkgver
  python2 setup.py install -O1 --root="$pkgdir"
  install -Dm644 "$srcdir/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
