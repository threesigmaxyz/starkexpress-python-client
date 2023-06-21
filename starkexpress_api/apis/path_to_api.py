import typing_extensions

from starkexpress_api.paths import PathValues
from starkexpress_api.apis.paths.api_v1_fees import ApiV1Fees
from starkexpress_api.apis.paths.api_v1_fees_fee_id import ApiV1FeesFeeId
from starkexpress_api.apis.paths.api_v1_mint import ApiV1Mint
from starkexpress_api.apis.paths.api_v1_orders_details import ApiV1OrdersDetails
from starkexpress_api.apis.paths.api_v1_orders import ApiV1Orders
from starkexpress_api.apis.paths.api_v1_orders_order_id import ApiV1OrdersOrderId
from starkexpress_api.apis.paths.api_v1_orderbooks import ApiV1Orderbooks
from starkexpress_api.apis.paths.api_v1_orderbooks_orderbook_id import ApiV1OrderbooksOrderbookId
from starkexpress_api.apis.paths.api_v1_orderbooks_orderbook_id_l1 import ApiV1OrderbooksOrderbookIdL1
from starkexpress_api.apis.paths.api_v1_orderbooks_orderbook_id_l2 import ApiV1OrderbooksOrderbookIdL2
from starkexpress_api.apis.paths.api_v1_settlements import ApiV1Settlements
from starkexpress_api.apis.paths.api_v1_assets import ApiV1Assets
from starkexpress_api.apis.paths.api_v1_assets_asset_id import ApiV1AssetsAssetId
from starkexpress_api.apis.paths.api_v1_assets_deploy import ApiV1AssetsDeploy
from starkexpress_api.apis.paths.api_v1_transactions import ApiV1Transactions
from starkexpress_api.apis.paths.api_v1_transactions_transaction_id import ApiV1TransactionsTransactionId
from starkexpress_api.apis.paths.api_v1_transfers import ApiV1Transfers
from starkexpress_api.apis.paths.api_v1_transfers_details import ApiV1TransfersDetails
from starkexpress_api.apis.paths.api_v1_users import ApiV1Users
from starkexpress_api.apis.paths.api_v1_users_register_details import ApiV1UsersRegisterDetails
from starkexpress_api.apis.paths.api_v1_users_user_id import ApiV1UsersUserId
from starkexpress_api.apis.paths.api_v1_vaults_deposit_details import ApiV1VaultsDepositDetails
from starkexpress_api.apis.paths.api_v1_vaults import ApiV1Vaults
from starkexpress_api.apis.paths.api_v1_vaults_vault_id import ApiV1VaultsVaultId
from starkexpress_api.apis.paths.api_v1_vaults_withdraw import ApiV1VaultsWithdraw

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_V1_FEES: ApiV1Fees,
        PathValues.API_V1_FEES_FEE_ID: ApiV1FeesFeeId,
        PathValues.API_V1_MINT: ApiV1Mint,
        PathValues.API_V1_ORDERS_DETAILS: ApiV1OrdersDetails,
        PathValues.API_V1_ORDERS: ApiV1Orders,
        PathValues.API_V1_ORDERS_ORDER_ID: ApiV1OrdersOrderId,
        PathValues.API_V1_ORDERBOOKS: ApiV1Orderbooks,
        PathValues.API_V1_ORDERBOOKS_ORDERBOOK_ID: ApiV1OrderbooksOrderbookId,
        PathValues.API_V1_ORDERBOOKS_ORDERBOOK_ID_L1: ApiV1OrderbooksOrderbookIdL1,
        PathValues.API_V1_ORDERBOOKS_ORDERBOOK_ID_L2: ApiV1OrderbooksOrderbookIdL2,
        PathValues.API_V1_SETTLEMENTS: ApiV1Settlements,
        PathValues.API_V1_ASSETS: ApiV1Assets,
        PathValues.API_V1_ASSETS_ASSET_ID: ApiV1AssetsAssetId,
        PathValues.API_V1_ASSETS_DEPLOY: ApiV1AssetsDeploy,
        PathValues.API_V1_TRANSACTIONS: ApiV1Transactions,
        PathValues.API_V1_TRANSACTIONS_TRANSACTION_ID: ApiV1TransactionsTransactionId,
        PathValues.API_V1_TRANSFERS: ApiV1Transfers,
        PathValues.API_V1_TRANSFERS_DETAILS: ApiV1TransfersDetails,
        PathValues.API_V1_USERS: ApiV1Users,
        PathValues.API_V1_USERS_REGISTERDETAILS: ApiV1UsersRegisterDetails,
        PathValues.API_V1_USERS_USER_ID: ApiV1UsersUserId,
        PathValues.API_V1_VAULTS_DEPOSITDETAILS: ApiV1VaultsDepositDetails,
        PathValues.API_V1_VAULTS: ApiV1Vaults,
        PathValues.API_V1_VAULTS_VAULT_ID: ApiV1VaultsVaultId,
        PathValues.API_V1_VAULTS_WITHDRAW: ApiV1VaultsWithdraw,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_V1_FEES: ApiV1Fees,
        PathValues.API_V1_FEES_FEE_ID: ApiV1FeesFeeId,
        PathValues.API_V1_MINT: ApiV1Mint,
        PathValues.API_V1_ORDERS_DETAILS: ApiV1OrdersDetails,
        PathValues.API_V1_ORDERS: ApiV1Orders,
        PathValues.API_V1_ORDERS_ORDER_ID: ApiV1OrdersOrderId,
        PathValues.API_V1_ORDERBOOKS: ApiV1Orderbooks,
        PathValues.API_V1_ORDERBOOKS_ORDERBOOK_ID: ApiV1OrderbooksOrderbookId,
        PathValues.API_V1_ORDERBOOKS_ORDERBOOK_ID_L1: ApiV1OrderbooksOrderbookIdL1,
        PathValues.API_V1_ORDERBOOKS_ORDERBOOK_ID_L2: ApiV1OrderbooksOrderbookIdL2,
        PathValues.API_V1_SETTLEMENTS: ApiV1Settlements,
        PathValues.API_V1_ASSETS: ApiV1Assets,
        PathValues.API_V1_ASSETS_ASSET_ID: ApiV1AssetsAssetId,
        PathValues.API_V1_ASSETS_DEPLOY: ApiV1AssetsDeploy,
        PathValues.API_V1_TRANSACTIONS: ApiV1Transactions,
        PathValues.API_V1_TRANSACTIONS_TRANSACTION_ID: ApiV1TransactionsTransactionId,
        PathValues.API_V1_TRANSFERS: ApiV1Transfers,
        PathValues.API_V1_TRANSFERS_DETAILS: ApiV1TransfersDetails,
        PathValues.API_V1_USERS: ApiV1Users,
        PathValues.API_V1_USERS_REGISTERDETAILS: ApiV1UsersRegisterDetails,
        PathValues.API_V1_USERS_USER_ID: ApiV1UsersUserId,
        PathValues.API_V1_VAULTS_DEPOSITDETAILS: ApiV1VaultsDepositDetails,
        PathValues.API_V1_VAULTS: ApiV1Vaults,
        PathValues.API_V1_VAULTS_VAULT_ID: ApiV1VaultsVaultId,
        PathValues.API_V1_VAULTS_WITHDRAW: ApiV1VaultsWithdraw,
    }
)
