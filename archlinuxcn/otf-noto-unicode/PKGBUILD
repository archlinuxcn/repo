pkgname=otf-noto-unicode
pkgver=7.3
pkgrel=1
pkgdesc='one Noto to rule them all'
arch=(any)
url='https://github.com/MY1L/Unicode'
source=(https://github.com/MY1L/Unicode/releases/download/NotoUni7/NotoUnicode-${pkgver}.otf
        46-noto-unicode.conf
        66-noto-unicode.conf)
sha256sums=('e575116ace42a06cf586ed9def869c692a427aa5cd338a5a1229a1d506725f1d'
            '055b7d0a079be4d0164b4a4c431e25cf5683710ab995bf4d704a17fbc3eb1be8'
            '3d8b705a13d1fbbdd16f3ef4fb30060bf26bb6a1ae5424a6e55edc89bda88036')

package() {
  install -Dm644 NotoUnicode-${pkgver}.otf -t "$pkgdir"/usr/share/fonts/OTF

  # Install fontconfig files
  install -Dm644 "$srcdir"/*-noto-unicode.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
