# Maintainer: zxp19821005 <zxp19821005 at 163 dot com>
pkgname=openshot-bin
_pkgname=OpenShot
pkgver=4.1.1
pkgrel=1
pkgdesc="An award-winning free and open-source video editor,is dedicated to delivering high quality video editing and animation solutions to the world."
arch=('x86_64')
url="http://www.openshot.org/"
_ghurl="https://github.com/OpenShot/openshot-qt"
license=('GPL-3.0-or-later')
provides=("${pkgname%-bin}=${pkgver}")
conflicts=("${pkgname%-bin}")
depends=(
    'ffmpeg'
    'glibc'
    'qt5-base'
    'qt5-svg'
    'qt5-x11extras'
    'python'
    'python-pyqt5'
    'python-requests'
    'python-defusedxml'
    'python-pillow'
    'python-certifi'
    'python-urllib3'
    'python-idna'
    'python-chardet'
    'python-charset-normalizer'
    'python-cryptography'
    'aom'
    'libass'
    'libasyncns'
    'libavc1394'
    'babl'
    'libbluray'
    'libbs2b'
    'libbsd'
    'libcaca'
    'cairo'
    'libcdio-paranoia'
    'chromaprint'
    'libdc1394'
    'double-conversion'
    'expat'
    'libffi'
    'fftw'
    'flac'
    'fribidi'
    'libgcrypt'
    'gdk-pixbuf2'
    'glib2'
    'libgme'
    'gmp'
    'gnutls'
    'libgpg-error'
    'graphite'
    'gsm'
    'krb5'
    'lcms2'
    'lilv'
    'liblqr'
    'libtool'
    'lz4'
    'xz'
    'imagemagick'
    'lame'
    'mpg123'
    'libmysofa'
    'ncurses'
    'libnsl'
    'nss'
    'numactl'
    'libogg'
    'openal'
    'ocl-icd'
    'opencv'
    'openjpeg2'
    'libopenmpt'
    'opus'
    'pango'
    'pcre'
    'pcre2'
    'libpgm'
    'pixman'
    'libpng'
    'protobuf'
    'libpulse'
    'libraw1394'
    'librsvg'
    'rubberband'
    'libsamplerate'
    'sdl2'
    'serd'
    'snappy'
    'libsndfile'
    'sndio'
    'libsodium'
    'sord'
    'libsoxr'
    'speex'
    'sratom'
    'libssh'
    'tbb'
    'libthai'
    'libtheora'
    'libtiff'
    'twolame'
    'systemd-libs'
    'libunistring'
    'libusb'
    'vid.stab'
    'libvorbis'
    'libvpx'
    'wavpack'
    'wayland'
    'libwebp'
    'libx11'
    'libxau'
    'libxcb'
    'libxcomposite'
    'libxcursor'
    'libxdamage'
    'libxdmcp'
    'libxext'
    'libxfixes'
    'libxi'
    'libxinerama'
    'libxkbcommon'
    'libxml2'
    'libxrandr'
    'libxrender'
    'libxss'
    'xvidcore'
    'libxv'
    'libxxf86vm'
    'zeromq'
    'zlib'
    'zstd'
    'zvbi'
    'xcb-util'
    'xcb-util-image'
    'xcb-util-keysyms'
    'xcb-util-renderutil'
    'xcb-util-wm'
)
optdepends=(
    'faac: for exporting audio using AAC'
    'python-sentry-sdk: for error reporting'
    'python-simplejson: for JSON handling'
    'python-dbus-next: for DBus integration'
    'python-pyopenssl: for SSL support'
    'codec2: for codec2 support'
    'flite: for text-to-speech'
    'libnorm: for NORM protocol'
    'python-selinux: for SELinux support'
    'shine: for MP3 encoding'
    'slang: for slang library support'
)
options=(
    '!strip'
)
source=(
    "${pkgname%-bin}-${pkgver}-x86_64.AppImage::${_ghurl}/releases/download/v${pkgver}/${_pkgname}-v${pkgver}-${CARCH}.AppImage"
    "${pkgname%-bin}.sh"
)
sha256sums=('662d0c3cec67ddc90df6a8b0c723c0aac0d3bddf0c3c467eff562e818bb8c72f'
            '40912f3657e52129985094b19047ac1d70451342b3933f736bedcd1a807c5e88')
prepare() {
    sed -i -e "
        s/@appname@/${pkgname%-bin}/g
        s/@runname@/${pkgname%-bin}-qt/g
    " "${srcdir}/${pkgname%-bin}.sh"
    rm -rf "${srcdir}/squashfs-root"
    chmod +x "${srcdir}/${pkgname%-bin}-${pkgver}-${CARCH}.AppImage"
    "${srcdir}/${pkgname%-bin}-${pkgver}-${CARCH}.AppImage" --appimage-extract > /dev/null
    sed -i -e "
        s/${pkgname%-bin}-qt-launch/${pkgname%-bin}/g
        s/Icon=${pkgname%-bin}-qt/Icon=${pkgname%-bin}/g
    " "${srcdir}/squashfs-root/usr/share/applications/org.${pkgname%-bin}.${_pkgname}.desktop"
    sed -i "s/org.${pkgname%-bin}.${_pkgname}.desktop/${pkgname%-bin}.desktop/g" \
        "${srcdir}/squashfs-root/usr/share/metainfo/org.${pkgname%-bin}.${_pkgname}.appdata.xml"
}
package() {
    install -Dm755 "${srcdir}/${pkgname%-bin}.sh" "${pkgdir}/usr/bin/${pkgname%-bin}"
    install -Dm755 -d "${pkgdir}/usr/lib/${pkgname%-bin}"
    cp -a "${srcdir}/squashfs-root/usr/bin/"* "${pkgdir}/usr/lib/${pkgname%-bin}"
    install -Dm644 "${srcdir}/squashfs-root/usr/share/applications/org.${pkgname%-bin}.${_pkgname}.desktop" \
        "${pkgdir}/usr/share/applications/${pkgname%-bin}.desktop"
    install -Dm644 "${srcdir}/squashfs-root/usr/share/metainfo/org.${pkgname%-bin}.${_pkgname}.appdata.xml" \
        "${pkgdir}/usr/share/metainfo/${pkgname%-bin}.appdate.xml"
    install -Dm644 "${srcdir}/squashfs-root/usr/share/mime/packages/org.${pkgname%-bin}.${_pkgname}.xml" \
        "${pkgdir}/usr/share/mime/packages/${pkgname%-bin}.xml"
    _icon_sizes=(64x64 128x128 256x256 512x512)
    for _icons in "${_icon_sizes[@]}";do
        install -Dm644 "${srcdir}/squashfs-root/usr/share/icons/hicolor/${_icons}/apps/${pkgname%-bin}-qt.png" \
            "${pkgdir}/usr/share/icons/hicolor/${_icons}/apps/${pkgname%-bin}.png"
    done
    install -Dm644 "${srcdir}/squashfs-root/usr/share/icons/hicolor/scalable/apps/${pkgname%-bin}-qt.svg" \
        "${pkgdir}/usr/share/icons/hicolor/scalable/apps/${pkgname%-bin}.svg"
}
