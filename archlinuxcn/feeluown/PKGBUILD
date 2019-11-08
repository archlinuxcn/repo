# Maintainer: Bruce Zhang <zttt183525594@gmail.com>
_pkgname=feeluown
pkgname=feeluown
pkgver=3.1.1
pkgrel=1
pkgdesc="FeelUOwn Music Player"
arch=('any')
url="https://github.com/cosven/FeelUOwn"
license=('GPL3')
depends=('python-quamash' 'python-pyqt5' 'mpv' 'python-beautifulsoup4' 'python-marshmallow' 'python-pycryptodome' 'python-requests' 'python-mutagen' 'python-fuzzywuzzy' 'python-opengl' 'python-janus')
makedepends=('python-setuptools' 'python-pip')
_name=${pkgname#python-}
source=(
	"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz" 
	"feeluown.desktop"
)
sha256sums=('4e17bf140660406708629b182551b7f856f421be52cf15b080222144515446a3'
            '2b2716ee280c1eeba6d20227173e1325c64a4a3fcb200e038e7777de5cddaebb')

build() {
	cd "$pkgname-$pkgver"
	LANG=en_US.UTF-8 python setup.py build
}

package() {
	cd "$pkgname-$pkgver"
	LANG=en_US.UTF-8 python setup.py install --root="$pkgdir/" --optimize=1 --skip-build

	# Install battery packages
	PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps fuo-local
	PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps fuo-xiami
	PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps fuo-netease
	PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps fuo-qqmusic

	install -D -m644 "$srcdir/$pkgname-$pkgver/feeluown/feeluown.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/feeluown.png"
	install -D -m644 "$srcdir/feeluown.desktop" "$pkgdir/usr/share/applications/feeluown.desktop"
}
