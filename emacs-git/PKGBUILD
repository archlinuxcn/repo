# Maintainer: Pedro A. López-Valencia <https://aur.archlinux.org/users/vorbote>

#######################################################################
# CAVEAT LECTOR
#######################################################################
#
#  Don't run this on a tmpfs unless you have oodles of RAM.
#  When the official git repo started, the size was about
#  200MB. As time passes, it is growing more and more.
#  Final directory size after a build is shy of 1Gb! 
#  Furthermore, the FSF isn't precisely rich and Savannah 
#  network costs aren't cheap. Keep your git checkout!
#
#  Keeping this directory in a safe place preserves the 
#  git repo and the src dir for faster compilation if 
#  you want. You may delete the pkg dir after successfully 
#  creating a package.
#
#  "makepkg -i" is your friend.
#
#######################################################################

#######################################################################
#
# Still reading? Here kid, have enough rope to hang yourself. :-)
#
#######################################################################

#######################################################################
# Assign "YES" to the variable you want enabled, empty otherwise
#######################################################################
GTK3="YES"       # Leave empty to compile with gtk+ 2 support.
LTO=             # Enable link-time optimization. Broken.
CAIRO=           # Very broken for me. Use at own risk.
XWIDGETS=        # Use GTK+ native widgets pulled from webkitgtk.
DOCS_HTML=       # Generate and install html documentation.
DOCS_PDF=        # Generate and install pdf documentation.
#######################################################################

pkgname=emacs-git
pkgver=25.1.50.r126330
pkgrel=1
pkgdesc="GNU Emacs. Master development branch."
arch=('i686' 'x86_64')
url="http://www.gnu.org/software/emacs/"
license=('GPL')
depends=('gpm' 'giflib' 'm17n-lib' 'desktop-file-utils' 'alsa-lib' 'imagemagick')
makedepends=('git')
#######################################################################
#######################################################################
if [[ $GTK3 = "YES" ]]; then depends+=('gtk3'); else depends+=('gtk2'); fi
if [[ $CAIRO = "YES" ]]; then depends+=('cairo'); fi
if [[ $XWIDGETS = "YES" ]]; then
  if [[ $GTK3 = "YES" ]]; then depends+=('webkitgtk'); else depends+=('webkitgtk2'); fi
fi
if [[ $DOCS_PDF = "YES" ]]; then makedepends+=('texlive-core'); fi
#######################################################################
#######################################################################
conflicts=('emacs')
provides=('emacs')
source=("$pkgname::git://git.savannah.gnu.org/emacs.git")
#source=("$pkgname::git+http://git.savannah.gnu.org/r/emacs.git")
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$pkgname"
  printf "%s.r%s" \
    "$(grep AC_INIT configure.ac | \
    sed -e 's/^.\+\ \([0-9]\+\.[0-9]\+\.[0-9]\+\).\+$/\1/')" \
    "$(git rev-list --count HEAD)"
}


# There is no need to run autogen.sh after first checkout.
# Doing so, breaks incremental compilation.
prepare() {
  cd "$srcdir/$pkgname"

  [[ -x configure ]] || ./autogen.sh
}

build() {
  cd "$srcdir/$pkgname"

  # Avoid hardening-wrapper (taken from emacs-pretest, thanks to Thomas Jost).
  export PATH=$(echo "$PATH" | sed 's!/usr/lib/hardening-wrapper/bin!!g')

  local _conf=(
    --prefix=/usr 
    --sysconfdir=/etc 
    --libexecdir=/usr/lib 
    --localstatedir=/var 
    --mandir=/usr/share/man 
    --with-gameuser=:games 
    --with-sound=alsa 
    --with-xft
    --with-modules)

#######################################################################
#######################################################################
  if [[ $GTK3 = "YES" ]]; then 
    _conf+=('--with-x-toolkit=gtk3' '--without-gconf' '--with-gsettings'); 
  else
    _conf+=('--with-x-toolkit=gtk2' '--with-gconf' '--without-gsettings');
  fi
  if [[ $LTO = "YES" ]]; then _conf+=('--enable-link-time-optimization'); fi
  if [[ $CAIRO = "YES" ]]; then _conf+=('--with-cairo'); fi
  if [[ $XWIDGETS = "YES" ]]; then _conf+=('--with-xwidgets'); fi
#######################################################################
#######################################################################

  ./configure "${_conf[@]}"

  # Using "make" instead of "make bootstrap" enables incremental
  # compiling. Less time recompiling. Yay! But if you may 
  # need to use bootstrap sometime, just add it to the command 
  # line.
  # Please note that incremental compilation implies that you 
  # are reusing your src directory!
  make

  # You may need to run this if loaddefs.el files become
  # corrupt.
  #cd "$srcdir/$pkgname/lisp"
  #make autoloads
  #cd ../

  # Optional documentation formats.
  if [[ $DOCS_HTML = "YES" ]]; then make html; fi
  if [[ $DOCS_PDF = "YES" ]]; then make pdf; fi
}

package() {
  cd "$srcdir/$pkgname"

  make DESTDIR="$pkgdir/" install

  # Install optional documentation formats
  if [[ $DOCS_HTML = "YES" ]]; then make DESTDIR="$pkgdir/" install-html; fi
  if [[ $DOCS_PDF = "YES" ]]; then make DESTDIR="$pkgdir/" install-pdf; fi

  # remove conflict with ctags package
  mv "$pkgdir"/usr/bin/{ctags,ctags.emacs}
  mv "$pkgdir"/usr/share/man/man1/{ctags.1.gz,ctags.emacs.1.gz}

  # remove conflict with texinfo
  rm "$pkgdir"/usr/share/info/info.info.gz

  # fix user/root permissions on usr/share files
  find "$pkgdir"/usr/share/emacs/ | xargs chown root:root

  # fix permssions on /var/games
  mkdir -p "$pkgdir"/var/games/emacs
  chmod 775 "$pkgdir"/var/games
  chmod 775 "$pkgdir"/var/games/emacs
  chown -R root:games "$pkgdir"/var/games
}

# vim:set ft=sh ts=2 sw=2 et:
