# Maintainer: spookyintheam <spookyintheam@protonmail.com>

pkgname=catppuccin-gtk-theme-macchiato
pkgver=0.7.3 
pkgrel=1
pkgdesc='Soothing pastel theme for GTK3 - Macchiato'
arch=('any')
license=('GPL3')
url='https://github.com/catppuccin/gtk'
source=("$pkgname-$pkgver-blue.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Blue-Dark.zip"
        "$pkgname-$pkgver-flamingo.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Flamingo-Dark.zip"
        "$pkgname-$pkgver-green.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Green-Dark.zip"
        "$pkgname-$pkgver-lavender.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Lavender-Dark.zip"
        "$pkgname-$pkgver-maroon.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Maroon-Dark.zip"
        "$pkgname-$pkgver-mauve.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Mauve-Dark.zip"
        "$pkgname-$pkgver-peach.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Peach-Dark.zip"
        "$pkgname-$pkgver-pink.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Pink-Dark.zip"
        "$pkgname-$pkgver-red.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Red-Dark.zip"
        "$pkgname-$pkgver-rosewater.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Rosewater-Dark.zip"
        "$pkgname-$pkgver-sapphire.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Sapphire-Dark.zip"
        "$pkgname-$pkgver-sky.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Sky-Dark.zip"
        "$pkgname-$pkgver-teal.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Teal-Dark.zip"
        "$pkgname-$pkgver-yellow.zip::$url/releases/download/v$pkgver/Catppuccin-Macchiato-Standard-Yellow-Dark.zip")

sha256sums=('f92b5a545a831952b2a55876578fca446954b4569aa24b17b748df4226434cfc'
            'b5b93b769bd33d1d6c471fa571d42e4ebf3077ae7bda3a3bbd7205f0d5c49dd6'
            'deb67edf3b892835cc335ea6dcfff0eaccbc7e8f4c11eb69543b850dbaf80a56'
            '09d0d717c49a86ec4f8dd1023e3cf79f59495de165a667a799adfb848d4caf42'
            'b227d9ea41bb63bccb675cea84967d68d5f8b0bca00d38f27ba0aea6931da2b8'
            '21d53db7eb99b088a2f74959662b176e22bbd63e8dcf85bba1c70994951b40c4'
            '31ca9effb41b141cf6b8b688f1dbb0afeac9b5164396e619bac784e39a22e46b'
            '77e3b40d1722ca1080671defca7961c5df055c2c31ba2c38647bb7364347b387'
            'aee72bcc91f081e05320a9ec1ffefd4769ef3fb5d671efa72e73c00396733164'
            '7bf5923c5cc1ca53a7a1209b2f6a0457506d30848c493b162430f0dd1a4a9a3b'
            '778fe61b718bb77ece0ae1526d8463123ead008ed57e04b237c04d1c8bdf20ac'
            'f4a80dbdf44ebb306dd6d1746d5bf9afa937c46c8c4e18a9f74a9742d623ec38'
            '9a6c68d24fc674e10862f47c536cccc43abcdc5768c1f123c04e5e3300e3126d'
            '09fee29669739ad029f6ba6db1ac997c5fec7fe97754db159f7c0def14978dc0')
package() {
  install -d "$pkgdir/usr/share/themes/"
  cp -r -a --no-preserve=ownership \
    Catppuccin-Macchiato-* "$pkgdir/usr/share/themes"
}
