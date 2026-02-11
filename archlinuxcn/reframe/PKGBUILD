# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=reframe
pkgver=1.11.0
pkgrel=1
pkgdesc="DRM/KMS based remote desktop for Linux that supports Wayland/NVIDIA/headless/login…"
arch=("x86_64" "i686" "aarch64" "armv7h")
url="https://reframe.alynx.one/"
license=("Apache-2.0")
depends=("glib2" "libepoxy" "libvncserver" "libxkbcommon" "libdrm" "systemd-libs" "glibc" "gtk4")
optdepends=("neatvnc: experimental neatvnc implementation")
makedepends=("git" "meson")
backup=("etc/${pkgname}/example.conf")
source=("git+https://github.com/AlynxZhou/${pkgname}.git#tag=v${pkgver}"
        "git+https://github.com/AlynxZhou/mvmath.git")
sha512sums=('SKIP'
            'SKIP')

prepare() {
  cd "${pkgname}"

  git submodule init
  git config submodule.deps/mvmath.url "${srcdir}/mvmath"
  git -c protocol.file.allow=always submodule update --recursive

  mkdir -p build
}

build() {
  cd "${pkgname}/build"

  arch-meson -D neatvnc=true . ..
  meson compile
}

package() {
  cd "${pkgname}/build"

  meson install --destdir "${pkgdir}"
}
