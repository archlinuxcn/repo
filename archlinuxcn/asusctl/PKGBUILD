# Maintainer: Fabian Bornschein <fabiscafe@archlinux.org>
# Contributor: Static_Rocket

pkgbase=asusctl
pkgname=(
  asusctl
  rog-control-center
)
pkgver=6.3.2
pkgrel=0.1
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
b2sums=('4bf6b850e19551426c2011cfb75e880fad1f7161a6f3200748d4dafe9a26d038676c1ba3df8bc68d4b080146e1f78abca07984860c0034c15ce0b742fe34477c')

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
    gcc-libs
    glibc
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
    gcc-libs
    glibc
    hicolor-icon-theme
    libayatana-appindicator
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
