# Maintainer: Fantix King
# Upstream Maintainer: Ethan Hall
# Contributors: Guillaume ALAUX, Daniel J Griffiths, Jason Chu, Geoffroy Carrier, Thomas Dziedzic, Dan Serban

pkgname=lib32-jre6
pkgver=6u45_b06
pkgrel=2
pkgdesc="Java 6 Runtime Environment (32-bit)"
url=http://www.oracle.com/technetwork/java/javase/downloads/index.html
arch=('x86_64')
license=(custom)
depends=('lib32-glibc' 'lib32-libxtst')
makedepends=(lynx)
install=jre.install
source=("http://download.oracle.com/otn-pub/java/jdk/${pkgver//_/-}/jdk-${pkgver%_*}-linux-i586.bin"
        'javaws-launcher'
	'construct.sh')
md5sums=('3269370b7c34e6cbfed8785d3d0c5cbd'
         '45c15a6b4767288f2f745598455ea2bf'
         '70b34ef3d5b997e7c15b1b50053d3e37')
DLAGENTS=('http::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -o %o %u --header "Cookie:oraclelicensejdk-${pkgver%_*}-oth-JPR=accept-securebackup-cookie;gpw_e24=http://edelivery.oracle.com"')
#         _arch=i586

build()
{
  rm -rf unbundle-jdk
  rm -rf linux-jdk

  cd ${srcdir}
  
  mkdir unbundle-jdk
  cd unbundle-jdk

  sh ../jdk-${pkgver%_*}-linux-i586.bin -noregister

  cd ..

  echo ${linux-jdk}
  sh construct.sh unbundle-jdk linux-jdk linux-jre
}

package()
{
  mkdir -p ${pkgdir}/opt/lib32-java6
  mv ${srcdir}/linux-jdk/jre ${pkgdir}/opt/lib32-java6

  mkdir -p ${pkgdir}/usr/lib/mozilla/plugins
  
  mkdir -p ${pkgdir}/usr/share/licenses/${pkgname}
  cp ${pkgdir}/opt/lib32-java6/jre/COPYRIGHT ${pkgdir}/usr/share/licenses/${pkgname}
  cp ${pkgdir}/opt/lib32-java6/jre/LICENSE ${pkgdir}/usr/share/licenses/${pkgname}
  cp ${pkgdir}/opt/lib32-java6/jre/THIRDPARTYLICENSEREADME.txt ${pkgdir}/usr/share/licenses/${pkgname}

  install "${srcdir}"/javaws-launcher "${pkgdir}"/opt/lib32-java6/jre/bin/javaws-launcher
}

