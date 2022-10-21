# Maintainer: ValHue <vhuelamo at gmail dot com>
# https://github.com/ValHue/AUR-PKGBUILDs
# Maintainer: qwivan <ivanngonline@hotmail.com>

pkgname="pushbullet-cli"
pkgver="1.2.2"
pkgrel="2"
pkgdesc="Command line tool for controlling PushBullet."
arch=('i686' 'x86_64')
url="https://github.com/GustavoKatel/pushbullet-cli"
license=('MIT')
depends=('python-pushbullet.py' 'python-click' 'python-keyrings-alt' 'python-magic')
provides=("${pkgname}")

source=("https://github.com/GustavoKatel/${pkgname}/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('bede70a79c94776d2e935466482056db59eaeea680118072392ddf1ae56d1392')

build() {
	cd "${pkgname}-${pkgver}"
    python setup.py build
}

package() {
	cd "${pkgname}-${pkgver}"
	python setup.py install --root="${pkgdir}" --optimize=1
}

# vim:set ts=4 sw=2 ft=sh et:
