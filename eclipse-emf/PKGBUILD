# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Stéphane Marguet (Stemp) <smarguet@gmail.com>
# Contributor: scippio <scippio [at] berounet.cz>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: Rubin Simons <rubin@xs4all.nl>

pkgname=eclipse-emf
pkgver=2.12.0
_reldate=201605260356
pkgrel=1
pkgdesc="EMF and XSD frameworks for the Eclipse platform"
arch=('any')
url="http://www.eclipse.org/modeling/emf/"
license=('EPL')
depends=('eclipse>=3.5')
_mirror="http://www.eclipse.org/downloads/download.php?r=1&file="
source=("$_mirror/modeling/emf/emf/downloads/drops/${pkgver}/R${_reldate}/emf-runtime-${pkgver}.zip"
	"$_mirror/modeling/emf/emf/downloads/drops/${pkgver}/R${_reldate}/xsd-runtime-${pkgver}.zip")
md5sums=('fccaa15ebfc51357ae1d2fffe3574efc'
         'fce2cc0cd2281d5765e29bf236b5e0be')

package() {
    _dest=$pkgdir/usr/lib/eclipse/dropins/${pkgname#eclipse-}/eclipse
	cd "${srcdir}/eclipse"
	find . -type f | while read f ; do
		install -Dm644 ${f} "${_dest}/${f}"
	done
}
