pkgname="ttf-victor-mono"
pkgdesc="Unoffical Victor Mono(TTF) AUR package"
pkgver=1.5.4
pkgrel=1
arch=("any")
sha256sums=("1d0d51443846800c88536ab5a0e5cfb3557ad7d3fa6d355193953dd6c98c40b6")
url="https://rubjo.github.io/victor-mono/"
source=("https://rubjo.github.io/victor-mono/VictorMonoAll.zip")
license=("custom:OFL")

package(){
   if [[ ! -d "$pkgdir/usr/share/fonts/TTF" ]]; then
	  mkdir -p $pkgdir/usr/share/fonts/TTF
   fi
   install -Dm644 TTF/*.ttf $pkgdir/usr/share/fonts/TTF/
}
