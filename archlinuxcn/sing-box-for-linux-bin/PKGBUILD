# Maintainer: Jia Yin<yenfeng.shetiko at gmail dot com>

pkgname=sing-box-for-linux-bin
pkgver=1.14.6
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
sha512sums_x86_64=('fdd5797215f9fdaeb5bfe6035e996775dfff4058e17866911a7de66a41470717deada4ff8d51c2a2406b953457fe45296f66565e18bcad217fb4c4c609e8f662')
sha512sums_aarch64=('a8d0784e24f80620baee0f0ae9214461b5fa200adacf16256f90f43f287c7d0d5ddb5c49232c81b121443194de4e4afc17bbd8fbf46eb13615af1b3ac2d6e07e')

package() {
    install -Dm644 LicenseRef-${pkgname}-${pkgver}-${pkgrel}-exception -T "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    find . -mindepth 1 -maxdepth 1 -type d -exec cp -r "{}" "${pkgdir}" \;
}
