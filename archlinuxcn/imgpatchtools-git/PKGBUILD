# Maintainer : Özgür Sarıer <echo b3pndXJzYXJpZXIxMDExNjAxMTE1QGdtYWlsLmNvbQo= | base64 -d>
# Maintainer : Simon Shi <simonsmh@gmail.com>

_pkgname=imgpatchtools
pkgname="${_pkgname}-git"
pkgver=0.3.r11.g30dcd07
pkgrel=1
pkgdesc="Patch img files with system.patch.dat, like OTA zip on PC"
arch=(x86_64 aarch64)
url="https://github.com/erfanoabdi/imgpatchtools"
license=(GPL3)
makedepends=(git zlib bzip2 openssl)
source=("git+$url.git")
sha256sums=(SKIP)

pkgver() {
	cd "$_pkgname"
	git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cd "$_pkgname"
	for dir in "applypatch" "android-base" "edify" "minzip" "otafault" "blockimg"
	do
		pushd $dir
		make
		popd
	done
	make all
}

package() {
	cd "$_pkgname"
	install -d "$pkgdir"/usr/bin/
	install -Dm755 bin/* "$pkgdir"/usr/bin/
	install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
