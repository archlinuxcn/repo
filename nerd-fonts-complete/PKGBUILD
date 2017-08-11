# Maintainer: Super Bo <supernbo at gmail dot com>
# Maintainer: glider <samtron1412 {at} gmail {dot} com>
pkgname=nerd-fonts-complete
pkgver=1.1.0
pkgrel=1
pkgdesc="collection of over 20 patched fonts (complete variant) for \
         powerline, devicons, and vim-devicons: includes Droid Sans, \
         Meslo, AnonymousPro, ProFont, Inconsolta, and many more"
arch=('any')
url="https://github.com/ryanoasis/nerd-fonts"
license=('MIT')
depends=('fontconfig' 'xorg-font-utils')
makedepends=('wget')
conflicts=('nerd-fonts-git' 'nerd-fonts-complete-mono-glyphs')
install=$pkgname.install
source=("$pkgname-$pkgver.tar.gz::https://github.com/ryanoasis/nerd-fonts/archive/v$pkgver.tar.gz")
sha256sums=('ee7ae13f09ec576e2fb3da71b8aa217eae152a64e375697f16529b7182cedb27')

prepare() {
  extension="otf"
  nerdfonts_dir="$srcdir/nerd-fonts-$pkgver/patched-fonts"
  fonts_dir="\"$nerdfonts_dir\""
  #
  # Start constructing `find` expression
  #
  implode() {
    # $1 is return variable name
    # $2 is sep
    # $3... are the elements to join
    local retname=$1 sep=$2 ret=$3
    shift 3 || shift $(($#))
    printf -v "$retname" "%s" "$ret${@/#/$sep}"
  }
  find_include="-and -name '*Complete*'"
  find_exclude=

  # Exclude everything we didn’t include
  exclude=("Font Awesome" "Font Linux" "Octicons" "Pomicons" "Nerd Font*Mono" "Windows Compatible")
  for delete in "${include[@]}"; do
    exclude=( "${exclude[@]/$delete}" )
  done
  # Delete empty elements
  for i in "${!exclude[@]}"; do
    [ "${exclude[$i]}" = '' ] && unset exclude[$i]
  done
  if [ ! -z "${exclude[*]}" ]; then
    implode find_exclude "*' -and \! -name '*" "${exclude[@]}"
    find_exclude="-and \! -name '*${find_exclude}*'"
  fi

  # Put it all together into the find command we want
  find_command="find $fonts_dir \( \( -name '*.[o,t]tf' -or -name '*.pcf.gz' \) $find_include $find_exclude \) -type f -print0"

  # Find all the font files and store in array
  files=()
  while IFS=  read -r -d $'\0'; do
    files+=("$REPLY")
  done < <(eval "$find_command")
  #
  # Remove duplicates (i.e. when both otf and ttf version present)
  #
  # Get list of file names without extensions
  files_dedup=( "${files[@]}" )
  for i in "${!files_dedup[@]}"; do
    files_dedup[$i]="${files_dedup[$i]%.*}"
  done

  # Remove duplicates
  for i in "${!files_dedup[@]}"; do
    for j in "${!files_dedup[@]}"; do
      [ $i = $j ] && continue
      if [ "${files_dedup[$i]}" = "${files_dedup[$j]}" ]; then
        ext="${files[$i]##*.}"
        # Only remove if the extension is the one we don’t want
        if [ "$ext" != "$extension" ]; then
          unset files[$i]
        fi
      fi
    done
  done

  # Copy fonts to the NerdFonts directory
  mkdir -p "$srcdir/NerdFonts"
  cp -f "${files[@]}" "$srcdir/NerdFonts"
}

package() {
  install -Dm644 -t $pkgdir/usr/share/fonts/OTF $srcdir/NerdFonts/*.otf
  install -Dm644 -t $pkgdir/usr/share/fonts/TTF $srcdir/NerdFonts/*.ttf
  install -Dm644 -t $pkgdir/usr/share/licenses/$pkgname $srcdir/nerd-fonts-$pkgver/LICENSE
}
