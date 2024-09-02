
#include "interface.h"

#include "PerfectMatching.h"

#include <memory>

struct matching {
    template<typename... Args>
    matching(Args&&... args)
    : actual(std::forward<Args>(args)...)
    {
    }

    PerfectMatching actual;
};

#ifdef __cplusplus
extern "C" {
#endif


matching_t matching_construct(int32_t node_num, int32_t edge_num_max) {
    matching_t result = nullptr;
    result = new matching(node_num, edge_num_max);
    return result;
}

void matching_destruct(matching_t matching) {
    delete matching;
}

int32_t matching_add_edge(matching_t matching, int32_t first_node, int32_t second_node, int32_t cost) {
    return matching->actual.AddEdge(first_node, second_node, cost);
}

void matching_solve(matching_t matching) {
    matching->actual.Solve();
}

int32_t matching_get_match(matching_t matching, int32_t node) {
    return matching->actual.GetMatch(node);
}

void matching_verbose(matching_t matching, bool verbose) {
    matching->actual.options.verbose = verbose;
}

int blossom5_julia_version_major() {
    return 0;
}

int blossom5_julia_version_minor() {
    return 4;
}

#ifdef __cplusplus
}
#endif
