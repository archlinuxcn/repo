# Maintainer: Rene Benner <renebenner + arch at gmail dot com>
# Maintainer: Chris Lane <aur at chrislane dot com>
# Contributor: Troy Engel <troyengel + arch at gmail dot com>
# Contributor: Callum Denby <me@callumdenby.com>
pkgname=aws-session-manager-plugin
pkgver=1.2.536.0
pkgrel=1
pkgdesc="AWS Session Manager Plugin for aws-cli."
arch=('x86_64' 'aarch64')
url="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html"
license=('Apache')
depends=('aws-cli')
backup=('usr/lib/systemd/system/session-manager-plugin.service' 'usr/sessionmanagerplugin/LICENSE' 'usr/sessionmanagerplugin/seelog.xml' 'usr/sessionmanagerplugin/VERSION')
options=('!strip' '!emptydirs')
source_x86_64=("${pkgname}-${pkgver}.deb"::https://s3.amazonaws.com/session-manager-downloads/plugin/${pkgver}/ubuntu_64bit/session-manager-plugin.deb)
source_aarch64=("${pkgname}-${pkgver}-aarch64.deb"::https://s3.amazonaws.com/session-manager-downloads/plugin/${pkgver}/ubuntu_arm64/session-manager-plugin.deb)
sha512sums_x86_64=('6e8862e981bcb1117ab138cc8458baa1411805409d03ad57571398338ae7177c5f8528af2bcb9a4522ca3acd190559956a0685e98321527e11345013ed1528ad')
sha512sums_aarch64=('d0bb279cd540a616e97ed3d74121edabc91c2e7f66dc1dec0c8bbac6a53981328be1e55e236da91b9ea183ba14f53b514169ec7507149be50faf96495ab4d2ae')

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
