# Maintainer: Joakim Nylén <me@jnylen.nu>
# Maintainer: Rashintha Maduneth <rashinthamaduneth@gmail.com>
# Maintainer: Dhananjay Balan <mail@dbalan.in>
# Contributor: ahrs

pkgname=mailspring
pkgver=1.7.1
pkgrel=1
pkgdesc="A beautiful, fast and maintained fork of Nylas Mail by one of the original authors."
arch=('x86_64')
license=('custom: GPL3 and (C) 2016-2019 Foundry 376, LLC.')
url="https://getmailspring.com/"
options=('!strip')

source=()
sha256sums_x86_64=('7f9bea33834494e019e6c1e451583a218e340c6c9cfc043c35e40fe6726e9e11')

source_x86_64=("https://github.com/Foundry376/Mailspring/releases/download/${pkgver}/mailspring-${pkgver}-amd64.deb")
depends=("libxss" "libtool" "c-ares" "ctemplate" "tidy" "libxkbfile" "libsecret" "gconf" "gtk3" "nss" "libglvnd")

optdepends=('libappindicator-gtk3: for system tray support' "libgnome-keyring: keyrings" "gnome-keyring: keyrings" )

package() {
	cd ${srcdir}

	tar -xvf data.tar.xz -C ${pkgdir} --exclude='./control'

	chmod -R go-w "${pkgdir}"/usr
}
