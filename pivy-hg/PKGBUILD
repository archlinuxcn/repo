# Maintainer: Christian Hesse <mail@eworm.de>
# Contributor/Submitter: <p.janouch@gmail.com>

pkgname=pivy-hg
pkgver=609.8eab90908f2a
pkgrel=1
pkgdesc="Coin binding for Python"
arch=('i686' 'x86_64')
url="http://pivy.coin3d.org"
license=('custom')
depends=('python2' 'soqt')
makedepends=('swig' 'mercurial')
provides=('pivy')
conflicts=('pivy')
source=('pivy::hg+https://bitbucket.org/Coin3D/pivy')

pkgver() {
	cd pivy/

	hg tip | head -n1 | tr -d ' ' | cut -d: --output-delimiter=. -f 2,3
}

package() {
	cd pivy/

	python2 setup.py install --root="${pkgdir}"

	install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

sha256sums=('SKIP')
