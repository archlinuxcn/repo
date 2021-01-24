# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Tomas Storck <storcktomas@gmail.com>
# Contributor: Tom Richards <tom@tomrichards.net>

pkgname=neovim-symlinks
pkgver=4
pkgrel=1
pkgdesc='Runs neovim if vi or vim is called'
arch=('any')
depends=('neovim' 'sh')
provides=('vim' 'vi')
conflicts=('vim' 'vi' 'vi-vim-symlink')

package() {
  install -dm755 "$pkgdir/usr/bin/"
  cd "$pkgdir/usr/bin/"

  echo -e '#!/bin/sh\nexec nvim -e "$@"'  > ex
  echo -e '#!/bin/sh\nexec nvim -RZ "$@"' > rview
  echo -e '#!/bin/sh\nexec nvim -Z "$@"'  > rvim
  echo -e '#!/bin/sh\nexec nvim -R "$@"'  > view
  echo -e '#!/bin/sh\nexec nvim -d "$@"'  > vimdiff
  chmod 755 *

  for _link in edit vedit vi vim; do
    ln -s nvim $_link
  done
}
