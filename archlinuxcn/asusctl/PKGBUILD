# Maintainer: Fabian Bornschein <fabiscafe@archlinux.org>
# Contributor: Static_Rocket

pkgbase=asusctl
pkgname=(
  asusctl
  rog-control-center
)
pkgver=6.3.4
pkgrel=1
pkgdesc="A control daemon, tools, and a collection of crates for interacting with ASUS ROG laptops"
arch=('x86_64')
url="https://asus-linux.org"
license=('MPL-2.0')
makedepends=(
  clang
  cmake
  fontconfig
  git
  hicolor-icon-theme
  libayatana-appindicator
  libinput
  libusb
  rust
  seatd
  systemd
)
source=("git+https://gitlab.com/asus-linux/asusctl.git#tag=$pkgver")
b2sums=('5066ebfa7edc27c88513671028847178a5b5fbf8b8113a384ba57961025185e80abf9ad7a0429d4b30be2d2dc5fa8ae023ad97239063fcf6571254e68c35d5d0')

prepare() {
  cd "${pkgbase}"

  # Keep rust/cargo build-dependency management inside the build directory
  export CARGO_HOME="${srcdir}/cargo"

  # Follow Rust package guidelines
  ## https://wiki.archlinux.org/title/Rust_package_guidelines
  export RUSTUP_TOOLCHAIN=stable
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "${pkgbase}"

  # Keep rust/cargo build-dependency management inside the build directory
  export CARGO_HOME="${srcdir}/cargo"

  # Follow Rust package guidelines
  ## https://wiki.archlinux.org/title/Rust_package_guidelines
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target

  make build
}

package_asusctl() {
  pkgdesc="${pkgdesc/tools/CLI tools}"
  depends=(
    glibc
    libgcc
    libusb
    systemd
    systemd-libs
  )
  conflicts=(gnome-shell-extension-asusctl-gnome)
  install=asusctl.install
  optdepends=(
    'acpi_call: fan control'
    'asusctltray: tray profile switcher'
    'rog-control-center: app to control asusctl'
    'supergfxctl: hybrid GPU control'
  )

  cd "${pkgbase}"
  export CARGO_HOME="${srcdir}/cargo"
  make DESTDIR="${pkgdir}" \
    install-asusctl \
    install-asusd \
    install-asusd_user \
    install-data-asusd \
    install-data-asusd_user
}

package_rog-control-center() {
  depends=(
    asusctl
    fontconfig
    freetype2
    glibc
    hicolor-icon-theme
    libayatana-appindicator
    libgcc
    libinput
    libxkbcommon
    mesa
    seatd
    systemd-libs
  )
  pkgdesc="App to control asusctl"

  cd "${pkgbase}"
  export CARGO_HOME="${srcdir}/cargo"
  make DESTDIR="${pkgdir}" \
    install-data-rog_gui \
    install-rog_gui
}
