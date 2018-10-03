# Maintainer: Josip Ponjavic <josipponjavic at gmail dot com>

pkgname=i3status-rust-git
pkgver=0.9.0.r557.g07e5ffe
pkgrel=1
pkgdesc='Very resourcefriendly and feature-rich replacement for i3status to use with bar programs (like i3bar and swaybar), written in pure Rust'
arch=('x86_64')
url='https://github.com/greshake/i3status-rust'
license=('GPL3')
depends=('libpulse')
makedepends=('git' 'rust')
optdepends=('alsa-utils: For the volume block'
            'curl: For the weather block'
            'lm_sensors: For the temperature block'
            'networkmanager: For the networkmanager block'
            'powerline-fonts: For all themes using the powerline arrow char'
            'pulseaudio: For the volume block'
            'speedtest-cli: For the speedtest block'
            'ttf-font-awesome-4: For the awesome icons'
            'upower: For the battery block')
provides=("${pkgname%-*}")
conflicts=("${pkgname%-*}")
install="${pkgname%-*}.install"
source=("${pkgname%-*}::git+$url")
sha1sums=('SKIP')

pkgver() {
  cd "${pkgname%-*}"
  echo $(grep '^version =' Cargo.toml|head -n1|cut -d\" -f2).r$(git rev-list --count HEAD).g$(git describe --always)
}

build() {
  cd "${pkgname%-*}"
  cargo build --release --features "pulseaudio"
}

package() {
  cd "${pkgname%-*}"
  install -Dm755 target/release/i3status-rs "$pkgdir/usr/bin/i3status-rs"
  install -Dm644 example_config.toml "$pkgdir/usr/share/doc/${pkgname%-*}/examples/example_config.toml"
  install -Dm644 example_icon.toml "$pkgdir/usr/share/doc/${pkgname%-*}/examples/example_icon.toml"
  install -Dm644 example_theme.toml "$pkgdir/usr/share/doc/${pkgname%-*}/examples/example_theme.toml"
}
