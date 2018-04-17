# Maintainer: Utsob Roy uroybd@gmail.com
# Contributor: Utsob Roy uroybd@gmail.com
pkgname=franz-bin
pkgver=5.0.0_beta.18
pkgrel=1
pkgdesc="Messaging app for WhatsApp, Slack, Telegram, HipChat, Hangouts and many many more. Binrary from debian package without compiling."
arch=('x86_64')
url="https://meetfranz.com"
license=('Apache')
groups=('')
depends=('gconf' 'libnotify' 'libappindicator-gtk2' 'libxtst' 'nss' 'libxss')
options=('!strip' '!emptydirs')
install=${pkgname}.install
source_x86_64=("https://github.com/meetfranz/franz/releases/download/v${pkgver//_/-}/franz_${pkgver//_/-}_amd64.deb")
sha512sums_x86_64=('dcee8ff93392c41f1d5e6d4c058fc5e05b592e6db23589f81207eeee0012d96fa569f0d8a79506e46b1ebd5575c4cb0840eedcc686fd9e4463323a0a29641faf')

package(){

	# Extract package data
	tar xf data.tar.xz -C "${pkgdir}"

	install -D -m644 "${pkgdir}/opt/Franz/LICENSES.chromium.html" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
