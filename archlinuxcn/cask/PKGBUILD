# Package inspired from homebrew

# Maintainer: Sebastien Duthil <duthils@duthils.net>

pkgname=cask
pkgver=0.8.4
pkgrel=1
pkgdesc="Project management tool for Emacs"
arch=('any')
url='https://github.com/cask/cask'
license=('GPL')
depends=('emacs' 'python')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('02f8bb20b33b23fb11e7d2a1d282519dfdb8b3090b9672448b8c2c2cacd3e478')

package() {
	cd "${srcdir}/${pkgname}-$pkgver"

	# cask executable needs to be one directory deeper than cask-cli.el
	__prefix="${pkgdir}/usr/share/${pkgname}"
	install -d "${__prefix}"
	install -Dm644 *.el "${__prefix}/"
	install -d "${__prefix}/bin"
	install -Dm755 "bin/cask" "${__prefix}/bin"
	install -d "${__prefix}/templates"
	install -Dm644 templates/* "${__prefix}/templates/"
	touch "${__prefix}/.no-upgrade"  # Stop cask performing self-upgrades.

	install -d "${pkgdir}/usr/bin"
	ln -s "/usr/share/cask/bin/cask" "${pkgdir}/usr/bin/"

	__site_lisp="${pkgdir}/usr/share/emacs/site-lisp/${pkgname}"
	install -d "${__site_lisp}"
	ln -s "/usr/share/${pkgname}/"cask{,-bootstrap}.el "${__site_lisp}/"
}
