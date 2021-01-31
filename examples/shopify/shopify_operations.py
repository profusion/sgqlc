import sgqlc.types
import sgqlc.operation
import shopify_schema

_schema = shopify_schema
_schema_root = _schema.shopify_schema

__all__ = ('Operations',)


def fragment_select_products():
    _frag = sgqlc.operation.Fragment(_schema.ProductConnection, 'SelectProducts')
    _frag_page_info = _frag.page_info()
    _frag_page_info.has_next_page()
    _frag_edges = _frag.edges()
    _frag_edges.cursor()
    _frag_edges_node = _frag_edges.node()
    _frag_edges_node.id()
    _frag_edges_node.handle()
    _frag_edges_node.description()
    _frag_edges_node.title()
    _frag_edges_node.total_inventory()
    _frag_edges_node_price_range_v2 = _frag_edges_node.price_range_v2()
    _frag_edges_node_price_range_v2_min_variant_price = _frag_edges_node_price_range_v2.min_variant_price()
    _frag_edges_node_price_range_v2_min_variant_price.__fragment__(fragment_money())
    _frag_edges_node_price_range_v2_max_variant_price = _frag_edges_node_price_range_v2.max_variant_price()
    _frag_edges_node_price_range_v2_max_variant_price.__fragment__(fragment_money())
    return _frag


def fragment_money():
    _frag = sgqlc.operation.Fragment(_schema.MoneyV2, 'Money')
    _frag.amount()
    _frag.currency_code()
    return _frag


class Fragment:
    money = fragment_money()
    select_products = fragment_select_products()


def query_initial_query():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='InitialQuery', variables=dict(first=sgqlc.types.Arg(sgqlc.types.non_null(shopify_schema.shopify_schema.Int)), after=sgqlc.types.Arg(shopify_schema.shopify_schema.String, default=None)))
    _op_shop = _op.shop()
    _op_shop.name()
    _op_shop.description()
    _op_shop.url()
    _op_products = _op.products(first=sgqlc.types.Variable('first'), after=sgqlc.types.Variable('after'))
    _op_products.__fragment__(fragment_select_products())
    return _op


def query_load_products():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='LoadProducts', variables=dict(first=sgqlc.types.Arg(sgqlc.types.non_null(shopify_schema.shopify_schema.Int)), after=sgqlc.types.Arg(sgqlc.types.non_null(shopify_schema.shopify_schema.String))))
    _op_products = _op.products(first=sgqlc.types.Variable('first'), after=sgqlc.types.Variable('after'))
    _op_products.__fragment__(fragment_select_products())
    return _op


class Query:
    initial_query = query_initial_query()
    load_products = query_load_products()


class Operations:
    fragment = Fragment
    query = Query
