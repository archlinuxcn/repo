# Maintainer: Alif <alive4ever at live dot com>

pkgname=tmux-bash-completion
pkgdesc="Bash completion for tmux"
pkgver=r13.847eda6
pkgrel=1
arch=("any")
url="https://github.com/imomaliev/tmux-bash-completion"
license=("custom")
makedepends=('git')
depends=("bash-completion" "tmux")
source=('git+https://github.com/imomaliev/tmux-bash-completion.git')
md5sums=('SKIP')

pkgver() {
	cd "$pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	cd "$pkgname/completions"
	for file in * ; do
		install -Dm644 $file "$pkgdir/usr/share/bash-completion/completions/$file"
	done
}

