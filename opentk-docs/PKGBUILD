pkgbase=opentk
pkgname=(opentk opentk-docs)
epoch=2
pkgver=1.1_4c
pkgrel=1
arch=(any)
license=("MIT")
makedepends=(doxygen texlive-core ghostscript)
options=(!emptydirs)
url="http://www.opentk.com"
source=("https://github.com/opentk/opentk/archive/${pkgver//_/-}.tar.gz"
"opentk.pc.in"
"opentk-winforms.pc.in"
"opentk-compat.pc.in")
sha1sums=('1eae1729720eb06cdd22ad6372346e2aa37b55c1'
          '1af9b1b5edd2b56023bf85c7aa79d6867fa6c94c'
          'b30246f657626e2223c252fbf9d176f32e56fb18'
          '933814784c3f73f007ed899abfea16e990c2836b')

prepare() {
	cd "$srcdir/opentk-${pkgver//_/-}/Source/Examples"
	sed -i "s,debug.log,/tmp/opentk_debug.log," ExampleBrowser.cs
	sed -i -e "s,debug.log,/tmp/opentk_debug.log,g" -e "s,trace.log,/tmp/opentk_trace.log,g" Main.cs
}

build() {
	cd "$srcdir/opentk-${pkgver//_/-}/Source/Build.UpdateVersion"
	xbuild Build.UpdateVersion.csproj /p:Configuration=Release
	cd ../..
	xbuild OpenTK.sln /p:Configuration=Release
	cd Documentation
	doxygen
}

package_opentk() {
	pkgdesc="Open source game development toolkit for .Net/Mono."
	depends=(mono sdl2 openal)
	cd "$srcdir/opentk-${pkgver//_/-}/Binaries/OpenTK/Release"
	rm *.xml
	find . -type f -exec install -Dm644 {} "$pkgdir/usr/lib/opentk/"{} \;
	find "$pkgdir" -name 'OpenTK*.dll' -exec gacutil -i {} -root "$pkgdir/usr/lib" \;
	cd ../../../Documentation
	install -Dm644 "License.txt" "$pkgdir/usr/share/licenses/$pkgname/License.txt"
	install -Dm644 "$srcdir/opentk.pc.in" "$pkgdir/usr/lib/pkgconfig/opentk.pc"
	install -m644 "$srcdir/opentk-winforms.pc.in" "$pkgdir/usr/lib/pkgconfig/opentk-winforms.pc"
	install -m644 "$srcdir/opentk-compat.pc.in" "$pkgdir/usr/lib/pkgconfig/opentk-compat.pc"
	find "$pkgdir/usr/lib/pkgconfig" -type f -exec sed -i "s|@VERSION@|${pkgver//_/-}|" {} \;;
}

package_opentk-docs() {
	pkgdesc="OpenTK documentation"
	cd "$srcdir/opentk-${pkgver//_/-}/Documentation/Source"
	find . -type f -exec install -Dm644 {} "$pkgdir/usr/share/doc/opentk/"{} \;
}
