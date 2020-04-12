# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Guo Yunhe <guoyunhebrave@gmail.com>
pkgname=fontweak
pkgver=1.3.1
pkgrel=6
pkgdesc="GUI front-end of fontconfig"
arch=(any)
url="https://github.com/guoyunhe/fontweak"
license=('GPL3')
groups=()
depends=('java-runtime')
makedepends=('java-environment' 'apache-ant')
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
changelog=
source=("https://github.com/guoyunhe/${pkgname}/archive/v1.3.1/${pkgname}-${pkgver}.tar.gz")
noextract=()
sha256sums=('7ef6f68cbccfafc868017da8fdbb517963621db6c3133bcfdb107d372c42aef0')

build() {
    cd ${srcdir}/${pkgname}-${pkgver}
    ant jar
}

package() {
    cd ${srcdir}/${pkgname}-${pkgver}

    mkdir -p ${pkgdir}/usr/bin
    cat > ${pkgdir}/usr/bin/${pkgname} << EOF
#!/bin/sh
exec java -jar "/usr/share/${pkgname}/${pkgname}.jar"
EOF
    chmod 0755 ${pkgdir}/usr/bin/${pkgname}

    install -D -m664 dist/${pkgname}.jar ${pkgdir}/usr/share/${pkgname}/${pkgname}.jar
    install -D -m664 icon.svg ${pkgdir}/usr/share/pixmaps/${pkgname}.svg
    install -D -m664 ${pkgname}.desktop ${pkgdir}/usr/share/applications/${pkgname}.desktop
}

