# Maintainer: Robert Ransom <rransom.8774@gmail.com>
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: William Rea <sillywilly@gmail.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=paman
pkgver=0.9.4
pkgrel=5
pkgdesc="Inspects and alters the state of the PulseAudio sound server"
arch=('i686' 'x86_64')
url="http://0pointer.de/lennart/projects/paman"
license=('GPL')
depends=('libglademm' 'pulseaudio')
changelog=ChangeLog
source=(http://0pointer.de/lennart/projects/paman/${pkgname}-${pkgver}.tar.gz)
md5sums=('4a77b129b0de8d261f2794ce3db518cc')
sha1sums=('d51d390a00222a51580c23c3d26547689b6d767b')
sha256sums=('9034087c4dd6caa19f6b59ba3b80c377b9dbff395fc1f94f890f2ba1173a5041')
sha384sums=('b75a75d6ad80cc17c61a772eb0b63279f400c87016e844be008d402c6a741e973b8dbfd76e81616d719e5f59968decc9')
sha512sums=('dc135b3cd14966a86ae22c3fc514c02f5a9fcb8f1eccadc37c52eb620a06edfe3a0f75360fcaa44e57c058812a673aa9d4e22572002c1bf999e40ccfd7350b44')

build() {
	cd ${srcdir}/paman-${pkgver} || return 1
	./configure --prefix=/usr --disable-lynx || return 1
	make || return 1
}

package() {
	cd ${srcdir}/paman-${pkgver} || return 1
	make DESTDIR=${pkgdir} install || return 1
}
