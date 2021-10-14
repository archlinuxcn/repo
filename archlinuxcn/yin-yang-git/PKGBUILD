# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Alexander F. Rødseth <xyproto at archlinux dot org>
# Contributor: neverix <nev at ateverix dot io>
# Contributor: Stepan Shabalin <stomperhomp at gmail dot com>
pkgname=yin-yang-git
pkgver=1.0.beta.r184.gee369f9
pkgrel=1
pkgdesc="Auto Nightmode for KDE, Gnome, Budgie, VSCode, Atom and more"
arch=('any')
url="https://github.com/oskarsh/Yin-Yang"
license=('MIT')
depends=('python-pyqt5' 'python-qtpy' 'python-suntime')
makedepends=('git')
optdepends=('kvantum-qt5: Kvantum theme support')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=("${pkgname%-git}::git+https://github.com/oskarsh/Yin-Yang.git")
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/${pkgname%-git}"
  git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
  cd "$srcdir/${pkgname%-git}"
  install -d "$pkgdir"/{opt/"${pkgname%-git}",usr/share/applications}
  cp -r ./* "$pkgdir/opt/${pkgname%-git}"
  rm -rf "$pkgdir/opt/${pkgname%-git}"/{.github,tests}
  rm -f "$pkgdir/opt/${pkgname%-git}"/{build,install.sh,main.spec,uninstall.sh}
  install -Dm755 "src/${pkgname%-git}" -t "$pkgdir/usr/bin"
  install -Dm644 "src/ui/assets/${pkgname%-git}.svg" -t \
    "$pkgdir/usr/share/icons/hicolor/scalable/apps"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/${pkgname%-git}"
  install -Dm644 assets/yin_yang.json -t \
    "$pkgdir/usr/lib/mozilla/native-messaging-hosts"

  cat <<EOF >"$pkgdir/usr/share/applications/${pkgname%-git}.desktop"
[Desktop Entry]
Type=Application
Version=1.4
Name=Yin & Yang
GenericName=Theme Switcher
Comment=Auto Nightmode for KDE, Gnome, Budgie, VSCode, Atom and more
Path=/opt/yin-yang
Exec=env QT_AUTO_SCREEN_SCALE_FACTOR=1 sh /usr/bin/yin-yang
Icon=/opt/yin-yang/src/ui/assets/yin-yang.svg
Terminal=false
Categories=Utility; System; Settings;
Keywords=night;dark;day;bright;color;theme;
EOF

  chmod 644 "$pkgdir/usr/share/applications/${pkgname%-git}.desktop"
}
