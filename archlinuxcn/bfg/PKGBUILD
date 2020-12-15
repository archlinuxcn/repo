# Maintainer: Alexander Phinikarides <alexisph@gmail.com>
pkgname=bfg
pkgver=1.13.1
pkgrel=1
pkgdesc='Removes large or troublesome blobs like git-filter-branch does, but faster.'
arch=('any')
url='http://rtyley.github.io/bfg-repo-cleaner/'
license=('GPL3')
depends=('java-runtime>8' 'bash')
source=("https://repo1.maven.org/maven2/com/madgag/${pkgname}/${pkgver}/${pkgname}-${pkgver}.jar"
        "${pkgname}.sh")
noextract=("${pkgname}-${pkgver}.jar")
sha256sums=('e5b3d90e45cafb6687a7c8f56b01aeb437705e52cb4cc6bfe010f2a728cd2c26'
            'a41ad8ff48364c1118e69f5c1c6c5c070d56ad1d2f9cd09bca3c095385a6b530')

package() {
  cd "${srcdir}"
  install -D -m755 "${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
  install -D -m644 "${pkgname}-${pkgver}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}
