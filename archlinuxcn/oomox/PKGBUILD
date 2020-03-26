# Maintainer: Laurent Treguier <laurent@treguier.org>

_oomox_ver=1.12.5.3
_oomox_theme_ver=1.11.1
_materia_theme_ver=20191017
#_materia_cmt=f1ad3125eea55f4fe88ceab1be83bd51ee5eba48
_arc_theme_ver=20190910
_archdroid_icons_ver=1.0.2
_gnome_colors_icons_ver=5.5.5
_oomoxify_ver=1.2
_base16_cmt=2ddee2a03653850ed2166e7766636bf1dfb21ca5
_numix_icons_cmt=1029e86ec58c387a5b3523380ee17f223f7e2de4
_numix_folders_icons_cmt=24e5f6c6603e7f798553d2f24a00de107713c333
_papirus_icons_ver=20191101
_suru_plus_icons_ver=30.0
_suru_plus_aspromauros_icons_ver=3.0

pkgname=oomox
pkgver=${_oomox_ver}
pkgrel=3
pkgdesc='Themix: GUI for generating different color variations
of Arc, Materia, Oomox themes
(GTK2, GTK3, Cinnamon, GNOME, MATE, Openbox, Xfwm),
ArchDroid, Gnome-Colors, Numix, Papirus, Suru++ icons,
and terminal palettes.
Have a hack for HiDPI in GTK2.'
arch=('i686' 'x86_64')
url='https://github.com/themix-project/oomox'
license=('GPL3')
depends=(
	'gtk3'
	'python-gobject'
	'glib2'  # oomox, materia, arc
	'gdk-pixbuf2'  # oomox, materia, arc
	'gtk-engine-murrine'  # oomox, materia, arc
	'gtk-engines'  # oomox, materia, arc
	'gnome-themes-extra'  # materia
	'sassc'  # oomox, materia, arc
	'librsvg'  # oomox, gnome-colors
	'sed'  # oomox, materia, arc, gnome-colors, archdroid
	'findutils'  # oomox, materia, arc, gnome-colors, arch-droid
	'grep'  # oomoxify, oomox, materia, arc, gnome-colors
	'bc'  # oomoxify, oomox, materia, arc, gnome-colors
	'zip'  # oomoxify
	'polkit'  # oomoxify
	'imagemagick'  # gnome-colors
	'parallel'  # materia, arc
	'optipng'  # materia, arc
	'python-pillow'  # import_pil
	'python-pystache'  #  base16_format
	'python-yaml'  #  base16_format

	'resvg'  # materia, arc
	##or
	#'inkscape'  # materia, arc
)
optdepends=(
	'xorg-xrdb: for the `xresources` theme'
	'breeze-icons: more fallback icons'
	'gksu: for applying Spotify theme from GUI without polkit'
	'colorz: additional image analyzer for "Import colors from image" plugin'
	'python-colorthief: additional image analyzer for "Import colors from image" plugin'
	'python-haishoku: additional image analyzer for "Import colors from image" plugin'
)
options=(
    '!strip'
)
provides=('oomox')
conflicts=('oomox-git')
    # "materia-theme-v${_materia_theme_ver}.tar.gz::https://github.com/nana-4/materia-theme/archive/v${_materia_theme_ver}.tar.gz"
    #"materia-theme-${_materia_theme_ver}.tar.gz::https://github.com/nana-4/materia-theme/archive/v${_materia_theme_ver}.tar.gz"
source=(
    "oomox-${_oomox_ver}.tar.gz::https://github.com/themix-project/oomox/archive/${_oomox_ver}.tar.gz"
    "oomox-gtk-theme-${_oomox_theme_ver}.tar.gz::https://github.com/themix-project/oomox-gtk-theme/archive/${_oomox_theme_ver}.tar.gz"
    "materia-theme-${_materia_theme_ver}.tar.gz::https://github.com/nana-4/materia-theme/archive/v${_materia_theme_ver}.tar.gz"
    "arc-theme-${_arc_theme_ver}.tar.gz::https://github.com/NicoHood/arc-theme/archive/${_arc_theme_ver}.tar.gz"
    "archdroid-icon-theme-${_archdroid_icons_ver}.tar.gz::https://github.com/themix-project/oomox-archdroid-icon-theme/archive/${_archdroid_icons_ver}.tar.gz"
    "gnome-colors-icon-theme-${_gnome_colors_icons_ver}.tar.gz::https://github.com/themix-project/oomox-gnome-colors-icon-theme/archive/${_gnome_colors_icons_ver}.tar.gz"
    "oomoxify-${_oomoxify_ver}.tar.gz::https://github.com/themix-project/oomoxify/archive/${_oomoxify_ver}.tar.gz"
    "base16_mirror-${_base16_cmt}.tar.gz::https://github.com/themix-project/base16_mirror/archive/${_base16_cmt}.tar.gz"
    "numix-icon-theme-${_numix_icons_cmt}.tar.gz::https://github.com/numixproject/numix-icon-theme/archive/${_numix_icons_cmt}.tar.gz"
    "numix-folders-${_numix_folders_icons_cmt}.tar.gz::https://github.com/numixproject/numix-folders/archive/${_numix_folders_icons_cmt}.tar.gz"
    "papirus-icon-theme-${_papirus_icons_ver}.tar.gz::https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/archive/${_papirus_icons_ver}.tar.gz"
    "suru-plus-icon-theme-${_suru_plus_icons_ver}.tar.gz::https://github.com/gusbemacbe/suru-plus/archive/v${_suru_plus_icons_ver}.tar.gz"
    "suru-plus-aspromauros-icon-theme-${_suru_plus_aspromauros_icons_ver}.tar.gz::https://github.com/gusbemacbe/suru-plus-aspromauros/archive/v${_suru_plus_aspromauros_icons_ver}.tar.gz"
)
md5sums=('57a89bdb6bad96991bd6ca1469bc07e0'
         '9fc8a375e6ba92915907fb2119ac41f2'
         '96cb7002228eaf9d91ddde285452daec'
         'd6f731276110588d05b95bd2e0b4cb2f'
         'cb669130685dcbf03a8f7f5738c71dc6'
         '8b4a9a1837211a3caf661ab825d66cb0'
         '4f5164a1e0492f4ae1829c8290da43d6'
         '67be13f352485c70970a1a18bedb9b21'
         '9df0d2aae9a4b8e2e170c9aeb7effc4f'
         '3fcb07cefe43a6a2fe4d977f124624ec'
         'aff32de8ba79cece700d863b0cb74cd1'
         'aba1a105215425e843b60b8edae38241'
         '9b1b8a22afc5ad45c997c8006d13b72d')

prepare() {
    cd ${srcdir}
    cp -pr "${pkgname}-gtk-theme-${_oomox_theme_ver}"/* "${pkgname}-${_oomox_ver}/plugins/theme_oomox/gtk-theme"
    #cp -pr "materia-theme-${_materia_theme_ver}"/* "${pkgname}-${_oomox_ver}/plugins/theme_materia/materia-theme"
	cp -pr "materia-theme-${_materia_theme_ver}"/* "${pkgname}-${_oomox_ver}/plugins/theme_materia/materia-theme"
    cp -pr "arc-theme-${_arc_theme_ver}"/* "${pkgname}-${_oomox_ver}/plugins/theme_arc/arc-theme"
    cp -pr "archdroid-icon-theme-${_archdroid_icons_ver}"/* "${pkgname}-${_oomox_ver}/plugins/icons_archdroid/archdroid-icon-theme"
    cp -pr "gnome-colors-icon-theme-${_gnome_colors_icons_ver}"/* "${pkgname}-${_oomox_ver}/plugins/icons_gnomecolors/gnome-colors-icon-theme"
    cp -pr "oomoxify-${_oomoxify_ver}"/* "${pkgname}-${_oomox_ver}/plugins/oomoxify"
    cp -pr "themix-plugin-base16-${_base16_cmt}"/* "${pkgname}-${_oomox_ver}/plugins/base16/base16_mirror"
    cp -pr "numix-icon-theme-${_numix_icons_cmt}"/* "${pkgname}-${_oomox_ver}/plugins/icons_numix/numix-icon-theme"
    cp -pr "numix-folders-${_numix_folders_icons_cmt}"/* "${pkgname}-${_oomox_ver}/plugins/icons_numix/numix-folders"
    cp -pr "papirus-icon-theme-${_papirus_icons_ver}"/* "${pkgname}-${_oomox_ver}/plugins/icons_papirus/papirus-icon-theme"
    cp -pr "suru-plus-${_suru_plus_icons_ver}"/* "${pkgname}-${_oomox_ver}/plugins/icons_suruplus/suru-plus"
    cp -pr "suru-plus-aspromauros-${_suru_plus_aspromauros_icons_ver}"/* "${pkgname}-${_oomox_ver}/plugins/icons_suruplus_aspromauros/suru-plus-aspromauros"
}

package() {
    _oomox_dir="/opt/${pkgname}"
    _oomox_gui_dir="${_oomox_dir}/oomox_gui"

    cd "${srcdir}/${pkgname}-${_oomox_ver}"
    make DESTDIR="${pkgdir}" APPDIR="${_oomox_dir}" PREFIX="/usr" install
    python -O -m compileall "${pkgdir}/${_oomox_gui_dir}" -d "${_oomox_gui_dir}"
}
