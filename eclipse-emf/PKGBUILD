# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Stéphane Marguet (Stemp) <smarguet@gmail.com>
# Contributor: scippio <scippio [at] berounet.cz>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: Rubin Simons <rubin@xs4all.nl>

pkgname=eclipse-emf
pkgver=2.11.1
_reldate=201508060404
pkgrel=1
pkgdesc="EMF and XSD frameworks for the Eclipse platform"
arch=('any')
url="http://www.eclipse.org/modeling/emf/"
license=('EPL')
depends=('eclipse>=3.5')
_mirror="http://www.eclipse.org/downloads/download.php?r=1&file="
source=("$_mirror/modeling/emf/emf/downloads/drops/${pkgver}/R${_reldate}/emf-runtime-${pkgver}.zip"
	"$_mirror/modeling/emf/emf/downloads/drops/${pkgver}/R${_reldate}/xsd-runtime-${pkgver}.zip")
sha256sums=('9c3e9af622c0c1e9bd00344998308fb5e23335bf169eb3c3634bcc596e704712'
            'db4467b9b2226f4bdba74679a8d8ffcb0fc138017f08213658de00333e7b918b')
package() {
    _dest=$pkgdir/usr/lib/eclipse/dropins/${pkgname#eclipse-}/eclipse
	cd "${srcdir}/eclipse"
	find . -type f | while read f ; do
		install -Dm644 ${f} "${_dest}/${f}"
	done
}
