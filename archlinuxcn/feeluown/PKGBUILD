# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
_pkgname=feeluown
pkgname=feeluown
pkgver=3.5a0
pkgrel=5
pkgdesc="FeelUOwn Music Player"
arch=('any')
url="https://github.com/cosven/FeelUOwn"
license=('GPL3')
depends=('python-qasync' 'python-pyqt5' 'mpv' 'python-opengl' 'python-janus' 'python-requests')
makedepends=('python-setuptools' 'python-pip')
optdepends=(
	'feeluown-local'
	'feeluown-netease'
	'feeluown-kuwo'
	'feeluown-xiami'
	'feeluown-qqmusic'
)
_name=${pkgname#python-}
source=(
	"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
	"feeluown.desktop"
)
sha256sums=('434599e87ecc77015be1ab800b23ddc53ea73ace7474773173ef0d6ea87101cf'
            'f093cccd74e29115782b30fcda28fb0c3b935091673b50882b332c934ed56065')
groups=('feeluown-full')

build() {
	cd "$pkgname-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$pkgname-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build
	install -D -m644 "$srcdir/$pkgname-$pkgver/feeluown/feeluown.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/feeluown.png"
	install -D -m644 "$srcdir/feeluown.desktop" "$pkgdir/usr/share/applications/FeelUOwn.desktop"
}
