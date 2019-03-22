# Maintainer: CountStarlight <countstarlight@gmail.com>
# Maintainer: wszqkzqk <wszqkzqk@gmail.com>
# Maintainer: ssfdust <ssfdust@gmail.com>

pkgname=deepin-wine-tim
pkgver=2.3.2.21158
deepintimver=2.0.0deepin4
pkgrel=6
pkgdesc="Tencent TIM (com.qq.office) on Deepin Wine For Archlinux"
arch=("x86_64")
url="http://tim.qq.com/"
license=('custom')
depends=('p7zip' 'wine' 'wine-mono' 'wine_gecko' 'xorg-xwininfo' 'wqy-microhei' 'adobe-source-han-sans-cn-fonts' 'adobe-source-han-serif-cn-fonts' 'lib32-alsa-lib' 'lib32-alsa-plugins' 'lib32-libpulse' 'lib32-openal' 'lib32-mpg123' 'lib32-gnutls')
conflicts=('wine-tim' 'deepin.com.qq.office' 'deepin-tim-for-arch')
install="deepin-wine-tim.install"
_mirror="https://mirrors.ustc.edu.cn/deepin"
source=("$_mirror/pool/non-free/d/deepin.com.qq.office/deepin.com.qq.office_${deepintimver}_i386.deb"
  "https://dldir1.qq.com/qqfile/qq/PCTIM2.3.2/21158/TIM${pkgver}.exe"
  "run.sh"
  "reg_files.tar.bz2"
  "update.policy")
md5sums=('d5c37cb4f960e13111ce24dbc0dd2d58'
  '11477a70c36eee0574860590b4bc8bd0'
  'afeded77e4fc00afaa4e79dee87b38b9'
  'ee35c8c0f69e03bb581ac39007d5cd3a'
  'a66646b473a3fbad243ac1afd64da07a')

build() {
  msg "Extracting DPKG package ..."
  mkdir -p "${srcdir}/dpkgdir"
  tar -xvf data.tar.xz -C "${srcdir}/dpkgdir"
  sed "s/\(Categories.*$\)/\1Network;/" -i "${srcdir}/dpkgdir/usr/share/applications/deepin.com.qq.office.desktop"
  msg "Extracting Deepin Wine TIM archive ..."
  7z x -aoa "${srcdir}/dpkgdir/opt/deepinwine/apps/Deepin-TIM/files.7z" -o"${srcdir}/deepintimdir"
  msg "Removing original outdated TIM directory ..."
  rm -r "${srcdir}/deepintimdir/drive_c/Program Files/Tencent/TIM"
  msg "Adding config files and fonts"
  tar -jxvf reg_files.tar.bz2 -C "${srcdir}/"
  cp userdef.reg "${srcdir}/deepintimdir/userdef.reg"
  cp system.reg "${srcdir}/deepintimdir/system.reg"
  cp update.policy "${srcdir}/deepintimdir/update.policy"
  cp user.reg "${srcdir}/deepintimdir/user.reg"
  ln -sf "/usr/share/fonts/wenquanyi/wqy-microhei/wqy-microhei.ttc" "${srcdir}/deepintimdir/drive_c/windows/Fonts/wqy-microhei.ttc"
  ln -sf "/usr/share/fonts/adobe-source-han-sans/SourceHanSansCN-Medium.otf" "${srcdir}/deepintimdir/drive_c/windows/Fonts/SourceHanSansCN-Medium.otf"
  ln -sf "/usr/share/fonts/adobe-source-han-serif/SourceHanSerifCN-Medium.otf" "${srcdir}/deepintimdir/drive_c/windows/Fonts/SourceHanSerifCN-Medium.otf"
  msg "Repackaging app archive ..."
  7z a -t7z -r "${srcdir}/files.7z" "${srcdir}/deepintimdir/*"
}

package() {
  msg "Preparing icons ..."
  install -d "${pkgdir}/usr/share"
  cp -a ${srcdir}/dpkgdir/usr/share/* "${pkgdir}/usr/share/"
  msg "Copying TIM to /opt/deepinwine/apps/Deepin-TIM ..."
  install -d "${pkgdir}/opt/deepinwine/apps/Deepin-TIM"
  install -m644 "${srcdir}/files.7z" "${pkgdir}/opt/deepinwine/apps/Deepin-TIM/"
  install -m755 "${srcdir}/run.sh" "${pkgdir}/opt/deepinwine/apps/Deepin-TIM/"
  install -m644 "${srcdir}/TIM$pkgver.exe" "${pkgdir}/opt/deepinwine/apps/Deepin-TIM/"
}
