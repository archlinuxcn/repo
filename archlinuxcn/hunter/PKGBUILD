# Maintainer: Jean Lucas <jean@4ray.co>

pkgname=hunter
pkgver=1.3.4
pkgrel=2
pkgdesc='ranger-like file browser written in Rust'
arch=(i686 x86_64)
url=https://github.com/rabite0/hunter
license=(WTFPL)
depends=(xdg-utils gst-plugins-base-libs)
makedepends=(rustup)
optdepends=('gst-plugins-good: media support'
            'gst-plugins-bad: media support'
            'gst-plugins-ugly: media support'
            'gst-libav: media support'
            'libsixel: media support'
            'nerd-fonts-complete: supported icon pack'
            'bat: syntax highlighting'
            'highlight: syntax highlighting'
            'libarchive: archive support'
            'p7zip: archive support'
            'w3m: HTML support'
            'links: HTML support'
            'elinks: HTML support'
            'lynx: HTML support'
            'poppler: PDF support'
            'mupdf-tools: PDF support')
source=(hunter-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz)
sha512sums=('dc7d4167037a08645f0480714eb864e5aad99957bd8177d963ad890e258323bf21ec6874bbe4f6cefb337ac0215b8304829d539fbfdc017d8c4fc1a346e47997')

build() {
  cd hunter-$pkgver
  rustup override set nightly
  cargo build --release
}

package() {
  cd hunter-$pkgver
  install -D target/release/hunter{,-media} -t "$pkgdir"/usr/bin
  install -Dm 644 README.md -t "$pkgdir"/usr/share/doc/hunter
  install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/hunter
}
