pkgname=sharpfont
pkgdesc="Cross-platform FreeType bindings for .NET"
pkgver=3.0.1
pkgrel=1
arch=(any)
license=("MIT")
url="https://github.com/Robmaister/SharpFont"
source=("https://github.com/Robmaister/SharpFont/archive/v$pkgver.tar.gz"
"deps.zip::https://github.com/Robmaister/SharpFont.Dependencies/archive/9db9d1c4c8ab4832d25765904ca0e78963810884.zip"
"sharpfont.pc")
depends=(mono freetype2)
sha1sums=('78ed473d66cb9d1771032b98931579534d08f61e'
          '18356b7e32152d372fbe59405ec3a1dcb7c64db2'
          '06f0b1549c5ecb11fef7a40e77e9a4c90cf1e3c7')
prepare() {
	cp -r SharpFont.Dependencies-*/* SharpFont-$pkgver/Dependencies/
	cd SharpFont-$pkgver/Source/SharpFont/TrueType
	mv EncodingId.cs EncodingID.cs
	mv Pclt.cs PCLT.cs
	mv PlatformId.cs PlatformID.cs
}

build() {
	cd "${srcdir}/SharpFont-$pkgver/Source"
	xbuild SharpFont.sln
}

package() {
	cd "${srcdir}/SharpFont-$pkgver"
	install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	cd Binaries/SharpFont/Debug
	find . -name 'SharpFont.dll*' -exec install -Dm644 {} "$pkgdir/usr/lib/sharpfont/"{} \;
	find "$pkgdir" -name '*.dll' -exec gacutil -i {} -root "$pkgdir/usr/lib" \;
	install -Dm644 "$srcdir/sharpfont.pc" "$pkgdir/usr/lib/pkgconfig/sharpfont.pc"
	sed -i "s,@VERSION@,$pkgver," "$pkgdir/usr/lib/pkgconfig/sharpfont.pc"
}
