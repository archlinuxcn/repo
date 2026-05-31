# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=servo
pkgver=0.2.0
pkgrel=1
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
             glibc
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
sha256sums=('6f4a0a78b8d67bc89953173c7fa8706be4f5200bf9ced2f31985bd87d2040186')

prepare() {
	cd "$pkgname"
	echo 'export PATH=$PATH:/opt/servo' > "$pkgname.sh"
	echo 'setenv PATH ${PATH}:/opt/servo' > "$pkgname.csh"
	cargo fetch --locked --target host-tuple
}

build() {
	cd "$pkgname"
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	./mach build --release
}

package() {
	servopath=$pkgname/target/release
	install -Dm0755 -t "$pkgdir/opt/servo/" "$servopath/servoshell"
	install -d "$pkgdir/opt/servo/resources/"
	cp -r $pkgname/resources/* "$pkgdir/opt/servo/resources"
	cd "$pkgname"
	install -Dm0755 -t "$pkgdir/etc/profile.d/" "$pkgname".{csh,sh}
}
