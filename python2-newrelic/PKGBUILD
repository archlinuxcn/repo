# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=python2-newrelic
pkgver=2.58.2.45
pkgrel=1
pkgdesc="Python agent for the New Relic web application performance monitoring service."
arch=('i686' 'x86_64')
url="http://newrelic.com/docs/python/new-relic-for-python"
license=("custom")
depends=('python2')
makedepends=('python2-setuptools')
source=("http://download.newrelic.com/python_agent/release/newrelic-${pkgver}.tar.gz"
        LICENSE)
sha512sums=('df992e919c07877c25b060fb7d203736d9e82d55a888f6daef0cfc73446c2955eda4d85fbc6e71659d9b2b04def55567784b700aa5f3ac785b98fb812e5126e2'
            'a9d8e4cf71c6bbb372aeb62fca5ced760ea00f406938d28cff57b9d9097abff1580649585f760e0131d59ff764aa2f5249b0ef19233981800211ede66633402b')

package() {
  cd newrelic-$pkgver
  python2 setup.py install -O1 --root="$pkgdir"
  install -Dm644 "$srcdir/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
