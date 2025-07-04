# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-dict-cn-nightly
_pkgbase=${pkgname%-nightly}
_schema_version=8.5.2
pkgver=8.5.2+r20250704.143925
pkgrel=1
epoch=1
pkgdesc="万象中文词库"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/rime_wanxiang"
_dict_url="${url}/releases/download/dict-nightly/9-base-zh-dicts.zip"
source=("schema-${_schema_version}.zip::${url}/releases/download/v${_schema_version}/rime-wanxiang-base.zip"
        "${_dict_url}")
b2sums=('SKIP'
        '853fe94038f040cffaacd8c306012b73433bd6cc231476320450d4920a60e5ec5523cca8ff5ec521147377fac5a411fb01565fdf09dbc3beff12bca886c7589e')
provides=("${_pkgbase}=${_schema_version}")
replaces=("${_pkgbase}")

makedepends=(curl rsync librime rime-prelude rime-essay)

pkgver() {
    _last_modified=$(curl -ILs -o /dev/null -w '%header{last-modified}' ${_dict_url})
    _dict_version=$(TZ="Asia/Shanghai" date -d "${_last_modified}" +%Y%m%d.%H%M%S)

    printf "%s+r%s" "${_schema_version}" "${_dict_version}"
}

_schema_folder_name="万象拼音标准版"
build() {
    cd "${srcdir}"

    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    rime_deployer --compile wanxiang.schema.yaml

    find . -type l -delete
}

package() {
    cd "${srcdir}"

    find zh_dicts -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    install -Dm664 ./build/wanxiang.*.bin -t "${pkgdir}"/usr/share/rime-data/build
}
