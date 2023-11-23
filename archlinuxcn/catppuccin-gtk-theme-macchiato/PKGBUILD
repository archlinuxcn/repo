# Maintainer: spookyintheam <spookyintheam@protonmail.com>

pkgname=catppuccin-gtk-theme-macchiato
pkgver=0.7.1 
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

sha256sums=('1474f73a1402b8f8061a6c3f571a21d69e9ba9b8d3a49e7d419eced1d855a43f'
            '74fe0495c638a4535c0d1b96c6887a23eeb538c510190be7119ce2f0053bfdeb'
            '63697f28f844502cae2ce061b0371f87846e5342c00b98fc539a94ce318ca176'
            '720ef77750dc41908408c7b562f5e9720bf45bd031cfe8ea9671d9e0c332739f'
            '3a58c63f2369cdd804172eb664637c857d5cc174b257e3f16410cd167a96588b'
            '9ab5628bb87328c20a02be53c5bb6b83c11be5a8eeecf035e31d958c27878e05'
            '6b49ea07ef6c31a7639e2da68de3c44808efa8b4ae3925782f8261b25244f9bc'
            '14640b91d8545d6c12b16a385f5d89169668370d4702c17f9ffed02c44e59442'
            '88354e7f83d0641cf23ebd08ba9b718347d7531eb42c6c2ce8540feb09ff7bcb'
            'c905456e55bfc8bf038a820ffcf227b21aeb4d98638a56908c289b45192b940b'
            'bd465d18c16e143a0ee3d1dd22e664869c0a2fab2d125d2bb8b74630098aae62'
            '9f21dbeaeb580c6a49958e9d8c8f39c549d120809d91b543d4429164034463c8'
            'f0558c89ddfbb888646d2a90b563062511af1b0169bea11cc105364c352c0c8b'
            'efcca444df907f2736abd069e692d6b0cd9398d3e4b12f5d10d0c79b24c27f00')
package() {
  install -d "$pkgdir/usr/share/themes/"
  cp -r -a --no-preserve=ownership \
    Catppuccin-Macchiato-* "$pkgdir/usr/share/themes"
}
