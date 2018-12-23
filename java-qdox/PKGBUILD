# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>
# Contributor: Alucryd <alucryd at gmail dot com>

pkgname='java-qdox'
pkgver='1.12.1'
pkgrel='2'
pkgdesc='A high speed, small footprint parser for extracting class/interface/method definitions from source files complete with JavaDoc @tags'
arch=('any')
url="http://qdox.codehaus.org/index.html"
license=('APACHE')
depends=('java-runtime')
source=("http://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/${pkgver}/qdox-${pkgver}.jar")
md5sums=('9fb6970f934f8d836ae8e6d133316ab4')
noextract=("qdox-${pkgver}.jar")

package() {
  install -Dm644 "${srcdir}/qdox-${pkgver}.jar" "${pkgdir}/usr/share/java/qdox/qdox.jar"
}
