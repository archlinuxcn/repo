# Maintainer: jswysnemc <snemc@qq.com>
pkgname=mark-shot
pkgver=0.1.50
pkgrel=1
pkgdesc='Qt 6 Wayland screenshot selection and annotation tool'
arch=('x86_64' 'aarch64')
url='https://github.com/jswysnemc/mark-shot'
license=('MIT')
# FFmpeg 大版本升级时 soname 整体 +1（libavformat.so.62 -> .so.63），
# 只写 'ffmpeg' 会让旧包在新 ffmpeg 上通过依赖检查却无法加载库。
# 这里列出 .so 名，makepkg 打包时自动展开为 libavformat.so=62-64 形式。
depends=('qt6-base' 'qt6-svg' 'qt6-wayland' 'layer-shell-qt' 'pipewire' 'grim' 'wl-clipboard' 'hicolor-icon-theme' 'python'
         'libavcodec.so' 'libavformat.so' 'libavutil.so' 'libavfilter.so' 'libswresample.so' 'libswscale.so')
makedepends=('cmake' 'ninja' 'pkgconf' 'git')
optdepends=(
    'xdg-desktop-portal: portal-based screenshot and screencast backend'
    'xclip: X11 clipboard backend'
    'python-rapidocr: preferred OCR backend'
    'python-pillow: image processing for code scanning'
    'python-zxing-cpp: preferred QR/barcode scanning backend'
    'tesseract: fallback OCR backend'
)
source=("${pkgname}-${pkgver}::git+${url}.git#tag=v${pkgver}")
sha256sums=('SKIP')

build() {
    cmake -S "${pkgname}-${pkgver}" -B build -G Ninja \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DMARK_SHOT_REQUIRE_FFMPEG=ON
    cmake --build build
}

package() {
    DESTDIR="${pkgdir}" cmake --install build
    install -Dm644 "${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
