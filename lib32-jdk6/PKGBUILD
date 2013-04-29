# Maintainer: Fantix King
# Upstream Maintainer: Ethan Hall
# Contributors: Guillaume ALAUX, Daniel J Griffiths, Jason Chu, Geoffroy Carrier, Thomas Dziedzic, Dan Serban

pkgname=lib32-jdk6
pkgver=6u45_b06
pkgrel=2
pkgdesc="Java 6 Development Kit (32-bit)"
url=http://www.oracle.com/technetwork/java/javase/downloads/index.html
arch=('x86_64')
license=(custom)
depends=('lib32-glibc' 'lib32-jre6')
makedepends=(lynx)
install=jdk.install
source=("http://download.oracle.com/otn-pub/java/jdk/${pkgver//_/-}/jdk-${pkgver%_*}-linux-i586.bin"
	'java-control-panel.desktop'
        'java-monitoring-and-management-console.desktop'
        'java-policy-settings.desktop'
        'java-visualvm.desktop'
        'java-web-start.desktop'
        'derby-network-server'
        'derby-network-server.conf'
	'construct.sh')
md5sums=('3269370b7c34e6cbfed8785d3d0c5cbd'
         'ed18a7939221cd9d9175b95326f07902'
         '1c096aec19c0e2a8becc0f6a6dee92dc'
         '7b0bb4587958f64c159f81a9866dbdc6'
         '77eb4b85ae6634d53bbca32ae4fe3d76'
         'd81a892f5bf469df99abe8ec6dacaab1'
         'a279e195e249000646895d93e199860d'
         '4bdff6982c66d24a879c424aaac3d04d'
         '70b34ef3d5b997e7c15b1b50053d3e37')

DLAGENTS=('http::/usr/bin/curl -fLC - --retry 3 --retry-delay 3 -o %o %u --header "Cookie:oraclelicensejdk-${pkgver%_*}-oth-JPR=accept-securebackup-cookie;gpw_e24=http://edelivery.oracle.com"')

build()
{
  rm -rf unbundle-jdk
  mkdir unbundle-jdk
  cd unbundle-jdk
  
  sh ../jdk-${pkgver%_*}-linux-i586.bin -noregister
  
  cd ..
	
  sh construct.sh unbundle-jdk linux-jdk linux-jre
  
  rm -rf linux-jdk/jre
}

package()
{
  install -d "${pkgdir}"/opt
  mv ${srcdir}/linux-jdk "${pkgdir}"/opt/lib32-java6
  mkdir -p "${pkgdir}"/usr/share/licenses/${pkgname}
  
  install -m644 "${pkgdir}"/opt/lib32-java6/COPYRIGHT "${pkgdir}"/usr/share/licenses/${pkgname}
  install -m644 "${pkgdir}"/opt/lib32-java6/LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}
  install -m644 "${pkgdir}"/opt/lib32-java6/THIRDPARTYLICENSEREADME.txt "${pkgdir}"/usr/share/licenses/${pkgname}
  
  for i in kinit ktab klist; do
    rm "${pkgdir}"/opt/lib32-java6/bin/${i}
    rm "${pkgdir}"/opt/lib32-java6/man/ja_JP.eucJP/man1/${i}.1
    rm "${pkgdir}"/opt/lib32-java6/man/man1/${i}.1
  done
}

