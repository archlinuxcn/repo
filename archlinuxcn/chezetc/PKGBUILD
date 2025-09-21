# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=chezetc
pkgver=202509.6
pkgrel=1
pkgdesc='Extending chezmoi to manage files under /etc and other root-owned directories'
arch=(any)
url='https://silverrainz.me/chezetc'
license=(MIT)
depends=(bash gettext python python-tomli python-tomli-w)
source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/SilverRainZ/chezetc/archive/refs/tags/$pkgver.tar.gz"
    chezetc
    )

sha256sums=('d10f0f0892ebd00b2a196191ea1e227da160c66d3b1d863425584fcce1926bd8'
            '10c022dc7f78dc00e1aeaad816a932fad7271bc2d2d0e8a4c12d14106471843b')

package() {
    cd "$srcdir"

    install -Dm775 $pkgname "$pkgdir/usr/bin/$pkgname"

    cd "$pkgname-$pkgver"

    install -Dm775 $pkgname "$pkgdir/usr/lib/$pkgname/$pkgname"

    for i in README.rst chezmoi.toml; do
        install -Dm644 $i "$pkgdir/usr/lib/$pkgname/"
    done

    for i in commands completions hooks utils; do
        install -Dm644 $i/* -t "$pkgdir/usr/lib/$pkgname/$i"
    done

    chmod +x "$pkgdir/usr/lib/$pkgname/utils/toml-merge.py"
    chmod +x "$pkgdir/usr/lib/$pkgname/commands/cd"
    chmod +x "$pkgdir/usr/lib/$pkgname/commands/editor"

    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}

# vim: set filetype=sh:
