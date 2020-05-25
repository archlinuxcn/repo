# Maintainer: Eric S. Londres <ericlondres@protonmail.com>
# Contributor: Joakim Nylén <me@jnylen.nu>
# Contributor: Rashintha Maduneth <rashinthamaduneth@gmail.com>
# Contributor: Dhananjay Balan <mail@dbalan.in>
# Contributor: ahrs

pkgname=mailspring
pkgver=1.7.8
pkgrel=1
pkgdesc="A beautiful, fast and maintained fork of Nylas Mail by one of the original authors."
arch=('x86_64')
license=('custom: GPL3 and (C) 2016-2019 Foundry 376, LLC.')
url="https://getmailspring.com/"
options=('!strip')

source=()

source_x86_64=("https://github.com/Foundry376/Mailspring/releases/download/${pkgver}/mailspring-${pkgver}-amd64.deb")
sha256sums_x86_64=('207fbf813b6da018a5b848e5dc1194b5996daab39adbd873b2cecb0565c105ce')

depends=("libxss" "libtool" "c-ares" "ctemplate" "tidy" "libxkbfile" "libsecret" "gtk3" "nss" "libglvnd")

optdepends=('libappindicator-gtk3: for system tray support' "libgnome-keyring: keyrings" "gnome-keyring: keyrings" )

package() {
	cd ${srcdir}

	tar -xvf data.tar.xz -C ${pkgdir} --exclude='./control'

	chmod -R go-w "${pkgdir}"/usr
}
