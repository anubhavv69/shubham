from ..testing.exclusions import compound

class Requirements: ...

class SuiteRequirements(Requirements):
    @property
    def create_table(self): ...
    @property
    def drop_table(self): ...
    @property
    def table_ddl_if_exists(self): ...
    @property
    def index_ddl_if_exists(self): ...
    @property
    def foreign_keys(self): ...
    @property
    def table_value_constructor(self): ...
    @property
    def standard_cursor_sql(self): ...
    @property
    def on_update_cascade(self): ...
    @property
    def non_updating_cascade(self): ...
    @property
    def deferrable_fks(self): ...
    @property
    def on_update_or_deferrable_fks(self): ...
    @property
    def queue_pool(self): ...
    @property
    def self_referential_foreign_keys(self): ...
    @property
    def foreign_key_ddl(self): ...
    @property
    def named_constraints(self): ...
    @property
    def implicitly_named_constraints(self): ...
    @property
    def unusual_column_name_characters(self) -> compound: ...
    @property
    def subqueries(self): ...
    @property
    def offset(self): ...
    @property
    def bound_limit_offset(self): ...
    @property
    def sql_expression_limit_offset(self): ...
    @property
    def parens_in_union_contained_select_w_limit_offset(self): ...
    @property
    def parens_in_union_contained_select_wo_limit_offset(self): ...
    @property
    def boolean_col_expressions(self): ...
    @property
    def nullable_booleans(self): ...
    @property
    def nullsordering(self): ...
    @property
    def standalone_binds(self): ...
    @property
    def standalone_null_binds_whereclause(self): ...
    @property
    def intersect(self): ...
    @property
    def except_(self): ...
    @property
    def window_functions(self): ...
    @property
    def ctes(self): ...
    @property
    def ctes_with_update_delete(self): ...
    @property
    def ctes_on_dml(self): ...
    @property
    def autoincrement_insert(self): ...
    @property
    def fetch_rows_post_commit(self): ...
    @property
    def group_by_complex_expression(self): ...
    @property
    def sane_rowcount(self): ...
    @property
    def sane_multi_rowcount(self): ...
    @property
    def sane_rowcount_w_returning(self): ...
    @property
    def empty_inserts(self): ...
    @property
    def empty_inserts_executemany(self): ...
    @property
    def insert_from_select(self): ...
    @property
    def full_returning(self): ...
    @property
    def insert_executemany_returning(self): ...
    @property
    def returning(self): ...
    @property
    def tuple_in(self): ...
    @property
    def tuple_in_w_empty(self): ...
    @property
    def duplicate_names_in_cursor_description(self): ...
    @property
    def denormalized_names(self): ...
    @property
    def multivalues_inserts(self): ...
    @property
    def implements_get_lastrowid(self): ...
    @property
    def emulated_lastrowid(self): ...
    @property
    def emulated_lastrowid_even_with_sequences(self): ...
    @property
    def dbapi_lastrowid(self): ...
    @property
    def views(self): ...
    @property
    def schemas(self): ...
    @property
    def cross_schema_fk_reflection(self): ...
    @property
    def foreign_key_constraint_name_reflection(self): ...
    @property
    def implicit_default_schema(self): ...
    @property
    def default_schema_name_switch(self): ...
    @property
    def server_side_cursors(self): ...
    @property
    def sequences(self): ...
    @property
    def no_sequences(self): ...
    @property
    def sequences_optional(self): ...
    @property
    def supports_lastrowid(self): ...
    @property
    def no_lastrowid_support(self): ...
    @property
    def reflects_pk_names(self): ...
    @property
    def table_reflection(self): ...
    @property
    def reflect_tables_no_columns(self): ...
    @property
    def comment_reflection(self): ...
    @property
    def view_column_reflection(self): ...
    @property
    def view_reflection(self): ...
    @property
    def schema_reflection(self): ...
    @property
    def primary_key_constraint_reflection(self): ...
    @property
    def foreign_key_constraint_reflection(self): ...
    @property
    def foreign_key_constraint_option_reflection_ondelete(self): ...
    @property
    def fk_constraint_option_reflection_ondelete_restrict(self): ...
    @property
    def fk_constraint_option_reflection_ondelete_noaction(self): ...
    @property
    def foreign_key_constraint_option_reflection_onupdate(self): ...
    @property
    def fk_constraint_option_reflection_onupdate_restrict(self): ...
    @property
    def temp_table_reflection(self): ...
    @property
    def temp_table_reflect_indexes(self): ...
    @property
    def temp_table_names(self): ...
    @property
    def has_temp_table(self) -> compound: ...
    @property
    def temporary_tables(self): ...
    @property
    def temporary_views(self): ...
    @property
    def index_reflection(self): ...
    @property
    def index_reflects_included_columns(self): ...
    @property
    def indexes_with_ascdesc(self): ...
    @property
    def indexes_with_expressions(self): ...
    @property
    def unique_constraint_reflection(self): ...
    @property
    def check_constraint_reflection(self): ...
    @property
    def duplicate_key_raises_integrity_error(self): ...
    @property
    def unbounded_varchar(self): ...
    @property
    def unicode_data(self): ...
    @property
    def unicode_ddl(self): ...
    @property
    def symbol_names_w_double_quote(self): ...
    @property
    def datetime_literals(self): ...
    @property
    def datetime(self): ...
    @property
    def datetime_timezone(self) -> compound: ...
    @property
    def time_timezone(self) -> compound: ...
    @property
    def datetime_implicit_bound(self) -> compound: ...
    @property
    def datetime_microseconds(self): ...
    @property
    def timestamp_microseconds(self): ...
    @property
    def timestamp_microseconds_implicit_bound(self) -> compound: ...
    @property
    def datetime_historic(self): ...
    @property
    def date(self): ...
    @property
    def date_coerces_from_datetime(self): ...
    @property
    def date_historic(self): ...
    @property
    def time(self): ...
    @property
    def time_microseconds(self): ...
    @property
    def binary_comparisons(self): ...
    @property
    def binary_literals(self): ...
    @property
    def autocommit(self): ...
    @property
    def isolation_level(self): ...
    def get_isolation_levels(self, config) -> None: ...
    @property
    def json_type(self): ...
    @property
    def json_array_indexes(self): ...
    @property
    def json_index_supplementary_unicode_element(self): ...
    @property
    def legacy_unconditional_json_extract(self): ...
    @property
    def precision_numerics_general(self): ...
    @property
    def precision_numerics_enotation_small(self): ...
    @property
    def precision_numerics_enotation_large(self): ...
    @property
    def precision_numerics_many_significant_digits(self): ...
    @property
    def cast_precision_numerics_many_significant_digits(self): ...
    @property
    def implicit_decimal_binds(self): ...
    @property
    def nested_aggregates(self): ...
    @property
    def recursive_fk_cascade(self): ...
    @property
    def precision_numerics_retains_significant_digits(self): ...
    @property
    def infinity_floats(self): ...
    @property
    def precision_generic_float_type(self): ...
    @property
    def floats_to_four_decimals(self): ...
    @property
    def fetch_null_from_numeric(self): ...
    @property
    def text_type(self): ...
    @property
    def empty_strings_varchar(self): ...
    @property
    def empty_strings_text(self): ...
    @property
    def expressions_against_unbounded_text(self): ...
    @property
    def selectone(self): ...
    @property
    def savepoints(self): ...
    @property
    def two_phase_transactions(self): ...
    @property
    def update_from(self): ...
    @property
    def delete_from(self): ...
    @property
    def update_where_target_in_subquery(self): ...
    @property
    def mod_operator_as_percent_sign(self): ...
    @property
    def percent_schema_names(self): ...
    @property
    def order_by_col_from_union(self): ...
    @property
    def order_by_label_with_expression(self): ...
    @property
    def order_by_collation(self): ...
    def get_order_by_collation(self, config) -> None: ...
    @property
    def unicode_connections(self): ...
    @property
    def graceful_disconnects(self): ...
    @property
    def independent_connections(self): ...
    @property
    def skip_mysql_on_windows(self): ...
    @property
    def ad_hoc_engines(self): ...
    @property
    def no_windows(self): ...
    @property
    def timing_intensive(self): ...
    @property
    def memory_intensive(self): ...
    @property
    def threading_with_mock(self): ...
    @property
    def sqlalchemy2_stubs(self): ...
    @property
    def python2(self): ...
    @property
    def python3(self): ...
    @property
    def pep520(self): ...
    @property
    def insert_order_dicts(self): ...
    @property
    def python36(self): ...
    @property
    def python37(self): ...
    @property
    def dataclasses(self): ...
    @property
    def python38(self): ...
    @property
    def cpython(self): ...
    @property
    def is64bit(self) -> compound: ...
    @property
    def patch_library(self): ...
    @property
    def non_broken_pickle(self): ...
    @property
    def predictable_gc(self): ...
    @property
    def no_coverage(self): ...
    @property
    def sqlite(self): ...
    @property
    def cextensions(self): ...
    @property
    def async_dialect(self): ...
    @property
    def asyncio(self) -> compound: ...
    @property
    def greenlet(self): ...
    @property
    def computed_columns(self): ...
    @property
    def computed_columns_stored(self): ...
    @property
    def computed_columns_virtual(self): ...
    @property
    def computed_columns_default_persisted(self): ...
    @property
    def computed_columns_reflect_persisted(self): ...
    @property
    def supports_distinct_on(self): ...
    @property
    def supports_is_distinct_from(self): ...
    @property
    def identity_columns(self): ...
    @property
    def identity_columns_standard(self): ...
    @property
    def regexp_match(self): ...
    @property
    def regexp_replace(self): ...
    @property
    def fetch_first(self): ...
    @property
    def fetch_percent(self): ...
    @property
    def fetch_ties(self): ...
    @property
    def fetch_no_order_by(self): ...
    @property
    def fetch_offset_with_options(self): ...
    @property
    def fetch_expression(self): ...
    @property
    def autoincrement_without_sequence(self): ...
    @property
    def generic_classes(self): ...