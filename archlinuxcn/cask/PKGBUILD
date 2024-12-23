# Package inspired from homebrew

# Maintainer: Eric Berquist <eric DOT berquist AT gmail>
# Contributor: Sebastien Duthil <duthils@duthils.net>

pkgname=cask
pkgver=0.9.0
pkgrel=1
pkgdesc="Project management tool for Emacs"
arch=('any')
url='https://github.com/cask/cask'
license=('GPL')
depends=('emacs' 'python')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('5db17efe3a91d36f457e70f097cba5ed5de505971894bf2ec839c38d8c2dd120')

package() {
	cd "${srcdir}/${pkgname}-$pkgver"

	# cask executable needs to be one directory deeper than cask-cli.el
	__prefix="${pkgdir}/usr/share/${pkgname}"
	install -d "${__prefix}"
	install -Dm644 *.el "${__prefix}/"
	install -d "${__prefix}/bin"
	install -Dm755 "bin/cask" "${__prefix}/bin"
	touch "${__prefix}/.no-upgrade"  # Stop cask performing self-upgrades.

	install -d "${pkgdir}/usr/bin"
	ln -s "/usr/share/cask/bin/cask" "${pkgdir}/usr/bin/"

	__site_lisp="${pkgdir}/usr/share/emacs/site-lisp/${pkgname}"
	install -d "${__site_lisp}"
	ln -s "/usr/share/${pkgname}/"cask{,-bootstrap}.el "${__site_lisp}/"
}
