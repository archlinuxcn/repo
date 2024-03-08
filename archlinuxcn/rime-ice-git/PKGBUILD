# Maintainer: everyx <lunt.luo#gmail.com>

_pkgbase=rime-ice
pkgbase=rime-ice-git
pkgname=(
  ${_pkgbase}-git
  ${_pkgbase}-pinyin-git
  ${_pkgbase}-double-pinyin-git
  ${_pkgbase}-double-pinyin-abc-git
  ${_pkgbase}-double-pinyin-mspy-git
  ${_pkgbase}-double-pinyin-sogou-git
  ${_pkgbase}-double-pinyin-flypy-git
  ${_pkgbase}-double-pinyin-ziguang-git
)

pkgver=r474.a03b57b
pkgrel=1
pkgdesc="Rime 配置：雾凇拼音 | 长期维护的简体词库"
arch=("any")
url="https://github.com/iDvel/rime-ice"
license=("GPL3")

makedepends=("git" "librime" "rime-prelude" "sed")

source=("${_pkgbase}::git+${url}.git")
sha512sums=("SKIP")

pkgver() {
  cd "${_pkgbase}" &&
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd "${_pkgbase}" &&
    mv default.yaml _default.yaml &&
    # Link essentials.
    for _f in $(pacman -Qql rime-prelude | grep -v "/$"); do ln -sf "$_f" .; done
}

_schemas=(
  rime_ice
  double_pinyin
  double_pinyin_abc
  double_pinyin_mspy
  double_pinyin_sogou
  double_pinyin_flypy
  double_pinyin_ziguang
)

build() {
  cd "${_pkgbase}"

  # 
  # 生成各方案的默认配置文件，注释掉所有非当前方案
  # 
  _suggestion_schemas=$(sed -n '/^schema_list:/,/^$/ {/^schema_list:/d; /^\s*#.*$/d; /^$/d; s/.*schema:\s*//g; s/\s*#.*//g; p }' _default.yaml)

  for _suggestion_schema_name in $_suggestion_schemas; do
    if [[ ! ${_schemas[*]} =~ (^|[[:space:]])"$_suggestion_schema_name"($|[[:space:]]) ]]; then
      sed -i "s/^\s*- schema: $_suggestion_schema_name .*\$/#&/" _default.yaml;
    fi
  done

  for _schema_name in "${_schemas[@]}"; do
    cp -f _default.yaml "${_schema_name}.default.yaml"

    for _suggestion_schema_name in $_suggestion_schemas; do
      if [[ ! $_schema_name =~ (^|[[:space:]])"$_suggestion_schema_name"($|[[:space:]]) ]]; then
        sed -i "s/^\s*- schema: $_suggestion_schema_name .*\$/#&/" "${_schema_name}.default.yaml";
      fi
    done
  done

  # 
  # 编译语料库
  # 
  _schemas_deps=()
  for _schema_name in "${_schemas[@]}"; do
    _deps=()
    mapfile -t _deps <<< "$(sed -n '/dependencies:/,/^$/ {/dependencies:/d; /^$/d; s/.*- *//g; s/ *#.*//g; p }' "$_schema_name.schema.yaml")"
    _schemas_deps=("${_schemas_deps[@]}" "${_deps[@]}")
  done

  mapfile -t _schemas_deps <<< "$(printf "%s\n" "${_schemas_deps[@]}" | sort -u)"

  # 仅编译 _schemas 中列出方案所依赖的语料库，按方案名字符长度排序
  _compile_schemas=("${_schemas_deps[@]}" "${_schemas[@]}")
  for _schema_name in "${_compile_schemas[@]}";
    do rime_deployer --compile "$_schema_name.schema.yaml";
  done

  find . -type l -delete

  rm -f custom_phrase.txt
}

conflicts=("rime-emoji")

_package_schema() {
  _schema_name=$1                                 # 方案名
  _suggestion=${2:-${_schema_name}.default.yaml}  # 默认配置源文件名

  cd "${srcdir}/${_pkgbase}"

  _install_base="${pkgdir}/usr/share/rime-data"

  # 方案默认配置
  install -Dm644 "$_suggestion" "$_install_base/rime_ice_suggestion.yaml"

  # lua
  [ -f "./rime.lua" ] && install -Dm644 ./rime.lua -t "$_install_base/"
  find lua -type f -exec sh -c 'install -Dm644 "$1" -t '"$_install_base"'/$(dirname $1)' shell {} \;

  # 
  # 处理词库
  # 
  # 获取当前方案依赖的所有方案
  _schemas_deps=()
  mapfile -t _schemas_deps <<< "$(
    sed -n '/dependencies:/,/^$/ {
      /dependencies:/d; # 去除 dependencies:
      /^$/d;            # 去除空行
      s/.*- *//g;       # 去除列表标记
      s/ *#.*//g;       # 去除注释部分
      p;                # 打印处理后的结果
    }' "$_schema_name.schema.yaml"
  )"
  mapfile -t _schemas_deps <<< "$(printf "%s\n" "${_schemas_deps[@]}" | sort -u)"

  _compile_schemas=("${_schemas_deps[@]}" "${_schema_name}")
  for _name in "${_compile_schemas[@]}"; do
    # schema 文件
    install -Dm644 "${_name}.schema.yaml" -t "$_install_base/";

    # 预编译的二进制语料库
    install -Dm644 ./build/"${_name}".*.{bin,yaml} -t "$_install_base/build";

    # emoji
    grep -q "opencc_config: emoji.json" "${_name}.schema.yaml" &&
        install -Dm644 ./opencc/* -t "$_install_base/opencc/"

    # __include 文件，例如：symbols.yaml
    _include_files=()
    mapfile -t _include_files <<< "$(
       sed -n '/__include:/ {
          s/ *__include: *//;        # 去除 dictionary: 后的内
          s/:.*//;                   # 去除 dictionary: 后的内
          s/ *#.*//g;                # 去除注释部分
          p;                         # 打印处理后的结果
        }' "$_name.schema.yaml"
    )"
    for _f in "${_include_files[@]}"; do
      if [ -f "${_f}.yaml" ]; then
        install -Dm644 "${_f}.yaml" -t "$_install_base/"
      fi
    done

    # 遍历所有依赖方案，获取所有所有依赖词库
    _dicts=()
    mapfile -t _dicts <<< "$(
      sed -n '/dictionary:/ {
        s/.*: *//;          # 去除 dictionary: 后的内容
        s/ *#.*//;          # 去除注释部分
        s/""//;             # 去除空引号
        /^[[:space:]]*$/d;  # 去除空行
        p;                  # 打印处理后的结果
      }' "$_name.schema.yaml"
    )"

    for _dict in "${_dicts[@]}"; do
      # 处理 import_tables
      _dict_import_tables=()
      mapfile -t _dict_import_tables <<< "$(
        sed -n '/import_tables:/,/^$/ {
          /^[^ ]/d;         # 删除不以空格开头的行
          s/.*: *//;        # 去除: 前内容和后随空格
          s/.*- *//g;       # 去除列表标记
          s/ *#.*//g;       # 去除注释部分
          p;                # 打印处理后的结果
          }' "${_dict}.dict.yaml"
      )"
      install -Dm644 "${_dict}.dict.yaml" -t "$_install_base/";
      
      # 处理 user_dict
      _dict_user_dict=()
      mapfile -t _dict_user_dict <<< "$(
        sed -n '/user_dict:/ {
          s/.*: *//;          # 去除 user_dict: 后的内容
          s/ *#.*//;          # 去除注释部分
          s/""//;             # 去除空引号
          /^[[:space:]]*$/d;  # 去除空行
          p;                  # 打印处理后的结果
        }' "$_name.schema.yaml"
      )"

      _dict_src_files=("${_dict_import_tables[@]}" "${_dict_user_dict[@]}")

      for _table_file in "${_dict_src_files[@]}"; do
        # 遍历词库文件，获取所有依赖词库文件
        for _f in "${_table_file}".*{yaml,txt}; do
          if [ -f "$_f" ]; then
            install -Dm644 "$_f" -t "$_install_base/$(dirname "${_table_file}")"
          fi
        done
      done

    done
  done
}

package_rime-ice-git() {
  pkgdesc='Rime 配置：雾凇拼音 | 长期维护的简体词库'
  provides=(rime-ice)
  conflicts=(
    # ${_pkgbase}
    ${_pkgbase}-pinyin
    ${_pkgbase}-double-pinyin
    ${_pkgbase}-double-pinyin-abc
    ${_pkgbase}-double-pinyin-mspy
    ${_pkgbase}-double-pinyin-sogou
    ${_pkgbase}-double-pinyin-flypy
    ${_pkgbase}-double-pinyin-ziguang
  )

  for _schema_name in "${_schemas[@]}"; do
    _package_schema "${_schema_name}" _default.yaml
  done
}

package_rime-ice-pinyin-git() {
  pkgdesc='Rime 配置：雾凇拼音 | 长期维护的简体词库 - 拼音方案'
  provides=(rime-ice-pinyin)
  conflicts=(
    ${_pkgbase}
    # ${_pkgbase}-pinyin
    ${_pkgbase}-double-pinyin
    ${_pkgbase}-double-pinyin-abc
    ${_pkgbase}-double-pinyin-mspy
    ${_pkgbase}-double-pinyin-sogou
    ${_pkgbase}-double-pinyin-flypy
    ${_pkgbase}-double-pinyin-ziguang
  )

  _package_schema rime_ice
}

package_rime-ice-double-pinyin-git() {
  pkgdesc='Rime 配置：雾凇拼音 | 长期维护的简体词库 - 自然码双拼'
  provides=(rime-ice-double-pinyin)
  conflicts=(
    ${_pkgbase}
    ${_pkgbase}-pinyin
    # ${_pkgbase}-double-pinyin
    ${_pkgbase}-double-pinyin-abc
    ${_pkgbase}-double-pinyin-mspy
    ${_pkgbase}-double-pinyin-sogou
    ${_pkgbase}-double-pinyin-flypy
    ${_pkgbase}-double-pinyin-ziguang
  )
 
  _package_schema double_pinyin
}

package_rime-ice-double-pinyin-abc-git() {
  pkgdesc='Rime 配置：雾凇拼音 | 长期维护的简体词库 - 智能ABC双拼'
  provides=(rime-ice-double-pinyin-abc)
  conflicts=(
    ${_pkgbase}
    ${_pkgbase}-pinyin
    ${_pkgbase}-double-pinyin
    # ${_pkgbase}-double-pinyin-abc
    ${_pkgbase}-double-pinyin-mspy
    ${_pkgbase}-double-pinyin-sogou
    ${_pkgbase}-double-pinyin-flypy
    ${_pkgbase}-double-pinyin-ziguang
  )

  _package_schema double_pinyin_abc
}

package_rime-ice-double-pinyin-mspy-git() {
  pkgdesc='Rime 配置：雾凇拼音 | 长期维护的简体词库 - 微软双拼'
  provides=(rime-ice-double-pinyin-mspy)
  conflicts=(
    ${_pkgbase}
    ${_pkgbase}-pinyin
    ${_pkgbase}-double-pinyin
    ${_pkgbase}-double-pinyin-abc
    # ${_pkgbase}-double-pinyin-mspy
    ${_pkgbase}-double-pinyin-sogou
    ${_pkgbase}-double-pinyin-flypy
    ${_pkgbase}-double-pinyin-ziguang
  )

  _package_schema double_pinyin_mspy
}

package_rime-ice-double-pinyin-sogou-git() {
  pkgdesc='Rime 配置：雾凇拼音 | 长期维护的简体词库 - 搜狗双拼'
  provides=(rime-ice-double-pinyin-sogou)
  conflicts=(
    ${_pkgbase}
    ${_pkgbase}-pinyin
    ${_pkgbase}-double-pinyin
    ${_pkgbase}-double-pinyin-abc
    ${_pkgbase}-double-pinyin-mspy
    # ${_pkgbase}-double-pinyin-sogou
    ${_pkgbase}-double-pinyin-flypy
    ${_pkgbase}-double-pinyin-ziguang
  )

  _package_schema double_pinyin_sogou
}

package_rime-ice-double-pinyin-flypy-git() {
  pkgdesc='Rime 配置：雾凇拼音 | 长期维护的简体词库 - 小鹤双拼'
  provides=(rime-ice-double-pinyin-flypy)
  conflicts=(
    ${_pkgbase}
    ${_pkgbase}-pinyin
    ${_pkgbase}-double-pinyin
    ${_pkgbase}-double-pinyin-abc
    ${_pkgbase}-double-pinyin-mspy
    ${_pkgbase}-double-pinyin-sogou
    # ${_pkgbase}-double-pinyin-flypy
    ${_pkgbase}-double-pinyin-ziguang
  )

  _package_schema double_pinyin_flypy
}

package_rime-ice-double-pinyin-ziguang-git() {
  pkgdesc='Rime 配置：雾凇拼音 | 长期维护的简体词库 - 紫光双拼'
  provides=(rime-ice-double-pinyin-ziguang)
  conflicts=(
    ${_pkgbase}
    ${_pkgbase}-pinyin
    ${_pkgbase}-double-pinyin
    ${_pkgbase}-double-pinyin-abc
    ${_pkgbase}-double-pinyin-mspy
    ${_pkgbase}-double-pinyin-sogou
    ${_pkgbase}-double-pinyin-flypy
    # ${_pkgbase}-double-pinyin-ziguang
  )

  _package_schema double_pinyin_ziguang
}
