
#include <stdint.h>

#include "visibility.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct matching* matching_t;

INTERFACE_EXPORT
matching_t matching_construct(int32_t node_num, int32_t edge_num_max);

INTERFACE_EXPORT
void matching_destruct(matching_t matching);

INTERFACE_EXPORT
int32_t matching_add_edge(matching_t matching, int32_t first_node, int32_t second_node, int32_t cost);

INTERFACE_EXPORT
void matching_solve(matching_t matching);

INTERFACE_EXPORT
int32_t matching_get_match(matching_t matching, int32_t node);

INTERFACE_EXPORT
void matching_verbose(matching_t matching, bool verbose);

INTERFACE_EXPORT
int blossom5_julia_version_major();

INTERFACE_EXPORT
int blossom5_julia_version_minor();

#ifdef __cplusplus
}
#endif
