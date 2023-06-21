import typing_extensions

from starkexpress_api.apis.tags import TagValues
from starkexpress_api.apis.tags.user_api import UserApi
from starkexpress_api.apis.tags.asset_api import AssetApi
from starkexpress_api.apis.tags.mint_api import MintApi
from starkexpress_api.apis.tags.transfer_api import TransferApi
from starkexpress_api.apis.tags.transaction_api import TransactionApi
from starkexpress_api.apis.tags.withdraw_api import WithdrawApi
from starkexpress_api.apis.tags.vault_api import VaultApi
from starkexpress_api.apis.tags.fee_api import FeeApi
from starkexpress_api.apis.tags.orderbook_api import OrderbookApi
from starkexpress_api.apis.tags.order_api import OrderApi
from starkexpress_api.apis.tags.settlement_api import SettlementApi
from starkexpress_api.apis.tags.deposit_api import DepositApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USER: UserApi,
        TagValues.ASSET: AssetApi,
        TagValues.MINT: MintApi,
        TagValues.TRANSFER: TransferApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.WITHDRAW: WithdrawApi,
        TagValues.VAULT: VaultApi,
        TagValues.FEE: FeeApi,
        TagValues.ORDERBOOK: OrderbookApi,
        TagValues.ORDER: OrderApi,
        TagValues.SETTLEMENT: SettlementApi,
        TagValues.DEPOSIT: DepositApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USER: UserApi,
        TagValues.ASSET: AssetApi,
        TagValues.MINT: MintApi,
        TagValues.TRANSFER: TransferApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.WITHDRAW: WithdrawApi,
        TagValues.VAULT: VaultApi,
        TagValues.FEE: FeeApi,
        TagValues.ORDERBOOK: OrderbookApi,
        TagValues.ORDER: OrderApi,
        TagValues.SETTLEMENT: SettlementApi,
        TagValues.DEPOSIT: DepositApi,
    }
)
