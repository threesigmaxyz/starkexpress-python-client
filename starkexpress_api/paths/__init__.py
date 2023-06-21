# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from starkexpress_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_FEES = "/api/v1/fees"
    API_V1_FEES_FEE_ID = "/api/v1/fees/{feeId}"
    API_V1_MINT = "/api/v1/mint"
    API_V1_ORDERS_DETAILS = "/api/v1/orders/details"
    API_V1_ORDERS = "/api/v1/orders"
    API_V1_ORDERS_ORDER_ID = "/api/v1/orders/{orderId}"
    API_V1_ORDERBOOKS = "/api/v1/orderbooks"
    API_V1_ORDERBOOKS_ORDERBOOK_ID = "/api/v1/orderbooks/{orderbookId}"
    API_V1_ORDERBOOKS_ORDERBOOK_ID_L1 = "/api/v1/orderbooks/{orderbookId}/l1"
    API_V1_ORDERBOOKS_ORDERBOOK_ID_L2 = "/api/v1/orderbooks/{orderbookId}/l2"
    API_V1_SETTLEMENTS = "/api/v1/settlements"
    API_V1_ASSETS = "/api/v1/assets"
    API_V1_ASSETS_ASSET_ID = "/api/v1/assets/{assetId}"
    API_V1_ASSETS_DEPLOY = "/api/v1/assets/deploy"
    API_V1_TRANSACTIONS = "/api/v1/transactions"
    API_V1_TRANSACTIONS_TRANSACTION_ID = "/api/v1/transactions/{transactionId}"
    API_V1_TRANSFERS = "/api/v1/transfers"
    API_V1_TRANSFERS_DETAILS = "/api/v1/transfers/details"
    API_V1_USERS = "/api/v1/users"
    API_V1_USERS_REGISTERDETAILS = "/api/v1/users/register-details"
    API_V1_USERS_USER_ID = "/api/v1/users/{userId}"
    API_V1_VAULTS_DEPOSITDETAILS = "/api/v1/vaults/deposit-details"
    API_V1_VAULTS = "/api/v1/vaults"
    API_V1_VAULTS_VAULT_ID = "/api/v1/vaults/{vaultId}"
    API_V1_VAULTS_WITHDRAW = "/api/v1/vaults/withdraw"
