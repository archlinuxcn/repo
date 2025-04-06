# Maintainer: Fabian Bornschein <fabiscafe@archlinux.org>
# Contributor: Static_Rocket

pkgbase=asusctl
pkgname=(
  asusctl
  rog-control-center
)
pkgver=6.1.12
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
b2sums=('b5117efa0d11d200ad661abcaad7ba9aedb206681a96ad33dbf549b6e6c5663821f36411947198eb8d448c03b6d65f05611fdabf21f0e6d0f8882b2f1df2e5fe')

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

_pick() {
  local p="$1" f d; shift
  for f; do
    d="$srcdir/$p/${f#$pkgdir/}"
    mkdir -p "$(dirname "$d")"
    mv "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

package_asusctl() {
  pkgdesc="${pkgdesc/tools/CLI tools}"
  depends=(
    gcc-libs
    glibc
    hicolor-icon-theme
    libusb
    systemd
    systemd-libs
  )
  conflicts=(gnome-shell-extension-asusctl-gnome)
  install=asusctl.install
  optdepends=(
    'acpi_call: fan control'
    'supergfxctl: hybrid GPU control'
    'asusctltray: tray profile switcher'
    'rog-control-center: app to control asusctl'
  )

  cd "${pkgbase}"
  export CARGO_HOME="${srcdir}/cargo"
  make DESTDIR="${pkgdir}" install

  _pick rogcc "${pkgdir}/usr/bin/rog-control-center" \
     "${pkgdir}/usr/share/applications/rog-control-center.desktop" \
     "${pkgdir}/usr/share/icons/hicolor/512x512/apps/rog-control-center.png" \
     "${pkgdir}/usr/share/rog-gui"
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
  mv rogcc/* "${pkgdir}"
}
