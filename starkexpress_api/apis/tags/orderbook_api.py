# coding: utf-8

"""
    StarkExpress API Docs

    An API for the StarkExpress platform.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from starkexpress_api.paths.api_v1_orderbooks.post import CreateOrderbook
from starkexpress_api.paths.api_v1_orderbooks_orderbook_id.get import GetOrderbook
from starkexpress_api.paths.api_v1_orderbooks_orderbook_id_l1.get import GetOrderbookLevel1Data
from starkexpress_api.paths.api_v1_orderbooks_orderbook_id_l2.get import GetOrderbookLevel2Data


class OrderbookApi(
    CreateOrderbook,
    GetOrderbook,
    GetOrderbookLevel1Data,
    GetOrderbookLevel2Data,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
