# Maintainer: K4YT3X <aur@k4yt3x.com>
pkgname=nspawn
pkgver=0.6
pkgrel=1
pkgdesc="A wrapper around machinectl for easy-deployment of nspawn.org containers"
arch=('any')
url="https://github.com/nspawn/nspawn"
license=('GPL3')
depends=('systemd')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/nspawn/nspawn/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('9a066f660ad05f36b2b176d8bffac8c8ff20911a05d2fbeab7210f6dd4e5ccbc1a774a036e5992ae44b1966631ddd65acad7d4993ec6b7a253661aad9c57c206')

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	install -D -m 755 nspawn "${pkgdir}/usr/bin/nspawn"
    install -D -m 644 LICENSE "${pkgdir}/usr/share/licenses/nspawn/LICENSE"
}
