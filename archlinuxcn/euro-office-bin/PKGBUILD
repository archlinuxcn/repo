# Maintainer: Felitendo
# This PKGBUILD is updated automatically:
# https://github.com/Felitendo/PKGBUILDS

pkgname=euro-office-bin
pkgver=9.3.5_2
pkgrel=1
pkgdesc="Office suite for documents, spreadsheets, presentations and PDFs, forked from ONLYOFFICE (upstream binary)"
arch=('x86_64' 'aarch64')
url="https://github.com/Euro-Office/DesktopEditors"
license=('AGPL-3.0-only')
# The app ships its own Qt 6, CEF, ICU and FFmpeg in /opt/euro-office. These
# are the libraries the bundle loads from the system (readelf -d over every
# ELF file in it), minus the Qt SQL drivers and Quick3D, which the editors
# never load. curl and xdg-utils are run as programs: curl for downloads,
# xdg-open and xdg-email for links. The fonts are the ones upstream's .deb
# depends on.
depends=('alsa-lib' 'at-spi2-core' 'brotli' 'bzip2' 'cairo' 'curl' 'dbus'
         'expat' 'fontconfig' 'freetype2' 'gdk-pixbuf2' 'glib2' 'glibc' 'gtk3'
         'harfbuzz' 'hicolor-icon-theme' 'krb5' 'libcups' 'libdrm' 'libgcc'
         'libglvnd' 'libnotify' 'libpulse' 'libstdc++' 'libx11' 'libxcb'
         'libxcomposite' 'libxdamage' 'libxext' 'libxfixes' 'libxkbcommon'
         'libxkbcommon-x11' 'libxrandr' 'mesa' 'nspr' 'nss' 'pango' 'sh'
         'ttf-carlito' 'ttf-dejavu' 'ttf-liberation' 'wayland' 'xcb-util'
         'xcb-util-cursor' 'xcb-util-image' 'xcb-util-keysyms'
         'xcb-util-renderutil' 'xcb-util-wm' 'xdg-utils' 'zlib' 'zstd')
optdepends=('ttf-ms-fonts: Microsoft fonts'
            'xdg-user-dirs: --new-document-templates')
provides=("euro-office=${pkgver}" 'euro-office-desktopeditors')
conflicts=('euro-office' 'euro-office-desktopeditors')
options=('!strip' '!debug' '!emptydirs')
# Tags are v<version>-<build> (v9.3.5-2) and the .deb carries the same
# version, so pkgver keeps the build number after an underscore.
_ver="${pkgver/_/-}"
source_x86_64=("${pkgname}-${pkgver}-x86_64.deb::${url}/releases/download/v${_ver}/euro-office-euro-office_${_ver}_amd64.deb")
source_aarch64=("${pkgname}-${pkgver}-aarch64.deb::${url}/releases/download/v${_ver}/euro-office-euro-office_${_ver}_arm64.deb")
noextract=("${pkgname}-${pkgver}-x86_64.deb" "${pkgname}-${pkgver}-aarch64.deb")
sha256sums_x86_64=('d1e9287bfb9278f69ca729e5df3d1dd260f58a2672f506a2efa64a4bb025e5a4')
sha256sums_aarch64=('1c9fac8f76a40b4d99a487569780365140e32148cd42de9bdf08d0feed01693a')

package() {
  # the app in /opt/euro-office plus the launcher, desktop entry, icons and
  # licences upstream's .deb installs
  bsdtar -xOf "$srcdir/${pkgname}-${pkgver}-${CARCH}.deb" 'data.tar.*' \
    | bsdtar -xpf - -C "$pkgdir" --exclude './usr/share/doc' ./opt ./usr

  # the onlyoffice packages own /usr/bin/desktopeditors as well
  rm "$pkgdir/usr/bin/desktopeditors"

  mv "$pkgdir/usr/share/licenses/euro-office-euro-office" \
     "$pkgdir/usr/share/licenses/$pkgname"
}
