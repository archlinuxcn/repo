# Maintainer: Daniel Goß <developer@flashsystems.de>
_npmname=tiddlywiki
pkgname=nodejs-${_npmname}
pkgver=5.1.22
pkgrel=1
pkgdesc='TiddlyWiki, a non-linear personal web notebook that anyone can use and keep forever, independently of any corporation. This is the nodejs server edition.'
arch=('any')
url="https://tiddlywiki.com/#TiddlyWiki%20on%20Node.js"
license=('BSD')
depends=('nodejs')
makedepends=('npm' 'jq')
source=("https://registry.npmjs.org/tiddlywiki/-/$_npmname-$pkgver.tgz"
        "${pkgname}-${pkgver}.license::https://raw.githubusercontent.com/Jermolene/TiddlyWiki5/master/license")
sha256sums=('36510869fd9a73e692f3ddc92abfd0e08d2b14b5cbd3b506384a29e0316978fa'
            'b1b005226880937f9bd76e89062371234faa8c4c6df5687bc09c0416a3f12808')
noextract=("$_npmname-$pkgver.tgz")

package() {
	npm install -g --user root --cache "${srcdir}/npm-cache" --prefix "${pkgdir}/usr" "${srcdir}/${_npmname}-${pkgver}.tgz"

	# Fix https://github.com/npm/npm/issues/9359
	find "${pkgdir}/usr" -type d -exec chmod 755 {} +

	# Fix https://bugs.archlinux.org/task/63396
	chown -R root:root "${pkgdir}"

	# Remove references to $pkgdir
	find "${pkgdir}" -type f -name package.json -print0 | xargs -0 sed -i "/_where/d"

	# Remove references to $srcdir
	local tmppackage="$(mktemp)"
	local pkgjson="${pkgdir}/usr/lib/node_modules/${_npmname}/package.json"
	jq '.|=with_entries(select(.key|test("_.+")|not))' "${pkgjson}" > "${tmppackage}"
	mv "${tmppackage}" "${pkgjson}"
	chmod 644 "${pkgjson}"

	# Install license from github
	install -Dm 644 "${srcdir}/${pkgname}-${pkgver}.license" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
