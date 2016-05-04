# Maintainer: Felix Yan <felixonmars@archlinux.org>

pkgname=python2-newrelic
pkgver=2.64.0.48
pkgrel=1
pkgdesc="Python agent for the New Relic web application performance monitoring service."
arch=('i686' 'x86_64')
url="http://newrelic.com/docs/python/new-relic-for-python"
license=("custom")
depends=('python2')
makedepends=('python2-setuptools')
source=("http://download.newrelic.com/python_agent/release/newrelic-${pkgver}.tar.gz"
        LICENSE)
sha512sums=('b51442bd90067b33e326b686940feede798e4e15b455f1bf138eb66e11371ff27c2bb8bd807c419e0f9c844c2c8573905c89d3362030693db6e2a4404641a0ca'
            'a9d8e4cf71c6bbb372aeb62fca5ced760ea00f406938d28cff57b9d9097abff1580649585f760e0131d59ff764aa2f5249b0ef19233981800211ede66633402b')

package() {
  cd newrelic-$pkgver
  python2 setup.py install -O1 --root="$pkgdir"
  install -Dm644 "$srcdir/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
