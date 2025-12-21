# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=servo
pkgver=0.0.3
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
             gperf
             llvm
             python
             python-distlib
             python-virtualenv
             rustup # doesn't work with system rust
             uv)
options=('!lto') # lto breaks linking
backup=("etc/profile.d/$pkgname".{csh,sh})
source=("$pkgname::git+$url.git#tag=v$pkgver")
sha256sums=('f5de8fd695045704faf351cbc0df0aa8409af72c28e95c2fbe5421bd2e6e5167')

prepare() {
	cd "$pkgname"
	echo 'export PATH=$PATH:/opt/servo' > "$pkgname.sh"
	echo 'setenv PATH ${PATH}:/opt/servo' > "$pkgname.csh"
	# sed -i -e '/install_rust_toolchain/d' python/servo/platform/base.py
	cargo fetch --locked --target "$(rustc --print host-tuple)"
}

build() {
	cd "$pkgname"
	# export RUSTUP_TOOLCHAIN=stable
	export CARGO_TARGET_DIR=target
	rustup component add rust-src rustc-dev llvm-tools-preview
	./mach bootstrap --skip-lints
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
