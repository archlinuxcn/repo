# Maintainer: Morgan <morganamilo@archlinux.org>
pkgname=paru
pkgver=2.2.0
pkgrel=1
pkgdesc='Feature packed AUR helper'
url='https://github.com/morganamilo/paru'
source=("$pkgname-$pkgver.tar.gz::https://github.com/Morganamilo/paru/archive/v$pkgver.tar.gz")
backup=("etc/paru.conf")
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
license=('GPL-3.0-or-later')
makedepends=('cargo')
depends=('git' 'pacman>=7.1' 'libalpm.so')
optdepends=('bat: colored pkgbuild printing' 'devtools: build in chroot and downloading pkgbuilds')
sha256sums=('213d55a67605ff69faefa523917fee7168ea5bf143be8cef800fb48c9759f348')

prepare() {
  cd "$pkgname-$pkgver"
  cargo fetch --locked --target "$(rustc -vV | sed -n 's|host: ||p')"
}

build () {
  cd "$srcdir/$pkgname-$pkgver"

  if pacman -T pacman-git > /dev/null; then
    _features+="git,"
  fi

  if [[ $CARCH != x86_64 ]]; then
    export CARGO_PROFILE_RELEASE_LTO=off
  fi

  cargo build --frozen --features "${_features:-}" --release --target-dir target
  ./scripts/mkmo locale/
}

package() {
  cd "$srcdir/$pkgname-$pkgver"

  install -Dm755 target/release/paru "${pkgdir}/usr/bin/paru"
  install -Dm644 paru.conf "${pkgdir}/etc/paru.conf"

  install -Dm644 man/paru.8 "$pkgdir/usr/share/man/man8/paru.8"
  install -Dm644 man/paru.conf.5 "$pkgdir/usr/share/man/man5/paru.conf.5"

  install -Dm644 completions/bash "${pkgdir}/usr/share/bash-completion/completions/paru.bash"
  install -Dm644 completions/fish "${pkgdir}/usr/share/fish/vendor_completions.d/paru.fish"
  install -Dm644 completions/zsh "${pkgdir}/usr/share/zsh/site-functions/_paru"

  install -d "$pkgdir/usr/share/"
  cp -r locale "$pkgdir/usr/share/"
}
