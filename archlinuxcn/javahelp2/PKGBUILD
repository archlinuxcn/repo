# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Alucryd <alucryd at gmail dot com>
# Contributor: Stefan Husmann <stefan-husmann at t-online dot de>
# Contributor: Simon Lipp <sloonz+aur at gmail dot com>

pkgname=javahelp2
pkgver=2.0.05.r90
pkgrel=2
# manual versioning
source=("${pkgname}::git+https://github.com/javaee/javahelp.git#commit=3ca862d8626096770598a3a256886d205246f4a4"
# https://github.com/javaee/javahelp/issues/47
        'compilation-version.patch')
sha256sums=('SKIP'
            'a65f356660a82d06a24cd21957c717e2abd87a809ef37700eab1826eb9b2ec2c')
pkgdesc="Java based help system"
arch=('any')
url="https://javaee.github.io/javahelp/"
license=('custom' 'CDDL' 'GPL2')
makedepends=('apache-ant' 'git')
depends=('java-runtime')

prepare(){
    cd "${srcdir}/${pkgname}"
    patch -p1 < "${srcdir}/compilation-version.patch"
}

build(){
    cd "${srcdir}/${pkgname}/javahelp_nbproject"
    ant release
}

package() {
    cd "${srcdir}/${pkgname}/javahelp_nbproject/dist/lib"
    install -dm755 "${pkgdir}/usr/share/java/javahelp"
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
    cd ../bin
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"
    cd ../../lib
    # These are jars from tomcat5 and jdic-stub.jar
    install -m644 -- *.jar "${pkgdir}/usr/share/java/javahelp"

    install -dm755 "${pkgdir}/usr/share/licenses"
    install -D -m644 -- "${srcdir}/${pkgname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
