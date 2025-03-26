# Maintainer: Alexander Phinikarides <alexisph@gmail.com>
pkgname=bfg
pkgver=1.15.0
pkgrel=1
pkgdesc='Removes large or troublesome blobs like git-filter-branch does, but faster.'
arch=('any')
url='http://rtyley.github.io/bfg-repo-cleaner/'
license=('GPL3')
depends=('java-runtime>=11' 'bash')
source=("https://repo1.maven.org/maven2/com/madgag/${pkgname}/${pkgver}/${pkgname}-${pkgver}.jar"
        "${pkgname}.sh")
noextract=("${pkgname}-${pkgver}.jar")
sha256sums=('dfe2885adc2916379093f02a80181200536856c9a987bf21c492e452adefef7a'
            'a41ad8ff48364c1118e69f5c1c6c5c070d56ad1d2f9cd09bca3c095385a6b530')

package() {
  cd "${srcdir}"
  install -D -m755 "${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}"
  install -D -m644 "${pkgname}-${pkgver}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}
