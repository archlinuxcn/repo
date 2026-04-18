_java_compile=21
_java_runtime=11
pkgname=flynarwhal
_pkgname=FlyNarwhal
pkgver=1.11.3
pkgrel=1
pkgdesc='基于 Compose Multiplatform 框架开发的适用于飞牛影视的跨平台客户端'
url='https://github.com/FNOSP/FlyNarwhal'
arch=('x86_64')
license=('AGPL-3.0-only')
depends=(
  "java-runtime>=${_java_runtime}"
  'alsa-lib'
  'bash'
  'fontconfig'
  'freetype2'
  'giflib'
  'glibc'
  'harfbuzz'
  'lcms2'
  'libgcc'
  'libglvnd'
  'libjpeg-turbo'
  'libpng'
  'libstdc++'
  'libvlc'
  'libx11'
  'libxext'
  'libxi'
  'libxrender'
  'libxtst'
  'zlib'
  'libvlc'
  'vlc-plugin-a52dec'
  'vlc-plugin-alsa'
  'vlc-plugin-aribb24'
  'vlc-plugin-ass'
  'vlc-plugin-bluray'
  'vlc-plugin-cddb'
  'vlc-plugin-dav1d'
  'vlc-plugin-dbus'
  'vlc-plugin-dca'
  'vlc-plugin-dvb'
  'vlc-plugin-dvd'
  'vlc-plugin-faad2'
  'vlc-plugin-ffmpeg'
  'vlc-plugin-firewire'
  'vlc-plugin-flac'
  'vlc-plugin-jpeg'
  'vlc-plugin-kate'
  'vlc-plugin-lirc'
  'vlc-plugin-mad'
  'vlc-plugin-mpeg2'
  'vlc-plugin-mpg123'
  'vlc-plugin-mtp'
  'vlc-plugin-nfs'
  'vlc-plugin-opus'
  'vlc-plugin-png'
  'vlc-plugin-pulse'
  'vlc-plugin-samplerate'
  'vlc-plugin-sftp'
  'vlc-plugin-shout'
  'vlc-plugin-smb'
  'vlc-plugin-soxr'
  'vlc-plugin-speex'
  'vlc-plugin-srt'
  'vlc-plugin-svg'
  'vlc-plugin-theora'
  'vlc-plugin-twolame'
  'vlc-plugin-vorbis'
  'vlc-plugin-x264'
  'vlc-plugin-x265'
  'vlc-plugin-zvbi'
  'vlc-plugins-base'
  'vlc-plugins-extra'
  'vlc-plugins-video-output'
)
makedepends=('git' "java-environment=${_java_compile}")
source=(
  "git+https://github.com/FNOSP/FlyNarwhal.git#tag=v${pkgver}"
  "com.jankinwu.fntv.desktop"
  "247370bc632c4c8325214f7d77057ec5c4e4f382.patch"
)
sha512sums=('0b86aed1403429f879e11adda357e31af3144bd06564bf90c85e5b2c63f17d9a41d4f7247ee64ac1664d25ed3cbb2ddcae3d0090c538724e2de5b0d6025349a8'
            'e67f81709455469198dbf8b13d4c7a4cc9b8243bab8d33fe676d7f7bbb904e984da48bf269a5ca63248446b9db1c2fc106da7c25a667e7cd5373114e6aef8e3f'
            'b343aa87203db41c31c677a3859f02b09e739c9e0c62314f20de3964bec18421833eaa8b84ae62382e5f6e11d5ecc64c0edbcd8fdffa4237baa2502dc7aca31a')

prepare() {
  cd "$srcdir/${_pkgname}"

  patch -p1 < "${srcdir}/247370bc632c4c8325214f7d77057ec5c4e4f382.patch"
}

build() {
  cd "$srcdir/${_pkgname}"
  export PATH="/usr/lib/jvm/java-${_java_compile}-openjdk/bin:$PATH"
  export JAVA_HOME="/usr/lib/jvm/java-${_java_compile}-openjdk"
  ./gradlew composeApp:createReleaseDistributable
}

package() {
  if [ $CARCH == "aarch64" ]; then
    _ARCH=aarch64
  else
    _ARCH=amd64
  fi
  cd "$srcdir/${_pkgname}/composeApp/build/compose/binaries/main-release/app/${_pkgname}"

  install -Dm755 "bin/${_pkgname}" "${pkgdir}/usr/lib/${pkgname}/bin/${_pkgname}"
  install -Dm755 "$srcdir/${_pkgname}/fntv-proxy/linux_${_ARCH}/fntv-proxy" "${pkgdir}/usr/lib/${pkgname}/bin/fntv-proxy"
  cp --reflink=auto -r lib/ "$pkgdir/usr/lib/$pkgname/"

  rm -rf "$pkgdir/usr/lib/$pkgname/lib/app/resources/lib"
  ln -sfr "$pkgdir/usr/lib/vlc" "$pkgdir/usr/lib/$pkgname/lib/app/resources/lib"

  # symlink
  install -dm755 "${pkgdir}/usr/bin"
  ln -sfr "$pkgdir/usr/lib/$pkgname/bin/${_pkgname}" "$pkgdir/usr/bin/${pkgname}"
  
  # icon
  install -Dm644 "lib/${_pkgname}.png" \
    "$pkgdir/usr/share/pixmaps/$pkgname.png"

  # .desktop file
  install -Dm644 "$srcdir/com.jankinwu.fntv.desktop" "${pkgdir}/usr/share/applications/com.jankinwu.fntv.desktop"
}


# vim: ts=2 sw=2 et: