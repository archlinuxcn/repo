# Maintainer: Dylan Araps <dylan.araps@gmail.com>
pkgname=neofetch
pkgver=2.0.2
pkgrel=1
pkgdesc="A CLI system information tool written in BASH that supports displaying images."
arch=('any')
url="https://github.com/dylanaraps/$pkgname"
license=('MIT')
conflicts=(${pkgname}-git)
depends=('bash')
optdepends=(
  'amarok: Current Song'
  'banshee: Current Song'
  'clementine: Current Song'
  'cmus: Current Song'
  'deadbeef: Current Song'
  'feh: Wallpaper Display'
  'gnome-music: Current Song'
  'gnome-screenshot: Take a screenshot'
  'gpmdp-remote: Current Song'
  'imagemagick: Image cropping / Thumbnail creation / Take a screenshot'
  'imlib2: Take a screenshot'
  'lollypop: Current Song'
  'maim: Take a screenshot'
  'moc: Current Song'
  'mpc: Current Song'
  'nitrogen: Wallpaper Display'
  'pragha: Current Song'
  'rhythmbox: Current Song'
  'scrot: Take a screenshot'
  'spotify: Current Song'
  'w3m: Display Images'
  'xdotool: See https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal'
  'xorg-xdpyinfo: Resolution detection (Single Monitor)'
  'xorg-xprop: Desktop Environment and Window Manager'
  'xorg-xrandr: Resolution detection (Multi Monitor + Refresh rates)'
  'xorg-xwininfo: See https://github.com/dylanaraps/neofetch/wiki/Images-in-the-terminal'
)
source=("https://github.com/dylanaraps/${pkgname}/archive/${pkgver}.tar.gz")
md5sums=('e4e2e118cde8de6f7e208d84c62604f5')

package() {
  cd "$srcdir/$pkgname-$pkgver/"
  make DESTDIR="${pkgdir}" install
  install -D -m644 LICENSE.md "$pkgdir/usr/share/licenses/${pkgname}/LICENSE.md"
}
