# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=servo
pkgver=0.0.4
pkgrel=2
pkgdesc='Parallel Browser Project: web browser written in Rust'
arch=(x86_64 i686)
url=https://github.com/servo/servo
license=(MPL-2.0)
depends=(bzip2
         fontconfig
         freetype2
         glu
         gst-plugins-bad
         libgl
         libxcursor
         libxi
         libxmu
         libxrandr
         mesa
         python-dbus
         ttf-font
         xcb-util)
install="$pkgname.install"
makedepends=(clang
             cmake
             curl
             git
             gperf
             llvm
             python
             python-distlib
             python-virtualenv
             rust
             uv)
options=('!lto') # lto breaks linking
backup=("etc/profile.d/$pkgname".{csh,sh})
source=("$pkgname::git+$url.git#tag=v$pkgver")
sha256sums=('09acfa3a96c5aa93fa974cef20bd5a3e19d6bdaafd8156feee80ecdc926fcaca')

prepare() {
	cd "$pkgname"
	echo 'export PATH=$PATH:/opt/servo' > "$pkgname.sh"
	echo 'setenv PATH ${PATH}:/opt/servo' > "$pkgname.csh"
	cargo fetch --locked --target "$(rustc --print host-tuple)"
}

build() {
	cd "$pkgname"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	./mach build --release
}

package() {
	servopath=$pkgname/target/release
	install -Dm0755 -t "$pkgdir/opt/servo/" "$servopath/servo"
	install -d "$pkgdir/opt/servo/resources/"
	cp -r $pkgname/resources/* "$pkgdir/opt/servo/resources"
	cd "$pkgname"
	install -Dm0755 -t "$pkgdir/etc/profile.d/" "$pkgname".{csh,sh}
}
