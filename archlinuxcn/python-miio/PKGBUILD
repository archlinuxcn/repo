# Maintainer: Patrick Lühne <patrick-arch@luehne.de>

pkgname=python-miio
pkgver=0.5.0.1
pkgrel=1
pkgdesc="Python library & console tool for controlling Xiaomi smart appliances"
url="https://github.com/rytilahti/python-miio"
arch=('any')
license=('GPL3')
depends=('python>=3.6' 'python-appdirs' 'python-attrs' 'python-click>=7' 'python-construct' 'python-cryptography' 'python-netifaces' 'python-pytz' 'python-tqdm' 'python-zeroconf')
optdepends=('python-android-backup-tools: Android backup extraction support')
source=("https://github.com/rytilahti/${pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('d82c4d52c7590892f7322d2d1a428a8dcb4843085a42374458bdfeeeacfc73a0f159d1a3bcc0612a5740d61dca472bbb022f912d20cf07ba2e1f9df6fdc52b20')

build() {
	cd ${pkgname}-${pkgver}
	python setup.py build
}

package() {
	cd ${pkgname}-${pkgver}
	python setup.py install --prefix=/usr --root="${pkgdir}"
	install -D -m644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
