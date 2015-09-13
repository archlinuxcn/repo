# Maintainer: yesuu zhang <yesuu79@qq.com>

pkgname=vim-fcitx
pkgver=1.2.4
pkgrel=5
pkgdesc="Keep and restore fcitx state for each buffer separately when leaving/re-entering insert mode. Like always typing English in normal mode, but Chinese in insert mode. "
arch=('any')
url="http://www.vim.org/scripts/script.php?script_id=3764"
license=('unknown')
groups=('vim-plugins')
depends=('vim>=7.0')
optdepends=('fcitx: input support')
source=('http://www.vim.org/scripts/download_script.php?src_id=21006')
sha256sums=('4b8560082fa9dae2a895ad8fa60a24392f47d12352072ba019f1fb5350fc1b78')

package() {
	cd ${srcdir}
	install --directory "${pkgdir}/usr/share/vim/vimfiles"
	cp -r plugin "${pkgdir}/usr/share/vim/vimfiles"
	cp -r so "${pkgdir}/usr/share/vim/vimfiles"
}
