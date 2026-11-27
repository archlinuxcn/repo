# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=sing-box-for-linux-bin
pkgver=1.14.5
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
sha512sums_x86_64=('62a312794b3c1076b8c8d074fe81f626a48e4391ab6413ba928a1ea8fb95ecea92fa02a03e3a7ad08de5fca24604a2c759bb709a85fbbe41d7d56c37978bf149')
sha512sums_aarch64=('fbc63cab2e41950ebf44325b61d5d4df5ccd01d103829a0f67835de420dceb2afb011f4db1e70b9ca9fffde6e58ea99a790a48dc31ad899394779ff2382539b6')

package() {
    install -Dm644 LicenseRef-${pkgname}-${pkgver}-${pkgrel}-exception -T "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    find . -mindepth 1 -maxdepth 1 -type d -exec cp -r "{}" "${pkgdir}" \;
}
