# Maintainer: Salvador Pardiñas <darkfm@vera.com.uy>
pkgname=woeusb-git
pkgver=3.2.9.r4.ge2a7468
pkgrel=1
pkgdesc="A Linux program to create Windows USB stick installer from a real Windows DVD or an image"
arch=('x86_64')
url="https://github.com/slacka/WoeUSB"
license=('GPL3')
groups=()
depends=('wxgtk3' 'grub' 'dosfstools'
		'parted' 'wget' 'ntfs-3g')
optdepends=('gksu')
makedepends=('git')
provides=("woeusb")
conflicts=("")
replaces=()
backup=()
options=()
install=
source=('git+https://github.com/slacka/WoeUSB.git')
noextract=()
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/WoeUSB"
  git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g' | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
	cd "$srcdir/WoeUSB"
	autoreconf --force --install
}

build() {
	cd "$srcdir/WoeUSB"
	autoconf
	./configure --with-wx-config=wx-config-gtk3
	make
}

package() {
	cd "$srcdir/WoeUSB"
	make DESTDIR="$pkgdir/" prefix="/usr/" install
}
