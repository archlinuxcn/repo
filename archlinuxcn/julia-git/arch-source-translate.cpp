//

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include <string>
#include <filesystem>

static std::string get_srcdir(void)
{
    auto env = getenv("JL_MAKEPKG_SRCDIR");
    if (env) {
        std::string src = env;
        while (src.back() == '/')
            src.pop_back();
        return src;
    }
    return {};
}
static auto srcdir = get_srcdir();
static std::filesystem::path basedir = "/usr/share/julia/base";

extern "C" __attribute__((weak)) void *jl_cstr_to_string(const char *str);

extern "C" void *jl_prepend_cwd(void *str)
{
    std::string cwd = std::filesystem::current_path();
    const char *_filename = (char*)str + sizeof(void*);
    while (_filename[0] == '.' && _filename[1] == '/')
        _filename += 2;
    std::string path = cwd + '/' + _filename;
    if (srcdir.empty()) {
        // Skip
    }
    else if (path.starts_with(srcdir + "/base/")) {
        path = "/usr/share/julia" + path.substr(srcdir.size());
    }
    else if (path.starts_with(srcdir + "/")) {
        path = path.substr(srcdir.size());
    }
    return jl_cstr_to_string(std::string(path).c_str());
}

extern "C" const char *jl_archlinux_translate_filename(const char *_filename)
{
    if (srcdir.empty())
        return _filename;
    while (_filename[0] == '.' && _filename[1] == '/')
        _filename += 2;
    static std::string filename;
    filename = _filename;
    if (filename[0] != '/') {
        filename = basedir / filename;
    }
    else if (filename.starts_with(srcdir + "/doc/")) {
        // no op
    }
    else if (filename.starts_with(srcdir + "/etc/")) {
        // no op
    }
    else if (filename.starts_with(srcdir + '/')) {
        filename = filename.substr(srcdir.size());
    }
    return filename.c_str();
}
