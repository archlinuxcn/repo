pkgname=udev-hid-bpf
pkgver=2.1.0
_pkgdate=20240704
pkgrel=1
pkgdesc='An automatic HID-BPF loader based on udev events written in rust.'
arch=(x86_64)
url='https://libevdev.pages.freedesktop.org/udev-hid-bpf/tutorial.html'
license=(GPL-2.0-or-later)
depends=(
  systemd-libs
  libelf
  zlib
  glibc
  gcc-libs
)
makedepends=(
  rust
  meson
  git
  cmake
  clang
  libbpf
  bpf
  linux-headers
)
conflicts=(udef-hid-bpf-git)
options=(!lto)
source=("git+https://gitlab.freedesktop.org/libevdev/udev-hid-bpf.git#tag=${pkgver}-${_pkgdate}")
b2sums=('5b190071fd01c2ec32843c19a3a3338ccd51975c88c8d90343ea25153288b9e11258e1a377db60ecf7269723cea87a22a2a8adb7b0ba64012da83c3a97347f98')

prepare() {
  cd udev-hid-bpf

  export RUSTUP_TOOLCHAIN=stable
  #CARGO_HOME="$srcdir/build/cargo-home" cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  local meson_options=(
    -D tests=disabled
    -D vmlinux-h=provided
    -D vmlinux-h-path=/usr/src/linux/vmlinux.h
  )

  arch-meson udev-hid-bpf build "${meson_options[@]}"
  meson compile -C build
}

package() {
  meson install -C build --destdir "${pkgdir}"

  install -Dt "${pkgdir}/usr/include/udev-hid-bpf" -m644 udev-hid-bpf/src/bpf/*.h
}
