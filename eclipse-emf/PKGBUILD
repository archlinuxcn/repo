# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Stéphane Marguet (Stemp) <smarguet@gmail.com>
# Contributor: scippio <scippio [at] berounet.cz>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: Rubin Simons <rubin@xs4all.nl>

pkgname=eclipse-emf
pkgver=2.10.2
_reldate=201501230452
pkgrel=1
pkgdesc="EMF and XSD frameworks for the Eclipse platform"
arch=('any')
url="http://www.eclipse.org/modeling/emf/"
license=('EPL')
depends=('eclipse>=3.5')
_mirror="http://www.eclipse.org/downloads/download.php?r=1&file="
source=("$_mirror/modeling/emf/emf/downloads/drops/${pkgver}/R${_reldate}/emf-runtime-${pkgver}.zip"
	"$_mirror/modeling/emf/emf/downloads/drops/${pkgver}/R${_reldate}/xsd-runtime-${pkgver}.zip")
sha256sums=('1243978ebfd2de2178b72c4227d4ee47b46d1d4d13442c3f1ae0a9ec0eef42f6'
            '8bb29f58772f2a1a2167ff8c4b825a58fdd64923c44aec0c48d66c5afcb76fc7')
package() {
	_dest="${pkgdir}"/usr/share/eclipse/dropins/${pkgname/eclipse-}/eclipse
	cd "${srcdir}/eclipse"
	find . -type f | while read f ; do
		install -Dm644 ${f} "${_dest}/${f}"
	done
}
