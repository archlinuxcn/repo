# Maintainer: SolarAquarion <shlomochoina@gmail.com>
# Contributor/co-maintainer: Miles "oddfox" Robinson <oddfox@gmail.com>
# Contributor/previous maintainer: Shanto <shanto@hotmail.com>
# Contributor/previous maintainer : Fredy García <frealgagu at gmail dot com>
# Contributor: igrekster <igrek+github@fastem.com> 2018.06.21 patch
# Contributor: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: JIN Xiao-Yong <jinxiaoyong@gmail.com>
# Contributor: bohoomil <@zoho.com>
# Infinality Remix patches: Philip Deljanov <philip dot deljanov at gmail dot com>

_pkgbasename=freetype2
pkgname=lib32-$_pkgbasename-infinality-ultimate
pkgver=2.10.1
pkgrel=2
_patchrel=2019.08.21
pkgdesc="TrueType font rendering library with Infinality patches and custom settings by bohoomil with Infinality Remix patches (32-bit)."
arch=(x86_64)
license=('GPL' 'MIT')
url="http://freetype.sourceforge.net"
groups=('infinality-bundle-multilib')
depends=('lib32-zlib' 'lib32-bzip2' 'lib32-libpng' 'lib32-harfbuzz')
makedepends=('gcc-multilib')
conflicts=('lib32-freetype2' 'lib32-freetype2-infinality' 'lib32-freetype2-git-infinality'
           'lib32-freetype2-ubuntu')
provides=('lib32-freetype2' 'lib32-freetype2-infinality' 'libfreetype.so=6-32')
options=('!libtool')
source=(#"https://download-mirror.savannah.gnu.org/releases/freetype/freetype-${pkgver}.tar.gz"{,.sig}
        #"https://download-mirror.savannah.gnu.org/releases/freetype/freetype-doc-${pkgver}.tar.gz"{,.sig}
        #"https://download-mirror.savannah.gnu.org/releases/freetype/ft2demos-${pkgver}.tar.gz"{,.sig}
        https://download.savannah.gnu.org/releases/freetype/freetype-${pkgver}.tar.xz
        https://download.savannah.gnu.org/releases/freetype/freetype-doc-${pkgver}.tar.xz
        https://download-mirror.savannah.gnu.org/releases/freetype/ft2demos-${pkgver}.tar.xz
        0001-Enable-table-validation-modules.patch
        0002-infinality-${pkgver}-${_patchrel}.patch
        0004-Enable-long-PCF-family-names.patch
        0005-freetype-2.5.2-more-demos.patch
        0006-infinality-remix-tweaks.patch
	0004-Properly-handle-phantom-points-for-variation-fonts-5.patch
        freetype2.sh
        infinality-settings.sh
	xft-settings.sh)

#sha256sums=('fccc62928c65192fff6c98847233b28eb7ce05f12d2fea3f6cc90e8b4e5fbe06'
#            '5fdc0fd118a0a82ff36054988b82ea2fc0da2302962b51d14ca2880ee4959fb2'
#            '0466f9c2cd609349b0bd1f1b7b85b1bffc52f72eb492a7195552d86e666d06ba'
#            'ac11a24b62a6c044cc245ea9fa2a0cbd9e2e62f2371873dd33084c28a76e7176'
#            'b2d511399924452297e4f2c039f3b85d22a5e17d115e5d865c27704887d6c519'
#            '54800d4da18611cf9232aad8b63d74a83153a51bb56dd39191678c738ffc8b53'
#            '36484db4b926ed026e7f32570573493b5a9793a129f08d54383a26d65a6af89b'
#            '94493ed2865fd32e5ef8ef3493fcb2ccaaf8be4c9e0eaa7b417fcbc47fe4314d'
#            'f7f8e09c44f7552c883846e9a6a1efc50377c4932234e74adc4a8ff750606467'
#            '1a5c12aa96e2ee66f7316b8ccb7012520b231a2d8ee21cfe4064aa28db35a57c'
#	'4842d1461c240cd0f60a7247ee038271fdb1067107bea9024be6bdbb218d1bd4')

sha256sums=('16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f'
            '2fc160eda64cb6ee9f357c3fd6ef5f1f2b6039f10da650c726b0db49f863341f'
            'b1857376bd3eaad4fdb4bc7894cb557310186856099494f32e8998ddc32b41e8'
            'ac11a24b62a6c044cc245ea9fa2a0cbd9e2e62f2371873dd33084c28a76e7176'
            'afdc909def9d7e839f227a83a4e3b58d4060a28861739f9e1ab5540e60929cc8'
            '54800d4da18611cf9232aad8b63d74a83153a51bb56dd39191678c738ffc8b53'
            '36484db4b926ed026e7f32570573493b5a9793a129f08d54383a26d65a6af89b'
            '94493ed2865fd32e5ef8ef3493fcb2ccaaf8be4c9e0eaa7b417fcbc47fe4314d'
            '38ac61033c349311f1180f5ebf5b5439f1b91bf2978cbd4cbbbcf279f32ae320'
            'f7f8e09c44f7552c883846e9a6a1efc50377c4932234e74adc4a8ff750606467'
            '1a5c12aa96e2ee66f7316b8ccb7012520b231a2d8ee21cfe4064aa28db35a57c'
            '4842d1461c240cd0f60a7247ee038271fdb1067107bea9024be6bdbb218d1bd4')


validpgpkeys=("58E0C111E39F5408C5D3EC76C1A60EACE707FDA5")

prepare() {
  # Rename source dir to allow building the demos
  #mv "${srcdir}/freetype-${pkgver}" "${srcdir}/${pkgname}"
  #mv "${srcdir}/ft2demos-${pkgver}" "${srcdir}/${pkgbase%-infinality}-demos"
  mv freetype-${pkgver} freetype2
  mv ft2demos-${pkgver} freetype2-demos

  #cd "${srcdir}/${pkgbase%-infinality}"
  cd freetype2
  patch -Np1 -i ../0001-Enable-table-validation-modules.patch
  patch -Np1 --verbose -i ../0002-infinality-${pkgver}-${_patchrel}.patch
  patch -Np1 -i ../0004-Enable-long-PCF-family-names.patch
  patch -Np1 --verbose -i ../0006-infinality-remix-tweaks.patch

  # https://bugs.archlinux.org/task/65629
  patch -Np1 -i ../0004-Properly-handle-phantom-points-for-variation-fonts-5.patch

  # Patching FreeType Demos
  #cd ../freetype2-demos
  #patch -Np1 -i ../0005-freetype-2.5.2-more-demos.patch

  # Suppress RPATH
  #sed -i "/X11_LIB:%=-R%/d" "graph/x11/rules.mk"
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  #cd "${srcdir}/${pkgbase%-infinality}"
  cd freetype2
  ./configure --prefix=/usr --disable-static  --with-harfbuzz --with-png --libdir=/usr/lib32
  make

  # Build demos
  #cd "${srcdir}/${pkgbase%-infinality}-demos"
  #cd freetype2-demos
  #make
}

check() {
  #cd "${srcdir}/${pkgbase%-infinality}"
  cd freetype2
  make -k check
}

#package_freetype2-infinality-ultimate() {
#  provides=("${pkgname%-infinality}" "lib${pkgname%2-infinality}.so")
#  conflicts=("${pkgname%-infinality}")
#  install="${pkgname%-infinality}.install"
#  backup=("etc/profile.d/${pkgname%-infinality}.sh")
#  options=("libtool")
#
#  cd "${srcdir}/${pkgname%-infinality}"
#  make DESTDIR="${pkgdir}" install
#  install -Dt "${pkgdir}/etc/profile.d" -m644 "${srcdir}/${pkgname%-infinality}.sh"
#}

#package_freetype2-demos-infinality() {
#  pkgdesc="Freetype tools and demos with Infinality patches and custom settings"
#  depends=("${pkgname%-demos-infinality}" "libx11")
#  provides=("${pkgname%-infinality}")
#  conflicts=("${pkgname%-infinality}")
#
#  cd "${srcdir}/${pkgname%-infinality}"
#  install -d "${pkgdir}/usr/bin"
#  for _i in bin/{f,t}t*; do
#    libtool --mode=install install $_i "${pkgdir}/usr/bin"
#  done
#}

#package_lib32-freetype2-docs-infinality() {
#  pkgdesc="Freetype documentation with Infinality patches and custom settings"
#  depends=("${pkgname%-docs-infinality}")
#  provides=("${pkgname%-infinality}")
#  conflicts=("${pkgname%-infinality}")
#
#  cd "${pkgname%-docs-infinality}"
#  install -d "${pkgdir}/usr/share/doc"
#  cp -a docs "${pkgdir}/usr/share/doc/${pkgname%-docs-infinality}"
#  rm -rf "${pkgdir}"/usr/{include,share,bin}
#}

package() {
  #cd "${srcdir}/${pkgbase%-infinality}"
  cd freetype2
  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{include,share,bin}
}

