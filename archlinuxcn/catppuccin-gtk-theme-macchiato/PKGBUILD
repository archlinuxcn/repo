# Maintainer: Catppuccin <releases@catppuccin.com>

pkgname=catppuccin-gtk-theme-macchiato
pkgver=0.7.5 # renovate: datasource=github-tags depName=catppuccin/gtk
pkgrel=2
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

sha256sums=('0b7abe8604e9aacc9f2afc92f354000daf60ccf294e6f0b3fe6418de40949d95'
            '88e6b70ce2035c83f1aa5857013637b79e4926d3cc6fc747d5054e2d73bf410b'
            'a1c7c3de5725e327262147715f4dcb3cf35bbc2bc830adab1209689f9bd66790'
            '5a66b0349b243776f0a82cd4569866be6577c2d5907feb474cfb069f6c18395d'
            '40bab01a58f34b0243efef926a0dd1eb19ef06e37c201781334229a5f53252de'
            'b9d0e024ad34036ad99162dacbb49321cb386c0abab0582238b57343ae069193'
            'e01b2958a0bb24bf496b8dce689ab2fd25eb9fd3446bbf211938b90e945119d6'
            'd26da74a5b80d97acdd5d67950e1b920f49c1f93ff2decf178d7c4ef15f0e9e9'
            '5293d168d43520575923b30864683ad0f86b9f520341859ec86973db6b17b700'
            '784814bbbae4af62a57888b6d31d4783303f68144f5681b89ce3e51ff3cef66b'
            '05f74d914789749be21a1e5b1967faa63ed4cdd9a1a3136ef7eb296c5929a7a6'
            '7fa14e3310025406271cb804ed4a8bb624210da8f413e4ffb4a90451ca30ca5f'
            'b3c4da4813cd02e26cb175d16d7d161dd4257989c5a751e5e83b133619ea08f1'
            'f582ff54a1987956f16a73db0c76ab523875e96df97d65c14df88448862315b6')
package() {
  install -d "$pkgdir/usr/share/themes/"
  cp -r -a --no-preserve=ownership \
    Catppuccin-Macchiato-* "$pkgdir/usr/share/themes"
}
