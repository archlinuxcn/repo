# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=rime-wanxiang
pkgname=(rime-wanxiang-dict rime-wanxiang-pro-dict rime-wanxiang-data rime-wanxiang-pro-data)
pkgver=13.3.3
pkgrel=1
pkgdesc="万象拼音：词库基于AI筛选和语料辅助筛选精干高效，配合全新语法模型，输入不再纠结。"
arch=(any)
license=('CC-BY-4.0')

url="https://github.com/amzxyz/rime_wanxiang"
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz"
        build.sh)
b2sums=('3e81d4765d8b1e9cb4e1548f4da9d3983861502ed86dae762db952a63b196394421757f661d9bb335d619e458149813b7ec0276166d1686f67514895a6cc31e7'
        'e1c0a4adf4a6175ac1343c9d94d5deb6d3e134b5258111849cc714893bb1fb70d308ffb900969e510087c59489318678a3e4ad88c8a134f03d90722a1202a672')

makedepends=("librime" "rime-prelude" "rime-essay" "sed" "python" "zip" "rsync")

# 拼写方案
declare -A _schemas=(
    # 注释掉的为方案支持不完善
    [flypy]="小鹤双拼"
    [mspy]="微软双拼"
    [zrm]="自然码"
    [sogou]="搜狗双拼"
    [abc]="智能ABC"
    [ziguang]="紫光双拼"
    # [pyjj]="拼音加加"
    # [gbpy]="国标双拼"
    # [lxsq]="乱序17"
    # [zrlong]="自然龙"
    # [hxlong]="汉心龙"
    [pinyin]="全拼"
)

# 辅助码类型
declare -A _fuzhus=(
  [zrm]="自然码"
  [moqi]="墨奇"
  [flypy]="小鹤"
  [hanxin]="汉心"
  [wubi]="五笔前2"
  [tiger]="虎码首末"
  [shouyou]="首右"
)

build() {
    cd "${srcdir}/rime_wanxiang-${pkgver}" || exit 1

    msg2 "release building..."
    bash .github/workflows/scripts/release-build.sh >/dev/null

    msg2 "schema building..."
    bash "${srcdir}"/build.sh
}

_package() {
    cd "${srcdir}"/dist/"${1//rime-wanxiang-/}" || exit 1
    find . -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;
}

package_rime-wanxiang-dict() {
    pkgdesc="万象拼音词库基础数据"
    replaces=("${pkgbase}-dict-zh")
    # shellcheck disable=SC2128
    _package "$pkgname"
}
package_rime-wanxiang-pro-dict() {
    pkgdesc="万象拼音双拼辅助码版词库基础数据"
    replaces=("${pkgbase}-dict-zh")
    conflicts=("$pkgbase-dict")
    # shellcheck disable=SC2128
    _package "$pkgname"
}

package_rime-wanxiang-data() {
    pkgdesc="万象拼音基础数据"
    depends=(lua librime rime-wanxiang-gram-zh-hans)
    optdepends=('libnotify: notification support in lua scripts')
    # shellcheck disable=SC2128
    _package "$pkgname"
}
package_rime-wanxiang-pro-data() {
    pkgdesc="万象拼音双拼辅助码版基础数据"
    depends=(lua librime rime-wanxiang-gram-zh-hans)
    optdepends=('libnotify: notification support in lua scripts')
    conflicts=("$pkgbase-data")
    # shellcheck disable=SC2128
    _package "$pkgname"
}

#
# ${pkgbase}-<schema>
# - ${pkgbase}-data
# - ${pkgbase}-dict-<schema>
#   - ${pkgbase}-dict
#
# ${pkgbase}-pro-<schema>
# - ${pkgbase}-pro-data
# - [${pkgbase}-pro-data-fuzhu]
#   - ${pkgbase}-pro-data-<fuzhu>-fuzhu
#     - ${pkgbase}-pro-dict-<fuzhu>-fuzhu
#       - ${pkgbase}-pro-dict
#
for _schema in "${!_schemas[@]}"; do
    _schema_name=${_schemas[$_schema]}

    # 基础版词库
    _pkgname=${pkgbase}-dict-${_schema} && pkgname+=("${_pkgname}")
    _conflicts=()
    for _schema_c in "${!_schemas[@]}"; do
        [[ "${_schema_c}" == "${_schema}" ]] && continue
        _conflicts+=("${pkgbase}-dict-${_schema_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音标准版词库（${_schema_name}方案）'
        depends=('${pkgbase}-dict=${pkgver}')
        conflicts=(${_conflicts[*]})
        _package ${_pkgname}
    }"

    # 基础版方案
    _pkgname=${pkgbase}-${_schema} && pkgname+=("${_pkgname}")
    _conflicts=()
    for _schema_c in "${!_schemas[@]}"; do
        [[ "${_schema_c}" == "${_schema}" ]] && continue
        _conflicts+=("${pkgbase}-${_schema_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音标准版（${_schema_name}方案）'
        depends=(${pkgbase}-data '${pkgbase}-dict-${_schema}=${pkgver}')
        conflicts=(${_conflicts[*]})
        install='post.install'
        _package ${_pkgname}
    }"

    if [[ $_schema != "pinyin" ]]; then
        # PRO 版方案
        _pkgname=${pkgbase}-pro-${_schema} && pkgname+=("${_pkgname}")
        _conflicts=()
        for _schema_c in "${!_schemas[@]}"; do
            [[ "${_schema_c}" == "${_schema}" ]] && continue
            _conflicts+=("${pkgbase}-pro-${_schema_c}")
        done
        eval "package_${_pkgname}() {
            pkgdesc='万象拼音双拼辅助码版（${_schema_name}方案）'
            depends=(${pkgbase}-pro-data '${pkgbase}-pro-data-fuzhu=${pkgver}')
            conflicts=(${_conflicts[*]})
            install='post.install'
            _package ${_pkgname}-zrm-fuzhu
        }"
    fi
done

for _fuzhu in "${!_fuzhus[@]}"; do
    _fuzhu_name=${_fuzhus[$_fuzhu]}

    # PRO 版词库
    _pkgname=${pkgbase}-pro-dict-${_fuzhu}-fuzhu && pkgname+=("${_pkgname}")
    _conflicts=()
    for _fuzhu_c in "${!_fuzhus[@]}"; do
        [[ "${_fuzhu_c}" == "${_schema}" ]] && continue
        _conflicts+=("${pkgbase}-dict-${_fuzhu_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音双拼辅助码词库（${_fuzhu_name}辅助）'
        depends=('${pkgbase}-pro-dict=${pkgver}')
        conflicts=(${_conflicts[*]})
        _package ${_pkgname}
    }"

    # PRO 版数据
    _pkgname=${pkgbase}-pro-data-${_fuzhu}-fuzhu && pkgname+=("${_pkgname}")
    _conflicts=()
    for _fuzhu_c in "${!_fuzhus[@]}"; do
        [[ "${_fuzhu_c}" == "${_schema}" ]] && continue
        _conflicts+=("${pkgbase}-pro-data-${_fuzhu_c}")
    done
    eval "package_${_pkgname}() {
        pkgdesc='万象拼音双拼辅助码版基础数据（${_fuzhu_name}辅助）'
        depends=('${pkgbase}-pro-dict-${_fuzhu}-fuzhu=${pkgver}')
        conflicts=(${_conflicts[*]})
        provides=('${pkgbase}-pro-data-fuzhu=${pkgver}')
        _package ${_pkgname}
    }"
done
