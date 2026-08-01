# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=servo
pkgver=0.4.0
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
backup=("etc/profile.d/$pkgname".{csh,sh})
source=("$pkgname::git+$url.git#tag=$pkgver")
sha256sums=('3936fe51a1a24d2a4ac72c33848c1f72f148282e579dfc32d83df2331027287d')

_srcenv() {
	cd "$pkgname"
	export CARGO_HOME="$srcdir"
	export CARGO_PROFILE_RELEASE_DEBUG=2
	export CARGO_PROFILE_RELEASE_STRIP=false
	export CARGO_PROFILE_RELEASE_LTO=true
	export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
	export CARGO_PROFILE_RELEASE_OPT_LEVEL=3
	export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	CFLAGS+=' -ffat-lto-objects'
	CXXFLAGS+=' -ffat-lto-objects'
	RUSTFLAGS+=" --remap-path-prefix $PWD=/"
}

prepare() {
	_srcenv
	echo 'export PATH=$PATH:/opt/servo' > "$pkgname.sh"
	echo 'setenv PATH ${PATH}:/opt/servo' > "$pkgname.csh"
	cargo fetch --locked --target host-tuple
}

build() {
	_srcenv
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
