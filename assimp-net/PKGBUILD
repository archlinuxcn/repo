# Maintainer: JKA Network <contacto@jkanetwork.com>
pkgname=assimp-net
pkgdesc="A .NET wrapper for the Open Asset Import Library (Assimp)."
pkgver=3.3.1
pkgrel=4
arch=(i686 x86_64)
license=("MIT")
url="https://www.nuget.org/packages/AssimpNet/"
source=("https://github.com/assimp/assimp-net/archive/3.3.1.tar.gz"
"assimp-net.pc.in"
"AssimpNet.dll.config")
depends=(assimp opentk)
makedepends=(dos2unix subversion mono)
sha1sums=('SKIP'
          '9d1ad601ca7e56327068840b10cab32da90cab04'
          'bfd87bdfad2eeb99553b8e7ba4b2029cbbf11042')

prepare() {
  cd "${srcdir}/$pkgname-$pkgver"
  find . -type f -exec dos2unix {} \;
  sed -i -e "s,Assimp32.so,libassimp.so,g" -e "s,Assimp64.so,libassimp.so,g" AssimpNet/Unmanaged/AssimpLibrary.cs
}
          
build() {
	cd "${srcdir}/$pkgname-$pkgver"
	xbuild AssimpNet.sln /p:Configuration=Net45-Debug
}

package() {
	cd "${srcdir}/$pkgname-$pkgver/AssimpNet/bin/Net45-Debug"
	install -Dm644 "AssimpLicense.txt" "$pkgdir/usr/share/licenses/$pkgname/AssimpLicense.txt"
	find . -name 'AssimpNet.dll*' -exec install -Dm644 {} "$pkgdir/usr/lib/$pkgname/"{} \;
	install -m644 "$srcdir/AssimpNet.dll.config" "$pkgdir/usr/lib/$pkgname/"
	find "$pkgdir" -name '*.dll' -exec gacutil -i {} -root "$pkgdir/usr/lib" \;
	install -Dm644 "$srcdir/assimp-net.pc.in" "$pkgdir/usr/lib/pkgconfig/assimp-net.pc"
	sed -i "s,@VERSION@,$pkgver," "$pkgdir/usr/lib/pkgconfig/assimp-net.pc"
}
