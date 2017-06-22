# Maintainer: Figue <ffigue at gmail>
# Contributor: Figue <ffigue at gmail>
# Contributor (Parabola): fauno <fauno@kiwwwi.com.ar>
# Thank you very much to the older contributors:
# Contributor: evr <evanroman at gmail>
# Contributor: Muhammad 'MJ' Jassim <UnbreakableMJ@gmail.com> 

pkgname=icecat
pkgver=52.1.0
_pkgver=${pkgver}-gnu1
_pkgverbase=${pkgver%%.*}
pkgrel=2
pkgdesc="GNU version of the Firefox browser."
arch=(i686 x86_64)
url="http://www.gnu.org/software/gnuzilla/"
license=('GPL' 'MPL' 'LGPL')
depends=('gtk3' 'gtk2' 'mozilla-common' 'libxt' 'startup-notification' 'mime-types' 'dbus-glib' 'alsa-lib' 'ffmpeg'
         'libvpx' 'icu' 'libevent' 'nss' 'hunspell' 'sqlite' 'ttf-font')
makedepends=('unzip' 'zip' 'diffutils' 'python2' 'yasm' 'mesa' 'imake' 'gconf' 'autoconf2.13'
             'libpulse' 'gst-plugins-base-libs' 'inetutils' 'cargo')
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'speech-dispatcher: Text-to-Speech')
source=(http://ftpmirror.gnu.org/gnuzilla/${pkgver}/${pkgname}-${_pkgver}.tar.bz2{,.sig}
#source=(https://ftp.gnu.org/gnu/gnuzilla/${pkgver}/${pkgname}-${_pkgver}.tar.bz2{,.sig}      ## Main upstream download site
#source=(https://mirrors.kernel.org/gnu/gnuzilla/${pkgver}/${pkgname}-${_pkgver}.tar.bz2      ## Good mirror
#source=(http://jenkins.trisquel.info/icecat/${pkgname}-${_pkgver}.tar.bz2      ## Official developer (Ruben Rodriguez) site. Probably only has developer releases.
        mozconfig icecat.desktop icecat-safe.desktop vendor.js
        fix-wifi-scanner.diff no-crmf.diff)

sha256sums=('0beff2a04fdc1b56d274133cd22ff546fd609c929954132ff6bf1b800a5b24f3'
            'SKIP'
            '1fe0c64404ec088ad3900bf482ab9cdd317b2f57c8fcc3b38e9f3321fb237b60'
            'c44eab35f71dd3028a74632463710d674b2e8a0682e5e887535e3233a3b7bbb3'
            '190577ad917bccfc89a9bcafbc331521f551b6f54e190bb6216eada48dcb1303'
            '4b50e9aec03432e21b44d18c4c97b2630bace606b033f7d556c9d3e3eb0f4fa4'
            '9765bca5d63fb5525bbd0520b7ab1d27cabaed697e2fc7791400abc3fa4f13b8'
            'ada119174a2a1779c4195a1b4506e8ae67c49c5306103158805a390237acc1c6')

validpgpkeys=(A57369A8BABC2542B5A0368C3C76EED7D7E04784) # Ruben Rodriguez (GNU IceCat releases key) <ruben@gnu.org>

prepare() {

  cd "${srcdir}/${pkgname}-${pkgver}"

  # Patch to move files directly to /usr/lib/icecat. No more symlinks.
  sed -e 's;$(libdir)/$(MOZ_APP_NAME)-$(MOZ_APP_VERSION);$(libdir)/$(MOZ_APP_NAME);g' -i config/baseconfig.mk
  sed -e 's;$(libdir)/$(MOZ_APP_NAME)-devel-$(MOZ_APP_VERSION);$(libdir)/$(MOZ_APP_NAME)-devel;g' -i config/baseconfig.mk

  # https://bugzilla.mozilla.org/show_bug.cgi?id=1314968
  patch -Np1 -i ../fix-wifi-scanner.diff

  # https://bugs.archlinux.org/task/54395
  patch -Np1 -i ../no-crmf.diff

  msg2 "Starting build..."

  cp -v ${srcdir}/mozconfig .mozconfig

  # WebRTC build tries to execute "python" and expects Python 2
  mkdir -p "$srcdir/path"
  ln -s /usr/bin/python2 "$srcdir/path/python"
}

build() {

  cd "${srcdir}/${pkgname}-${pkgver}"
  ICECATDIR="/usr/lib/${pkgname}" && export ICECATDIR

  # _FORTIFY_SOURCE causes configure failures
  CPPFLAGS+=" -O2"

  # Hardening
  LDFLAGS+=" -Wl,-z,now"

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

