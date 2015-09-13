pkgname=assimp-net
pkgdesc="A .NET wrapper for the Open Asset Import Library (Assimp)."
pkgver=3.3.1
pkgrel=2
arch=(any)
license=("MIT")
url="https://code.google.com/p/assimp-net"
source=("$pkgname::svn+http://assimp-net.googlecode.com/svn/tags/$pkgver"
"assimp-net.pc.in"
"AssimpNet.dll.config")
depends=(assimp opentk)
makedepends=(dos2unix subversion mono)
sha1sums=('SKIP'
          '9d1ad601ca7e56327068840b10cab32da90cab04'
          'bfd87bdfad2eeb99553b8e7ba4b2029cbbf11042')

prepare() {
  cd "$srcdir/$pkgname"
  find . -type f -exec dos2unix {} \;
  sed -i -e "s,Assimp32.so,libassimp.so,g" -e "s,Assimp64.so,libassimp.so,g" AssimpNet/Unmanaged/AssimpLibrary.cs
}
          
build() {
	cd "${srcdir}/$pkgname"
	xbuild AssimpNet.sln /p:Configuration=Net45-Debug
}

package() {
	cd "${srcdir}/$pkgname/AssimpNet/bin/Net45-Debug"
	install -Dm644 "AssimpLicense.txt" "$pkgdir/usr/share/licenses/$pkgname/AssimpLicense.txt"
	find . -name 'AssimpNet.dll*' -exec install -Dm644 {} "$pkgdir/usr/lib/$pkgname/"{} \;
	install -m644 "$srcdir/AssimpNet.dll.config" "$pkgdir/usr/lib/$pkgname/"
	find "$pkgdir" -name '*.dll' -exec gacutil -i {} -root "$pkgdir/usr/lib" \;
	install -Dm644 "$srcdir/assimp-net.pc.in" "$pkgdir/usr/lib/pkgconfig/assimp-net.pc"
	sed -i "s,@VERSION@,$pkgver," "$pkgdir/usr/lib/pkgconfig/assimp-net.pc"
}
