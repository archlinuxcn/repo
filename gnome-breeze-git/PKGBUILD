# Maintainer: TheNumb <me (at) thenumb (dot) eu>

pkgname=gnome-breeze-git
pkgver=42.f8dafee
pkgrel=1
pkgdesc="A GTK theme created to match with the new Plasma 5 Breeze."
arch=('any')
url="https://github.com/dirruk1/gnome-breeze"
license=('LGPL')
optdepends=("gtk2: GTK+2 theme" "gtk3: GTK+3 theme")
makedepends=('git')
conflicts=('gtk-theme-breezy-gtk3' 'gtk-theme-breezy-gtk2' ' gtk-theme-breezy')
source=(${pkgname}::"git+https://github.com/dirruk1/gnome-breeze.git")
md5sums=('SKIP')

pkgver()
{
    cd "${srcdir}/${pkgname}"
    echo "$(git rev-list --count HEAD).$(git rev-parse --short HEAD)"
}
    
package() {
    cd "${srcdir}/${pkgname}"
    find Breeze* -type f -exec install -Dm644 '{}' "$pkgdir/usr/share/themes/{}" \;
}
