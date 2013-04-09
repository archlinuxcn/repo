# Maintainer: Arnaud Fortier <warnaud@gmail.com>
# Maintainer: Philippe DUCRETTET <ecolinux@gmx.com>

pkgname=fvwm-patched
pkgver=2.6.3
pkgrel=1
pkgdesc="A multiple large virtual desktop window manager originally derived from twm patched with http://abdn.ac.uk/~u15dm4/fvwm/ and some other"
url="http://www.fvwm.org"
depends=('imlib' 'fribidi' 'perl' 'libstroke' 'libxpm' 'libxinerama' 'readline' 'libxft' 'librsvg')
conflicts=('fvwm' 'fvwm-devel')
provides=('fvwm''fvwm-devel')
options=('docs')
source=(ftp://ftp.fvwm.org/pub/fvwm/version-2/fvwm-$pkgver.tar.bz2 
        $pkgname.desktop 
	01-fvwm-translucent-menus.patch
	02-ColourBorders.patch
	03-ResizeOutlineThin.patch
	04-Conditionals.patch
	05-FlatSeparators.patch
	06-BorderUnderTitle.patch
	07-InactiveFont.patch
	08-FluxRoundedCorners.patch
	09-TopBorder.patch
	10-ButtonWidth.patch
	11-MultiBorder.patch
	12-FvwmButtonsTips.patch
	13-FvwmIconMan.patch
	14-Hover.patch
	15-FirstItemUnderPointer.patch
	16-TextOffset.patch
	17-ThinGeometryProxy.patch)
md5sums=('9327f4b6951751a4c117c1580d910043'
	 'e298c89dd8f7315c90d839dbac068670'
	 '4b68e51fe69d9e6b124deaa0156bca7a'
	 '8afc398a1072ef4dd5f9ff258c3bb6fa'
	 '01e4a4cee7780315a275b4428802c49f'
	 'fdb78083da0f0149ce4f32392e58a95e'
	 '209e2c1fa66bc5b502fba2cbe3a04f8a'
	 'a4e89818e29436165e99e49819f48464'
	 '1cceee901466d34953910bd598332d2f'
	 'e053d2f34f527a62831563e26b7cdeb7'
	 'df092cf82fce48896f9054697519626f'
	 'a8312189b8e5d9d2c294d7cce66fe271'
	 'ce8d47eea51abe0b594a42d17602b574'
	 'c683c7645d479dfb8bf5ec0b755cbb1e'
	 '64ce6e92d9466e40c462431a76232ddc'
	 '951bd67053093e8a0c253c2ed8af95aa'
	 'c12d238cbefc25bd19879401c327e6fe'
	 'd41d8cd98f00b204e9800998ecf8427e'
	 '9df3958e5b2e1f3c5ed3721e2f3a5cdd')
arch=('i686' 'x86_64')
license=('GPL')

build() {
  cd $startdir/src/fvwm-$pkgver
  #Patching
  # Enables real transparency on menus
  echo "** Applying Translucent menus patch **"
  patch -p0 < $startdir/01-fvwm-translucent-menus.patch || return 1
  # Enables different colours on window's borders
  echo "** Applying ColourBorders patch **"
  patch -p0 < $startdir/02-ColourBorders.patch || return 1
  # Enables a single piwel rectangle when resizing
  echo "** Applying Resize Outline Thin patch **"
  patch -p0 < $startdir/03-ResizeOutlineThin.patch || return 1
  # Enables other conditions for windows :)
  echo "** Applying Conditional patch **"
  patch -p0 < $startdir/04-Conditionals.patch || return 1
  # Enables the use of Flat Separators (single pixel separator)
  echo "** Applying flat separators patch **"
  patch -p0 < $startdir/05-FlatSeparators.patch || return 1
  # Adds a border under the titlebar
  echo "** Applying border under titlebar patch **"
  patch -p0 < $startdir/06-BorderUnderTitle.patch || return 1
  # Enables the use of a different font for Inactive windows
  echo "** Applying inactive fonts patch **"
  patch -p0 < $startdir/07-InactiveFont.patch || return 1
  # A mix of FluxboxHandles and RoundedCorners
  # you can't activate both on the same window
  # Add corners in fluxbox style
  # or add rounded corners
  echo "** Applying FluxRounded Corners patch **"
  patch -p0 < $startdir/08-FluxRoundedCorners.patch || return 1
  # Sets the top border to a single pixel
  echo "** Applying Top Border patch **"
  patch -p0 < $startdir/09-TopBorder.patch || return 1
  # Sets the width of the title buttons
  echo "** Applying Button Width patch **"
  patch -p0 < $startdir/10-ButtonWidth.patch || return 1
  # Enables the use of 8 pixmaps for each borders
  echo "** Applying Multiborder patch **"
  patch -p0 < $startdir/11-MultiBorder.patch || return 1
  # Enables the uses of tips on FvwmButtons
  echo "** Applying FvwmButtonTips patch **"
  patch -p0 < $startdir/12-FvwmButtonsTips.patch || return 1
  # Enables rounded corners on FvwmIconMan
  echo "** Applying FvwmIconMan patch **"
  patch -p0 < $startdir/13-FvwmIconMan.patch || return 1
  # Allows you to specify button pixmaps that will be shown when you move the mouse over the buttons
  echo "** Applying Hover patch **"
  patch -p0 < $startdir/14-Hover.patch || return 1
  # Menus with titles are opened so that the first item is under the pointer without warping
  echo "** Applying First Item Under Pointer patch **"
  patch -p0 < $startdir/15-FirstItemUnderPointer.patch || return 1
  # Enables Offset of the text in TitleBar
  echo "** Applying TextOffset patch **"
  patch -p0 < $startdir/16-TextOffset.patch || return 1
  # The geometry window and proxy windows have a single pixel border
  echo "** Applying ThinGeometry patch **"
  patch -p0 < $startdir/17-ThinGeometryProxy.patch || return 1
  ./configure --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib \
    --with-stroke \
    --enable-perllib \
    --enable-xinerama \
    --enable-bidi \
    --enable-nls --enable-iconv \
    --enable-xft
  make || return 1
  make DESTDIR="${pkgdir}" install || return 1
  install -d "${pkgdir}/etc/fvwm"
  install -D -m644 sample.fvwmrc/* "${pkgdir}/etc/fvwm" || return 1
  rm -f "${pkgdir}"/etc/fvwm/Makefile*
  install -D -m644 ../fvwm-patched.desktop "${pkgdir}/etc/X11/sessions/fvwm-devel.desktop" || return 1
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING" || return 1
}
