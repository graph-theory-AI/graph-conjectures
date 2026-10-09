# Conjecture names: old identifier vs new name

Every conjecture in the corpus now carries a canonical short `name` of the form `PREFIX_english_name` (field `name` in `data/problems.json`, `data/arxiv_conjectures.json`, `data/bondy_murty_conjectures.json`, `data/others_conjectures.json`; machine-readable mapping in [`data/conjecture_names.json`](data/conjecture_names.json)).

* `PREFIX` is the corpus: `OPG` (Open Problem Garden), `AX` (arXiv-extracted), `BM` (Bondy–Murty Appendix A), `OTH` (others).
* `english_name` is a few lowercase words (letters, digits, underscores) conveying the statement: objects, parameter, shape of the claim. No `conjecture`/`problem` words, no paper-local numbering; author names only for conjectures universally known by them.
* All 1034 names are distinct. Slight variants of one statement (special cases, directed analogues, duplicates across corpora, sibling questions on one quantity) share a leading stem and differ by a trailing qualifier, e.g. `OPG_bridgeless_cycle_double_cover` / `OPG_bridgeless_cycle_double_cover_strong_5` / `BM_bridgeless_cycle_double_cover_5_cycles`.
* The old identifier is unchanged and remains the key for review files, site URLs, `relations.json` and the sibling repositories: OPG slug, arXiv review id `<arxiv_id>__<NN>`, Bondy–Murty `bm_id`, others `id`.

Total: 1034 names (OPG 227, AX 768, BM 38, OTH 1).

## Open Problem Garden (OPG)

| old id | new name | title |
|---|---|---|
| `2_colouring_a_graph_without_a_monochromatic_maximum_clique` | `OPG_odd_hole_free_nonmonochromatic_max_cliques` | 2-colouring a graph without a monochromatic maximum clique |
| `3_colourability_of_arrangements_of_great_circles` | `OPG_great_circle_arrangements_3_colorable` | 3-Colourability of Arrangements of Great Circles |
| `3_decomposition_conjecture` | `OPG_cubic_tree_cycles_matching_decomposition` | 3-Decomposition Conjecture |
| `3_edge_coloring_conjecture` | `OPG_cubic_3_edge_colorable_edge_removal` | 3-Edge-Coloring Conjecture |
| `3_flow_conjecture` | `OPG_nowhere_zero_3_flow_4_connected` | 3-flow conjecture |
| `4_connected_graphs_are_not_uniquely_hamiltonian` | `OPG_4_connected_second_hamilton_cycle` | 4-connected graphs are not uniquely hamiltonian |
| `4_flow_conjecture` | `OPG_nowhere_zero_4_flow_petersen_free` | 4-flow conjecture |
| `57_regular_moore_graph` | `OPG_moore_graph_degree_57_existence` | 57-regular Moore graph? |
| `5_flow_conjecture` | `OPG_nowhere_zero_5_flow_bridgeless` | 5-flow conjecture |
| `5_local_tensions` | `OPG_edge_width_5_local_tension` | 5-local-tensions |
| `a_generalization_of_vizings_theorem` | `OPG_uniform_hypergraph_vizing_edge_coloring` | A generalization of Vizing's Theorem? |
| `a_gold_grabbing_game` | `OPG_gold_grabbing_tree_game_strategy` | A gold-grabbing game |
| `a_homomorphism_problem_for_flows` | `OPG_cayley_homomorphism_transfers_group_flows` | A homomorphism problem for flows |
| `acyclic_edge_coloring` | `OPG_acyclic_edge_coloring_delta_plus_2` | Acyclic edge-colouring |
| `acyclic_list_colouring_of_planar_graphs` | `OPG_planar_acyclically_5_choosable` | Acyclic list colouring of planar graphs. |
| `adams_conjecture` | `OPG_adam_arc_reversal_fewer_cycles` | Ádám's Conjecture |
| `algorithm_for_graph_homomorphisms` | `OPG_graph_homomorphism_single_exponential_algorithm` | Algorithm for graph homomorphisms |
| `almost_all_non_hamiltonian_3_regular_graphs_are_1_connected` | `OPG_non_hamiltonian_cubic_almost_all_bridged` | Almost all non-Hamiltonian 3-regular graphs are 1-connected |
| `antichains_in_the_cycle_continuous_order` | `OPG_cycle_continuous_order_infinite_antichain` | Antichains in the cycle continuous order |
| `antidirected_trees_in_digraphs` | `OPG_digraph_arcs_antidirected_trees` | Antidirected trees in digraphs |
| `approximation_ratio_for_k_outerplanar_graphs` | `OPG_edge_disjoint_paths_approx_k_outerplanar` | Approximation ratio for k-outerplanar graphs |
| `approximation_ratio_for_maximum_edge_disjoint_paths_problem` | `OPG_edge_disjoint_paths_approx_planar_sqrtn` | Approximation Ratio for Maximum Edge Disjoint Paths problem |
| `arc_disjoint_directed_cycles_in_regular_directed_graphs` | `OPG_regular_digraph_arc_disjoint_cycles` | Arc-disjoint directed cycles in regular directed graphs |
| `arc_disjoint_out_branching_and_in_branching` | `OPG_arc_strong_disjoint_out_in_branchings` | Arc-disjoint out-branching and in-branching |
| `arc_disjoint_strongly_connected_spanning_subdigraphs` | `OPG_digraph_arc_disjoint_strong_spanning_subdigraphs` | Arc-disjoint strongly connected spanning subdigraphs |
| `are_almost_all_graphs_determined_by_their_spectrum` | `OPG_almost_all_graphs_determined_by_spectrum` | Are almost all graphs determined by their spectrum? |
| `are_critical_k_forests_tight` | `OPG_critical_k_forest_is_k_tree` | ¿Are critical k-forests tight? |
| `are_different_notions_of_the_crossing_number_the_same` | `OPG_pair_crossing_equals_crossing_number` | Are different notions of the crossing number the same? |
| `asymptotic_distribution_of_form_of_polyhedra` | `OPG_polyhedra_vertex_edge_ratio_distribution` | Asymptotic Distribution of Form of Polyhedra |
| `barnettes_conjecture` | `OPG_barnette_cubic_planar_bipartite_hamiltonian` | Barnette's Conjecture |
| `behzads_conjecture` | `OPG_total_coloring_max_degree_plus_2` | Total Colouring Conjecture |
| `bene_conjecture_graph_theoretic_form_0` | `OPG_benes_multistage_graph_rearrangeable` | Beneš Conjecture (graph-theoretic form) |
| `book_thickness_of_subdivisions` | `OPG_book_thickness_subdivision_bounded_function` | Book Thickness of Subdivisions |
| `bouchets_6_flow_conjecture` | `OPG_nowhere_zero_6_flow_bidirected` | Bouchet's 6-flow conjecture |
| `bounding_the_chromatic_number_of_triangle_free_graphs_with_fixed_maximum_degree` | `OPG_triangle_free_chromatic_half_max_degree` | Bounding the chromatic number of triangle-free graphs with fixed maximum degree |
| `bounding_the_on_line_choice_number_in_terms_of_the_choice_number` | `OPG_online_choice_number_minus_choice_unbounded` | Bounding the on-line choice number in terms of the choice number |
| `caccetta_haggkvist_conjecture` | `OPG_caccetta_haggkvist_outdegree_short_cycle` | Caccetta-Häggkvist Conjecture |
| `characterizing_aleph_0_aleph_1_graphs` | `OPG_aleph0_aleph1_graphs_characterization` | Characterizing (aleph_0,aleph_1)-graphs |
| `choice_number_of_k_chromatic_graphs_of_bounded_order` | `OPG_choice_number_k_chromatic_mk_vertices` | Choice Number of k-Chromatic Graphs of Bounded Order |
| `choosability_of_graph_powers` | `OPG_graph_square_choice_number_subquadratic` | Choosability of Graph Powers |
| `chords_of_longest_cycles` | `OPG_3_connected_longest_cycle_chord` | Chords of longest cycles |
| `chromatic_number_of_common_graphs` | `OPG_common_graphs_bounded_chromatic_number` | Chromatic Number of Common Graphs |
| `chromatic_number_of_frac_3_3_power_of_graph` | `OPG_fractional_power_chromatic_3_3_2_delta` | Chromatic number of $\frac{3}{3}$-power of graph |
| `chromatic_number_of_random_lifts_of_complete_graphs` | `OPG_random_lift_k5_chromatic_concentration` | Chromatic number of random lifts of complete graphs |
| `circular_choosability_of_planar_graphs` | `OPG_planar_circular_choosability_upper_bound` | Circular choosability of planar graphs |
| `circular_chromatic_number_of_triangle_free_planar_graphs` | `OPG_triangle_free_subcubic_planar_circular_chromatic` | Circular coloring triangle-free subcubic planar graphs |
| `circular_colouring_the_orthogonality_graph` | `OPG_orthogonality_graph_circular_chromatic_4` | Circular colouring the orthogonality graph |
| `circular_flow_number_of_regular_class_1_graphs` | `OPG_circular_flow_number_regular_class_1` | Circular flow number of regular class 1 graphs |
| `circular_flow_numbers_of_r_graphs` | `OPG_odd_r_graph_circular_flow_bound` | Circular flow numbers of $r$-graphs |
| `coloring_and_immersion` | `OPG_chromatic_number_forces_kt_immersion` | Coloring and immersion |
| `coloring_random_subgraphs` | `OPG_random_half_subgraph_chromatic_lower_bound` | Coloring random subgraphs |
| `coloring_the_odd_distance_graph` | `OPG_odd_distance_graph_chromatic_infinite` | Coloring the Odd Distance Graph |
| `coloring_the_union_of_degenerate_graphs` | `OPG_forest_plus_2_degenerate_5_colorable` | Coloring the union of degenerate graphs |
| `colouring_the_square_of_a_planar_graph` | `OPG_wegner_planar_square_chromatic_bound` | Colouring the square of a planar graph |
| `complete_bipartite_subgraphs_of_perfect_graphs` | `OPG_perfect_graph_large_complete_bipartite_subgraph` | Complete bipartite subgraphs of perfect graphs |
| `complexity_of_the_h_factor_problem` | `OPG_h_factor_min_degree_np_hard` | Complexity of the H-factor problem. |
| `consecutive_non_orientable_embedding_obstructions` | `OPG_minor_minimal_obstruction_two_nonorientable_surfaces` | Consecutive non-orientable embedding obstructions |
| `cores_of_cayley_graphs` | `OPG_cayley_graph_core_is_cayley` | Cores of Cayley graphs |
| `cores_of_strongly_regular_graphs` | `OPG_strongly_regular_core_complete_or_self` | Cores of strongly regular graphs |
| `counting_3_colorings_of_the_hex_lattice` | `OPG_hex_lattice_3_colorings_growth_rate` | Counting 3-colorings of the hex lattice |
| `covering_powers_of_cycles_with_equivalence_subgraphs` | `OPG_cycle_powers_equivalence_covering_number_linear` | Covering powers of cycles with equivalence subgraphs |
| `crossing_numbers_and_coloring` | `OPG_crossing_number_vs_chromatic_number` | Crossing numbers and coloring |
| `crossing_sequences` | `OPG_crossing_sequences_decreasing_genus_realizable` | Crossing sequences |
| `cycle_double_cover_conjecture` | `OPG_bridgeless_cycle_double_cover` | Cycle double cover conjecture |
| `cycle_double_covers_containing_predefined_2_regular_subgraphs` | `OPG_bridgeless_cycle_double_cover_prescribed_2_factor` | Cycle Double Covers Containing Predefined 2-Regular Subgraphs |
| `cycles_in_graphs_of_large_chromatic_number` | `OPG_high_chromatic_cycles_0_mod_k` | Cycles in Graphs of Large Chromatic Number |
| `cyclic_spanning_subdigraph_with_small_cyclomatic_number` | `OPG_cyclic_spanning_subdigraph_cyclomatic_independence` | Cyclic spanning subdigraph with small cyclomatic number |
| `decomposing_a_connected_graph_into_paths` | `OPG_gallai_path_decomposition_half_n` | Decomposing a connected graph into paths. |
| `decomposing_an_eulerian_graph_into_cycles` | `OPG_eulerian_cycle_decomposition_hajos_n_half` | Decomposing an eulerian graph into cycles. |
| `decomposing_an_eulerian_graph_into_cycles_with_no_two_consecutives_edges_on_a_prescirbed_eulerian_tour` | `OPG_eulerian_cycle_decomposition_avoiding_tour_transitions` | Decomposing an eulerian graph into cycles with no two consecutives edges on a prescribed eulerian tour. |
| `decomposing_an_even_tournament_in_directed_paths` | `OPG_even_tournament_directed_path_decomposition` | Decomposing an even tournament in directed paths. |
| `decomposing_eulerian_graphs` | `OPG_eulerian_cycle_decomposition_compatible_transition_system` | Decomposing eulerian graphs |
| `decomposing_k_arc_strong_tournament_into_k_spanning_strong_digraphs` | `OPG_arc_strong_tournament_spanning_strong_decomposition` | Decomposing k-arc-strong tournament into k spanning strong digraphs |
| `decomposing_the_prism_of_a_3_connected_cubic_planar_graphs_in_hamilton_cycles` | `OPG_prism_planar_cubic_hamilton_decomposition` | Hamilton decomposition of prisms over 3-connected cubic planar graphs |
| `degenerate_colorings_of_planar_graphs` | `OPG_planar_degenerate_5_coloring` | Degenerate colorings of planar graphs |
| `directed_cycle_of_length_twice_the_minimum_outdegree` | `OPG_oriented_outdegree_directed_path_2k` | Directed path of length twice the minimum outdegree |
| `do_any_three_longest_paths_in_a_connected_graph_have_a_vertex_in_common` | `OPG_three_longest_paths_common_vertex` | Do any three longest paths in a connected graph have a vertex in common? |
| `does_the_symmetric_chromatic_function_distinguish_trees` | `OPG_chromatic_symmetric_function_distinguishes_trees` | Does the chromatic symmetric function distinguish between trees? |
| `domination_in_cubic_graphs` | `OPG_cubic_3_connected_domination_third` | Domination in cubic graphs |
| `domination_in_plane_triangulations` | `OPG_plane_triangulation_domination_n_4` | Domination in plane triangulations |
| `double_critical_graph_conjecture` | `OPG_double_critical_graphs_are_complete` | Double-critical graph conjecture |
| `drawing_disconnected_graphs_on_surfaces` | `OPG_disjoint_union_optimal_drawing_surfaces` | Drawing disconnected graphs on surfaces |
| `earth_moon_problem` | `OPG_earth_moon_biplanar_chromatic_number` | Earth-Moon Problem |
| `edge_disjoint_hamilton_cycles` | `OPG_strong_tournament_disjoint_hamilton_cycles` | Edge-disjoint Hamilton cycles in highly strongly connected tournaments. |
| `edge_list_coloring_conjecture` | `OPG_list_edge_chromatic_equals_edge_chromatic` | Edge list coloring conjecture |
| `edge_reconstruction_conjecture` | `OPG_reconstruction_edge_deleted_subgraphs` | Edge Reconstruction Conjecture |
| `end_devouring_rays` | `OPG_countable_end_devouring_disjoint_rays` | End-Devouring Rays |
| `erdos_faber_lovasz_conjecture` | `OPG_erdos_faber_lovasz_cliques_chromatic` | Erdős–Faber–Lovász conjecture |
| `erdos_posa_property_for_long_directed_cycles` | `OPG_erdos_posa_long_directed_cycles` | Erdős-Posa property for long directed cycles |
| `every_4_connected_toroidal_graph_has_a_hamilton_cycle` | `OPG_4_connected_toroidal_hamiltonian` | Every 4-connected toroidal graph has a Hamilton cycle |
| `every_prism_over_a_3_connected_planar_graph_is_hamiltonian` | `OPG_prism_planar_3_connected_hamiltonian` | Every prism over a 3-connected planar graph is hamiltonian. |
| `exact_colorings_of_graphs` | `OPG_exact_edge_coloring_infinite_complete_subgraph` | Exact colorings of graphs |
| `extremal_problem_on_the_number_of_tree_endomorphism` | `OPG_tree_endomorphisms_star_max_path_min` | Extremal problem on the number of tree endomorphism |
| `faithful_cycle_covers` | `OPG_faithful_cycle_cover_even_weights` | Faithful cycle covers |
| `finding_k_edge_outerplanar_graph_embeddings` | `OPG_k_edge_outerplanar_embedding_polynomial` | Finding k-edge-outerplanar graph embeddings |
| `forcing_a_2_regular_minor` | `OPG_average_degree_forces_2_regular_minor` | Forcing a 2-regular minor |
| `forcing_a_k_6_minor` | `OPG_min_degree_7_forces_k6_minor` | Forcing a $K_6$-minor |
| `fractional_hadwiger` | `OPG_hadwiger_fractional_chromatic_minor` | Fractional Hadwiger |
| `frankls_union_closed_sets_conjecture` | `OPG_frankl_union_closed_frequent_element` | Frankl's union-closed sets conjecture |
| `friendly_partitions` | `OPG_regular_graphs_friendly_partition_almost_all` | Friendly partitions |
| `geodesic_cycles_and_tuttes_theorem` | `OPG_3_connected_geodesic_cycles_peripheral_lengths` | Geodesic cycles and Tutte's Theorem |
| `goldbergs_conjecture` | `OPG_goldberg_edge_chromatic_max_degree_density` | Goldberg's conjecture |
| `good_edge_labelings` | `OPG_good_edge_labeling_max_density` | Good Edge Labelings |
| `graceful_tree_conjecture` | `OPG_all_trees_graceful_labeling` | Graceful Tree Conjecture |
| `grahams_conjecture_on_tree_reconstruction` | `OPG_tree_iterated_line_graph_orders` | Graham's conjecture on tree reconstruction |
| `graphs_with_a_forbidden_induced_tree_are_chi_bounded` | `OPG_gyarfas_sumner_forbidden_tree_chi_bounded` | Graphs with a forbidden induced tree are chi-bounded |
| `grunbaums_conjecture` | `OPG_grunbaum_triangulation_dual_3_edge_colorable` | Grunbaum's Conjecture |
| `half_integral_flow_polynomial_values` | `OPG_flow_polynomial_positive_at_5_5` | Half-integral flow polynomial values |
| `hamilton_cycle_in_small_d_diregular_graphs` | `OPG_diregular_oriented_small_hamilton_cycle` | Hamilton cycle in small d-diregular graphs |
| `hamiltonian_cycles_in_line_graphs` | `OPG_4_connected_hamiltonian_line_graphs` | Hamiltonian cycles in line graphs |
| `hamiltonian_cycles_in_line_graphs_of_infinite_graphs` | `OPG_infinite_line_graph_hamiltonian_4_connected` | Hamiltonian cycles in line graphs of infinite graphs |
| `hamiltonian_cycles_in_powers_of_infinite_graphs` | `OPG_infinite_graph_powers_hamiltonian` | Hamiltonian cycles in powers of infinite graphs |
| `hamiltonian_paths_and_cycles_in_vertex_transitive_graphs` | `OPG_vertex_transitive_hamiltonian_path` | Hamiltonian paths and cycles in vertex transitive graphs |
| `hamiltonicity_of_cayley_graphs` | `OPG_cayley_graphs_hamiltonian_cycle` | Hamiltonicity of Cayley graphs |
| `hedetniemis_conjecture` | `OPG_hedetniemi_tensor_product_chromatic_min` | Hedetniemi's Conjecture |
| `high_connectivity_no_k_n` | `OPG_highly_connected_no_kn_minor_planar` | Highly connected graphs with no K_n minor |
| `high_girth_low_degree_4_chromatic_graphs` | `OPG_4_regular_4_chromatic_high_girth` | 4-regular 4-chromatic graphs of high girth |
| `highly_arc_transitive_two_ended_digraphs` | `OPG_highly_arc_transitive_two_ended_tiles` | Highly arc transitive two ended digraphs |
| `hoand_reed_conjecture` | `OPG_hoang_reed_outdegree_nearly_disjoint_cycles` | Hoàng-Reed Conjecture |
| `imbalance_conjecture` | `OPG_edge_imbalance_multiset_graphic` | Imbalance conjecture |
| `infinite_uniquely_hamiltonian_graphs` | `OPG_infinite_regular_uniquely_hamiltonian` | Infinite uniquely hamiltonian graphs |
| `intersecting_two_perfect_matchings` | `OPG_cubic_two_perfect_matchings_odd_cut` | The intersection of two perfect matchings |
| `jaegers_modular_orientation_conjecture` | `OPG_jaeger_modular_orientation_4k_edge_connected` | Jaeger's modular orientation conjecture |
| `jones_conjecture` | `OPG_jones_planar_feedback_vertex_cycle_packing` | Jones' conjecture |
| `jorgensens_conjecture` | `OPG_highly_connected_no_k6_minor_apex` | Jorgensen's Conjecture |
| `kriesells_conjecture` | `OPG_kriesell_edge_disjoint_steiner_trees` | Kriesell's Conjecture |
| `laplacian_degrees_of_a_graph` | `OPG_laplacian_eigenvalues_vs_degree_sequence` | Laplacian Degrees of a Graph |
| `large_acyclic_induced_subdigraph_in_a_planar_oriented_graph` | `OPG_planar_oriented_induced_acyclic_3_5` | Large acyclic induced subdigraph in a planar oriented graph. |
| `large_induced_forest_in_a_planar_graph` | `OPG_planar_induced_forest_half_vertices` | Large induced forest in a planar graph. |
| `linear_hypergraphs_with_dimension_3` | `OPG_linear_hypergraph_dimension_3_triangle_intersection` | Linear Hypergraphs with Dimension 3 |
| `linial_berge_path_partition_duality` | `OPG_linial_digraph_path_partition_k_norm` | Linial-Berge path partition duality |
| `list_chromatic_number_and_maximum_degree_of_bipartite_graphs` | `OPG_bipartite_list_chromatic_log_max_degree` | List chromatic number and maximum degree of bipartite graphs |
| `list_colorings_of_edge_critical_graphs` | `OPG_edge_critical_delta_list_edge_colorable` | List colorings of edge-critical graphs |
| `list_colourings_of_complete_multipartite_graphs_with_2_big_parts` | `OPG_complete_multipartite_two_big_parts_choosability` | List Colourings of Complete Multipartite Graphs with 2 Big Parts |
| `list_hadwiger_conjecture` | `OPG_hadwiger_list_kt_minor_free_choosable` | List Hadwiger Conjecture |
| `list_total_colouring_conjecture` | `OPG_total_graph_list_chromatic_equals_chromatic` | List Total Colouring Conjecture |
| `long_directed_cycles_in_digraph_with_minimum_in_and_out_degree` | `OPG_oriented_in_out_degree_long_cycle` | Long directed cycles in diregular digraphs |
| `lovasz_path_removal_conjecture` | `OPG_lovasz_induced_path_removal_connectivity` | Lovász Path Removal Conjecture |
| `m_n_cycle_covers` | `OPG_bridgeless_cycle_double_cover_5_cycles` | (m,n)-cycle covers |
| `mapping_planar_graphs_to_odd_cycles` | `OPG_planar_girth_4k_homomorphism_odd_cycle` | Mapping planar graphs to odd cycles |
| `matching_cut_and_girth` | `OPG_matching_cut_average_degree_girth` | Matching cut and girth |
| `matchings_extends_to_hamilton_cycles_in_hypercubes` | `OPG_hypercube_matching_extends_hamiltonian_cycle` | Matchings extend to Hamiltonian cycles in hypercubes |
| `melnikovs_valency_variety_problem` | `OPG_valency_variety_chromatic_lower_bound` | Melnikov's valency-variety problem |
| `minimal_graphs_with_a_prescribed_number_of_spanning_trees` | `OPG_min_order_given_spanning_tree_count` | Minimal graphs with a prescribed number of spanning trees |
| `minimum_number_of_transitive_subtournaments_of_order_3_in_a_tournament` | `OPG_tournament_arc_disjoint_transitive_triples` | Minimum number of arc-disjoint transitive subtournaments of order 3 in a tournament |
| `mixing_circular_colourings_0` | `OPG_circular_coloring_mixing_number_rational` | Mixing Circular Colourings |
| `monochromatic_reachability_vs_rainbow_triangles` | `OPG_tournament_rainbow_triangle_or_monochromatic_reachability` | Monochromatic reachability or rainbow triangles |
| `monochromatic_vertex_colorings_inherited_from_perfect_matchings` | `OPG_perfect_matching_inherited_colorings_cancellation` | Monochromatic vertex colorings inherited from Perfect Matchings |
| `monochromatoc_reachability_in_arc_colored_digraphs` | `OPG_arc_colored_digraph_monochromatic_absorbing_set` | Monochromatic reachability in arc-colored digraphs |
| `multicolour_erdos_hajnal_conjecture` | `OPG_erdos_hajnal_multicolor_edge_coloring` | Multicolour Erdős--Hajnal Conjecture |
| `nearly_spanning_regular_subgraphs` | `OPG_regular_nearly_spanning_k_regular_subgraph` | Nearly spanning regular subgraphs |
| `negative_association_in_uniform_forests` | `OPG_uniform_random_forest_negative_association` | Negative association in uniform forests |
| `non_edges_vs_feedback_edge_sets_in_digraphs` | `OPG_digraph_feedback_arcs_vs_non_edges` | Non-edges vs. feedback edge sets in digraphs |
| `number_of_cliques_in_minor_closed_classes` | `OPG_kt_minor_free_cliques_count_exponential` | Number of Cliques in Minor-Closed Classes |
| `obstacle_number_of_planar_graphs` | `OPG_planar_obstacle_number_bounded` | Obstacle number of planar graphs |
| `odd_cycle_transversal_in_triangle_free_graphs` | `OPG_triangle_free_odd_cycle_edge_transversal` | Odd-cycle transversal in triangle-free graphs |
| `odd_cycles_and_low_oddness` | `OPG_cubic_odd_2_factors_oddness_2` | Odd cycles and low oddness |
| `oriented_chromatic_number_of_planar_graphs` | `OPG_planar_oriented_chromatic_number_max` | Oriented chromatic number of planar graphs |
| `oriented_trees_in_n_chromatic_digraphs` | `OPG_chromatic_digraph_oriented_trees_2k` | Oriented trees in n-chromatic digraphs |
| `packing_t_joins` | `OPG_graft_t_join_packing_two_thirds` | Packing T-joins |
| `partial_list_coloring` | `OPG_partial_list_coloring_tn_over_chi` | Partial List Coloring |
| `partial_list_coloring_0` | `OPG_partial_list_coloring_lambda_r_monotone` | Partial List Coloring |
| `partition_of_a_cubic_3_connected_graphs_into_paths_of_length_2` | `OPG_cubic_3_connected_p3_path_partition` | Partition of a cubic 3-connected graphs into paths of length 2. |
| `partitioning_edge_connectivity` | `OPG_edge_connectivity_partition_a_plus_b` | Partitioning edge-connectivity |
| `partitioning_planar_digraphs` | `OPG_planar_oriented_two_acyclic_parts` | The Two Color Conjecture |
| `partitionning_a_tournament_into_k_strongly_connected_subtournaments` | `OPG_strong_tournament_partition_strong_subtournaments` | Partitionning a tournament into k-strongly connected subtournaments. |
| `pebbling_a_cartesian_product` | `OPG_graham_pebbling_cartesian_product` | Pebbling a cartesian product |
| `pentagon_problem` | `OPG_pentagon_cubic_girth_c5_homomorphism` | Pentagon problem |
| `petersen_coloring_conjecture` | `OPG_petersen_coloring_bridgeless_cubic` | Petersen coloring conjecture |
| `ptas_for_feedback_arc_set_in_tournaments` | `OPG_tournament_feedback_arc_set_ptas` | PTAS for feedback arc set in tournaments |
| `ramsey_properties_of_cayley_graphs` | `OPG_abelian_cayley_graph_ramsey_logarithmic` | Ramsey properties of Cayley graphs |
| `random_stable_roommates` | `OPG_random_stable_roommates_solution_probability` | Random stable roommates |
| `real_roots_of_the_flow_polynomial` | `OPG_flow_polynomial_real_roots_below_4` | Real roots of the flow polynomial |
| `reconstruction_conjecture` | `OPG_reconstruction_vertex_deck_isomorphic` | Reconstruction conjecture |
| `reeds_omega_delta_and_chi_conjecture` | `OPG_reed_chromatic_omega_delta_average` | Reed's omega, delta, and chi conjecture |
| `rysers_conjecture` | `OPG_ryser_r_partite_hypergraph_cover_matching` | Ryser's conjecture |
| `seagull_problem` | `OPG_independence_2_clique_minor_half_n` | Seagull problem |
| `seymours_r_graph_conjecture` | `OPG_r_graph_edge_chromatic_r_plus_1` | Seymour's r-graph conjecture |
| `seymours_second_neighbourhood_conjecture` | `OPG_seymour_second_neighborhood_outdegree` | Seymour's Second Neighbourhood Conjecture |
| `seymours_self_minor_conjecture` | `OPG_infinite_graph_proper_self_minor` | Seymour's self-minor conjecture |
| `shannon_capacity_of_the_seven_cycle` | `OPG_shannon_capacity_c7` | Shannon capacity of the seven-cycle |
| `shuffle_exchange_conjecture_graph_theoretic_form` | `OPG_shuffle_exchange_rearrangeable_stages_2n_1` | Shuffle-Exchange Conjecture (graph-theoretic form) |
| `sidorenkos_conjecture` | `OPG_sidorenko_bipartite_homomorphism_density` | Sidorenko's Conjecture |
| `signing_a_graph_to_have_small_magnitude_eigenvalues` | `OPG_regular_signing_eigenvalues_2_sqrt_d` | Signing a graph to have small magnitude eigenvalues |
| `simultaneous_partition_of_hypergraphs` | `OPG_two_hypergraphs_simultaneous_r_partition` | Simultaneous partition of hypergraphs |
| `small_universal_point_sets_for_planar_graphs` | `OPG_planar_universal_point_set_linear` | Universal point sets for planar graphs |
| `splitting_a_digraph_with_minimum_outdegree_constraints` | `OPG_digraph_outdegree_splitting_two_parts` | Splitting a digraph with minimum outdegree constraints |
| `stable_set_meeting_all_longest_directed_paths` | `OPG_digraph_stable_set_meets_longest_paths` | Stable set meeting all longest directed paths. |
| `star_chromatic_index_of_complete_graphs` | `OPG_star_chromatic_index_complete_linear` | Star chromatic index of complete graphs |
| `star_chromatic_index_of_cubic_graphs` | `OPG_star_chromatic_index_cubic_6` | Star chromatic index of cubic graphs |
| `strong_5_cycle_double_cover_conjecture` | `OPG_bridgeless_cycle_double_cover_strong_5` | Strong 5-cycle double cover conjecture |
| `strong_colorability` | `OPG_strongly_2_delta_colorable_max_degree` | Strong colorability |
| `strong_edge_colouring_conjecture` | `OPG_strong_edge_chromatic_delta_squared_bound` | Strong edge colouring conjecture |
| `strong_matchings_and_covers` | `OPG_infinite_hypergraph_strongly_maximal_matching` | Strong matchings and covers |
| `subdivision_of_a_transitive_tournament_in_digraphs_with_large_outdegree` | `OPG_outdegree_transitive_tournament_subdivision` | Subdivision of a transitive tournament in digraphs with large outdegree. |
| `subgraph_of_large_average_degree_and_large_average_degree` | `OPG_average_degree_subgraph_large_girth` | Subgraph of large average degree and large girth. |
| `switching_reconstruction_conjecture` | `OPG_reconstruction_switching_5_vertices` | Switching reconstruction conjecture |
| `switching_reconstruction_of_digraphs` | `OPG_reconstruction_switching_digraphs_12_vertices` | Switching reconstruction of digraphs |
| `the_berge_fulkerson_conjecture` | `OPG_berge_fulkerson_cubic_6_perfect_matchings` | The Berge-Fulkerson conjecture |
| `the_bermond_thomassen_conjecture` | `OPG_bermond_thomassen_outdegree_disjoint_cycles` | The Bermond-Thomassen Conjecture |
| `the_bollobas_eldridge_catlin_conjecture_on_graph_packing` | `OPG_bollobas_eldridge_catlin_max_degree_packing` | The Bollobás-Eldridge-Catlin Conjecture on graph packing |
| `the_borodin_kostochka_conjecture` | `OPG_borodin_kostochka_chromatic_max_degree_clique` | The Borodin-Kostochka Conjecture |
| `the_circular_embedding_conjecture` | `OPG_2_connected_circular_surface_embedding` | The circular embedding conjecture |
| `the_crossing_number_of_the_complete_bipartite_graph` | `OPG_crossing_number_complete_bipartite_zarankiewicz` | The Crossing Number of the Complete Bipartite Graph |
| `the_crossing_number_of_the_complete_graph` | `OPG_crossing_number_complete_graph_harary_hill` | The Crossing Number of the Complete Graph |
| `the_crossing_number_of_the_hypercube` | `OPG_crossing_number_hypercube_limit_5_32` | The Crossing Number of the Hypercube |
| `the_erdos_hajnal_conjecture` | `OPG_erdos_hajnal_induced_cliques` | The Erdös-Hajnal Conjecture |
| `three_4_flows_conjecture` | `OPG_three_4_flows_bridgeless_edge_partition` | The three 4-flows conjecture |
| `three_chromatic_0_2_graphs` | `OPG_0_2_graphs_chromatic_number_3` | Three-chromatic (0,2)-graphs |
| `triangle_free_strongly_regular_graphs` | `OPG_strongly_regular_triangle_free_eighth` | Triangle free strongly regular graphs |
| `triangle_packing_vs_triangle_edge_transversal` | `OPG_tuza_triangle_packing_edge_transversal` | Triangle-packing vs triangle edge-transversal. |
| `turan_number_of_a_finite_family` | `OPG_turan_number_finite_family_single_member` | Turán number of a finite family. |
| `turans_problem_for_hypergraphs` | `OPG_turan_3_uniform_k4_k5_free` | Turán's problem for hypergraphs |
| `unfriendly_partitions` | `OPG_countable_graph_unfriendly_partition` | Unfriendly partitions |
| `unions_of_triangle_free_graphs` | `OPG_k4_free_countable_union_triangle_free` | Unions of triangle free graphs |
| `uniquely_hamiltonian_graphs` | `OPG_regular_graphs_not_uniquely_hamiltonian` | r-regular graphs are not uniquely hamiltonian. |
| `unit_vector_flows` | `OPG_bridgeless_unit_vector_s2_flow` | Unit vector flows |
| `universal_highly_arc_transitive_digraphs` | `OPG_highly_arc_transitive_universal_digraph` | Universal highly arc transitive digraphs |
| `universal_steiner_triple_systems` | `OPG_universal_steiner_triple_systems_characterization` | Universal Steiner triple systems |
| `vertex_coloring_of_graph_fractional_powers` | `OPG_fractional_power_chromatic_general` | Vertex Coloring of graph fractional powers |
| `vertex_minor_closed_classes_are_chi_bounded` | `OPG_vertex_minor_closed_chi_bounded` | Are vertex minor closed classes chi-bounded? |
| `weak_pentagon_problem` | `OPG_pentagon_weak_cubic_5_edge_coloring` | Weak pentagon problem |
| `weak_saturation_of_the_cube_in_the_clique` | `OPG_weak_saturation_cube_in_clique` | Weak saturation of the cube in the clique |
| `weighted_colouring_of_hexagonal_graphs` | `OPG_hexagonal_weighted_coloring_9_8_bound` | Weighted colouring of hexagonal graphs. |
| `what_is_the_largest_graph_of_positive_curvature` | `OPG_largest_planar_positive_curvature_graph` | What is the largest graph of positive curvature? |
| `what_is_the_smallest_number_of_disjoint_spanning_trees_made_a_graph_hamiltonian` | `OPG_successive_shortest_spanning_trees_hamiltonian` | What is the smallest number of disjoint spanning trees made a graph Hamiltonian |
| `woodalls_conjecture` | `OPG_woodall_dicut_disjoint_dijoins` | Woodall's Conjecture |

## arXiv-extracted (AX)

| old id | new name | title |
|---|---|---|
| `0806.0178__00` | `AX_gnp_chromatic_concentration_lower_bound` | Open problem on lower bound for concentration interval |
| `0911.0885__00` | `AX_plane_triangle_free_distant_precoloring_extension` | Conjecture 1.4 |
| `1010.2472__00` | `AX_4_colorability_fixed_surface_polynomial_time` | Open Problem: polynomial-time 4-colorability on fixed surfaces |
| `1302.2158__00` | `AX_girth_5_planar_list_critical_bounded` | Conjecture 1.7 |
| `1404.6356__00` | `AX_4_colorability_fixed_surface_complexity` | 4-colorability on Fixed Surfaces (Open Step in Thomassen's Program) |
| `1407.5833__00` | `AX_identifying_codes_hereditary_vc_dimension_dichotomy` | VC-Dimension Dichotomy for Identifying Codes (Approximation) |
| `1408.4257__00` | `AX_block_stable_random_graph_diameter_bound` | Informal Conjecture (diameter bound improvement) |
| `1410.5292__00` | `AX_ordered_ramsey_matching_vs_triangle_order` | Open problem: ordered Ramsey number of matchings vs triangles |
| `1410.5292__01` | `AX_ordered_ramsey_matching_exponent_gap` | Open problem: true ordered Ramsey number of matchings |
| `1505.01616__00` | `AX_k_coloring_maximal_local_connectivity_k` | Question 1.7 |
| `1505.05637__00` | `AX_corruption_detection_expansion_threshold` | Open Problem: Expansion vs. Corruption Detection |
| `1507.00547__00` | `AX_set_mapping_theorem_l_equals_1` | Open Problem: Reducing l to 1 in the Set Mapping Theorem |
| `1507.01120__00` | `AX_planar_graphs_bounded_queue_number` | Queue Number of Planar Graphs |
| `1507.08208__00` | `AX_barat_thomassen_refined_max_degree_connectivity` | Conjecture 1.2 |
| `1508.03437__00` | `AX_planar_c4_c7_free_3_choosable` | Open Question on 3-Choosability for Forbidden Cycles 4–7 and 4–6 |
| `1508.03437__01` | `AX_planar_c4_c8_free_correspondence_coloring` | Informal Conjecture on Correspondence Chromatic Number of Planar Graphs Without Cycles 4–8 |
| `1509.06563__00` | `AX_bounded_clique_large_chi_consecutive_holes_extension` | Informal Conjecture (generalization of 1.3 to bounded clique number) |
| `1509.06563__01` | `AX_constricting_hole_lengths_bounded_gaps` | Conjecture 1.5 |
| `1509.06563__02` | `AX_constricting_hole_lengths_density_zero` | Problem 1.6 |
| `1509.06563__03` | `AX_controlled_triangle_free_chromatic_4_hole` | Informal Question (on 2.1 for ℓ = 4) |
| `1510.06964__00` | `AX_triangular_lattice_5_colorings_kempe_class` | Open case: WSK algorithm on the triangular lattice for q=5 |
| `1601.01129__00` | `AX_normal_graphs_cover_sizes_max_order` | Problem 1 |
| `1601.01129__01` | `AX_normal_graphs_random_gnp_whp` | Open Question (normality of random graphs) |
| `1601.01197__00` | `AX_surface_triangle_free_3_coloring_linear` | Open Problem (linear-time 3-coloring output) |
| `1601.01886__00` | `AX_tree_pathwidth_path_partition_height_2k` | Optimality of factor 2 in Lemma 4 |
| `1602.05184__00` | `AX_szeged_wiener_difference_2_connected_2n` | Conjecture 5 |
| `1603.07056__00` | `AX_social_graphs_contraction_clique_count_characterization` | Characterization of Social Graphs |
| `1604.02317__00` | `AX_disjoint_paths_stability_two_np_complete` | Informal Conjecture (vertex-disjoint paths, stability number two) |
| `1604.07976__00` | `AX_spanning_tree_polytope_xc_bounded_genus` | Conjecture 1 |
| `1604.07976__01` | `AX_spanning_tree_polytope_xc_minor_closed` | Conjecture 2 |
| `1605.00442__00` | `AX_token_sliding_chordal_clique_tree_degree` | Question 1 |
| `1605.07411__00` | `AX_gyarfas_sumner_oriented_iff_forest` | Conjecture 2 |
| `1605.07411__01` | `AX_oriented_chi_bounded_forbidden_oriented_star` | Conjecture 4 |
| `1605.07411__02` | `AX_oriented_chi_bounded_forbidden_p4_orientations` | Conjecture 5 |
| `1606.06011__00` | `AX_chen_chvatal_lines_bridges_finite_exceptions` | Conjecture 2.2 |
| `1606.06011__01` | `AX_chen_chvatal_lines_bridges_path_elongation` | Open question on counter-examples to ℓ(G)+br(G)≥\|G\| |
| `1606.06265__00` | `AX_triangle_free_planar_fractional_chromatic_bound` | Fractional Chromatic Number Bound for Planar Triangle-Free Graphs |
| `1606.06810__00` | `AX_kt_immersion_free_clique_count` | Conjecture on maximum cliques with no $K_t$-immersion |
| `1606.06810__01` | `AX_kt_subdivision_free_clique_count_exponent` | Conjecture on optimal exponential constant for $K_t$-subdivision clique count |
| `1608.03040__00` | `AX_majority_coloring_digraphs_3_colors` | Conjecture 2 |
| `1608.03040__01` | `AX_majority_coloring_digraphs_1_over_k` | Conjecture 9 |
| `1608.03040__02` | `AX_majority_coloring_digraphs_beta_3_colors` | Open Problem 1 |
| `1608.03040__03` | `AX_majority_coloring_tournaments_3_colors` | Open Problem 2 |
| `1608.03040__04` | `AX_majority_coloring_eulerian_digraphs_3_colors` | Open Problem 3 |
| `1608.03040__05` | `AX_majority_coloring_digraphs_2_colorable_recognition` | Open Problem 5 |
| `1608.03040__06` | `AX_majority_coloring_digraphs_choosability_constant` | Open Problem 7 |
| `1608.03040__07` | `AX_majority_coloring_digraphs_fractional_weight` | Open Problem 8 |
| `1608.07028__00` | `AX_properly_colored_kn_longest_rainbow_cycle` | Open Problem: error term for longest rainbow cycle |
| `1608.07568__00` | `AX_subcubic_tsp_walk_5_4_n` | Conjecture 1 |
| `1608.07680__00` | `AX_cone_crossing_number_minimum_function` | Problem 1 |
| `1608.07680__01` | `AX_cone_crossing_number_2_page_redrawing` | Problem 4 |
| `1608.07680__02` | `AX_cone_crossing_number_simple_graphs_asymptotics` | Conjecture on $f_s(k)$ asymptotics |
| `1609.00314__00` | `AX_forest_of_lanterns_pervasive` | Conjecture: every forest of lanterns is pervasive |
| `1609.05458__00` | `AX_ryser_near_extremal_hypergraphs_projective_planes` | Informal Problem (projective plane structure in near-extremal constructions) |
| `1609.06257__00` | `AX_gallai_path_decomposition_odd_semi_cliques` | Question 1.1 |
| `1610.00239__00` | `AX_bipartite_johnson_lindenstrauss_bounded_norms` | Conjecture 2.4 |
| `1610.00876__00` | `AX_outdegree_transitive_tournament_subdivision_semidegree` | Conjecture 3 |
| `1610.00876__01` | `AX_digraph_subdivision_oriented_trees_min_outdegree` | Conjecture 4 |
| `1610.00876__02` | `AX_digraph_subdivision_maderian_disjoint_union` | Conjecture 7 |
| `1610.00876__03` | `AX_digraph_subdivision_oriented_trees_chromatic_2k` | Conjecture 11 |
| `1610.00876__04` | `AX_digraph_subdivision_dichromatic_complete_digraph` | Problem 12 |
| `1610.00876__05` | `AX_digraph_subdivision_strong_connectivity_maderian` | Problem 16 |
| `1611.01270__00` | `AX_permutation_property_testing_query_bounds` | Open Problem (better query complexity bounds for property testing) |
| `1611.02400__00` | `AX_multitasking_interference_increases_with_depth` | Open Problem (interference worsens with depth) |
| `1611.02400__01` | `AX_multitasking_capacity_average_degree_log_n` | Open Problem (multitasker at average degree $\Theta(\log n)$) |
| `1611.03196__00` | `AX_fair_representation_path_partition_independent_set` | Conjecture 1.6 |
| `1611.03196__01` | `AX_fair_representation_knn_perfect_matching` | Conjecture 1.9 |
| `1611.03196__02` | `AX_fair_representation_matching_delta_plus_2` | Conjecture 1.14 |
| `1611.03196__03` | `AX_fair_representation_bipartite_matching_under_representation` | Conjecture 1.15 |
| `1612.06539__00` | `AX_clique_chromatic_dense_gnp_tight_constant` | Informal Conjecture on Tight Constant for Clique Chromatic Number |
| `1612.07540__00` | `AX_planar_cover_graph_poset_dimension_height` | Open problem: dimension of posets with planar cover graphs vs. height |
| `1612.08698__00` | `AX_degenerate_graphs_flexibility_d_plus_1_lists` | Problem 1 |
| `1612.09143__00` | `AX_gnp_h_free_clique_count_threshold` | Motivating Question (Introduction) |
| `1701.03366__00` | `AX_z5_antisymmetric_flow_edge_connected_digraphs` | Antisymmetric variant of Jaeger's weak 3-flow conjecture |
| `1701.05597__00` | `AX_widespread_multigraph_all` | Conjecture 1.8 |
| `1701.05597__01` | `AX_widespread_multigraph_chi_2_subdivision_free` | Conjecture 1.10 |
| `1701.05597__02` | `AX_subdivision_free_chi_bounded_multigraph_characterization` | Open Question: first pervasiveness characterisation |
| `1702.00588__00` | `AX_triangle_free_planar_3_coloring_requests` | Problem 1 |
| `1702.01094__00` | `AX_large_chromatic_rainbow_hole_consecutive_vertices` | Question (rainbow hole with $s$ consecutive rainbow vertices) |
| `1702.01094__01` | `AX_large_chromatic_induced_path_uniquely_covered` | Question (uniquely-covered vertices in an induced path) |
| `1702.01607__00` | `AX_tournament_large_domination_forces_si` | Problem 3 |
| `1702.01607__01` | `AX_tournament_large_domination_small_subtournament` | Problem 4 |
| `1702.02888__00` | `AX_planar_independence_number_n_over_4` | Open Problem (independence number of planar graphs) |
| `1703.05380__00` | `AX_interactive_sum_choice_strict_non_complete` | Conjecture 1.1 |
| `1703.07871__00` | `AX_spaghetti_tree_path_decomposition_chi_bounded` | Conjecture 3 |
| `1704.00125__00` | `AX_thin_overlays_sublinear_separators_unbounded_degree` | Informal Conjecture (Section 1.2): dropping bounded-degree assumption |
| `1704.00125__01` | `AX_independent_set_apx_hard_nonsublinear_separators` | Open Problem (Section 1.2): APX-hardness on classes without sublinear separators |
| `1704.02367__00` | `AX_ordered_removal_lemma_regularity_free_proof` | Open Problem: Regularity-free proof for the ordered removal lemma |
| `1704.02367__01` | `AX_ordered_removal_lemma_binary_matrices_polynomial` | Open Problem: Better parameter dependence for ordered binary matrix removal |
| `1705.02166__00` | `AX_euclidean_ramsey_unit_distance_vs_copy` | Question 1.1 |
| `1705.02166__01` | `AX_euclidean_ramsey_l3_vs_lm` | Open problem: $E^n \not\to (\ell_3, \ell_m)$ for large $m$ |
| `1705.02166__02` | `AX_euclidean_ramsey_diameter_free_bound` | Open problem: removing diameter dependence from Theorem 1.1 |
| `1705.04609__00` | `AX_bounded_clique_large_chi_consecutive_holes` | Conjecture 1.8 |
| `1706.00337__00` | `AX_kk_free_bounded_treewidth_max_chromatic` | Problem 3 |
| `1706.02896__00` | `AX_quartic_eulerian_digraphs_diplanar_obstructions` | Problem 1.2 |
| `1706.05642__00` | `AX_h_free_clique_maximizers_polynomial_error` | Informal Conjecture (error term in Proposition 1.4) |
| `1707.03747__00` | `AX_perfect_graphs_tight_skew_partitions_count` | Open Question on Number of Tight Skew Partitions |
| `1707.03888__00` | `AX_additive_chi_approx_minor_closed_triangle_free` | Open question: additive approximation for triangle-free graphs |
| `1707.03888__01` | `AX_additive_chi_approx_kk_minor_free` | Open question: better additive approximation for $K_{4k_0+1}$-minor-free graphs |
| `1707.09402__00` | `AX_independent_fvs_linear_forest_free_complexity` | Complexity of Independent Feedback Vertex Set for H-free graphs (linear forest cases) |
| `1708.00423__00` | `AX_triangle_free_digraph_domination_polynomial_alpha` | Conjecture 3.5 |
| `1708.02370__00` | `AX_clustered_chromatic_minor_closed_treedepth_bound` | Conjecture 4 |
| `1708.07369__00` | `AX_ramsey_nice_forest_families_eventually` | Question 1.1 |
| `1708.07369__01` | `AX_ramsey_nice_forest_families_infinitely_often` | Conjecture 1.5 |
| `1708.08486__00` | `AX_f3n_subspace_free_sets_exponential_base` | Informal Question (correct exponential constant in r(n,m)) |
| `1708.08486__01` | `AX_popular_progression_tower_height_small_primes` | Conjecture (Theorem 2 extends to primes p < 19) |
| `1708.09100__00` | `AX_erdos_ginzburg_ziv_constant_fixed_k` | Open Question on s((Z/kZ)^n) for fixed k |
| `1709.04036__00` | `AX_triangle_free_planar_2_degenerate_7_8` | Conjecture 1.1 |
| `1709.04036__01` | `AX_triangle_free_planar_2_degenerate_5_6` | Informal belief: 5/6 bound attainable |
| `1709.04440__00` | `AX_arithmetic_k_cycle_removal_optimal_exponent` | Question 1.4 |
| `1709.09050__00` | `AX_cop_number_planar_classification` | Classification of planar graphs by cop number |
| `1709.09050__01` | `AX_cop_number_outerplanar_classification` | Classification of outerplanar graphs by cop number |
| `1709.09050__02` | `AX_capture_time_planar_linear_tightness` | Tightness of linear capture time bound for planar graphs |
| `1709.09050__03` | `AX_capture_time_higher_genus_bounds` | Capture time bounds for higher genus graphs |
| `1710.02727__00` | `AX_minor_closed_col_star_characterization` | Conjecture 4 |
| `1710.03117__00` | `AX_polynomial_expansion_balanced_separator_constant_m` | Informal Conjecture (constant-size M) |
| `1710.06282__00` | `AX_erdos_posa_planar_minor_k_log_k` | Conjecture 1.2 |
| `1710.06282__01` | `AX_erdos_posa_treewidth_packing_k_log_k` | Conjecture 1.4 |
| `1710.10663__00` | `AX_list_decodable_zero_rate_codes_asymptotics` | Informal Conjecture on exact asymptotics of maxcode_L for even L |
| `1710.11281__00` | `AX_cop_number_genus_sqrt_g_growth` | Conjecture 8 |
| `1710.11281__01` | `AX_cop_number_riemannian_surfaces_genus_bounded` | Question (Riemannian surfaces): cop number bounded by genus |
| `1710.11281__02` | `AX_cop_number_riemannian_surfaces_cop_convergence` | Question (Riemannian surfaces): cop converging to robber |
| `1710.11281__03` | `AX_cop_number_riemannian_surfaces_worst_genus` | Question (Riemannian surfaces): worst surfaces of fixed genus |
| `1710.11281__04` | `AX_cop_number_riemannian_surfaces_area_supremum` | Question (Riemannian surfaces): supremum of cop number for geometrically bounded surfaces |
| `1710.11281__05` | `AX_cop_number_riemannian_surfaces_constant_curvature` | Question (Riemannian surfaces): constant curvature surfaces |
| `1801.06824__00` | `AX_generalized_coloring_number_cc_characterization` | Open Problem: Characterization of parameters satisfying (CC) |
| `1802.03727__00` | `AX_separation_choosability_grows_min_degree` | Conjecture 1.3 |
| `1802.03727__01` | `AX_dense_bipartite_induced_or_large_clique` | Conjecture 1.4 |
| `1802.03727__02` | `AX_dense_bipartite_induced_triangle_free_log` | Conjecture 1.5 |
| `1802.03727__03` | `AX_dense_bipartite_induced_large_girth` | Conjecture 1.6 |
| `1802.04179__00` | `AX_planar_c4_c5_fractional_chromatic_infimum` | Problem 1.3 |
| `1802.04179__01` | `AX_planar_c4_c5_fractional_chromatic_11_3` | Informal conjecture on optimality of 11/3 |
| `1802.05582__00` | `AX_distributed_coloring_sparse_sublinear_rounds` | Open problem on sublinear round complexity |
| `1802.05582__01` | `AX_distributed_delta_list_coloring_randomized_rounds` | Question on randomized list-coloring round complexity |
| `1803.01051__00` | `AX_list_chromatic_fraction_delta_small_clique` | Question 1.5 |
| `1803.01051__01` | `AX_list_chromatic_reed_bound` | List-chromatic analogue of Reed's Conjecture |
| `1803.03588__00` | `AX_rodl_theorem_polynomial_delta_dependence` | Polynomial dependence of $\delta$ on $d$ in Rödl's theorem |
| `1803.05396__00` | `AX_pt_free_3_coloring_polynomial_large_t` | Open Problem: Complexity of 3-colourability of $P_t$-free graphs |
| `1803.05396__01` | `AX_pt_free_independent_set_polynomial_t_7` | Open Problem: Polynomial-time maximum independent set on $P_t$-free graphs |
| `1803.08462__00` | `AX_hypergraph_max_cut_excess_sqrt_m` | Θ(√m) excess conjecture for hypergraph cuts |
| `1803.10962__00` | `AX_single_conflict_coloring_euler_genus_sqrt` | Conjecture 3 |
| `1803.10962__01` | `AX_single_conflict_coloring_degenerate_log_n` | Informal conjecture on single-conflict chromatic number of degenerate graphs |
| `1804.01060__00` | `AX_coherent_ideal_forest_filleting` | Conjecture 2.4 |
| `1804.06104__00` | `AX_neighbor_sum_distinguishing_delta_plus_constant` | Open Problem: $\Delta + O(1)$ bound for neighbour sum distinguishing colourings |
| `1804.06104__01` | `AX_avd_edge_coloring_probabilistic_barrier` | Informal Conjecture: probabilistic methods insufficient for the $\Delta+2$ bound |
| `1804.07431__00` | `AX_c_closed_graphs_maximal_cliques_exponent` | Open Problem (exact exponent for maximal cliques in c-closed graphs) |
| `1805.06848__00` | `AX_edge_statistics_induced_density_1_over_e` | Conjecture 1.1 (The Edge-statistics Conjecture) |
| `1805.06848__01` | `AX_edge_statistics_large_inducibility_1_over_e` | Conjecture 1.2 (The Large Inducibility Conjecture) |
| `1806.00541__00` | `AX_correlation_polytope_extension_complexity_treewidth` | Conjecture 2 |
| `1806.00825__00` | `AX_short_rainbow_cycles_proper_incident_edges` | Conjecture 4 |
| `1806.00825__01` | `AX_short_rainbow_circuits_matroids` | Conjecture 12 |
| `1806.04188__00` | `AX_binary_matroid_claw_triangle_chi_bounded` | Conjecture 1.6 |
| `1806.06770__00` | `AX_algebraic_connectivity_graph_complement_supremum` | Closing Question |
| `1806.09726__00` | `AX_online_ramsey_random_painter_growth_rate` | Conjecture 7 |
| `1806.09726__01` | `AX_subgraph_query_complexity_km_random` | Conjecture 9 |
| `1806.09726__02` | `AX_online_ramsey_off_diagonal_alteration_bound` | Informal conjecture on generalization of Theorem 4 to all $\tilde{r}(m,n)$ |
| `1806.11196__00` | `AX_pt_free_3_coloring_polynomial_all_t` | Question 1.1 |
| `1807.04969__00` | `AX_erdos_posa_planar_minor_constant_polynomial` | Open Problem (constant c vs. \|H\|) |
| `1808.01605__00` | `AX_large_fractional_chromatic_high_girth_subgraph` | Conjecture 4 |
| `1808.01605__01` | `AX_large_chromatic_high_girth_dense_subgraph` | Conjecture 6 |
| `1808.10370__00` | `AX_cluster_vertex_deletion_2_approximation` | 2-Approximation Conjecture for Cluster-VD |
| `1809.05439__00` | `AX_girth_5_planar_fractional_hub_colors` | Informal conjecture on improved color ratio in Theorem 5 |
| `1809.08324__00` | `AX_bipartite_digraph_caccetta_haggkvist_girth` | Conjecture 1.2 |
| `1809.08324__01` | `AX_bipartite_digraph_caccetta_haggkvist_asymmetric` | Conjecture 1.5 |
| `1810.00058__00` | `AX_sparse_h_free_anticomplete_pairs_linear` | Conjecture 1.4 |
| `1810.00058__01` | `AX_sparse_h_free_anticomplete_pairs_triangle` | Open case H = K3 for Conjecture 1.4 |
| `1810.00058__02` | `AX_sparse_h_free_c_sparse_pairs` | Conjecture 3.4 |
| `1810.00065__00` | `AX_ternary_graphs_3_colorable` | Open Problem: 3-colourability of ternary graphs |
| `1810.00811__00` | `AX_sparse_strong_erdos_hajnal_forests` | Conjecture 1.5 (sparse strong EH-property) |
| `1810.06704__00` | `AX_sparse_neighborhoods_critical_bounded_clique` | Question 1.3 |
| `1810.06704__01` | `AX_sparse_neighborhoods_chromatic_below_delta` | Question 1.4 |
| `1810.08314__00` | `AX_layered_treewidth_bounded_queue_number` | Open problem on queue-number of bounded layered treewidth graphs |
| `1811.08750__00` | `AX_generalized_turan_additive_approximation_np_hard` | Conjecture 1.8 |
| `1811.12252__00` | `AX_graph_isomorphism_h1_h2_free_dichotomy` | Research Question (Introduction) |
| `1811.12252__01` | `AX_graph_isomorphism_fpt_clique_width` | Open Question: FPT Algorithm for Graph Isomorphism Parameterized by Clique-Width |
| `1811.12252__02` | `AX_clique_width_h1_h2_free_boundedness` | Open Cases: Clique-Width Classification for $(H_1,H_2)$-Free Graphs |
| `1811.12650__00` | `AX_frozen_coloring_glauber_delta_o_n` | Informal: Δ = o(n) condition not necessary for Corollary 2 |
| `1811.12650__01` | `AX_frozen_coloring_probability_exponent` | Informal: Exponent in Theorem 1 not optimal |
| `1812.02420__00` | `AX_circular_digraph_homomorphism_complexity` | Problem 2.15 |
| `1812.02420__01` | `AX_circular_digraph_homomorphism_np_complete_cyclic` | Conjecture 2.16 |
| `1812.02420__02` | `AX_fractional_dichromatic_number_complexity` | Problem 3.21 |
| `1812.02420__03` | `AX_directed_kneser_graphs_existence` | Problem 5.40 |
| `1812.07327__00` | `AX_fractional_chromatic_hall_ratio_gap_function` | Problem 4 |
| `1812.07327__01` | `AX_fractional_chromatic_hall_ratio_degree_weighted` | Problem 5 |
| `1812.07327__02` | `AX_bounded_expansion_hall_ratio_shallow_minors` | Problem 8 |
| `1812.09215__00` | `AX_lipschitz_bijection_dictator_xor_inverse` | Informal Question (Section 2) |
| `1812.09752__00` | `AX_hat_guessing_number_degree_degeneracy_bounds` | Problem 1.4 |
| `1812.09752__01` | `AX_hat_guessing_number_complete_bipartite` | Open question: exact value of $HG(K_{n,n})$ |
| `1901.01797__00` | `AX_local_search_ptas_monotone_fo_optimization` | Open Problem (Section 1.1) |
| `1902.06473__00` | `AX_quantum_sorting_poset_lower_bounds_equivalent` | Conjecture on LB and QLB equivalence |
| `1902.06830__00` | `AX_gnm_subgraph_moderate_deviations_sparse` | Remark 1.2 (Open Problem on Sparse Densities) |
| `1902.07018__00` | `AX_list_ramsey_k12_odd_k` | Open question on $R_\ell(K_{1,2}, k)$ for odd $k$ |
| `1902.07018__01` | `AX_list_ramsey_clique_2_colors_equality` | Open problem on equality $R_\ell(K_r, 2) = R(K_r, 2)$ for $r > 3$ |
| `1902.10878__00` | `AX_bipartite_concatenation_phi_ceiling_formula` | Informal Conjecture (Introduction) — analogue of Kneser's theorem |
| `1902.10878__01` | `AX_bipartite_concatenation_psi_symmetry` | Open Question — symmetry of $\psi$ (biconstrained case) |
| `1903.04761__00` | `AX_perfect_graphs_combinatorial_mis_algorithm` | Combinatorial Polynomial-Time Algorithm for MIS/MWIS in Perfect Graphs |
| `1903.04761__01` | `AX_mwis_long_hole_prism_free_fpt` | FPT Algorithm for MWIS in (Long-Hole, k-Prism)-Free Graphs |
| `1903.04863__00` | `AX_behrend_sets_avoiding_mixed_sign_patterns` | Informal question on Behrend-style sets avoiding affine patterns with mixed-sign coefficients |
| `1903.04863__01` | `AX_corners_popular_difference_abelian_groups` | Informal conjecture on extending Mandache's Theorem 1.1 to all abelian groups |
| `1903.05363__00` | `AX_crossing_critical_max_degree_optimal_bounds` | Optimal degree bounds $D_c$ for small $c$ |
| `1903.11287__00` | `AX_convex_unit_distance_realization_gk` | Open Question on Convex Unit Distance Realization of Graphs $G_k$ |
| `1903.11685__00` | `AX_lattice_cube_list_colorability_threshold` | Optimal n for $L^d_n$-list-colorability |
| `1904.02595__00` | `AX_direct_product_multipartite_independence_equals_irredundance` | Conjecture 1.2 |
| `1904.06184__00` | `AX_perfect_matching_flip_switchable_recognition` | Open Question: Recognition of Switchable Graphs |
| `1904.12060__00` | `AX_list_total_coloring_delta_plus_2` | Conjecture 5 |
| `1904.12273__00` | `AX_induced_detour_path_excess_3` | Open Problem (induced st-path of excess length three) |
| `1904.12273__01` | `AX_long_odd_hole_heavy_path_lemma` | Informal Conjecture (heavy path extension) |
| `1904.12273__02` | `AX_long_odd_hole_detection_running_time` | Open Question (running time improvement for long hole detection) |
| `1905.05312__00` | `AX_book_number_triangle_count_extremal_density` | Conjecture 1.1 |
| `1905.10483__00` | `AX_clique_factor_product_dimension_asymptotics` | Open Problem: asymptotic behavior of $Q(s,r)$ when $s$ and $r$ grow together |
| `1905.12142__00` | `AX_gnp_subgraph_count_anticoncentration_bound` | Conjecture 1.12 |
| `1907.00351__00` | `AX_minor_closed_class_dichromatic_number_2` | Question 1 |
| `1907.01083__00` | `AX_perfect_graphs_combinatorial_independent_set_algorithm` | Open problem: Combinatorial algorithm for MIS on perfect graphs |
| `1907.04066__00` | `AX_near_triangulation_4_coloring_extension_complexity` | Problem 1 |
| `1907.04066__01` | `AX_plane_near_cubic_coloring_cone_b5` | Conjecture 8 |
| `1907.04585__00` | `AX_mwis_qptas_forest_subdivision_free` | Conjecture 1.3 |
| `1907.06019__00` | `AX_exterior_algebra_self_annihilating_extremal` | Question on extremal self-annihilating subspaces (Theorem 2.3) |
| `1907.06019__01` | `AX_exterior_algebra_mutually_annihilating_extremal` | Question on extremal mutually annihilating pairs (Theorem 2.4) |
| `1907.07250__00` | `AX_hypercube_coloring_1_ball_reconstruction_threshold` | Gap problem for 1-ball reconstruction threshold |
| `1907.11429__00` | `AX_mycielski_graphs_independence_ratio` | Open problem on minimum independence ratio of Mycielski graphs |
| `1907.11600__00` | `AX_tree_decomposition_edge_connectivity_leaf_count` | Conjecture 5 |
| `1907.12091__00` | `AX_cycle_count_m_edges_exponential_base` | Conjecture 2 |
| `1907.12999__00` | `AX_kt_minor_free_independence_n_over_t` | Conjecture 1 |
| `1907.12999__01` | `AX_minor_ramsey_ks_free_sublinear_bound` | Conjecture on $MR_t(s,k)$ for $s \geq 4$ |
| `1908.03694__00` | `AX_quantum_ergodicity_small_spectral_window` | Open problem on quantum ergodicity over small spectral windows (Remark 1.2) |
| `1908.03788__00` | `AX_avoidable_paths_two_disjoint_pk` | Question 1.12 |
| `1908.03788__01` | `AX_avoidable_non_path_family_existence` | Question 4.1 |
| `1908.06300__00` | `AX_bounded_subdeterminant_integer_programs_polynomial` | Conjecture on polynomial-time solvability of bounded sub-determinant integer programs |
| `1908.06300__01` | `AX_stable_set_bounded_ocp_arbitrary_genus` | Open question on stable set for bounded ocp and arbitrary Euler genus |
| `1909.05988__00` | `AX_link_hypergraph_ramsey_rate_odd_girth` | Exact Ramsey growth rate dependence on G for link hypergraphs |
| `1909.05988__01` | `AX_hypergraph_independence_fk_order` | Determine the order of f_k(N; s, t) in general |
| `1909.07141__00` | `AX_disproportionate_division_2n_minus_2_cuts` | Informal Conjecture (f(n) = 2n−2) |
| `1909.07141__01` | `AX_disproportionate_division_circle_measure_bipartition` | Conjecture 3.1 |
| `1909.08426__00` | `AX_independent_set_h_free_polynomial_dichotomy` | Classical MIS Dichotomy Conjecture |
| `1909.08426__01` | `AX_independent_set_h_free_fpt_dichotomy` | Parameterized MIS Dichotomy |
| `1909.08426__02` | `AX_independent_set_fpt_blownup_p4_free` | Conjecture 1 |
| `1909.08426__03` | `AX_independent_set_fpt_blownup_path_free` | Conjecture 2 |
| `1909.08426__04` | `AX_independent_set_fpt_h_free_candidates` | Informal belief on FPT candidates |
| `1909.11578__00` | `AX_symmetric_intersecting_vector_families_size` | Size of symmetric intersecting families in $[k]^n$ |
| `1909.11578__01` | `AX_symmetric_intersecting_vector_families_set_intersecting` | Largest symmetric intersecting families are set-intersecting |
| `1909.11578__02` | `AX_symmetric_intersecting_vector_families_polynomial_gain` | Polynomial improvement on symmetric intersecting family size bound |
| `1909.12175__00` | `AX_p_entropic_matroids_prime_representable` | Open problem: p-entropic matroids linear for prime p |
| `1910.00697__00` | `AX_chi_bounded_not_polynomially_chi_bounded` | Open problem: χ-bounded vs. polynomially χ-bounded |
| `1911.03427__00` | `AX_induced_arithmetic_removal_higher_complexity` | Open Problem (Extending Induced Arithmetic Removal to Higher Complexity and General Groups) |
| `1911.03427__01` | `AX_induced_arithmetic_removal_abelian_groups` | Informal Conjecture (Induced Arithmetic Removal for Arbitrary Abelian Groups) |
| `1911.03427__02` | `AX_induced_arithmetic_removal_complexity_1_polynomial` | Informal Conjecture (Polynomial Quantitative Bound for Complexity 1 Systems) |
| `1912.01570__00` | `AX_planar_fvs_face_packing_ratio_2` | Conjecture 2 |
| `1912.02342__00` | `AX_bounded_vc_dimension_erdos_hajnal` | Conjecture 4.1 |
| `1912.07205__00` | `AX_triangulation_4_coloring_complex_mixed_parity` | Conjecture 8 |
| `1912.07722__00` | `AX_acyclic_subgraph_chromatic_oriented_function` | Problem 1.1 |
| `1912.07722__01` | `AX_acyclic_subgraph_chromatic_tournament_exponent` | Conjecture 4.1 |
| `1912.07965__00` | `AX_planar_expansions_edge_erdos_posa` | Open Problem (edge-EP property characterization for planar graph expansions) |
| `1912.08328__00` | `AX_blowup_ramsey_prefactor_depends_on_g` | Conjecture on unavoidable G-dependence in Theorem 2 |
| `1912.11246__00` | `AX_prism_pyramid_theta_turtle_free_separators` | Conjecture 2.2 |
| `1912.11246__01` | `AX_even_hole_free_independent_set_complexity` | Open problem: MIS complexity in even-hole-free graphs |
| `1912.11246__02` | `AX_prism_pyramid_theta_wheel_free_separators` | Open problem: polynomial separator property for (prism, pyramid, theta, even wheel)-free graphs |
| `2001.01552__00` | `AX_strong_coloring_numbers_tame_representation` | Question 6 |
| `2001.01552__01` | `AX_strong_coloring_numbers_tame_representation_negative` | Informal conjecture: negative answer to Question 6 |
| `2001.01607__00` | `AX_even_hole_k4_diamond_free_treewidth` | Open Question: (even hole, K4, diamond)-free treewidth/cliquewidth |
| `2001.01607__01` | `AX_theta_triangle_free_bounded_degree_treewidth` | Open Question: (theta, triangle)-free graphs of bounded degree |
| `2001.01607__02` | `AX_triangle_s123_free_cliquewidth` | Open Question: (triangle, S1,2,3)-free graphs cliquewidth |
| `2001.01607__03` | `AX_mis_complexity_even_hole_k4_free` | Maximum Independent Set complexity for (even hole, K4)-free and (theta, triangle)-free graphs |
| `2001.01607__04` | `AX_mis_complexity_subdivided_claw_free_p7` | Maximum Independent Set complexity for H-free graphs when H contains P7, S1,1,3, or S1,2,2 |
| `2001.03794__00` | `AX_grundy_coloring_half_graph_free_fpt` | FPT on $H_{t,t}$-free graphs for Grundy Coloring and b-Chromatic Core |
| `2001.03794__01` | `AX_grundy_coloring_biclique_free_fpt` | FPT on $K_{t,t}$-free graphs for Grundy Coloring |
| `2001.03794__02` | `AX_partial_grundy_coloring_parameterized_complexity` | Parameterized complexity of Partial Grundy Coloring on general graphs |
| `2001.09679__00` | `AX_sublinear_separator_expansion_exponent_exact` | Informal open question on the exact value of $b_\varepsilon$ |
| `2001.09679__01` | `AX_sublinear_separator_expansion_exponent_one_sided` | Informal conjecture $b'_\varepsilon = b_\varepsilon$ for $0<\varepsilon<\tfrac{1}{2}$ |
| `2002.00258__00` | `AX_surface_excluded_minors_hoppers_exist` | Informal Conjecture on Existence of Hoppers for Large Euler Genus |
| `2002.00496__00` | `AX_ladder_minor_bumping_universal_constant` | Informal Conjecture on Universal N0 for Bumping a Ladder |
| `2002.00496__01` | `AX_poset_cover_graph_unavoidable_minors_characterization` | Open Problem: Characterization of Unavoidable Graphs |
| `2002.00496__02` | `AX_poset_cover_graph_unavoidable_minors_kelly` | Conjecture 6 |
| `2002.05383__00` | `AX_planar_recoloring_linear_diameter_min_colors` | Problem 3 |
| `2002.11100__00` | `AX_star_contraction_clique_minor_strategy_generality` | Informal conjecture on the generality of the probabilistic minor strategy |
| `2003.01846__00` | `AX_outerplanar_strongly_perfect_characterization` | Informal Conjecture (outerplanar strongly perfect graphs) |
| `2003.05185__00` | `AX_perfect_graphs_combinatorial_mwis_algorithm` | Combinatorial polynomial-time algorithm for MWIS in perfect graphs |
| `2003.05185__01` | `AX_mwis_p7_free_complexity` | MWIS in P7-free graphs |
| `2003.07061__00` | `AX_epsilon_t_nets_size_computation` | The $\varepsilon$-$t$-Net Problem |
| `2004.02657__00` | `AX_3_graph_homeomorph_exponent_5_2` | Conjecture 1.2 |
| `2004.05942__00` | `AX_pentagon_contact_representation_algorithm_terminates` | Algorithm Termination Conjecture |
| `2004.06788__00` | `AX_cubic_many_3_edge_colorings_reflexive` | Informal Conjecture on reflexive graphs and coloring abundance |
| `2004.07214__00` | `AX_dom_enum_incomparability_st_free_posets` | Conjecture 7.1 |
| `2004.07214__01` | `AX_dom_enum_incomparability_cobipartite_free` | Conjecture 7.3 |
| `2004.07457__00` | `AX_bipartite_asymmetric_list_sizes_optimal` | Problem 3 |
| `2004.07457__01` | `AX_bipartite_asymmetric_list_sizes_krivelevich_alon` | Conjecture 7 |
| `2004.10180__00` | `AX_c5_free_triangle_removal_exponent` | Optimality of the $o(n^{3/2})$ bound in Corollary 1.4 |
| `2004.10180__01` | `AX_linear_equation_free_sets_sqrt_n` | Improvement of the bound in Theorem 1.12 |
| `2004.12166__00` | `AX_mis_approximation_h_free_improved` | Conjecture 5 (Improved Approximation Conjecture) |
| `2004.12166__01` | `AX_mis_approximation_h_free_optimal_exponent` | Question: optimal approximation exponent for MIS in H-free graphs |
| `2004.14789__00` | `AX_polynomial_expansion_bounded_twin_width_speculation` | Informal Conjecture (polynomial expansion and bounded twin-width) |
| `2004.14789__01` | `AX_twin_width_nowhere_dense_fo_superclass` | Question (common superclass for FPT FO model checking) |
| `2005.05042__00` | `AX_k_creature_free_polynomial_minimal_separators` | Conjecture 1.4 |
| `2005.09767__00` | `AX_group_connectivity_exponentially_many_flows` | Conjecture 1.10 |
| `2005.10849__00` | `AX_cop_number_girth_exponent_quarter` | Optimality of the exponent 1/4 |
| `2005.12568__00` | `AX_convex_drawings_vs_pseudocircular_drawings` | Open problem: convex drawings vs. pseudocircular drawings |
| `2005.12861__00` | `AX_induced_detour_path_fixed_k` | Question 1.5 |
| `2006.00534__00` | `AX_minimal_complements_count_sqrt_n` | Conjecture 7 |
| `2006.00534__01` | `AX_minimal_complements_count_prime_order` | Question 8 |
| `2006.00534__02` | `AX_maximal_supplement_solid_subset_optimal` | Question 9 |
| `2006.00534__03` | `AX_minimal_complements_random_subset_threshold` | Question 10 |
| `2006.09269__00` | `AX_planar_recoloring_girth_5_six_colors` | Conjecture 5 |
| `2006.09877__00` | `AX_small_classes_bounded_twin_width` | The Small Conjecture |
| `2006.09877__01` | `AX_polynomial_expansion_bounded_twin_width` | Question: polynomial expansion and twin-width |
| `2007.14161__00` | `AX_twin_width_mis_dominating_approximability` | Informal conjecture on MIS approximability vs. Min Dominating Set |
| `2008.01616__00` | `AX_map_isomorphism_quadratic_lower_bound` | Conjecture 1.2 |
| `2008.01616__01` | `AX_map_isomorphism_superlinear_lower_bound` | Open subproblem: conditional superlinear lower bound |
| `2008.03587__00` | `AX_zombie_number_leaf_attachment_invariance` | Question 4.1 |
| `2008.03587__01` | `AX_zombie_number_subdivision_increase` | Question 4.2 |
| `2008.05504__00` | `AX_even_hole_free_bounded_degree_treewidth` | Conjecture 2 |
| `2008.05504__01` | `AX_bounded_degree_treewidth_induced_wall` | Conjecture 3 |
| `2008.09692__00` | `AX_cell_3_colorable_3_flowable_subcontraction` | Conjecture 11 |
| `2009.03418__00` | `AX_crossing_number_kn_minus_matching` | Conjecture 5 |
| `2009.05691__00` | `AX_shortest_even_hole_detection` | Open Problem: Finding a Shortest Even Hole |
| `2009.05691__01` | `AX_holes_length_divisible_3_detection` | Open Question: Detecting Holes of Length Divisible by Three |
| `2009.07840__00` | `AX_friends_strangers_random_connectivity_threshold` | Informal Conjecture (§1.2, Theorem 1.1 remarks) |
| `2009.07840__01` | `AX_friends_strangers_isolated_vertex_cutoff_coincide` | Open Question (§1.2, Theorem 1.4 remarks) |
| `2009.12189__00` | `AX_planar_fractional_vertex_arboricity_2` | Conjecture 1.1 |
| `2009.13319__00` | `AX_heroic_sets_bounded_dichromatic_characterization` | Problem 1.2 |
| `2009.13319__01` | `AX_heroic_sets_hero_oriented_forest` | Conjecture 4.2 |
| `2009.13319__02` | `AX_heroic_sets_clique_oriented_forest` | Conjecture 4.4 |
| `2009.13319__03` | `AX_heroic_sets_minimal_tournament_families` | Research direction: minimal heroic tournament families |
| `2010.05735__00` | `AX_tournament_path_powers_exponent_constant` | Open Problem: exact constant in the exponent |
| `2010.05992__00` | `AX_near_sunflower_exponential_bound` | Near-sunflower analogue of the Erdős-Rado Sunflower Conjecture |
| `2010.05992__01` | `AX_binary_focal_family_bound_not_tight` | Informal conjecture on non-tightness of upper bound for binary focal families |
| `2010.08988__00` | `AX_oriented_matroid_even_directed_circuit` | Problem 1.4 |
| `2011.08049__00` | `AX_genus_approximation_spherical_density_regime` | Open Problem (Spherical Density Regime) |
| `2012.05112__00` | `AX_divisible_subdivision_clique_minor_f_growth` | Open Problem (asymptotic behavior of f(H,q)) |
| `2012.05112__01` | `AX_divisible_subdivision_g_q_linear` | Informal Conjecture (linearity of g(q)) |
| `2101.03537__00` | `AX_ordered_pure_pairs_n_polylog` | Informal belief on Conjecture 1.7 and polylog bound |
| `2102.01034__00` | `AX_surface_k_dicolorability_complexity_4_5` | Problem 4.4 |
| `2102.04994__00` | `AX_erdos_hajnal_c8_complement_c8` | Erdős-Hajnal property for $\{C_8, \overline{C_8}\}$ |
| `2102.07705__00` | `AX_oriented_tree_avoiding_2_coloring_complexity` | Open Complexity Problem (2-F-PFC for oriented trees of maximum degree ≥ 3) |
| `2102.10061__00` | `AX_planar_weak_coloring_number_quadratic_log` | Conjecture 4 |
| `2102.10220__00` | `AX_k_colorable_deletion_clique_free_sharp` | Conjecture on sharpness of Theorem 1.1 |
| `2102.10220__01` | `AX_k_colorable_deletion_odd_wheel_sharp` | Conjecture on sharpness of Theorem 1.5 |
| `2102.10220__02` | `AX_k_colorable_deletion_neighborhood_edge_cover` | Question 2.1 |
| `2102.10220__03` | `AX_k_colorable_deletion_mnk_asymptotics` | Open problem on $m(n,k)$ for fixed $k \geq 2$ |
| `2103.05036__00` | `AX_random_embedding_expected_faces_linear` | Conjecture 1 |
| `2103.05998__00` | `AX_hitting_max_independent_sets_graph_chromatic` | Informal Conjecture on Chromatic Number of $G_{m,t}$ |
| `2103.08698__00` | `AX_sublinear_separators_fractional_treewidth_fragile` | Informal Conjecture (fractional treewidth-fragility of sublinear-separator classes) |
| `2103.08698__01` | `AX_fo_minimization_approximation_bounded_expansion_ptas` | Problem 6 |
| `2103.08698__02` | `AX_fo_maximization_approximation_nowhere_dense` | Problem 7 |
| `2103.10497__00` | `AX_sunflower_bounded_vc_dimension_exponential` | Conjecture 1.1 |
| `2103.10684__00` | `AX_quasi_clique_minor_gap_infimum` | Question 1.6 |
| `2103.10684__01` | `AX_kt_minor_free_recoloring_single_class` | Question 1.7 |
| `2103.15175__00` | `AX_list_ramsey_chromatic_family_exact` | Conjecture on $R_\ell(\mathcal{H}_s, k)$ |
| `2103.15175__01` | `AX_list_ramsey_exponential_constant_k3` | Determine the exponential constant in $R_\ell(H,k)$ |
| `2103.17094__00` | `AX_intersection_graphs_polynomial_weak_coloring_numbers` | Question (polynomial weak coloring numbers for intersection graph classes) |
| `2104.11626__00` | `AX_triangle_removal_vs_dfl_growth` | Informal Conjecture on similar growth of $N_{DFL}(\varepsilon)$ and $1/\delta_{TRL}(\varepsilon)$ |
| `2105.01780__00` | `AX_treewidth_fragile_weighted_vertex_cover_ptas` | Open Problem: PTAS for weighted minimization problems in fractionally treewidth-fragile classes |
| `2105.01787__00` | `AX_5_coloring_p4_rp3_free_complexity` | Open Problem: 5-Coloring complexity for H-free graphs with a P4 component |
| `2105.01787__01` | `AX_list_coloring_rp3_free_np_hard` | Open Question: NP-hardness of List-k-Coloring on rP3-free graphs |
| `2105.02383__00` | `AX_acyclic_digraph_ramsey_bounded_degree_polynomial` | Open problem on parameters governing $\overrightarrow{r}_1(H)$ |
| `2105.07370__00` | `AX_rodl_h_free_restricted_union_cover` | Union cover variant (open problem) |
| `2105.15195__00` | `AX_monochromatic_subset_sums_density_tight` | Conjecture on tightness of the upper bound for all r ≥ 3 |
| `2106.03261__00` | `AX_c4_free_counting_lemma_characterization` | Question 1.1 |
| `2106.03261__01` | `AX_c4_free_counting_petersen_dodecahedron` | Open Problem 2.17 |
| `2106.04894__00` | `AX_littlewood_offord_geometric_nonzero_vectors` | Question 1 |
| `2106.04894__01` | `AX_littlewood_offord_o_minimal_sqrt_n` | Conjecture 1.2 |
| `2106.14762__00` | `AX_runsort_permuton_horizontal_uniformity_direct` | Direct Proof of Horizontal Uniformity |
| `2107.02882__00` | `AX_twin_width_connected_domination_no_kernel` | Open problem: no-kernel lower bound at twin-width 4 for Connected/Total k-Dominating Set |
| `2107.05995__00` | `AX_hat_guessing_degenerate_bounded` | Informal Belief on Degeneracy Bound for Hat Guessing Number |
| `2107.05995__01` | `AX_hat_guessing_random_graph_sublinear` | Question on Typical Hat Guessing Number of G(n,1/2) |
| `2107.05995__02` | `AX_hat_guessing_universal_vertex_addition` | Problem on Hat Guessing Number After Adding a Universal Vertex |
| `2107.11780__00` | `AX_poly_chi_bounded_forests_known_complete` | Informal remark on completeness of known forests satisfying Esperet's conjecture |
| `2108.00987__00` | `AX_odd_cycle_ramsey_multiplicity_exact` | Conjecture 4 |
| `2108.00991__00` | `AX_threshold_ramsey_multiplicity_paths_exact` | Conjecture 3 |
| `2108.02685__00` | `AX_irregular_spanning_subgraph_regular_graphs` | Conjecture 1.1 |
| `2108.02685__01` | `AX_irregular_spanning_subgraph_min_degree` | Conjecture 1.2 |
| `2108.12669__00` | `AX_triangle_free_planar_3_coloring_count` | Conjecture 1 |
| `2109.00327__00` | `AX_kt_minor_free_universal_graph_separators` | Open Problem (Section 1): Balanced Separator for $U_t$ |
| `2109.00618__00` | `AX_multiplicative_group_matrix_rank_sharp_bounds` | Open problem: improved quantitative rank bounds |
| `2109.01310__00` | `AX_four_families_free_logarithmic_treewidth` | Conjecture 1.10 |
| `2109.09205__00` | `AX_ramsey_goodness_books_threshold_not_tight` | Informal Belief on Non-Optimality of p-Goodness Bound |
| `2109.09205__01` | `AX_ramsey_goodness_regularity_free_proof` | Question on Eliminating the Regularity Lemma from Nikiforov–Rousseau's General Theorem |
| `2110.00278__00` | `AX_forest_free_polynomial_chi_omega_power` | Conjecture 1.3 |
| `2110.09403__00` | `AX_kt_minor_free_list_chromatic_2t` | Problem 1 |
| `2110.09970__00` | `AX_ell_holed_graphs_structure_small_ell` | Open Problem: characterisation of ℓ-holed graphs for ℓ ∈ {4, 5, 6} |
| `2110.10530__00` | `AX_tree_bounded_growth_r_burnable` | Conjecture 7 |
| `2110.14521__00` | `AX_active_clustering_clique_algorithm_optimal` | Conjecture 5 |
| `2110.15429__00` | `AX_grid_arithmetic_progression_discrepancy_tight` | Conjecture (Section 7) |
| `2111.00282__00` | `AX_twin_width_approximation_unordered_graphs` | Open Challenge: Efficient Approximation of Twin-Width for Unordered Graphs |
| `2111.00532__00` | `AX_pure_pairs_blockade_transversal_triangle_polynomial` | Question 1.3 |
| `2111.00532__01` | `AX_pure_pairs_blockade_polynomial_ordered_graphs` | Informal: which graphs H admit polynomial-size pure pairs |
| `2111.00532__02` | `AX_pure_pairs_blockade_strong_transversal_characterization` | Informal: characterization of graphs with the strong transversal property |
| `2111.07147__00` | `AX_plane_graphs_weak_diameter_2_coloring` | Question 6 |
| `2112.02313__00` | `AX_degenerate_graphs_polynomial_kempe_sequences` | Polynomial Kempe sequences for degenerate graphs |
| `2112.02378__00` | `AX_segment_graphs_kr_free_linear_induced` | Problem 1.2 |
| `2112.08456__00` | `AX_convex_complete_geometric_k_planar_partition` | Question 9 |
| `2201.00328__00` | `AX_implicit_representation_speed_sqrt_n_labels` | Question (Section 3, implicit representation for speed $2^{O(n\log n)}$) |
| `2201.00328__01` | `AX_implicit_representation_speed_n23_labels` | Question (Section 3, implicit representation for speed $2^{n^{1+\varepsilon}}$) |
| `2201.04062__00` | `AX_pure_pairs_sparse_excluded_linear_side` | Possibility 1.6 |
| `2201.04062__01` | `AX_pure_pairs_sparse_excluded_stronger_coherence` | Open question on Theorem 3.3 with stronger coherence |
| `2201.08204__00` | `AX_clique_3_triangle_free_induced_bounded` | Question 3.1 |
| `2201.08204__01` | `AX_odd_dicycle_free_digraph_dichromatic_bounded` | Question 3.2 |
| `2201.09115__00` | `AX_kst_minor_free_choosable_k44_k35` | Question 1 |
| `2201.09115__01` | `AX_kst_minor_free_choosable_2s_t` | Question 2 |
| `2201.09115__02` | `AX_kst_minor_free_choosable_fixed_s` | Open problem: Woodall's conjecture for fixed s |
| `2201.09115__03` | `AX_kst_minor_free_choosable_smallest_counterexample` | Open problem: smallest counterexample to Woodall's conjecture |
| `2202.01006__00` | `AX_chordal_digraphs_dichromatic_construction_size` | Open problem on construction size |
| `2202.05557__00` | `AX_forest_free_polynomial_chi_bounded` | Conjecture 1.3 |
| `2202.05557__01` | `AX_path_free_polynomial_chi_tau_d` | Question: Extending Theorem 1.6 to paths |
| `2202.05557__02` | `AX_hereditary_tau_d_bounded_implies_polynomial` | Question: Polynomial bound analogue of Esperet's conjecture for $\tau_d$ |
| `2202.06810__00` | `AX_structured_graph_codes_f2c_odd_n` | Open case of Theorem 3 for odd $n$ |
| `2202.07293__00` | `AX_intersection_graphs_asymptotic_dimension_tight` | Optimal bound question |
| `2202.07746__00` | `AX_random_embedding_expected_faces_third_n` | Conjecture 4 |
| `2202.09118__00` | `AX_poly_chi_bounded_hereditary_characterization` | Question (which hereditary classes are poly-χ-bounded?) |
| `2202.09118__01` | `AX_poly_chi_bounded_odd_multihole_free` | Open problem (poly-χ-bounded for k-multihole with only odd cycles) |
| `2202.09118__02` | `AX_forest_free_polynomial_chi_all_forests` | Informal conjecture (polynomial Gyárfás–Sumner) |
| `2202.09118__03` | `AX_poly_chi_bounded_trees_disjoint_union` | Open problem (disjoint union of good trees) |
| `2202.09118__04` | `AX_poly_chi_bounded_self_isolating_all` | Question (are all graphs self-isolating?) |
| `2202.10412__00` | `AX_forest_free_polynomial_chi_good` | Informal Conjecture (every forest is good) |
| `2202.10412__01` | `AX_broom_nondominating_copy_no_scattering` | Conjecture 2.3 |
| `2202.11988__00` | `AX_counting_perfect_matchings_alpha_2_hard` | Conjecture 3 |
| `2202.13306__00` | `AX_heroes_complete_multipartite_delta_1_2_2` | Question 1.4 |
| `2202.13306__01` | `AX_heroes_k1_join_delta_1_1_h` | Question 5.4 |
| `2202.13977__00` | `AX_tournament_strong_eh_backedge_forest` | Conjecture 1.5 |
| `2202.13977__01` | `AX_tournament_strong_eh_three_backedges_d5` | Informal question: can the D5-freeness hypothesis in Theorem 1.6 be dropped? |
| `2203.03612__00` | `AX_f_free_induced_girth_preserving_bounded` | Girth Conjecture (strengthening of Theorem 3) |
| `2203.06775__00` | `AX_c4_diamond_theta_prism_bounded_treewidth` | Conjecture 1.6 |
| `2204.00722__00` | `AX_unit_segment_graphs_twin_width_delineated` | Open Question (unit segment graphs delineation) |
| `2204.01938__00` | `AX_r_free_digraphs_near_acyclic` | Conjecture on r-free digraphs with r > 2n/3 |
| `2204.01938__01` | `AX_random_orientation_feedback_arc_surplus` | Suspected directed surplus of a random B-free orientation (Remark 1.6) |
| `2204.10119__00` | `AX_k6_minor_6_regular_graphs` | Conjecture 1.3 |
| `2204.10119__01` | `AX_k6_minor_min_6_max_8` | Informal Conjecture: min degree $\geq 6$, max degree $\leq 8$ forces $K_6$ minor |
| `2204.10119__02` | `AX_k6_minor_bipartite_min_degree_5` | Open Question: minimum degree five in Theorem 1.6 |
| `2204.10119__03` | `AX_k5_minor_bipartite_average_degree_5` | Informal Conjecture: average degree $\geq 5$ and max degree $\leq 6$ forces $K_5$ minor in bipartite graphs |
| `2204.12330__00` | `AX_groups_uniform_twin_width_strictly_stronger` | Informal Conjecture (uniform twin-width strictly stronger than twin-width) |
| `2204.12330__01` | `AX_groups_infinite_twin_width_explicit_construction` | Question (explicit group with infinite twin-width) |
| `2204.12330__02` | `AX_sparse_twin_width_queue_number_separation` | Open Problem (separating twin-width and queue number on sparse graphs) |
| `2204.12683__00` | `AX_subcubic_triangle_free_fractional_19_7` | Conjecture 1.6 |
| `2205.07498__00` | `AX_z3_flow_critical_density_genus_coefficient` | Problem 1.6 |
| `2205.08181__00` | `AX_arrangement_graphs_4_critical_infinite_family` | Belief on 4-vertex-critical arrangement graphs |
| `2205.09302__00` | `AX_dope_matrices_generic_conditions_ert_sufficient` | Conjecture on Sufficiency of Conditions E, R, T for Generic Tuples |
| `2205.12764__00` | `AX_planar_square_root_np_complete` | Conjecture 1.3 |
| `2206.00186__00` | `AX_large_chromatic_dense_minor_edge_density` | Informal conjecture on improving the $g(t)$ lower bound |
| `2206.00594__00` | `AX_induced_cycle_packing_bounded_mis_polynomial` | Conjecture 1.3 |
| `2206.00594__01` | `AX_induced_cycle_packing_sparse_twin_width` | Open Question: bounded twin-width for sparse $\mathcal{O}_k$-free graphs |
| `2206.00594__02` | `AX_induced_cycle_packing_odd_mis_tractable` | Informal conjecture: MIS tractable in bounded-iocp graphs |
| `2206.10733__00` | `AX_happy_triples_bound_small_max_degree` | Open problem on happy triples for $l < k/2$ |
| `2206.11371__00` | `AX_set_coloring_ramsey_chromatic_variant_equality` | Informal Conjecture on R(n;r,s) vs R'(n;r,s) near Turán density |
| `2206.12335__00` | `AX_1_independent_percolation_q3_signs_model` | Conjecture 6.2 |
| `2206.12335__01` | `AX_1_independent_percolation_hypercube_giant_threshold` | Problem 6.4 |
| `2206.13635__00` | `AX_kt_minor_free_hypergraph_chromatic_bound` | Conjecture 2 |
| `2206.13635__01` | `AX_kt_minor_free_hypergraph_3_colorable` | Problem 1 |
| `2207.07775__00` | `AX_ramsey_multiplicity_polite_integers` | Conjecture 1.5 |
| `2207.07775__01` | `AX_ramsey_multiplicity_mixed_blowup_coloring` | Conjecture 5.3 |
| `2207.07775__02` | `AX_ramsey_multiplicity_lollipop_bonbon` | Conjecture 5.4 |
| `2207.12684__00` | `AX_arithmetic_hyperbolic_surface_diameter_log_volume` | Informal conjecture on the actual diameter |
| `2207.13651__00` | `AX_random_irregular_subgraph_property_range` | Informal Conjecture on Property (*) for d = o(n/log n) |
| `2208.06629__00` | `AX_lazy_transpositions_shuffle_t_counters_exact` | Problem 3 |
| `2208.06630__00` | `AX_reachability_network_min_transpositions` | Problem 1 |
| `2208.06630__01` | `AX_reachability_network_2_uniformity_lazy_transpositions` | Conjecture 1 |
| `2208.06858__00` | `AX_levine_hat_intersecting_success_vanishes` | Conjecture 2.1 |
| `2208.06858__01` | `AX_levine_hat_monotone_success_vanishes` | Conjecture 2.2 |
| `2208.06858__02` | `AX_levine_hat_intersecting_kneser_independence` | Conjecture 2.6 |
| `2208.06858__03` | `AX_independence_ratio_random_subset_gap_positive` | Conjecture 2.8 |
| `2208.06858__04` | `AX_independence_ratio_binomial_subset_gap_positive` | Conjecture 2.9 |
| `2208.10074__00` | `AX_sublinear_separators_product_structure_tree_depth` | Conjecture (product structure with bounded tree-depth and tight clique size) |
| `2208.10074__01` | `AX_sublinear_separators_product_structure_treewidth` | Open Problem 6 |
| `2209.09107__00` | `AX_alon_tarsi_orientation_half_out_degree` | Question 6.1 |
| `2209.09107__01` | `AX_alon_tarsi_matching_removal_half_delta` | Question 6.2 |
| `2209.12023__00` | `AX_twin_width_matrices_infinite_fields` | Open question on twin-width over infinite fields |
| `2210.03545__00` | `AX_grid_ramsey_rectangle_vs_clique` | Grid Ramsey Problem (gr(G_{2x2}, K_n)) |
| `2210.03545__01` | `AX_grid_ramsey_equals_hypergraph_clique_star` | Informal Conjecture: r(K^(3)_4, S^(3)_n) and gr(G_{2x2}, K_n) have the same order |
| `2210.03545__02` | `AX_hypergraph_ramsey_k4_minus_edge_star` | Informal Conjecture: r(K^(3)_{4-e}, S^(3)_n) = Theta(n^2 / log n) |
| `2210.09227__00` | `AX_multidimensional_ramsey_r2_superexponential` | Problem 4.1 |
| `2210.09227__01` | `AX_multidimensional_ramsey_r2_vs_erdos_szekeres` | Problem 4.2 |
| `2210.12699__00` | `AX_subdigraph_half_vertices_min_outdegree_gap` | Open problem: closing the gap for $d(s)$ |
| `2210.12754__00` | `AX_random_graph_hereditary_extremal_probability_range` | Open Problem (characterizing edge probabilities for Theorem 1.1) |
| `2210.12754__01` | `AX_random_graph_hereditary_extremal_bipartite_asymptotics` | Open Problem (accurate estimate in the bipartite case) |
| `2210.12754__02` | `AX_random_graph_hereditary_extremal_polynomial_saving` | Informal Conjecture (polynomial saving in the bipartite case) |
| `2210.13720__00` | `AX_linear_growth_tree_strong_product_subgraph` | Conjecture 14 |
| `2210.15076__00` | `AX_turan_h_free_bounded_matching_number` | Extension to H-free graphs |
| `2210.16971__00` | `AX_directed_sidorenko_bipartite_homomorphism` | Conjecture 1.4 |
| `2210.16971__01` | `AX_directed_sidorenko_forcing_cycle_homomorphism` | Conjecture 1.7 |
| `2210.16971__02` | `AX_sidorenko_asymmetric_classical_equivalent` | Equivalence of asymmetric and classical Sidorenko properties |
| `2211.01032__00` | `AX_random_embedding_faces_gnp_logarithmic` | Conjecture 1.13 |
| `2211.01032__01` | `AX_random_embedding_faces_gnp_all_p` | Conjecture 9.1 |
| `2211.01032__02` | `AX_random_embedding_faces_dense_logarithmic` | Conjecture 9.3 |
| `2211.01032__03` | `AX_random_embedding_faces_nonorientable_complete` | Conjecture 9.5 |
| `2211.01032__04` | `AX_random_embedding_faces_nonorientable_vs_orientable` | Conjecture 9.6 |
| `2211.14218__00` | `AX_shotgun_assembly_second_threshold_all_radii` | Informal Conjecture (second phase transition for all radii) |
| `2211.14218__01` | `AX_shotgun_assembly_second_threshold_radius_2` | Question |
| `2212.02737__00` | `AX_clean_classes_finite_family_characterization` | Question: finite families yielding clean H-free classes |
| `2212.05133__00` | `AX_neighborly_boxes_limit_one_half` | Conjecture on the asymptotic of n(2,d) |
| `2212.05133__01` | `AX_neighborly_boxes_limit_exists` | Open question on existence of lim n(2,d)/d^2 |
| `2301.02020__00` | `AX_independent_set_reconfiguration_diameter_k4_cubic` | Conjecture 4 |
| `2301.02020__01` | `AX_independent_set_reconfiguration_diameter_max_k` | Question 8 |
| `2301.02138__00` | `AX_even_hole_free_chordal_modulator` | Informal Conjecture (chordal modulator characterization for even-hole-free graphs) |
| `2301.02177__00` | `AX_kromatic_claw_free_grassmannian_subvariety` | Grassmannian Subvariety Construction Problem |
| `2301.08707__00` | `AX_separating_path_system_strong_2n` | Problem 3 |
| `2301.08707__01` | `AX_separating_path_system_rainbow_cover_linear` | Problem 4 |
| `2301.11019__00` | `AX_point_set_random_distances_reconstruction_threshold` | Informal conjecture on sharp threshold for linear-proportion reconstruction |
| `2301.13305__00` | `AX_graph_codes_even_edges_density_vanishes` | Question 1.1 |
| `2301.13305__01` | `AX_graph_codes_k4_density_vanishes` | Informal question: is $d_{K_4}(n) = o(1)$? |
| `2301.13305__02` | `AX_graph_codes_linear_even_h_bounds` | Open problem: tighter bounds for linear graph-codes |
| `2301.13305__03` | `AX_graph_codes_cube_length_interval_vectors` | Open problem: binary vectors with cube-length forbidden symmetric difference |
| `2301.13305__04` | `AX_graph_codes_odd_intersection_edge_coloring` | Open problem: minimum edge-coloring with odd intersection property |
| `2302.02995__00` | `AX_treedepth_bound_treewidth_binary_tree_path` | Open Problem: sharpness of the treedepth bound in Theorem 1 |
| `2302.04986__00` | `AX_hitting_max_stable_sets_forest_free` | Conjecture 1.8 |
| `2302.04986__01` | `AX_hitting_max_stable_sets_pt_free` | Conjecture 1.13 |
| `2302.04986__02` | `AX_hitting_max_stable_sets_p5_polynomial` | Conjecture 1.17 |
| `2302.04986__03` | `AX_hitting_max_stable_sets_mt_polynomial` | Conjecture 1.20 |
| `2302.04986__04` | `AX_hitting_max_stable_sets_two_stars` | Open problem on $\eta$-boundedness for disjoint union of two stars |
| `2302.08182__00` | `AX_mis_planar_induced_minor_free_quasipolynomial` | Question 2 |
| `2302.08922__00` | `AX_path_induced_rooted_tree_polynomial_chi` | Polynomial bounds for path-induced copy theorem (1.2) |
| `2302.08922__01` | `AX_forest_free_polynomial_chi_gyarfas_sumner` | Polynomial bounds for the Gyárfás-Sumner conjecture |
| `2302.12633__00` | `AX_neighborhood_complexity_planar_tight_bound` | Problem 41 |
| `2302.12633__01` | `AX_neighborhood_complexity_kt_minor_free_polynomial` | Problem 42 |
| `2302.13312__00` | `AX_planar_odd_degree_linear_forests_matching` | Conjecture 2 |
| `2303.11766__00` | `AX_forest_free_multibounding_chi_bound` | Conjecture 1.6 |
| `2304.01281__00` | `AX_regular_graph_top_eigenvalues_limit_points` | Conjecture 1.3 |
| `2304.03567__00` | `AX_digraph_forward_connected_pairs_approximation_ratio` | Problem 1 |
| `2304.03567__01` | `AX_digraph_strong_balanced_bitree_linear_constant` | Problem 2 |
| `2304.03567__02` | `AX_digraph_left_maximal_dfs_tree_complexity` | Problem 3 |
| `2304.03567__03` | `AX_digraph_forward_connected_pairs_request_approximation` | Problem 4 |
| `2304.03567__04` | `AX_digraph_strong_forward_cover_log_n` | Conjecture 1 |
| `2304.04246__00` | `AX_minor_free_choosability_trivial_bound_characterization` | Problem 1 |
| `2304.04690__00` | `AX_2_extremal_digraphs_hajos_characterization` | Conjecture 9.2 |
| `2305.13422__00` | `AX_tournament_flash_rainbow_edge_coloring_exact` | Conjecture 1.7 |
| `2305.14132__00` | `AX_set_coloring_ramsey_zero_rate_equality` | Informal Conjecture (Equality in Theorem 1.1 near the zero-rate threshold) |
| `2305.15585__00` | `AX_tournament_local_chromatic_out_neighborhood_degeneracy` | Question 10 |
| `2305.15585__01` | `AX_tournament_local_chromatic_out_neighborhood_cycle` | Conjecture 11 |
| `2305.15585__02` | `AX_tournament_local_chromatic_random_tournament` | Conjecture 12 |
| `2305.15585__03` | `AX_tournament_local_chromatic_sublog_threshold_3` | Conjecture 13 |
| `2305.16258__00` | `AX_even_hole_diamond_free_tree_independence` | Conjecture 1.6 |
| `2305.16258__01` | `AX_even_hole_kt_free_logarithmic_treewidth` | Conjecture 1.7 |
| `2306.04710__00` | `AX_heroic_sets_bounded_dichromatic_finite_families` | Question 1.1 |
| `2306.04710__01` | `AX_heroes_oriented_star_delta_1_m_m` | Open problem: hero status of $\Delta(1,m,m')$ for degree-4 oriented stars |
| `2306.04710__02` | `AX_heroes_delta_1_2_2_k1_p2_free` | Open problem: hero status of $\Delta(1,2,2)$ |
| `2307.02816__00` | `AX_minor_free_underlying_treewidth_polynomial_treedepth` | Question 1 |
| `2307.02816__01` | `AX_topological_minor_free_treewidth_product_structure` | Question 2 |
| `2307.02816__02` | `AX_minor_free_p_centered_coloring_polynomial` | Question 3 |
| `2307.06455__00` | `AX_polynomial_nikiforov_all_graphs_viral` | Conjecture 1.8 |
| `2307.08361__00` | `AX_degree_bounded_classes_polynomial_bounding_function` | Polynomial degree-bounding function for hereditary degree-bounded classes |
| `2307.08361__01` | `AX_degree_bounded_classes_c4_free_polynomial` | Polynomial bound in k for C4-free subgraphs |
| `2307.15048__00` | `AX_random_graph_correspondence_chromatic_n_logn` | Conjecture 1.4 |
| `2307.15512__00` | `AX_meyniel_cop_number_k_uniform_hypergraph` | Conjecture 1.4 |
| `2308.02981__00` | `AX_separable_index_pattern_avoiding_polynomial` | Question 1.2 |
| `2308.02981__01` | `AX_separable_index_parameterized_complexity` | Question 1.3 |
| `2308.05208__00` | `AX_vantage_sign_patterns_r_dependence_gap` | Gap in $r$-dependence of sign-pattern bound |
| `2308.05208__01` | `AX_vantage_square_roots_sum_components_gap` | Gap in connected-component count for sums of square roots |
| `2308.05208__02` | `AX_vantage_protrusive_ordering_5_points` | Five-point protrusive-but-not-witnessed construction |
| `2308.07653__00` | `AX_connectivity_code_torus_product_cycles` | Open Problem: m(C_t × C_s) for all t, s |
| `2308.10833__00` | `AX_ramsey_sqrt_edges_bound_multicolor` | Informal Problem: extending the $\sqrt{m}$ Ramsey bound to more than two colors for graphs |
| `2308.15387__00` | `AX_s_color_connected_vertices_asymptotic` | Conjecture 4.2 |
| `2308.15387__01` | `AX_s_color_connected_vertices_transition` | Question 4.3 |
| `2308.15387__02` | `AX_intersecting_hypergraph_cover_number_min_edges` | Question 4.4 |
| `2308.15387__03` | `AX_intersecting_hypergraph_subset_edges_minimum` | Question 4.5 |
| `2308.15387__04` | `AX_intersecting_hypergraph_uniform_subset_edge_counts` | Question 4.6 |
| `2308.15721__00` | `AX_odd_minor_free_clustered_chromatic_treedepth` | Conjecture 2 |
| `2309.04385__00` | `AX_cube_complex_boundary_distance_rigidity` | Question 1 |
| `2309.04460__00` | `AX_rainbow_cycle_average_degree_loglog_factor` | Question 10.1 |
| `2309.04460__01` | `AX_rainbow_expander_color_separated_spanning_decomposition` | Question 10.2 |
| `2309.04460__02` | `AX_group_subset_signed_product_identity` | Question 10.3 |
| `2309.04460__03` | `AX_transpositions_product_identity_minimum` | Question 10.4 |
| `2309.07905__00` | `AX_induced_menger_bounded_degree_linear_separator` | Conjecture 1.4 |
| `2310.04265__00` | `AX_tournament_clique_number_simultaneous_ordering` | Question 3.5 |
| `2310.04265__01` | `AX_tournament_clique_number_substitution_polynomial_bounded` | Question 3.10 |
| `2310.04265__02` | `AX_tournament_clique_number_twin_width_bounded` | Conjecture 3.12 |
| `2310.04265__03` | `AX_tournament_clique_number_twin_width_ordering` | Conjecture 3.13 |
| `2310.04265__04` | `AX_tournament_clique_number_bst_ordering` | Conjecture 3.16 |
| `2310.04265__05` | `AX_tournament_clique_number_gyarfas_sumner_backedge` | Conjecture 4.3 (Gyárfás-Sumner for Tournaments) |
| `2310.04265__06` | `AX_ordered_graph_matching_free_chi_bounded` | Conjecture 4.11 |
| `2310.04265__07` | `AX_tournament_clique_number_domination_cluster` | Conjecture 5.3 (Large dom implies an ω̄-cluster) |
| `2310.04265__08` | `AX_tournament_clique_number_local_global` | Conjecture 5.6 |
| `2310.04265__09` | `AX_tournament_clique_number_bounded_witness` | Question 5.9 |
| `2310.04265__10` | `AX_tournament_clique_number_critical_infinitely_many` | Conjecture 5.10 |
| `2310.04265__11` | `AX_tournament_clique_number_substitution_digraphs` | Conjecture 6.1 |
| `2310.12891__00` | `AX_vertex_critical_edge_robust_fixed_k` | Open case of Erdős's problem for fixed small k |
| `2311.00779__00` | `AX_flip_distance_complexity_binary_trees_rotation` | Complexity of Rotation Distance Between Binary Search Trees |
| `2311.00779__01` | `AX_flip_distance_complexity_rectangulations` | Complexity of Flip Distance Between Rectangulations |
| `2311.01416__00` | `AX_non_averaging_sets_n_quarter_tight` | Informal Conjecture on h(n) |
| `2311.01887__00` | `AX_ramsey_number_arbitrary_growth_rate_approximation` | Conjecture 10 |
| `2311.05066__00` | `AX_padded_strings_unavoidable_substring_sets` | Question 8.3 |
| `2311.05500__00` | `AX_universal_graph_bounded_density_edge_count` | Conjecture 1.1 |
| `2311.05713__00` | `AX_pt_free_3_coloring_polynomial_linear_forests` | Converse to Theorem 1.1 (3-Coloring dichotomy for $H$-free graphs) |
| `2311.05713__01` | `AX_h_free_coloring_dichotomy_all_k` | Full dichotomy for $k$-Coloring on $H$-free graphs ($k\geq 3$) |
| `2311.05719__00` | `AX_clean_classes_t_clock_free` | Conjecture 1.3 |
| `2312.01028__00` | `AX_complete_topological_graph_linear_disjoint_edges` | Optimal disjoint-edges bound in complete simple topological graphs |
| `2312.06895__00` | `AX_clique_ramsey_minimizer_complete_graph` | Conjecture 1.2 |
| `2312.06895__01` | `AX_clique_ramsey_minimizer_q_colors` | q-color generalization of Conjecture 1.2 |
| `2312.13061__00` | `AX_near_eulerian_triangulation_precoloring_polynomial` | Conjecture 3 |
| `2312.13061__01` | `AX_near_eulerian_triangulation_precoloring_separated_faces` | Conjecture 4 |
| `2312.13965__00` | `AX_multicolor_ramsey_hypergraph_tower_height` | Problem 1.1 |
| `2312.13965__01` | `AX_multicolor_ramsey_3_graph_every_exponent` | Problem 4.1 |
| `2401.00299__00` | `AX_hypercube_subcube_partitions_matchings_counting` | Problem 1.1 |
| `2401.00299__01` | `AX_hypercube_subcube_partitions_ratio_growth` | Problem 1.2 |
| `2401.00299__02` | `AX_hypercube_subcube_partitions_dimension_2_asymptotics` | Problem 1.9 |
| `2401.00299__03` | `AX_hypercube_subcube_partitions_dimension_2_bound` | Informal conjecture on $f_2(d)$ |
| `2401.00299__04` | `AX_hypercube_subcube_partitions_ratio_subexponential` | Problem 1.10 |
| `2401.00359__00` | `AX_sparse_hypergraph_ramsey_double_exponential_degree` | Conjecture 6.1 |
| `2401.00359__01` | `AX_sparse_hypergraph_turan_exponent_max_degree` | Conjecture 6.2 |
| `2401.00359__02` | `AX_sparse_hypergraph_turan_latin_square_exponent` | Conjecture 6.4 |
| `2401.00359__03` | `AX_sparse_hypergraph_turan_dense_linear_subhypergraph` | Conjecture 6.5 |
| `2401.06062__00` | `AX_prime_cayley_graph_joined_union_decomposition` | Question 1.1 |
| `2401.06062__01` | `AX_prime_cayley_graph_finite_ring_characterization` | Question 4.28 |
| `2401.06062__02` | `AX_prime_cayley_graph_tensor_product_complete` | Question 4.31 |
| `2402.04237__00` | `AX_coloring_graph_polynomial_determination` | Problem 11 |
| `2402.04237__01` | `AX_coloring_graph_polynomial_random_graph_distinguishing` | Problem 12 |
| `2402.08418__00` | `AX_tournament_anti_sidorenko_orientation_every_tree` | Conjecture 1.12 |
| `2402.10782__00` | `AX_tournament_ordering_clique_approximation_algorithm` | Conjecture 4.2 |
| `2402.10782__01` | `AX_tournament_c_fas_paths_matchings_complexity` | Problem 4.4 |
| `2403.02298__00` | `AX_oriented_triangle_free_acyclic_number_sqrt` | Conjecture 3 |
| `2403.02298__01` | `AX_oriented_triangle_free_dichromatic_number_max` | Conjecture 4 |
| `2403.08303__00` | `AX_erdos_hajnal_polynomial_rodl_hereditary_families` | Conjecture 10 |
| `2404.02021__00` | `AX_off_diagonal_3_ramsey_pair_complexity` | Conjecture 4.1 |
| `2404.02021__01` | `AX_off_diagonal_3_ramsey_purely_exponential` | Conjecture 4.3 |
| `2404.02021__02` | `AX_off_diagonal_3_ramsey_superpolynomial_exponent` | Conjecture 4.6 |
| `2404.02021__03` | `AX_off_diagonal_3_ramsey_linear_subexponential` | Conjecture 4.7 |
| `2404.02021__04` | `AX_off_diagonal_3_ramsey_tripartite_nlogn` | Informal conjecture on tripartite off-diagonal Ramsey numbers |
| `2404.03472__00` | `AX_cover_free_families_optimal_size` | Problem 5.1 (cover-free families) |
| `2404.03472__01` | `AX_graph_reconstruction_mis_queries_randomized_nonadaptive` | Problem 5.2 (randomised non-adaptive optimality) |
| `2404.03472__02` | `AX_graph_reconstruction_mis_queries_adaptive_deterministic` | Problem 5.3 (adaptive vs non-adaptive gap) |
| `2405.03455__00` | `AX_erdos_szekeres_collinear_variant_ell_dependence` | Open Problem (Introduction) |
| `2405.05902__00` | `AX_sparse_host_hereditary_turan_number` | Problem 1.1 |
| `2405.05902__01` | `AX_sparse_host_hereditary_turan_even_cycles` | Conjecture 6.1 |
| `2405.10854__00` | `AX_genus_distribution_unimodal` | Conjecture 10 |
| `2405.10854__01` | `AX_genus_distribution_log_concave_triangulations` | Conjecture 11 |
| `2405.14795__00` | `AX_rainbow_stacking_random_colorings_sharp_threshold` | Problem 3.1 |
| `2405.14795__01` | `AX_rainbow_stacking_odd_complete_proper_colorings` | Question 3.3 |
| `2405.15353__00` | `AX_tea_sharing_optimal_sequence_exponential_length` | Question 6.1 |
| `2407.08927__00` | `AX_even_hole_free_independent_set_polynomial` | Open Problem: Polynomial-time MWIS on even-hole-free graphs |
| `2407.08927__01` | `AX_even_hole_free_coloring_polynomial` | Open Problem: Polynomial-time Coloring on even-hole-free graphs |
| `2407.18800__00` | `AX_toroidal_5_choosability_critical_6_critical` | Conjecture 2 |
| `2407.18800__01` | `AX_toroidal_5_choosability_equals_5_colorable` | Conjecture 3 |
| `2407.18800__02` | `AX_toroidal_5_choosability_edge_width_4` | Conjecture 4 |
| `2407.18800__03` | `AX_toroidal_5_choosability_prism_canvas_spacing` | Conjecture 8 |
| `2407.21360__00` | `AX_clustered_coloring_strong_product_path_tight` | Conjecture 7 |
| `2407.21360__01` | `AX_clustered_coloring_strong_product_exponent_tight` | Conjecture 8 |
| `2408.02400__00` | `AX_chromatic_cochromatic_gap_three_small_clique` | Problem 1.5 |
| `2409.05039__00` | `AX_split_digraph_strong_2_kernel_half` | Open question on strong 2-kernels in split digraphs |
| `2409.18220__00` | `AX_positive_square_energy_lower_bound_4n_5` | Informal Conjecture (improved linear bound) |
| `2410.13008__00` | `AX_annulus_digraph_winding_one_crossing_free` | Conjecture 1.2 |
| `2410.13008__01` | `AX_weightable_digraphs_np_characterization` | Informal Question (NP-characterization of weightable digraphs) |
| `2410.16495__00` | `AX_large_treewidth_unavoidable_induced_subgraphs` | Question 1.1 |
| `2410.20498__00` | `AX_hypercube_statistic_lambda_d_1_limit` | Conjecture on $\lambda(d,1)$ |
| `2410.20498__01` | `AX_hypercube_statistic_lambda_tight_bounds` | Open problem on tight bounds for $\lambda(d,s)$ |
| `2410.23566__00` | `AX_unavoidability_bounded_average_degree_polynomial` | Problem 6 |
| `2410.23566__01` | `AX_unavoidability_linear_blowup_closure` | Conjecture 7 |
| `2410.23566__02` | `AX_unavoidability_tree_blowup_optimal_constant` | Problem 8 |
| `2410.23566__03` | `AX_unavoidability_vertex_deletion_ratio_bounded` | Conjecture 9 |
| `2410.23566__04` | `AX_unavoidability_tree_extensions_exponential` | Conjecture 10 |
| `2410.23566__05` | `AX_unavoidability_linear_extension_closure` | Conjecture 11 |
| `2410.23566__06` | `AX_unavoidability_forest_extensions_rate` | Problem 12 |
| `2411.13812__00` | `AX_hypergraph_ramsey_polynomial_iterated_blowup` | Conjecture 1.1 |
| `2411.13812__01` | `AX_hypergraph_ramsey_tower_tightly_connected` | Conjecture 4.2 |
| `2412.21194__00` | `AX_f2n_two_coloring_no_monochromatic_subspace` | Conjecture 5.1 |
| `2501.00567__00` | `AX_triangle_free_chromatic_spectral_radius_log` | Conjecture 1.7 |
| `2501.09839__00` | `AX_coarse_treewidth_additive_quasi_isometry` | Open question on Theorem 1.2 with $L=1$ |
| `2502.04177__00` | `AX_strong_coloring_number_bramble_polynomial_expansion` | Question 2 |
| `2502.04726__00` | `AX_cyclic_clique_minor_min_degree_bound` | Question 1.2 |
| `2502.04726__01` | `AX_lollipop_active_path_complete_graph_criterion` | Question 4.1 |
| `2502.04726__02` | `AX_lollipop_active_vertices_optimal_cycle` | Question 4.2 |
| `2502.04726__03` | `AX_min_degree_3_cycle_linear_chords` | Question 4.3 |
| `2502.05289__00` | `AX_induced_subdivision_containment_subcubic_planar_dichotomy` | Conjecture 1.5 |
| `2502.05289__01` | `AX_induced_disjoint_paths_variants_complexity_gap` | Informal Question on Complexity Gap Between Induced Disjoint Paths Variants |
| `2502.14398__00` | `AX_cyclic_permutation_swap_diameter_prime` | Conjecture 3.4 |
| `2502.14398__01` | `AX_cyclic_permutation_swap_diameter_extremal` | Conjecture 3.6 |
| `2502.14398__02` | `AX_cyclic_permutation_swap_diameter_monotone` | Question 3.9 |
| `2503.05562__00` | `AX_domination_packing_ratio_bounded_given_class` | Question 1.1 |
| `2503.05562__01` | `AX_domination_packing_ratio_bounded_characterization` | Question 9.1 |
| `2503.16882__00` | `AX_negative_p_energy_path_minimum` | Conjecture 2 |
| `2503.20045__00` | `AX_chromatic_threshold_odd_cycles_undirected` | Question 1.1 |
| `2503.20045__01` | `AX_chromatic_threshold_digraph_cycle_orientations` | Question 1.2 |
| `2503.20045__02` | `AX_chromatic_threshold_digraph_fixed_subdigraph` | Question 4.1 |
| `2503.20045__03` | `AX_chromatic_threshold_digraph_minimum_epsilon` | Question 4.2 |
| `2503.23191__00` | `AX_oriented_graph_semidegree_non_antidirected_paths` | Question 5.1 |
| `2504.00153__00` | `AX_intersectionwise_chi_guarding_classes` | Question 1 (Intersectionwise χ-guarding) |
| `2504.01548__00` | `AX_defective_coloring_blowup_chromatic_ratio` | Problem 1.4 |
| `2504.07764__00` | `AX_rooted_kk_minor_free_unrealizable_colorings` | Conjecture 4 |
| `2504.08266__00` | `AX_merge_width_radius_1_chi_bounded` | Question 1.4 |
| `2504.08266__01` | `AX_merge_width_transduction_neighborhood_complexity` | Conjecture 1.7 |
| `2504.08327__00` | `AX_one_crossing_5_critical_degree_four` | Conjecture 1 |
| `2504.08327__01` | `AX_one_crossing_4_colorable_degree_5` | Conjecture 2 |
| `2504.08327__02` | `AX_one_crossing_4_connected_degree_four` | Conjecture 5 |
| `2504.08327__03` | `AX_one_crossing_bichromatic_forbidding_diamond_generation` | Conjecture 30 |
| `2505.05339__00` | `AX_regular_independence_edge_deletion_cubic_infinite` | Question 4.1 |
| `2505.05339__01` | `AX_regular_independence_edge_deletion_degree_4` | Question 4.2 |
| `2505.05339__02` | `AX_r_partite_hypergraph_matching_drop_deletion` | Conjecture 4.3 |
| `2505.05339__03` | `AX_cayley_line_hypergraph_matching_drop` | Question 4.4 |
| `2505.05997__00` | `AX_largest_clique_minor_opt_approximation` | Open Problem: polytime $f(\mathrm{OPT})$-approximation for largest complete minor |
| `2505.24100__00` | `AX_induced_even_cycle_saturation_edge_addition` | Question 1.7 |
| `2505.24100__01` | `AX_induced_even_cycle_saturation_polynomial_size` | Question 1.8 |
| `2506.07264__00` | `AX_positive_square_energy_at_least_n` | Conjecture 1.2 |
| `2506.07264__01` | `AX_positive_square_energy_unicyclic_odd_cycle` | Conjecture 9.1 |
| `2506.07264__02` | `AX_positive_square_energy_equality_trees` | Conjecture 9.2 |
| `2506.07264__03` | `AX_positive_square_energy_equals_n_unicyclic` | Conjecture 9.3 |
| `2506.07264__04` | `AX_positive_square_energy_clique_number_3` | Conjecture 9.4 |
| `2506.07264__05` | `AX_positive_square_energy_maximal_planar_3n` | Conjecture 9.5 |
| `2506.08810__00` | `AX_induced_saturated_no_finite_infinite_family` | Problem 21 |
| `2506.08810__01` | `AX_induced_saturated_flip_graph_disconnected` | Problem 22 |
| `2506.08810__02` | `AX_induced_saturated_countable_tournament_arc_reversal` | Problem 23 |
| `2506.08810__03` | `AX_induced_saturated_infinite_tournament_perturbation` | Conjecture 24 |
| `2506.08810__04` | `AX_induced_saturated_infinite_hypergraph` | Conjecture 25 |
| `2506.08810__05` | `AX_induced_saturated_infinite_edge_colored_clique` | Conjecture 26 |
| `2506.10227__00` | `AX_sun_free_graphs_chi_bounded` | Informal conjecture on sun-free $\chi$-boundedness without net exclusion |
| `2506.17777__00` | `AX_tverberg_number_s_convex_sets` | Problem 1.4 |
| `2507.04254__00` | `AX_modular_chromatic_index_0k_graphs` | Conjecture 13 |
| `2507.10840__00` | `AX_geometric_graph_monotone_path_cover_superlinear` | Conjecture 1.4 |
| `2507.10840__01` | `AX_geometric_graph_plane_path_cover_bound` | Problem 5.1 |
| `2507.10840__02` | `AX_geometric_graph_zigzag_path_cover_number` | Problem 5.2 |
| `2507.12748__00` | `AX_partition_polytope_diameter_4_thirds` | Conjecture 1.3 |
| `2508.08703__00` | `AX_regular_4_critical_no_critical_edge` | Problem 5.2 |
| `2508.08870__00` | `AX_generic_norm_distinct_distances_lower_bound` | Conjecture 1.5 |
| `2508.14332__00` | `AX_coarse_menger_distance_2_paths` | Open case: Coarse Menger Conjecture for c=2 |
| `2509.02561__00` | `AX_small_doubling_sumset_covering_family` | Conjecture 15 |
| `2509.07174__00` | `AX_coarse_menger_bounded_genus_surfaces` | Conjecture 1.2 (Coarse Menger conjecture for surfaces) |
| `2509.08762__00` | `AX_coarse_menger_bounded_genus` | Informal conjecture: coarse Menger for bounded genus |
| `2509.09031__00` | `AX_quasi_isometry_multiplicative_to_additive_classes` | Conjecture 1.2 |
| `2509.09035__00` | `AX_fat_minor_quasi_isometry_trees_planar` | Informal question: validity of Conjecture 1.2 for trees and planar graphs |
| `2510.01791__00` | `AX_sparse_graph_cut_small_chromatic_number` | Conjecture 1.3 |
| `2510.01916__00` | `AX_circuit_distance_polygons_np_hard` | Conjecture 21 |
| `2510.11311__00` | `AX_odd_cycle_orientations_avoidable` | Conjecture 6.1 |
| `2510.11311__01` | `AX_height_function_digraphs_not_avoidable` | Question 6.2 |
| `2510.11311__02` | `AX_c4_orientations_avoidable` | Question 6.3 |
| `2510.11311__03` | `AX_eulerian_avoidable_digraphs_characterization` | Eulerian-avoidability characterization |
| `2510.11311__04` | `AX_c4_orientations_eulerian_avoidable` | Question 6.4 |
| `2511.02892__00` | `AX_ordered_complete_graph_monochromatic_nonnested_matching` | Problem 1.1 |
| `2511.02892__01` | `AX_random_4_regular_graph_polynomial_coefficient` | Problem 2.1 |
| `2511.02892__02` | `AX_cycles_union_k4_copies_4_colorable` | Problem 3.1 |
| `2511.02892__03` | `AX_cubic_truncation_strong_6_edge_coloring` | Problem 4.1 |
| `2511.02892__04` | `AX_cubic_2_homogeneous_coloring_4_colors` | Problem 5.1 |
| `2511.02892__05` | `AX_cubic_2_homogeneous_coloring_finite_exceptions` | Problem 5.2 |
| `2511.02892__06` | `AX_bridgeless_2_flow_4_flow_pair` | Conjecture 6.1 |
| `2511.02892__07` | `AX_bicritical_snarks_almost_group_connected` | Problem 7.1 |
| `2511.03864__00` | `AX_tree_independence_polynomial_biclique_free` | Question 5.2 |
| `2511.03864__01` | `AX_tree_independence_polynomial_induced_biclique_number` | Question 5.3 |
| `2511.07601__00` | `AX_schnyder_wood_uihpt_weak_limit` | Conjecture 1.5 |
| `2511.07601__01` | `AX_schnyder_wood_half_plane_triangulations_existence` | Open question on Schnyder woods for general half-plane triangulations |
| `2511.07601__02` | `AX_schnyder_wood_random_wooded_triangulations_limit` | Open question on local limit of uniformly random wooded triangulations |
| `2512.08049__00` | `AX_spectrally_symmetric_graph_edge_density` | Problem 1 |
| `2512.10438__00` | `AX_tournament_color_avoiding_path_non_transitive` | Problem 5.1 |
| `2512.17232__00` | `AX_anticomplete_xy_paths_erdos_posa_optimal` | Conjecture 6 |
| `2512.17342__00` | `AX_flow_reconfiguration_5_flow_connected` | Problem 1.1 |
| `2512.17342__01` | `AX_flow_reconfiguration_group_implies_integer` | Problem 2.6 |
| `2601.12746__00` | `AX_circular_drawing_digraph_forbidden_characterization` | Open Question on Circular Drawing Characterisation |
| `2601.13072__00` | `AX_3_coloring_diameter_2_quasipolynomial` | Problem 1 |
| `2601.15082__00` | `AX_domination_packing_ratio_bounded_2_independence` | Problem 1 |
| `2601.15082__01` | `AX_domination_2_independence_tied_classes` | Problem 2 |
| `2601.15245__00` | `AX_degenerate_kr_free_fractional_chromatic_max` | Problem 4.1 |
| `2601.15245__01` | `AX_degenerate_triangle_free_subexponential_order_coloring` | Problem 6.1 |
| `2601.15245__02` | `AX_degenerate_triangle_free_max_degree_coloring` | Problem 6.2 |
| `2601.15245__03` | `AX_degenerate_kr_free_extremal_order_exponential` | Problem 6.3 |
| `2601.15245__04` | `AX_degenerate_kr_free_fractional_chromatic_sublinear` | Problem 6.4 |
| `2602.07435__00` | `AX_cop_number_sublinear_treedepth` | Problem 9 |
| `2602.16333__00` | `AX_vertex_transitive_digraph_linear_perimeter_gap` | Conjecture 4.1 |
| `2602.16333__01` | `AX_vertex_transitive_digraph_circumference_vs_undirected` | Conjecture 4.2 |
| `2602.16333__02` | `AX_vertex_transitive_digraph_longest_cycles_intersect` | Question 4.3 |
| `2602.16333__03` | `AX_vertex_transitive_digraph_path_vs_cycle` | Question 4.4 |
| `2603.02786__00` | `AX_arithmetic_progression_packing_constant_4_3` | Conjecture 1 |
| `2603.02786__01` | `AX_arithmetic_progression_packing_primes_asymptotic` | Conjecture 4 |
| `2603.02786__02` | `AX_arithmetic_progression_packing_near_sqrt_n` | Conjecture 5 |
| `2603.02786__03` | `AX_arithmetic_progression_packing_two_regimes` | Conjecture 6 |
| `2603.02786__04` | `AX_arithmetic_progression_packing_fixed_n` | Conjecture 7 |
| `2603.14427__00` | `AX_borodin_kostochka_list_dp_equality_threshold` | Question 5 |
| `2603.17630__00` | `AX_spanning_tree_anticoncentration_min_degree` | Conjecture 4.1 |
| `2603.17630__01` | `AX_spanning_tree_nonisomorphic_count_min_degree` | Conjecture 4.2 |
| `2603.28614__00` | `AX_spanning_trees_pivot_gray_code` | Problem 1 |
| `2604.09449__00` | `AX_color_balanced_bipartite_matching_sqrt_k` | Conjecture 6.1 |
| `2604.09449__01` | `AX_color_balanced_complete_matching_constant_bound` | Conjecture 6.2 |
| `2604.09449__02` | `AX_color_balanced_spanning_forest_bounds` | Problem 6.3 |
| `2604.09449__03` | `AX_color_balanced_hamilton_cycle_bounds` | Problem 6.4 |
| `2604.13700__00` | `AX_regular_digraph_directed_treewidth_ratio_limit` | Problem 2 |
| `2604.13700__01` | `AX_regular_digraph_directed_treewidth_best_constant` | Informal Question on optimal directed tree-width constant for regular digraphs |
| `2605.13628__00` | `AX_restricted_difference_3_ap_free_density` | Problem 8 |
| `2605.13628__01` | `AX_restricted_difference_triangle_removal_lemma` | Problem 9 |

## Bondy–Murty Appendix A (BM)

| old id | new name | title |
|---|---|---|
| `bm-003` | `BM_reconstruction_infinite_hypomorphic_mutual_subgraph` | Halin's conjecture on hypomorphic infinite graphs |
| `bm-011` | `BM_edge_connected_graphs_tree_decomposition` | Barát–Thomassen conjecture |
| `bm-013` | `BM_bridgeless_cycle_double_cover_small` | Bondy's small cycle double cover conjecture |
| `bm-014` | `BM_bridgeless_cycle_double_cover_5_cycles` | Five cycle double cover conjecture |
| `bm-016` | `BM_linear_arboricity_regular_graphs` | Linear arboricity conjecture |
| `bm-021` | `BM_cubic_second_hamilton_cycle_polynomial` | Finding a second Hamilton cycle in a cubic graph |
| `bm-022` | `BM_k_disjoint_odd_paths_conp` | Internally disjoint odd paths: is it in co-NP? |
| `bm-025` | `BM_spanning_k_connected_bipartite_subgraph` | Thomassen's spanning k-connected bipartite subgraph conjecture |
| `bm-026` | `BM_bridgeless_cycle_double_cover_orientable_5` | Orientable five cycle double cover conjecture |
| `bm-029` | `BM_5_connected_nonplanar_k5_subdivision` | Kelmans–Seymour conjecture |
| `bm-031` | `BM_thrackle_edges_at_most_vertices` | Conway's thrackle conjecture |
| `bm-032` | `BM_planar_integer_length_straight_line_drawing` | Harborth's conjecture (integral straight-line drawings) |
| `bm-033` | `BM_erdos_sos_trees_edge_bound` | Erdős–Sós conjecture |
| `bm-034` | `BM_even_cycle_turan_number_lower_bound` | Even-cycle Turán number |
| `bm-037` | `BM_diagonal_ramsey_constructive_exponential_lower_bound` | Constructive exponential lower bound for diagonal Ramsey numbers |
| `bm-038` | `BM_diagonal_ramsey_kth_root_limit` | Limit of $r(k,k)^{1/k}$ |
| `bm-039` | `BM_tree_ramsey_number_2n_minus_2` | Burr–Erdős tree Ramsey conjecture |
| `bm-041` | `BM_hadwiger_minor_chromatic` | Hadwiger's conjecture |
| `bm-042` | `BM_hajos_k5_k6_subdivision_chromatic` | Hajós conjecture for $k = 5$ and $k = 6$ |
| `bm-045` | `BM_erdos_lovasz_tihany_disjoint_chromatic_split` | Erdős–Lovász Tihany conjecture |
| `bm-046` | `BM_el_zahar_erdos_induced_disjoint_union` | El-Zahar–Erdős conjecture |
| `bm-050` | `BM_triangle_free_infinite_chromatic_induced_trees` | Gyárfás's tree conjecture for triangle-free graphs |
| `bm-053` | `BM_toroidal_delete_3_vertices_4_colorable` | Albertson's toroidal colouring conjecture |
| `bm-054` | `BM_plane_unit_distance_chromatic_number` | Chromatic number of the plane (Hadwiger–Nelson problem) |
| `bm-057` | `BM_1_factorization_dense_regular_graphs` | 1-factorization conjecture |
| `bm-060` | `BM_edge_coloring_kempe_changes_reach_optimal` | Vizing's interchange conjecture |
| `bm-062` | `BM_kotzig_unique_k_path_nonexistence` | Kotzig's unique $k$-path conjecture |
| `bm-064` | `BM_longest_cycles_k_connected_intersection` | Smith's conjecture on longest cycles |
| `bm-065` | `BM_cubic_cyclically_4_connected_long_cycle` | Bondy's linear-length cycle conjecture for cyclically 4-edge-connected cubic graphs |
| `bm-066` | `BM_long_cycles_pairwise_intersecting_hitting_set` | Birmelé's conjecture on long cycles |
| `bm-070` | `BM_caccetta_haggkvist_weighted_cycle` | Weighted Caccetta–Häggkvist conjecture |
| `bm-079` | `BM_4_connected_hamiltonian_claw_free` | Matthews–Sumner conjecture |
| `bm-080` | `BM_barnette_simple_4_polytopes_hamiltonian` | Barnette's conjecture on 4-regular 4-polytopes |
| `bm-085` | `BM_planar_cubic_three_hamilton_cycles_triangle` | Cantoni's conjecture |
| `bm-088` | `BM_vertex_transitive_finitely_many_non_hamiltonian` | Thomassen's conjecture on Hamiltonian vertex-transitive graphs |
| `bm-089` | `BM_k_tough_graphs_hamiltonian` | Chvátal's toughness conjecture |
| `bm-090` | `BM_hypohamiltonian_min_degree_4` | Hypohamiltonian graphs of minimum degree at least 4 |
| `bm-091` | `BM_bipartite_hypotraceable_nonexistence` | Grötschel's conjecture on bipartite hypotraceable graphs |

## Others (OTH)

| old id | new name | title |
|---|---|---|
| `meyniels-conjecture` | `OTH_meyniel_cop_number_sqrt_n` | Meyniel's conjecture on the cop number |
