# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=sing-box-for-linux-bin
pkgver=1.14.3
pkgrel=1
pkgdesc="Linux client for sing-box, The universal proxy platform."
arch=('x86_64' 'aarch64' )
url="https://sing-box.sagernet.org/"
license=("GPL-3.0-or-later" "LicenseRef-${pkgname}-exception")
depends=('c-ares'
	'ffmpeg'
	'gtk3'
	'libevent' 
	'libvpx'
	'libxslt'
	'libxss'
	'minizip'
	'nss'
	're2'
	'snappy'
	'libnotify'
	'libappindicator-gtk3'
	'polkit'
)
install=sing-box-for-linux-bin.install
provides=("sing-box-for-linux")
conflicts=("sing-box-for-linux")
source=("LicenseRef-${pkgname}-${pkgver}-${pkgrel}-exception::https://raw.githubusercontent.com/SagerNet/sing-box/v${pkgver}/LICENSE")
source_x86_64=("SFL-${pkgname}-${pkgver}-${pkgrel}-x64.pkg.tar.zst::https://github.com/SagerNet/sing-box/releases/download/v${pkgver}/SFL-${pkgver}-x64.pkg.tar.zst")
source_aarch64=("SFL-${pkgname}-${pkgver}-${pkgrel}-aarch64.pkg.tar.zst::https://github.com/SagerNet/sing-box/releases/download/v${pkgver}/SFL-${pkgver}-aarch64.pkg.tar.zst")

sha512sums=('35b76843c30240d073dbffade3cc76f569e01b273974d2a7110fcb41fca76b22c0be04da0aac33157083f188ebf69177e1f5a158f08327c4d235996877b53ab4')
sha512sums_x86_64=('a5f61e502c1d3a34f860de564b748fe95dc2e2dd56af0d063fb324bb02eb57a49d53cff790dea9a0f5feb306c3716accde826ea49c5f17e0d9f52397613c3327')
sha512sums_aarch64=('4a5f09ce367d3f99f3aeacc3e5ddd1efe722599e6385e68c5ae1513d651fb23fee2c26567f83e1fe418b70248c82d910f2c8fd5e60aac6fca1b76028cd181938')

package() {
    install -Dm644 LicenseRef-${pkgname}-${pkgver}-${pkgrel}-exception -T "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    find . -mindepth 1 -maxdepth 1 -type d -exec cp -r "{}" "${pkgdir}" \;
}
