# Maintainer : Özgür Sarıer <echo b3pndXJzYXJpZXIxMDExNjAxMTE1QGdtYWlsLmNvbQo= | base64 -d>
# Maintainer : Simon Shi <simonsmh@gmail.com>

pkgname=imgpatchtools
pkgver=0.3.r11.g30dcd07
pkgrel=1
pkgdesc="Patch img files with system.patch.dat, like OTA zip on PC"
arch=(x86_64 aarch64)
url="https://github.com/erfanoabdi/imgpatchtools"
license=(GPL3)
makedepends=(git zlib bzip2 openssl)
source=("git+https://github.com/erfanoabdi/$pkgname.git")
sha256sums=(SKIP)

pkgver() {
	cd "$pkgname"
	git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cd "$pkgname"
	mkdir -p bin
	for dir in "applypatch" "android-base" "edify" "minzip" "otafault" "blockimg"
	do
		pushd $dir
		make -j
		popd
	done
	make all -j
}

package() {
	cd "$pkgname"
	install -d "$pkgdir"/usr/bin/
	install -Dm755 bin/* "$pkgdir"/usr/bin/
	install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
