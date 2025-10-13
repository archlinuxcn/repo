# Maintainer: Fabian Bornschein <fabiscafe@archlinux.org>
# Contributor: Static_Rocket

pkgbase=asusctl
pkgname=(
  asusctl
  rog-control-center
)
pkgver=6.1.14
pkgrel=0.2
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
b2sums=('fb1228cbf898abd9809a74f7ac161589ee184206d9e66b8930ea2a2cd50d0f17a61b50eea8efdc0397026ff98edcd9cca749b204e632446f8858b26b3777aff7')

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
