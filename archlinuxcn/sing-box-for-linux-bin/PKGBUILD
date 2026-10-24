# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=sing-box-for-linux-bin
pkgver=1.14.4
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
sha512sums_x86_64=('54a106e1b015bc9432e5cfe8b1a99bc5f0f3ff06c8a2c3e4bd036aab9a30622ccde3d6901deb3d3decb04c31b948b7389e180bbc87676b301e55236328de9ecd')
sha512sums_aarch64=('201f51697f2645af556254e8a21aadd18b28ce099d4becc6a4f1b2ee7078e133ad694cdbfdc0fc8b33d4607226834f9ce6ff3cea3060912d686c5ef37d702149')

package() {
    install -Dm644 LicenseRef-${pkgname}-${pkgver}-${pkgrel}-exception -T "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    find . -mindepth 1 -maxdepth 1 -type d -exec cp -r "{}" "${pkgdir}" \;
}
