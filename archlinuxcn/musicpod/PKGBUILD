# Maintainer: Dee.H.Y <dongfengweixiao at hotmail dot com>
# Contributor: Mark Wagie <mark dot wagie at proton dot me>
# This repository is a fork of musicpod-git.
# Before executing makepkg, you can set FVM_CACHE_PATH to $HOME/fvm or the path specified by the cachePath field in the $HOME/.config/fvm/.fvmrc file.

pkgname="musicpod"
pkgver=2.16.0
pkgrel=2
pkgdesc="Music, radio, television and podcast player"
url="https://github.com/ubuntu-flutter-community/musicpod"
license=('GPL-3.0-or-later')
arch=('x86_64' 'aarch64')
depends=(
  'alsa-lib'
  'at-spi2-core'
  'cairo'
  'fontconfig'
  'freetype2'
  'fribidi'
  'gdk-pixbuf2'
  'glib2'
  'glibc'
  'gnutls'
  'gtk3'
  'harfbuzz'
  'lcms2'
  'libarchive'
  'libdrm'
  'libepoxy'
  'libgcc'
  'libglvnd'
  'libnotify'
  'libpulse'
  'libstdc++'
  'libunwind'
  'libva'
  'libvdpau'
  'libx11'
  'libxcb'
  'libxext'
  'libxfixes'
  'libxkbcommon'
  'libxrandr'
  'libxss'
  'libxv'
  'mesa'
  'pango'
  'wayland'
  'xz'
  'zlib'
)
makedepends=(
  'clang'
  'cmake'
  'fvm'
  'git'
  'lld'
  'llvm'
  'ninja'
  'patchelf'
  'rustup'
)

options=('!lto')

_pkgsrc="$pkgname-$pkgver"
_pkgext="tar.gz"
source=("$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext" "org.feichtmeier.Musicpod.desktop")
sha256sums=('a266df60dd79c1b8327da84810cc6ad241eb29b806cda47ea0e6028923634439'
            '2c25d7e7ee10f3e53ac918a39c357c5c338426c0c3b631e63e5ddd525e15fce3')

build() {
  export FVM_CACHE_PATH="$SRCDEST/fvm-cache"

  cd "$_pkgsrc"
  fvm install

  fvm flutter --disable-analytics
  #fvm flutter pub upgrade --major-versions
  fvm flutter --no-version-check pub get
  fvm flutter clean && fvm flutter build linux --release
}

package() {
  if [ $CARCH == "aarch64" ]; then
    FLUTTER_ARCH=arm64
  else
    FLUTTER_ARCH=x64
  fi

  cd "$_pkgsrc/build/linux/$FLUTTER_ARCH/release/bundle"

  install -Dm755 "musicpod" "$pkgdir/usr/lib/$pkgname/$pkgname"
  cp --reflink=auto -r lib/ "$pkgdir/usr/lib/$pkgname/"
  cp --reflink=auto -r data/ "$pkgdir/usr/lib/$pkgname/"

  # runpath
  patchelf --set-rpath '$ORIGIN/lib' "$pkgdir/usr/lib/$pkgname/$pkgname"
  for i in "$pkgdir/usr/lib/$pkgname/lib"/*.so; do
    [ -z "$(patchelf --print-rpath "$i")" ] && continue
    patchelf --set-rpath '$ORIGIN' "$i"
  done

  # symlink
  install -dm755 "${pkgdir}/usr/bin"
  ln -sfr "$pkgdir/usr/lib/$pkgname/$pkgname" "$pkgdir/usr/bin/${pkgname}"

  # icon
  install -Dm644 "$srcdir/$_pkgsrc/snap/gui/$pkgname.png" \
    "$pkgdir/usr/share/pixmaps/$pkgname.png"

  # .desktop file
  install -Dm644 "$srcdir/org.feichtmeier.Musicpod.desktop" "${pkgdir}/usr/share/applications/org.feichtmeier.Musicpod.desktop"

  # license
  install -Dm644 "$srcdir/$_pkgsrc/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"
}
