# Maintainer: Rene Benner <renebenner + arch at gmail dot com>
# Maintainer: Chris Lane <aur at chrislane dot com>
# Contributor: Troy Engel <troyengel + arch at gmail dot com>
# Contributor: Callum Denby <me@callumdenby.com>
pkgname=aws-session-manager-plugin
pkgver=1.2.398.0
pkgrel=1
pkgdesc="AWS Session Manager Plugin for aws-cli."
arch=('x86_64' 'aarch64')
url="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html"
license=('custom')
depends=('aws-cli')
backup=('usr/lib/systemd/system/session-manager-plugin.service' 'usr/sessionmanagerplugin/LICENSE' 'usr/sessionmanagerplugin/seelog.xml' 'usr/sessionmanagerplugin/VERSION')
options=('!strip' '!emptydirs')
source_x86_64=("${pkgname}-${pkgver}.deb"::https://s3.amazonaws.com/session-manager-downloads/plugin/${pkgver}/ubuntu_64bit/session-manager-plugin.deb)
source_aarch64=("${pkgname}-${pkgver}-aarch64.deb"::https://s3.amazonaws.com/session-manager-downloads/plugin/${pkgver}/ubuntu_arm64/session-manager-plugin.deb)
sha512sums_x86_64=('0368f28430f348c7ca9ac1db00a930d48e927d3bcc8527d0357cdb04a65d82390ddcfd22447eb8ccec83c6ca65082ffa1001ed27614e799cb44d57b45c01ad5d')
sha512sums_aarch64=('0bf95f9675ffedf4ffe09c028435083999d3b689eed7cc7f802bb3aacebe4be67fd18b6d4d95c5cd4b3c4b5eecfac5dd309e67ee2397b316cd6f16bfba59e0e9')

# Version history with new versions is here.
#  https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html#plugin-version-history

package(){

	# Extract package data
	tar xzf data.tar.gz -C "${pkgdir}"

	# Fix directories structure differencies
	cd "${pkgdir}"
	mkdir -p usr/bin
	mkdir -p usr/lib 2> /dev/null; mv lib/* usr/lib; rm -rf lib
	rm -rf etc/
	sed -i 's/usr\/local/usr/' usr/lib/systemd/system/session-manager-plugin.service
	mv usr/local/* usr; rm -rf usr/local
	ln -sf /usr/sessionmanagerplugin/bin/session-manager-plugin usr/bin/session-manager-plugin
	cd ..
}
