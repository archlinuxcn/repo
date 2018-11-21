# Contributor: Jonas Heinrich <onny@project-insanity.org>
# Maintainer: Horo <horo@yoitsu.moe>

pkgname=parsoid-git
_pkgname=parsoid
pkgver=v0.3.0.r2009.g6693ee4d1
pkgrel=1
pkgdesc="A bidirectional wikitext parser and runtime"
arch=('any')
url="https://www.mediawiki.org/wiki/Parsoid"
license=('GPL2')
depends=('nodejs')
makedepends=('git' 'npm')
optdepends=(
    'mediawiki: MediaWiki engine'
)
conflicts=('parsoid')
replaces=('parsoid')
provides=('parsoid')
backup=(usr/share/webapps/parsoid/localsettings.js
	usr/share/webapps/parsoid/config.yaml)
source=("git+https://gerrit.wikimedia.org/r/p/mediawiki/services/parsoid"
        "parsoid.service"
        "parsoid.install"
        "parsoid.sysusers"
        "parsoid.tmpfiles")

sha512sums=('SKIP'
            '3733d08751209fdef134940bbcce48efd0f380e13a8df466a7a1010450857a924aa364628242e4307cf40f4a34e60c1aeb1400d9a5b9fed88b448ed549e4d3f1'
            '70473c30f7d78f40da1ab91c717e012575687e5edde18011d7a8759fc7ad0ad28a20514794a836d855b409a9becb4c779365d72dc3d5dcd62275d05f558876e8'
            '7f2346af222052e2e685d859e0bb7a7c7c9f03988f772856e0888cad299cb3870afdc280feb9e2798e7989d3382f68f689d43a685b466ce9f138edb77b20de3a'
            '6158afa3c276ddb5090166680621b7b9213f3d73b2d1a95181f5441631be039e7d454228d2f214f1411bb7f953475ddbd368e89eaa2288ac200ac666a57a6a99')
options=('!strip')
install="parsoid.install"
pkgver() {
  cd "$_pkgname"
  git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g' 
}
build() { 
    cd $srcdir/parsoid
    npm install
}
package() {
    cd $srcdir/parsoid
    cp localsettings.example.js localsettings.js    
    cp config.example.yaml config.yaml
    mkdir -p "${pkgdir}/usr/share/webapps/${_pkgname}"
    tar c --exclude=.git . | tar x -C "${pkgdir}/usr/share/webapps/${_pkgname}/"
    install -Dm644 "${srcdir}/parsoid.service" "${pkgdir}/usr/lib/systemd/system/parsoid.service"
    install -D "COPYING.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 "$srcdir"/parsoid.sysusers "$pkgdir"/usr/lib/sysusers.d/parsoid.conf
    install -Dm644 "$srcdir"/parsoid.tmpfiles "$pkgdir"/usr/lib/tmpfiles.d/parsoid.conf
}

