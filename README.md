# starkexpress-api [![Github Actions][gha-badge]][gha] [![PyPi][pypi-badge]][pypi] [![License: MIT][license-badge]][license]
[gha]: https://github.com/threesigmaxyz/starkexpress-python-client/actions
[gha-badge]: https://github.com/threesigmaxyz/starkexpress-python-client/actions/workflows/main.yml/badge.svg
[pypi]: https://pypi.org/
[pypi-badge]: https://img.shields.io/pypi/v/github
[license]: https://opensource.org/licenses/MIT
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg


An API for the StarkExpress platform.

- API version: 1.0
- Package version: 0.0.1

## Requirements.

Python &gt;&#x3D;3.7


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/threesigmaxyz/starkexpress-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/threesigmaxyz/starkexpress-python-client.git`)

Then import the package:
```python
import starkexpress_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import starkexpress_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import starkexpress_api
from pprint import pprint
from starkexpress_api.apis.tags import asset_api
from starkexpress_api.model.api_error_response_dto import ApiErrorResponseDto
from starkexpress_api.model.asset_type import AssetType
from starkexpress_api.model.deploy_asset_model import DeployAssetModel
from starkexpress_api.model.enable_asset_model import EnableAssetModel
from starkexpress_api.model.filter_options import FilterOptions
from starkexpress_api.model.tenant_asset_dto import TenantAssetDto
from starkexpress_api.model.tenant_asset_dto_paginated_response_dto import TenantAssetDtoPaginatedResponseDto
# Defining the host is optional and defaults to https://testnet-api.starkexpress.io
# See configuration.py for a list of all supported configuration parameters.
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = starkexpress_api.Configuration(
    host = "https://testnet-api.starkexpress.io",
    access_token = 'YOUR_ACCESS_TOKEN'
)

# Enter a context with an instance of the API client
with starkexpress_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = asset_api.AssetApi(api_client)
    deploy_asset_model = DeployAssetModel(
        type=AssetType("Eth"),
        name="name_example",
        symbol="symbol_example",
        uri="uri_example",
        quantum="quantum_example",
    ) # DeployAssetModel | The asset deployment request.

    try:
        # Deploy Asset
        api_response = api_instance.deploy_asset(deploy_asset_model)
        pprint(api_response)
    except starkexpress_api.ApiException as e:
        print("Exception when calling AssetApi->deploy_asset: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://testnet-api.starkexpress.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AssetApi* | [**deploy_asset**](docs/apis/tags/AssetApi.md#deploy_asset) | **post** /api/v1/assets/deploy | Deploy Asset
*AssetApi* | [**enable_asset**](docs/apis/tags/AssetApi.md#enable_asset) | **post** /api/v1/assets | Enable Asset
*AssetApi* | [**get_all_assets**](docs/apis/tags/AssetApi.md#get_all_assets) | **get** /api/v1/assets | Get All Assets
*AssetApi* | [**get_asset**](docs/apis/tags/AssetApi.md#get_asset) | **get** /api/v1/assets/{assetId} | Get Asset
*DepositApi* | [**deposit_details**](docs/apis/tags/DepositApi.md#deposit_details) | **post** /api/v1/vaults/deposit-details | Returns the deposit details for a given asset.
*FeeApi* | [**configure_fee_model**](docs/apis/tags/FeeApi.md#configure_fee_model) | **post** /api/v1/fees | Configure Fee Model
*FeeApi* | [**get_fee_model**](docs/apis/tags/FeeApi.md#get_fee_model) | **get** /api/v1/fees/{feeId} | Get Fee Model
*MintApi* | [**mint_assets**](docs/apis/tags/MintApi.md#mint_assets) | **post** /api/v1/mint | Mint Assets
*OrderApi* | [**cancel_order**](docs/apis/tags/OrderApi.md#cancel_order) | **delete** /api/v1/orders/{orderId} | Cancel Order (Not Implemented)
*OrderApi* | [**order_details**](docs/apis/tags/OrderApi.md#order_details) | **post** /api/v1/orders/details | Get Order Details (Not Implemented)
*OrderApi* | [**submit_order**](docs/apis/tags/OrderApi.md#submit_order) | **post** /api/v1/orders | Submit Order (Not Implemented)
*OrderbookApi* | [**create_orderbook**](docs/apis/tags/OrderbookApi.md#create_orderbook) | **post** /api/v1/orderbooks | Create Orderbook (Not Implemented)
*OrderbookApi* | [**get_orderbook**](docs/apis/tags/OrderbookApi.md#get_orderbook) | **get** /api/v1/orderbooks/{orderbookId} | Get Orderbook (Not Implemented)
*OrderbookApi* | [**get_orderbook_level1_data**](docs/apis/tags/OrderbookApi.md#get_orderbook_level1_data) | **get** /api/v1/orderbooks/{orderbookId}/l1 | Get Orderbook L1 Data (Not Implemented)
*OrderbookApi* | [**get_orderbook_level2_data**](docs/apis/tags/OrderbookApi.md#get_orderbook_level2_data) | **get** /api/v1/orderbooks/{orderbookId}/l2 | Get Orderbook L2 Data (Not Implemented)
*SettlementApi* | [**submit_settlement**](docs/apis/tags/SettlementApi.md#submit_settlement) | **post** /api/v1/settlements | Submit Settlement
*TransactionApi* | [**get_all_transactions**](docs/apis/tags/TransactionApi.md#get_all_transactions) | **get** /api/v1/transactions | Get All Transactions
*TransactionApi* | [**get_transaction**](docs/apis/tags/TransactionApi.md#get_transaction) | **get** /api/v1/transactions/{transactionId} | Get Transaction
*TransferApi* | [**transfer**](docs/apis/tags/TransferApi.md#transfer) | **post** /api/v1/transfers | Transfer Asset
*TransferApi* | [**transfer_details**](docs/apis/tags/TransferApi.md#transfer_details) | **post** /api/v1/transfers/details | Get Transfer Details
*UserApi* | [**e_ip712_details**](docs/apis/tags/UserApi.md#e_ip712_details) | **get** /api/v1/users/register-details | Get EIP712 data to be signed
*UserApi* | [**get_all_users**](docs/apis/tags/UserApi.md#get_all_users) | **get** /api/v1/users | Get All Users
*UserApi* | [**get_user**](docs/apis/tags/UserApi.md#get_user) | **get** /api/v1/users/{userId} | Get User
*UserApi* | [**register_user**](docs/apis/tags/UserApi.md#register_user) | **post** /api/v1/users | Register new User
*VaultApi* | [**get_all_vaults**](docs/apis/tags/VaultApi.md#get_all_vaults) | **get** /api/v1/vaults | Get All Vaults
*VaultApi* | [**get_vault**](docs/apis/tags/VaultApi.md#get_vault) | **get** /api/v1/vaults/{vaultId} | Get a single Vault
*WithdrawApi* | [**withdraw**](docs/apis/tags/WithdrawApi.md#withdraw) | **post** /api/v1/vaults/withdraw | Withdraw Asset

## Documentation For Models

 - [ApiErrorDto](docs/models/ApiErrorDto.md)
 - [ApiErrorResponseDto](docs/models/ApiErrorResponseDto.md)
 - [AssetType](docs/models/AssetType.md)
 - [BatchMintRequestModel](docs/models/BatchMintRequestModel.md)
 - [BigInteger](docs/models/BigInteger.md)
 - [ConfigureFeeModel](docs/models/ConfigureFeeModel.md)
 - [CreateOrderbookModel](docs/models/CreateOrderbookModel.md)
 - [DataAvailabilityModes](docs/models/DataAvailabilityModes.md)
 - [DeployAssetModel](docs/models/DeployAssetModel.md)
 - [DepositDetailsDto](docs/models/DepositDetailsDto.md)
 - [DepositDetailsModel](docs/models/DepositDetailsModel.md)
 - [DomainDto](docs/models/DomainDto.md)
 - [EnableAssetModel](docs/models/EnableAssetModel.md)
 - [ErrorCodes](docs/models/ErrorCodes.md)
 - [FeeAction](docs/models/FeeAction.md)
 - [FeeConfigDto](docs/models/FeeConfigDto.md)
 - [FeeDto](docs/models/FeeDto.md)
 - [FilterOptions](docs/models/FilterOptions.md)
 - [MemberDescriptionDto](docs/models/MemberDescriptionDto.md)
 - [MemberValueDto](docs/models/MemberValueDto.md)
 - [MintDataModel](docs/models/MintDataModel.md)
 - [MintRequestDataModel](docs/models/MintRequestDataModel.md)
 - [OrderDetailsDto](docs/models/OrderDetailsDto.md)
 - [OrderDetailsModel](docs/models/OrderDetailsModel.md)
 - [OrderDto](docs/models/OrderDto.md)
 - [OrderFillDto](docs/models/OrderFillDto.md)
 - [OrderSide](docs/models/OrderSide.md)
 - [OrderbookAssetDto](docs/models/OrderbookAssetDto.md)
 - [OrderbookDto](docs/models/OrderbookDto.md)
 - [OrderbookLevel1DataDto](docs/models/OrderbookLevel1DataDto.md)
 - [OrderbookLevel2DataDto](docs/models/OrderbookLevel2DataDto.md)
 - [OrderbookLevel2EntryDto](docs/models/OrderbookLevel2EntryDto.md)
 - [PaginationDto](docs/models/PaginationDto.md)
 - [RegisterDetailsDto](docs/models/RegisterDetailsDto.md)
 - [RegisterUserModel](docs/models/RegisterUserModel.md)
 - [SettlementInfoModel](docs/models/SettlementInfoModel.md)
 - [SettlementOrderModel](docs/models/SettlementOrderModel.md)
 - [SignatureModel](docs/models/SignatureModel.md)
 - [StarkExOperation](docs/models/StarkExOperation.md)
 - [SubmitOrderModel](docs/models/SubmitOrderModel.md)
 - [SubmitSettlementModel](docs/models/SubmitSettlementModel.md)
 - [TenantAssetDto](docs/models/TenantAssetDto.md)
 - [TenantAssetDtoPaginatedResponseDto](docs/models/TenantAssetDtoPaginatedResponseDto.md)
 - [TransactionDto](docs/models/TransactionDto.md)
 - [TransactionDtoPaginatedResponseDto](docs/models/TransactionDtoPaginatedResponseDto.md)
 - [TransactionModel](docs/models/TransactionModel.md)
 - [TransactionStatus](docs/models/TransactionStatus.md)
 - [TransferDetailsDto](docs/models/TransferDetailsDto.md)
 - [TransferDetailsModel](docs/models/TransferDetailsModel.md)
 - [TransferModel](docs/models/TransferModel.md)
 - [UserDto](docs/models/UserDto.md)
 - [UserDtoPaginatedResponseDto](docs/models/UserDtoPaginatedResponseDto.md)
 - [UserWithVaultsDto](docs/models/UserWithVaultsDto.md)
 - [VaultDto](docs/models/VaultDto.md)
 - [VaultDtoPaginatedResponseDto](docs/models/VaultDtoPaginatedResponseDto.md)
 - [WithdrawDetailsDto](docs/models/WithdrawDetailsDto.md)
 - [WithdrawModel](docs/models/WithdrawModel.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## oauth2

- **Type**: OAuth
- **Flow**: application
- **Token URL**: https://starkexpress-testnet.eu.auth0.com/oauth/token
- **Scopes**: 
 - **write:users**: Access user write operations.
 - **read:users**: Access user read operations.
 - **read:tenant_assets**: Access tenant asset read operations.
 - **write:tenant_assets**: Access tenant asset write operations.
 - **mint:assets**: Access mint operations.
 - **read:vaults**: Access vault read operations.
 - **write:transfers**: Access transfer write operations.
 - **read:transfers**: Access transfer read operations.
 - **write:smart-contracts**: Access to deploying smart contracts.
 - **write:settlements**: Access settlement write operations.


---
<a name="documentation-for-about-us"></a>
## About Us
[Three Sigma](https://threesigma.xyz/) is a venture builder firm focused on blockchain engineering, research, and investment. Our mission is to advance the adoption of blockchain technology and contribute towards the healthy development of the Web3 space.
If you are interested in joining our team, please contact us [here](mailto:info@threesigma.xyz).

---

<p align="center">
    <a href="https://starkexpress.io" target="_blank">
        <img src="https://threesigma.xyz/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fthree-sigma-labs-research-capital-white.0f8e8f50.png&w=2048&q=75" width="75%" />
    </a>
</p>
