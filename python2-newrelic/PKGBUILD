# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=python2-newrelic
pkgver=2.52.0.40
pkgrel=1
pkgdesc="Python agent for the New Relic web application performance monitoring service."
arch=('i686' 'x86_64')
url="http://newrelic.com/docs/python/new-relic-for-python"
license=("custom")
depends=('python2')
makedepends=('python2-setuptools')
source=("http://download.newrelic.com/python_agent/release/newrelic-${pkgver}.tar.gz"
        LICENSE)

package() {
  cd newrelic-$pkgver
  python2 setup.py install -O1 --root="$pkgdir"
  install -Dm644 "$srcdir/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

sha512sums=('0cd6c54b45fb0d33c3eee325666256ab2ad3f04815ac80bf8f9974cf934ab708f29ed58b7d71f7866e4dcf8295ff3f562e47ddaccdc6293f639db7b28585ae24'
            'a9d8e4cf71c6bbb372aeb62fca5ced760ea00f406938d28cff57b9d9097abff1580649585f760e0131d59ff764aa2f5249b0ef19233981800211ede66633402b')
