# Maintainer  : farseerfc <farseerfc@archlinuxcn.org>
# Contributor : Fernando "Firef0x" G.P. da Silva <firefgx { aT ) gmail [ d0t } com>
# Contributor : Sander Boom <sander at inflowmotion dot nl> (From sublime-text-dev)
# Contributor : realitygaps <realitygaps at yahoo dot com> (From sublime-text-dev)
# Contributor : ska <skatiger (at} gmail {dot) com> (From sublime-text-imfix)

pkgname=('sublime-text-dev-imfix' 'sublime-text-dev-zh-cn' 'sublime-text-dev-zh-tw')
pkgver=3.3103
pkgrel=1
arch=('i686' 'x86_64')
url="http://www.sublimetext.com/3"
license=('custom')
depends=('desktop-file-utils' 'gtk2' 'libpng')
optdepends=('gksu: sudo-save support')
provides=("sublime-text-dev=${pkgver}" 'sublime-text-nightly')
conflicts=('sublime-text-dev' 'sublime-text-nightly')
options=('!strip')
changelog=README.md

_pkgname=sublime_text_3
_pkgname1="${_pkgname}_imfix"
_branchname="SublimeText-i18n-zh-master"

install=${_pkgname1}.install

source=("${_branchname}.zip::https://github.com/farseerfc/SublimeText-i18n-zh/archive/master.zip"
        "LICENSE"
        "${_pkgname}.sh"
        "${_pkgname1}.sh")
source_i686=("https://download.sublimetext.com/${_pkgname}_build_${pkgver:2}_x32.tar.bz2")
source_x86_64=("http://download.sublimetext.com/${_pkgname}_build_${pkgver:2}_x64.tar.bz2")

sha512sums=('dcdbe5c4aeea56c66f284ca0bd7bc9ff1b31e3e5f63cdc5ae694b90252a6606564e7defa5ad317025b11faa59f962a4d9cc2b3d4355ebd02edbced715892d6f4'
            '54b356867e6699fe88130c183ec76ea631f4afeab1a15f37e9ecd460f726bc7c80f056fd57637c24a67b865522e9d3bb5156414fe3cc5d091be9e1f21ef0f31f'
            '32023ae446a981cbf22c1e7c056d1bec76b1a8c4cba1a625d8314331c947ff3d12adaa24f267794f270de76a1170d19405a57100db1054760bfeeb29950bb5a0'
            '3ed8d47663d6e825ff3321155a65e1afa691fea541b96500d11ac763c55741db5712a307f6695fdf5f6d09a71d195efea494736026612bac5d0e410bc1e43c1f')
sha512sums_i686=('1ed5225be25208a2cd35a0ed6819aa01fd8253c40cf28b1f9408cceb86c67191afcd7cb519f1c04b8c6f0d0fd700a7de83447d343709da679901d22df2f910bf')
sha512sums_x86_64=('b51f25c376c06b4261d9e797fb0374532d2fdf86c96af5a7cf0847cb6f7514a7ceda894a4e9b5c63efe0053f6651f52dced9f438a319ddc4991524199a5b65bc')

build() {
  cp "${srcdir}/${_branchname}/dist/any/desktop/"* .
  cp "${srcdir}/${_branchname}/dist/any/zh_CN/"* .
  cp "${srcdir}/${_branchname}/dist/any/zh_TW/"* .
  cp "${srcdir}/${_branchname}/src/fix/imfix/sublime_imfix.c" .
  gcc -shared -o libsublime-imfix.so `pkg-config --libs --cflags gtk+-2.0` -fPIC sublime_imfix.c
}

_package_common() {
  # Copy everything
  install -d "${pkgdir}/opt"
  cp --preserve=mode -r "${_pkgname}" "${pkgdir}/opt/${_pkgname}"

  # Install IM fix library
  install -Dm755 libsublime-imfix.so \
    ${pkgdir}/opt/${_pkgname}/libsublime-imfix.so

  # Install icons and desktop shortcuts
  for res in 16x16 32x32 48x48 128x128 256x256; do
    install -d "${pkgdir}/usr/share/icons/hicolor/${res}/apps"
    ln -sf "/opt/${_pkgname}/Icon/${res}/sublime-text.png" \
    "${pkgdir}/usr/share/icons/hicolor/${res}/apps/sublime-text.png"
  done

  install -d "${pkgdir}/usr/share/applications"
  install -Dm644 ${_pkgname}.desktop \
    "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -Dm644 ${_pkgname1}.desktop \
    "${pkgdir}/usr/share/applications/${_pkgname1}.desktop"

  # Install bin file
  install -d "${pkgdir}/usr/bin"
  install -Dm755 ${_pkgname}.sh "${pkgdir}/usr/bin/${_pkgname}"
  install -Dm755 ${_pkgname1}.sh "${pkgdir}/usr/bin/${_pkgname1}"

  # Make symbolic links
  ln -sf "/usr/bin/${_pkgname1}" "${pkgdir}/usr/bin/subl3"

  # Install license file
  install -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_sublime-text-dev-imfix() {
  pkgdesc="Sophisticated text editor for code, HTML and prose, development build with Fcitx input method support"

  _package_common
}

package_sublime-text-dev-zh-cn() {
  pkgdesc="Sophisticated text editor for code, HTML and prose, development build with Simplified Chinese translation and Fcitx input method support"

  rm "${_pkgname}/Packages/Default.sublime-package"
  install -Dm644 Default.zh_CN.sublime-package \
    ${_pkgname}/Packages/Default.sublime-package

  _package_common

  # Install license file
  install -Dm644 LICENSE.zh_CN "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.zh_CN"
}

package_sublime-text-dev-zh-tw() {
  pkgdesc="Sophisticated text editor for code, HTML and prose, development build with Traditional Chinese translation and Fcitx input method support"

  rm "${_pkgname}/Packages/Default.sublime-package"
  install -Dm644 Default.zh_TW.sublime-package \
    ${_pkgname}/Packages/Default.sublime-package

  _package_common

  # Install license file
  install -Dm644 LICENSE.zh_TW "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.zh_TW"
}

# vim:set sts=2 sw=2 ts=2 et:
