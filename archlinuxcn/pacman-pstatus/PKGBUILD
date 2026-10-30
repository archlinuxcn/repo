# Author and Maintainer: renyuneyun <renyuneyun@gmail.com>
# Original author: Samantha McVey <samantham@posteo.net>
# Copyright (C) 2017 - 2019
# This file and project are licensed under the GPLv2 or greater at your choice.
# For more information view the license included or visit:
# https://www.gnu.org/licenses/gpl-2.0.html

pkgname=pacman-pstatus
pkgver=0.3.1
pkgrel=1
arch=('any')
url='https://gitlab.com/renyuneyun/pacman-ps'
license=('GPL')
depends=('python')
makedepends=('git')
conflicts=('pacman-ps')
pkgdesc="Provides a command to identify which running processes have files that \
  have changed on disk.  It also provides a pacman hook and pacman-ps to also show \
  which packages own the files that are still open. (forked from samcv's pacman-ps)"
install='pacman-ps.install'

options=('!strip')
source=("git+https://gitlab.com/renyuneyun/pacman-ps#tag=v$pkgver")
md5sums=('SKIP')

package() {
  LICENSE_DIR="/usr/share/licenses"
  BIN_DIR="/usr/bin"
  LIB_DIR="/usr/lib/pacman-ps"
  HOOK_DIR="/etc/pacman.d/hooks"
  MAN_DIR="/usr/share/man/man1"

  repodir=${srcdir}/pacman-ps

  install -D -m 644 ${repodir}/pacman-ps-post.hook ${pkgdir}${HOOK_DIR}/pacman-ps-post.hook
  install -D -m 644 ${repodir}/pacman-ps-pre.hook ${pkgdir}${HOOK_DIR}/pacman-ps-pre.hook

  install -D -m 755 ${repodir}/pacman-ps.py ${pkgdir}${LIB_DIR}/pacman-ps.py
  install -D -m 755 ${repodir}/ps-lsof.py ${pkgdir}${LIB_DIR}/ps-lsof.py

  mkdir -p ${pkgdir}${BIN_DIR}
  ln -sr ${pkgdir}${LIB_DIR}/pacman-ps.py ${pkgdir}${BIN_DIR}/pacman-ps
  ln -sr ${pkgdir}${LIB_DIR}/ps-lsof.py ${pkgdir}${BIN_DIR}/ps-lsof

  install -D -m 755 ${repodir}/pacman-ps-record.sh ${pkgdir}${BIN_DIR}/pacman-ps-record.sh
  install -D -m 755 ${repodir}/pacman-ps-optimize-db.sh ${pkgdir}${BIN_DIR}/pacman-ps-optimize-db.sh

  install -D -m 644 ${repodir}/license.txt ${pkgdir}${LICENSE_DIR}/${pkgname}/license.txt

  install -D -m 644 ${repodir}/pacman-ps.1 ${pkgdir}${MAN_DIR}/pacman-ps.1
}
