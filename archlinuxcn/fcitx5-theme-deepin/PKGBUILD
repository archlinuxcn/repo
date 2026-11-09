# Maintainer: Cryolitia <cryolitia at gmail dot com>

pkgname=fcitx5-theme-deepin
pkgver=1.0.1
pkgrel=3
pkgdesc="Deepin theme for fcitx5"
arch=('any')
url="https://github.com/linuxdeepin/fcitx5-theme-deepin"
license=('CC-BY-SA-4.0')
source=("https://github.com/linuxdeepin/fcitx5-theme-deepin/archive/$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('ce6ba21ee8dda7074f728c1b85f1a74176e9ac95a37c19ece19dfef90a05b579b31615981b4e3bbabe64d73e6cc5abc10edb03e3beaaa602d9a160eac62b3c8c')

package() {
  cd fcitx5-theme-deepin-$pkgver
  for _variant in light dark; do
    _variant_name=deepin-$_variant
    install -Dvm644 -t "$pkgdir"/usr/share/fcitx5/themes/$_variant_name/ $_variant_name/*
  done
}
