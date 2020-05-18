# Contributor: Jonas Heinrich <onny@project-insanity.org>
# Maintainer: Horo <horo@yoitsu.moe>

pkgname=parsoid
_pkgname=parsoid
pkgver=0.12.0_a13
pkgrel=2
pkgdesc="A bidirectional wikitext parser and runtime"
arch=('any')
url="https://www.mediawiki.org/wiki/Parsoid"
license=('GPL2')
depends=('nodejs' 'npm')
makedepends=('git' 'python2')
optdepends=(
    'mediawiki: MediaWiki engine'
)
conflicts=('parsoid-git')
provides=('parsoid')
backup=(usr/share/webapps/parsoid/localsettings.js
	usr/share/webapps/parsoid/config.yaml
	etc/webapps/parsoid/config.yaml
        etc/webapps/parsoid/localsettings.js)
source=("https://github.com/wikimedia/parsoid/archive/v${pkgver//_/-}.zip"
        "parsoid.service"
        "parsoid.install"
        "parsoid.sysusers"
        "parsoid.tmpfiles")

options=('!strip')
install="parsoid.install"
prepare() {
    cp -R $srcdir/parsoid-${pkgver//_/-} $srcdir/parsoid
}
build() { 
    cd $srcdir/parsoid
    alias python="python2"
    npm install
}
package() {
    cd $srcdir/parsoid
    mkdir -p "${pkgdir}/usr/share/webapps/${_pkgname}"
    cp -R . "${pkgdir}/usr/share/webapps/${_pkgname}/"

    install -d  "$pkgdir"/etc/webapps/${_pkgname}
    cp "$srcdir/parsoid/localsettings.example.js" "$pkgdir"/etc/webapps/${_pkgname}/localsettings.js
    cp "$srcdir/parsoid/config.example.yaml" "$pkgdir"/etc/webapps/${_pkgname}/config.yaml
    
    ln -s /etc/webapps/${_pkgname}/config.yaml "$pkgdir"/usr/share/webapps/${_pkgname}/config.yaml
    ln -s /etc/webapps/${_pkgname}/localsettings.js "$pkgdir"/usr/share/webapps/${_pkgname}/localsettings.js
    
    install -Dm644 "${srcdir}/parsoid.service" "${pkgdir}/usr/lib/systemd/system/parsoid.service"
    install -Dm644 "$srcdir"/parsoid.sysusers "$pkgdir"/usr/lib/sysusers.d/parsoid.conf
    install -Dm644 "$srcdir"/parsoid.tmpfiles "$pkgdir"/usr/lib/tmpfiles.d/parsoid.conf
    install -D "COPYING.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

sha512sums=('155cd6c213c1587601ab0185b64ff565e34075eb7ed09bc0407bf4e39d9d9c14765724a226920f2109276f1f099fa8ca1c2130cc6b03035e0bd642bb8f4e5bee'
            '3733d08751209fdef134940bbcce48efd0f380e13a8df466a7a1010450857a924aa364628242e4307cf40f4a34e60c1aeb1400d9a5b9fed88b448ed549e4d3f1'
            '176c83b9bce00f63c0783f795ab5cb22746ccaab2ac49b13d71d974255b4eddadbbd481979c10bd5318194498cd3f2ce07af85ebf92508baa91ea4d4c7ee00c5'
            '7f2346af222052e2e685d859e0bb7a7c7c9f03988f772856e0888cad299cb3870afdc280feb9e2798e7989d3382f68f689d43a685b466ce9f138edb77b20de3a'
            '6158afa3c276ddb5090166680621b7b9213f3d73b2d1a95181f5441631be039e7d454228d2f214f1411bb7f953475ddbd368e89eaa2288ac200ac666a57a6a99')
