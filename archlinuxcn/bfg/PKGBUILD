# Maintainer: Alexander Phinikarides <alexisph@gmail.com>
pkgname=bfg
pkgver=1.14.0
pkgrel=1
pkgdesc='Removes large or troublesome blobs like git-filter-branch does, but faster.'
arch=('any')
url='http://rtyley.github.io/bfg-repo-cleaner/'
license=('GPL3')
depends=('java-runtime>8' 'bash')
source=("https://repo1.maven.org/maven2/com/madgag/${pkgname}/${pkgver}/${pkgname}-${pkgver}.jar"
        "${pkgname}.sh")
noextract=("${pkgname}-${pkgver}.jar")
sha256sums=('1a75e9390541f4b55d9c01256b361b815c1e0a263e2fb3d072b55c2911ead0b7'
            'a41ad8ff48364c1118e69f5c1c6c5c070d56ad1d2f9cd09bca3c095385a6b530')

package() {
  cd "${srcdir}"
  install -D -m755 "${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
  install -D -m644 "${pkgname}-${pkgver}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}
