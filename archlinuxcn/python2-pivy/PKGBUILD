# Maintainer: Florian Pritz <bluewind@xinu.at>
# Contributor: Christian Hesse <mail@eworm.de>
# Contributor/Submitter: <p.janouch@gmail.com>

pkgname=python2-pivy
pkgver=20101207
pkgrel=1
pkgdesc="Coin binding for Python"
arch=('i686' 'x86_64')
url="http://pivy.coin3d.org"
license=('custom')
depends=('python2' 'soqt')
makedepends=('swig' 'mercurial')
source=("pivy::hg+https://bitbucket.org/Coin3D/pivy#tag=pivy-$pkgver")
md5sums=('SKIP')
replaces=(pivy)
provides=(pivy)

package() {
	cd "$srcdir/pivy"

	python2 setup.py install --root="${pkgdir}"

	install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

