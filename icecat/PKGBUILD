# Maintainer: Figue <ffigue at gmail>
# Contributor: Figue <ffigue at gmail>
# Contributor (Parabola): fauno <fauno@kiwwwi.com.ar>
# Thank you very much to the older contributors:
# Contributor: evr <evanroman at gmail>
# Contributor: Muhammad 'MJ' Jassim <UnbreakableMJ@gmail.com> 

pkgname=icecat
pkgver=45.5.1
_pkgver=${pkgver}-gnu1
_pkgverbase=${pkgver%%.*}
pkgrel=4
pkgdesc="GNU version of the Firefox browser."
arch=(i686 x86_64)
url="http://www.gnu.org/software/gnuzilla/"
license=('GPL' 'MPL' 'LGPL')
depends=('gtk2' 'mozilla-common' 'libxt' 'startup-notification' 'mime-types'
         'dbus-glib' 'alsa-lib' 'ffmpeg' 'desktop-file-utils'
         'libvpx' 'icu' 'libevent' 'nss' 'hunspell' 'sqlite' 'ttf-font')
makedepends=('unzip' 'zip' 'diffutils' 'python2' 'yasm' 'mesa' 'imake' 'gconf'
             'libpulse' 'gst-plugins-base-libs' 'inetutils')
optdepends=('networkmanager: Location detection via available WiFi networks'
            'upower: Battery API')
options=('!emptydirs' '!makeflags')
install=icecat.install
source=(http://ftpmirror.gnu.org/gnuzilla/${pkgver}/${pkgname}-${_pkgver}.tar.bz2{,.sig}
#source=(https://ftp.gnu.org/gnu/gnuzilla/${pkgver}/${pkgname}-${_pkgver}.tar.bz2{,.sig}      ## Main upstream download site
#source=(https://mirrors.kernel.org/gnu/gnuzilla/${pkgver}/${pkgname}-${_pkgver}.tar.bz2      ## Good mirror
#source=(http://jenkins.trisquel.info/icecat/${pkgname}-${_pkgver}.tar.bz2      ## Official developer (Ruben Rodriguez) site. Probably only has developer releases.
        mozconfig
        icecat.desktop
        icecat-safe.desktop
        vendor.js
        gcc6-fix-compilation-for-IceCat.patch
        firefox-gcc-6.0.patch
        mozilla-1228540-1.patch)

sha256sums=('8163e5bc53f69d9f9b0fc5e9f95fae33da8139ae0f902756751cadbaa27e6ee9'
            'SKIP'
            'cafb2793d58f0298cf171b7f8745805cf72a1a6c1252451db5f0f630b95846c0'
            'c44eab35f71dd3028a74632463710d674b2e8a0682e5e887535e3233a3b7bbb3'
            '190577ad917bccfc89a9bcafbc331521f551b6f54e190bb6216eada48dcb1303'
            '4b50e9aec03432e21b44d18c4c97b2630bace606b033f7d556c9d3e3eb0f4fa4'
            '329cf6753d29ae64a4336a8a76ee71f0d331a39132159401e4d11de65b708a07'
            '4d1e1ddabc9e975ed39f49e134559a29e01cd49439e358233f1ede43bf5a52bf'
            'd1ccbaf0973615c57f7893355e5cd3a89efb4e91071d0ec376e429b50cf6ed19')

validpgpkeys=(A57369A8BABC2542B5A0368C3C76EED7D7E04784) # Ruben Rodriguez (GNU IceCat releases key) <ruben@gnu.org>

prepare() {

  cd "${srcdir}/${pkgname}-${pkgver}"

  # Patch to move files directly to /usr/lib/icecat. No more symlinks.
  sed -e 's;$(libdir)/$(MOZ_APP_NAME)-$(MOZ_APP_VERSION);$(libdir)/$(MOZ_APP_NAME);g' -i config/baseconfig.mk
  sed -e 's;$(libdir)/$(MOZ_APP_NAME)-devel-$(MOZ_APP_VERSION);$(libdir)/$(MOZ_APP_NAME)-devel;g' -i config/baseconfig.mk

  # Compilation fix (FS#49243 and FS#49363), internet and Thunderbird package
  patch -Np1 -i $srcdir/gcc6-fix-compilation-for-IceCat.patch
  patch -Np1 -i $srcdir/firefox-gcc-6.0.patch

  # Patch harfbuzz (following Thunderbird in [extra])
  patch -Np1 -i $srcdir/mozilla-1228540-1.patch

  msg2 "Starting build..."

  cp -v ${srcdir}/mozconfig .mozconfig

  # WebRTC build tries to execute "python" and expects Python 2
  mkdir "$srcdir/path"
  ln -s /usr/bin/python2 "$srcdir/path/python"
}

build() {

  cd "${srcdir}/${pkgname}-${pkgver}"
  ICECATDIR="/usr/lib/${pkgname}" && export ICECATDIR

  # _FORTIFY_SOURCE causes configure failures
  CPPFLAGS+=" -O2"

  # Hardening
  LDFLAGS+=" -Wl,-z,now"

  # GCC 6
  CFLAGS+=" -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2"
  CXXFLAGS+=" -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2"

  export PATH="$srcdir/path:$PATH"

  make -f client.mk build
}

package () {

  cd "${srcdir}/${pkgname}-${pkgver}"

  make -f client.mk DESTDIR="${pkgdir}" install

  msg2 "Finishing..."
  install -m755 -d ${pkgdir}/usr/share/applications
  install -m755 -d ${pkgdir}/usr/share/pixmaps

  for i in 16 32 48; do
      install -Dm644 ${srcdir}/${pkgname}-${pkgver}/browser/branding/official/default${i}.png \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/icecat.png"
  done
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/browser/branding/official/default48.png ${pkgdir}/usr/share/pixmaps/icecat.png
  install -Dm644 ${srcdir}/icecat.desktop ${pkgdir}/usr/share/applications/
  install -Dm644 ${srcdir}/icecat-safe.desktop ${pkgdir}/usr/share/applications/

  # implement vendor.js setting the locale to match the os don't disable our languages extensions
  # https://projects.archlinux.org/svntogit/packages.git/commit/trunk/PKGBUILD?h=packages/firefox&id=281a95c2cca0db88904603d7808936f52797a690
  install -Dm644 "${srcdir}"/vendor.js "${pkgdir}${ICECATDIR}/browser/defaults/preferences/vendor.js"

  # We don't want the development stuff
  rm -rv "$pkgdir"/usr/{include,lib/icecat-devel,share/idl}
}

