#include "jlcxx/jlcxx.hpp"

#include <lemon/list_graph.h>
#include <lemon/matching.h>

#include <functional>

using namespace lemon;
using namespace std;

std::string compiledebug()
{
   return "baseline compilation works";
}

namespace jlcxx
{
  template<> struct SuperType<ListGraph::NodeIt> { typedef ListGraph::Node type; };
  template<> struct SuperType<ListGraph::EdgeIt> { typedef ListGraph::Edge type; };
  template<> struct SuperType<ListDigraph::NodeIt> { typedef ListDigraph::Node type; };
  // no appropriate factory error
  //template<> struct SuperType<ListDigraph::ArcIt> { typedef ListDigraph::Arc type; };
}

JLCXX_MODULE define_julia_module(jlcxx::Module& mod)
{
  mod.method("compiledebug", &compiledebug);

  mod.add_type<ListGraph::Node>("ListGraphNode");
  mod.add_type<ListDigraph::Node>("ListDigraphNode");
  mod.add_type<ListGraph::Edge>("ListGraphEdge");
  mod.add_type<ListDigraph::Arc>("ListDigraphArc");

  mod.method("id", static_cast<int(*)(ListGraph::Node)>(&ListGraph::id));
  mod.method("id", static_cast<int(*)(ListGraph::Edge)>(&ListGraph::id));
  mod.method("id", static_cast<int(*)(ListDigraph::Node)>(&ListDigraph::id));
  mod.method("id", static_cast<int(*)(ListDigraph::Arc)>(&ListDigraph::id));

  mod.add_type<ListGraph>("ListGraph")
    .method("addNode"  , &ListGraph::addNode)
    .method("addEdge"  , &ListGraph::addEdge);
  mod.add_type<ListDigraph>("ListDigraph")
    .method("addNode"  , &ListDigraph::addNode)
    .method("addArc"   , &ListDigraph::addArc);

  mod.add_type<ListGraph::NodeIt>("ListGraphNodeIt", jlcxx::julia_base_type<ListGraph::Node>())
    .constructor<const ListGraph&>()
    .method("iternext", &ListGraph::NodeIt::operator++);
  mod.add_type<ListDigraph::NodeIt>("ListDigraphNodeIt", jlcxx::julia_base_type<ListDigraph::Node>())
    .constructor<const ListDigraph&>()
    .method("iternext", &ListDigraph::NodeIt::operator++);
  mod.add_type<ListGraph::EdgeIt>("ListGraphEdgeIt", jlcxx::julia_base_type<ListGraph::Edge>())
    .constructor<const ListGraph&>()
    .method("iternext", &ListGraph::EdgeIt::operator++);
  // no appropriate factory error
  //mod.add_type<ListDigraph::ArcIt>("ListDigraphArcIt", jlcxx::julia_base_type<ListDigraph::ArcIt>())
  //  .constructor<const ListDigraph&>()
  //  .method("iternext", &ListDigraph::ArcIt::operator++);

  mod.add_type<ListGraph::NodeMap<int>>("ListGraphNodeMapInt")
    .constructor<const ListGraph&>()
    .method("set", &ListGraph::NodeMap<int>::set);
  mod.add_type<ListDigraph::NodeMap<int>>("ListDigraphNodeMapInt")
    .constructor<const ListDigraph&>()
    .method("set", &ListDigraph::NodeMap<int>::set);
  mod.add_type<ListGraph::EdgeMap<int>>("ListGraphEdgeMapInt")
    .constructor<const ListGraph&>()
    .method("set", &ListGraph::EdgeMap<int>::set);

  mod.add_type<MaxWeightedPerfectMatching<ListGraph, ListGraph::EdgeMap<int>>>("MaxWeightedPerfectMatchingListGraphInt")
    .constructor<const ListGraph&, const ListGraph::EdgeMap<int>&>()
    .method("mate", &MaxWeightedPerfectMatching<ListGraph, ListGraph::EdgeMap<int>>::mate)
    .method("run", &MaxWeightedPerfectMatching<ListGraph, ListGraph::EdgeMap<int>>::run)
    .method("matchingWeight", &MaxWeightedPerfectMatching<ListGraph, ListGraph::EdgeMap<int>>::matchingWeight);

}

