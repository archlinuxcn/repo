# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Stéphane Marguet (Stemp) <smarguet@gmail.com>
# Contributor: scippio <scippio [at] berounet.cz>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: Rubin Simons <rubin@xs4all.nl>

pkgname=eclipse-emf
pkgver=2.11.0
_reldate=201506010402
pkgrel=1
pkgdesc="EMF and XSD frameworks for the Eclipse platform"
arch=('any')
url="http://www.eclipse.org/modeling/emf/"
license=('EPL')
depends=('eclipse>=3.5')
_mirror="http://www.eclipse.org/downloads/download.php?r=1&file="
source=("$_mirror/modeling/emf/emf/downloads/drops/${pkgver}/R${_reldate}/emf-runtime-${pkgver}.zip"
	"$_mirror/modeling/emf/emf/downloads/drops/${pkgver}/R${_reldate}/xsd-runtime-${pkgver}.zip")
sha256sums=('0f84c8348f1ec0c958b3abd0c6509e1ae793fe8394eacd51349ba7338c118052'
            '948be83fe4216bacae2c61189d0bec9097add1e0842a12383f43e28a2be6610f')
package() {
	_dest="${pkgdir}"/usr/lib/eclipse/
	cd "${srcdir}/eclipse"
	find . -type f | while read f ; do
		install -Dm644 ${f} "${_dest}/${f}"
	done
}
