_pkgbase=r8168
pkgname=${_pkgbase}-dkms
pkgver=8.046.00
pkgrel=3
pkgdesc="A kernel module for Realtek 8168 network cards"
url="http://www.realtek.com.tw"
license=("GPL")
arch=('i686' 'x86_64')
depends=('glibc' 'dkms')
conflicts=("${_pkgbase}")
optdepends=('linux-headers: Needed for build the module for Arch kernel'
	'linux-lts-headers: Needed for build the module for LTS Arch kernel'
	'linux-zen-headers: Needed for build the module for ZEN Arch kernel')
source=(https://github.com/mtorromeo/r8168/archive/$pkgver/r8168-$pkgver.tar.gz
#source=(https://az695102.vo.msecnd.net/rtdrivers/cn/nic/0012-r8168-8.046.00.tar.bz2
        dkms.conf)
install=r8168-dkms.install

#prepare() {
#	cd "r8168-$pkgver"
#	patch -p1 -i "$srcdir/linux-4.15-2.patch"
#}
 

package() {
	install -Dm644 dkms.conf "${pkgdir}/usr/src/${_pkgbase}-${pkgver}/dkms.conf"

	sed -e "s/@PKGNAME@/${_pkgbase}/g" \
		-e "s/@PKGVER@/${_pkgbase}/g" \
		-i "${pkgdir}/usr/src/${_pkgbase}-${pkgver}/dkms.conf"

	cd "${_pkgbase}-$pkgver"
	rm src/Makefile_linux24x
	cp -dr --no-preserve='ownership' src "${pkgdir}/usr/src/${_pkgbase}-${pkgver}/src"
}
sha256sums=('b2e66b03b696ba55c9fb7c896db8ac5377233d14120520735d31c33147d0d4c3'
            '260d8142e944f3144cbc704534e662d427318d8b32dc7a2852a855be72e8d763')
