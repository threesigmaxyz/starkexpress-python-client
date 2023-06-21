# coding: utf-8

"""
    StarkExpress API Docs

    An API for the StarkExpress platform.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from starkexpress_api import schemas  # noqa: F401


class ErrorCodes(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ModelStateInvalid": "MODEL_STATE_INVALID",
            "InvalidGuid": "INVALID_GUID",
            "FilterIsRequired": "FILTER_IS_REQUIRED",
            "UsernameRequired": "USERNAME_REQUIRED",
            "UsernameLengthInvalid": "USERNAME_LENGTH_INVALID",
            "UsernameAlreadyRegistered": "USERNAME_ALREADY_REGISTERED",
            "UsersRequired": "USERS_REQUIRED",
            "UserIdRequired": "USER_ID_REQUIRED",
            "UserIdNotFound": "USER_ID_NOT_FOUND",
            "AddressRequired": "ADDRESS_REQUIRED",
            "AddressInvalid": "ADDRESS_INVALID",
            "AddressAlreadyRegistered": "ADDRESS_ALREADY_REGISTERED",
            "StarkSignatureRequired": "STARK_SIGNATURE_REQUIRED",
            "StarkSignatureRRequired": "STARK_SIGNATURE_RREQUIRED",
            "StarkSignatureSRequired": "STARK_SIGNATURE_SREQUIRED",
            "StarkSignatureInvalid": "STARK_SIGNATURE_INVALID",
            "StarkKeyRequired": "STARK_KEY_REQUIRED",
            "StarkKeyLengthInvalid": "STARK_KEY_LENGTH_INVALID",
            "StarkKeyFormatInvalid": "STARK_KEY_FORMAT_INVALID",
            "StarkKeyAlreadyInuse": "STARK_KEY_ALREADY_INUSE",
            "Eip712SignatureRequired": "EIP712SIGNATURE_REQUIRED",
            "Eip712SignatureInvalid": "EIP712SIGNATURE_INVALID",
            "AssetAlreadyWhitelisted": "ASSET_ALREADY_WHITELISTED",
            "AssetDisabled": "ASSET_DISABLED",
            "InvalidAssetType": "INVALID_ASSET_TYPE",
            "AssetAddressIsNotAContract": "ASSET_ADDRESS_IS_NOT_ACONTRACT",
            "AssetContractIsNotMintable": "ASSET_CONTRACT_IS_NOT_MINTABLE",
            "AssetIdRequired": "ASSET_ID_REQUIRED",
            "AssetNameRequired": "ASSET_NAME_REQUIRED",
            "AssetSymbolRequired": "ASSET_SYMBOL_REQUIRED",
            "AssetQuantumRequired": "ASSET_QUANTUM_REQUIRED",
            "AssetUriRequired": "ASSET_URI_REQUIRED",
            "AssetAlreadyRegistered": "ASSET_ALREADY_REGISTERED",
            "AssetNotRegistered": "ASSET_NOT_REGISTERED",
            "AssetNotConfirmed": "ASSET_NOT_CONFIRMED",
            "AssetNotSupported": "ASSET_NOT_SUPPORTED",
            "AssetQuantumInvalid": "ASSET_QUANTUM_INVALID",
            "OperationAmountRequired": "OPERATION_AMOUNT_REQUIRED",
            "OperationAmountInvalid": "OPERATION_AMOUNT_INVALID",
            "OperationAmountUnquantizable": "OPERATION_AMOUNT_UNQUANTIZABLE",
            "VaultNotRegistered": "VAULT_NOT_REGISTERED",
            "VaultOutOfBounds": "VAULT_OUT_OF_BOUNDS",
            "VaultIdRequired": "VAULT_ID_REQUIRED",
            "TokenIdRequired": "TOKEN_ID_REQUIRED",
            "StarkTypeInvalid": "STARK_TYPE_INVALID",
            "StarkTypeInvalidFormat": "STARK_TYPE_INVALID_FORMAT",
            "StarkTypeRequired": "STARK_TYPE_REQUIRED",
            "MintsRequired": "MINTS_REQUIRED",
            "MintingBlobRequired": "MINTING_BLOB_REQUIRED",
            "DuplicatedUserIds": "DUPLICATED_USER_IDS",
            "DuplicatedMints": "DUPLICATED_MINTS",
            "ExistingMintingBlob": "EXISTING_MINTING_BLOB",
            "DataAvailabilityRequired": "DATA_AVAILABILITY_REQUIRED",
            "FeeActionRequired": "FEE_ACTION_REQUIRED",
            "FeeBasisPointsRequired": "FEE_BASIS_POINTS_REQUIRED",
            "FeeNotConfigured": "FEE_NOT_CONFIGURED",
            "FeeBasisPointOutOfRange": "FEE_BASIS_POINT_OUT_OF_RANGE",
            "FeeVaultIdRequired": "FEE_VAULT_ID_REQUIRED",
            "FeeQuantizedAmountRequired": "FEE_QUANTIZED_AMOUNT_REQUIRED",
            "BuyVaultIdRequired": "BUY_VAULT_ID_REQUIRED",
            "BuyAmountRequired": "BUY_AMOUNT_REQUIRED",
            "SellVaultIdRequired": "SELL_VAULT_ID_REQUIRED",
            "SellAmountRequired": "SELL_AMOUNT_REQUIRED",
            "OrderARequired": "ORDER_AREQUIRED",
            "OrderBRequired": "ORDER_BREQUIRED",
            "OrderAFeeAmountRequired": "ORDER_AFEE_AMOUNT_REQUIRED",
            "OrderBFeeAmountRequired": "ORDER_BFEE_AMOUNT_REQUIRED",
            "OrderAFeeDestinationVaultIdRequired": "ORDER_AFEE_DESTINATION_VAULT_ID_REQUIRED",
            "OrderBFeeDestinationVaultIdRequired": "ORDER_BFEE_DESTINATION_VAULT_ID_REQUIRED",
            "SenderVaultIdRequired": "SENDER_VAULT_ID_REQUIRED",
            "ReceiverVaultIdRequired": "RECEIVER_VAULT_ID_REQUIRED",
            "ExpirationTimestampRequired": "EXPIRATION_TIMESTAMP_REQUIRED",
            "NonceRequired": "NONCE_REQUIRED",
            "TransactionIdNotFound": "TRANSACTION_ID_NOT_FOUND",
            "AssetTypeRequired": "ASSET_TYPE_REQUIRED",
            "SenderDataAvailabilityModeRequired": "SENDER_DATA_AVAILABILITY_MODE_REQUIRED",
            "ReceiverDataAvailabilityModeRequired": "RECEIVER_DATA_AVAILABILITY_MODE_REQUIRED",
            "MintingBlobNotFound": "MINTING_BLOB_NOT_FOUND",
            "InvalidHexString": "INVALID_HEX_STRING",
            "TenantNameAlreadyRegistered": "TENANT_NAME_ALREADY_REGISTERED",
            "TenantIdNotFound": "TENANT_ID_NOT_FOUND",
            "TenantOwnerRequired": "TENANT_OWNER_REQUIRED",
            "StarkExInstanceNotFound": "STARK_EX_INSTANCE_NOT_FOUND",
            "StarkExContractAlreadyRegistered": "STARK_EX_CONTRACT_ALREADY_REGISTERED",
            "StarkExNameAlreadyRegistered": "STARK_EX_NAME_ALREADY_REGISTERED",
            "StarkExAddressRequired": "STARK_EX_ADDRESS_REQUIRED",
            "StarkExContractTokensAdminKeyRequired": "STARK_EX_CONTRACT_TOKENS_ADMIN_KEY_REQUIRED",
            "StarkExInstanceNameRequired": "STARK_EX_INSTANCE_NAME_REQUIRED",
            "ValidiumTreeHeightRequired": "VALIDIUM_TREE_HEIGHT_REQUIRED",
            "ZkRollupTreeHeightRequired": "ZK_ROLLUP_TREE_HEIGHT_REQUIRED",
            "ValidiumTreeHeightOutOfRange": "VALIDIUM_TREE_HEIGHT_OUT_OF_RANGE",
            "ZkRollupTreeHeightOutOfRange": "ZK_ROLLUP_TREE_HEIGHT_OUT_OF_RANGE",
            "StarkExHostnameRequired": "STARK_EX_HOSTNAME_REQUIRED",
            "StarkExVersionRequired": "STARK_EX_VERSION_REQUIRED",
            "StarkExHostnameInvalid": "STARK_EX_HOSTNAME_INVALID",
            "StarkExVersionNotSupported": "STARK_EX_VERSION_NOT_SUPPORTED",
            "IsUniqueMintingEnabledRequired": "IS_UNIQUE_MINTING_ENABLED_REQUIRED",
            "StarkExCertificateRequired": "STARK_EX_CERTIFICATE_REQUIRED",
            "StarkExCertificateIsInvalid": "STARK_EX_CERTIFICATE_IS_INVALID",
            "StarkExInstanceTokenAdminPrivateKeySecretNotFound": "STARK_EX_INSTANCE_TOKEN_ADMIN_PRIVATE_KEY_SECRET_NOT_FOUND",
            "StarkExDeploymentBlockMissing": "STARK_EX_DEPLOYMENT_BLOCK_MISSING",
            "StarkExDeploymentBlockOutOfRange": "STARK_EX_DEPLOYMENT_BLOCK_OUT_OF_RANGE",
            "OrderbookIdRequired": "ORDERBOOK_ID_REQUIRED",
            "BaseAssetIdRequired": "BASE_ASSET_ID_REQUIRED",
            "QuoteAssetIdRequired": "QUOTE_ASSET_ID_REQUIRED",
            "BaseAssetPrecisionRequired": "BASE_ASSET_PRECISION_REQUIRED",
            "QuoteAssetPrecisionRequired": "QUOTE_ASSET_PRECISION_REQUIRED",
            "OrderIdRequired": "ORDER_ID_REQUIRED",
            "OrderSideRequired": "ORDER_SIDE_REQUIRED",
            "OrderPriceRequired": "ORDER_PRICE_REQUIRED",
            "OrderAmountRequired": "ORDER_AMOUNT_REQUIRED",
            "InsufficientBalance": "INSUFFICIENT_BALANCE",
            "TimestampOutsideValidRange": "TIMESTAMP_OUTSIDE_VALID_RANGE",
            "TransferIntoSameVault": "TRANSFER_INTO_SAME_VAULT",
            "ConflictingVaultAssets": "CONFLICTING_VAULT_ASSETS",
            "FeeAlreadyConfigured": "FEE_ALREADY_CONFIGURED",
            "MintingBlobInvalid": "MINTING_BLOB_INVALID",
            "TokenIdInvalid": "TOKEN_ID_INVALID",
            "TenantOwnerUnauthorized": "TENANT_OWNER_UNAUTHORIZED",
            "InternalError": "INTERNAL_ERROR",
        }
    
    @schemas.classproperty
    def MODEL_STATE_INVALID(cls):
        return cls("ModelStateInvalid")
    
    @schemas.classproperty
    def INVALID_GUID(cls):
        return cls("InvalidGuid")
    
    @schemas.classproperty
    def FILTER_IS_REQUIRED(cls):
        return cls("FilterIsRequired")
    
    @schemas.classproperty
    def USERNAME_REQUIRED(cls):
        return cls("UsernameRequired")
    
    @schemas.classproperty
    def USERNAME_LENGTH_INVALID(cls):
        return cls("UsernameLengthInvalid")
    
    @schemas.classproperty
    def USERNAME_ALREADY_REGISTERED(cls):
        return cls("UsernameAlreadyRegistered")
    
    @schemas.classproperty
    def USERS_REQUIRED(cls):
        return cls("UsersRequired")
    
    @schemas.classproperty
    def USER_ID_REQUIRED(cls):
        return cls("UserIdRequired")
    
    @schemas.classproperty
    def USER_ID_NOT_FOUND(cls):
        return cls("UserIdNotFound")
    
    @schemas.classproperty
    def ADDRESS_REQUIRED(cls):
        return cls("AddressRequired")
    
    @schemas.classproperty
    def ADDRESS_INVALID(cls):
        return cls("AddressInvalid")
    
    @schemas.classproperty
    def ADDRESS_ALREADY_REGISTERED(cls):
        return cls("AddressAlreadyRegistered")
    
    @schemas.classproperty
    def STARK_SIGNATURE_REQUIRED(cls):
        return cls("StarkSignatureRequired")
    
    @schemas.classproperty
    def STARK_SIGNATURE_RREQUIRED(cls):
        return cls("StarkSignatureRRequired")
    
    @schemas.classproperty
    def STARK_SIGNATURE_SREQUIRED(cls):
        return cls("StarkSignatureSRequired")
    
    @schemas.classproperty
    def STARK_SIGNATURE_INVALID(cls):
        return cls("StarkSignatureInvalid")
    
    @schemas.classproperty
    def STARK_KEY_REQUIRED(cls):
        return cls("StarkKeyRequired")
    
    @schemas.classproperty
    def STARK_KEY_LENGTH_INVALID(cls):
        return cls("StarkKeyLengthInvalid")
    
    @schemas.classproperty
    def STARK_KEY_FORMAT_INVALID(cls):
        return cls("StarkKeyFormatInvalid")
    
    @schemas.classproperty
    def STARK_KEY_ALREADY_INUSE(cls):
        return cls("StarkKeyAlreadyInuse")
    
    @schemas.classproperty
    def EIP712SIGNATURE_REQUIRED(cls):
        return cls("Eip712SignatureRequired")
    
    @schemas.classproperty
    def EIP712SIGNATURE_INVALID(cls):
        return cls("Eip712SignatureInvalid")
    
    @schemas.classproperty
    def ASSET_ALREADY_WHITELISTED(cls):
        return cls("AssetAlreadyWhitelisted")
    
    @schemas.classproperty
    def ASSET_DISABLED(cls):
        return cls("AssetDisabled")
    
    @schemas.classproperty
    def INVALID_ASSET_TYPE(cls):
        return cls("InvalidAssetType")
    
    @schemas.classproperty
    def ASSET_ADDRESS_IS_NOT_ACONTRACT(cls):
        return cls("AssetAddressIsNotAContract")
    
    @schemas.classproperty
    def ASSET_CONTRACT_IS_NOT_MINTABLE(cls):
        return cls("AssetContractIsNotMintable")
    
    @schemas.classproperty
    def ASSET_ID_REQUIRED(cls):
        return cls("AssetIdRequired")
    
    @schemas.classproperty
    def ASSET_NAME_REQUIRED(cls):
        return cls("AssetNameRequired")
    
    @schemas.classproperty
    def ASSET_SYMBOL_REQUIRED(cls):
        return cls("AssetSymbolRequired")
    
    @schemas.classproperty
    def ASSET_QUANTUM_REQUIRED(cls):
        return cls("AssetQuantumRequired")
    
    @schemas.classproperty
    def ASSET_URI_REQUIRED(cls):
        return cls("AssetUriRequired")
    
    @schemas.classproperty
    def ASSET_ALREADY_REGISTERED(cls):
        return cls("AssetAlreadyRegistered")
    
    @schemas.classproperty
    def ASSET_NOT_REGISTERED(cls):
        return cls("AssetNotRegistered")
    
    @schemas.classproperty
    def ASSET_NOT_CONFIRMED(cls):
        return cls("AssetNotConfirmed")
    
    @schemas.classproperty
    def ASSET_NOT_SUPPORTED(cls):
        return cls("AssetNotSupported")
    
    @schemas.classproperty
    def ASSET_QUANTUM_INVALID(cls):
        return cls("AssetQuantumInvalid")
    
    @schemas.classproperty
    def OPERATION_AMOUNT_REQUIRED(cls):
        return cls("OperationAmountRequired")
    
    @schemas.classproperty
    def OPERATION_AMOUNT_INVALID(cls):
        return cls("OperationAmountInvalid")
    
    @schemas.classproperty
    def OPERATION_AMOUNT_UNQUANTIZABLE(cls):
        return cls("OperationAmountUnquantizable")
    
    @schemas.classproperty
    def VAULT_NOT_REGISTERED(cls):
        return cls("VaultNotRegistered")
    
    @schemas.classproperty
    def VAULT_OUT_OF_BOUNDS(cls):
        return cls("VaultOutOfBounds")
    
    @schemas.classproperty
    def VAULT_ID_REQUIRED(cls):
        return cls("VaultIdRequired")
    
    @schemas.classproperty
    def TOKEN_ID_REQUIRED(cls):
        return cls("TokenIdRequired")
    
    @schemas.classproperty
    def STARK_TYPE_INVALID(cls):
        return cls("StarkTypeInvalid")
    
    @schemas.classproperty
    def STARK_TYPE_INVALID_FORMAT(cls):
        return cls("StarkTypeInvalidFormat")
    
    @schemas.classproperty
    def STARK_TYPE_REQUIRED(cls):
        return cls("StarkTypeRequired")
    
    @schemas.classproperty
    def MINTS_REQUIRED(cls):
        return cls("MintsRequired")
    
    @schemas.classproperty
    def MINTING_BLOB_REQUIRED(cls):
        return cls("MintingBlobRequired")
    
    @schemas.classproperty
    def DUPLICATED_USER_IDS(cls):
        return cls("DuplicatedUserIds")
    
    @schemas.classproperty
    def DUPLICATED_MINTS(cls):
        return cls("DuplicatedMints")
    
    @schemas.classproperty
    def EXISTING_MINTING_BLOB(cls):
        return cls("ExistingMintingBlob")
    
    @schemas.classproperty
    def DATA_AVAILABILITY_REQUIRED(cls):
        return cls("DataAvailabilityRequired")
    
    @schemas.classproperty
    def FEE_ACTION_REQUIRED(cls):
        return cls("FeeActionRequired")
    
    @schemas.classproperty
    def FEE_BASIS_POINTS_REQUIRED(cls):
        return cls("FeeBasisPointsRequired")
    
    @schemas.classproperty
    def FEE_NOT_CONFIGURED(cls):
        return cls("FeeNotConfigured")
    
    @schemas.classproperty
    def FEE_BASIS_POINT_OUT_OF_RANGE(cls):
        return cls("FeeBasisPointOutOfRange")
    
    @schemas.classproperty
    def FEE_VAULT_ID_REQUIRED(cls):
        return cls("FeeVaultIdRequired")
    
    @schemas.classproperty
    def FEE_QUANTIZED_AMOUNT_REQUIRED(cls):
        return cls("FeeQuantizedAmountRequired")
    
    @schemas.classproperty
    def BUY_VAULT_ID_REQUIRED(cls):
        return cls("BuyVaultIdRequired")
    
    @schemas.classproperty
    def BUY_AMOUNT_REQUIRED(cls):
        return cls("BuyAmountRequired")
    
    @schemas.classproperty
    def SELL_VAULT_ID_REQUIRED(cls):
        return cls("SellVaultIdRequired")
    
    @schemas.classproperty
    def SELL_AMOUNT_REQUIRED(cls):
        return cls("SellAmountRequired")
    
    @schemas.classproperty
    def ORDER_AREQUIRED(cls):
        return cls("OrderARequired")
    
    @schemas.classproperty
    def ORDER_BREQUIRED(cls):
        return cls("OrderBRequired")
    
    @schemas.classproperty
    def ORDER_AFEE_AMOUNT_REQUIRED(cls):
        return cls("OrderAFeeAmountRequired")
    
    @schemas.classproperty
    def ORDER_BFEE_AMOUNT_REQUIRED(cls):
        return cls("OrderBFeeAmountRequired")
    
    @schemas.classproperty
    def ORDER_AFEE_DESTINATION_VAULT_ID_REQUIRED(cls):
        return cls("OrderAFeeDestinationVaultIdRequired")
    
    @schemas.classproperty
    def ORDER_BFEE_DESTINATION_VAULT_ID_REQUIRED(cls):
        return cls("OrderBFeeDestinationVaultIdRequired")
    
    @schemas.classproperty
    def SENDER_VAULT_ID_REQUIRED(cls):
        return cls("SenderVaultIdRequired")
    
    @schemas.classproperty
    def RECEIVER_VAULT_ID_REQUIRED(cls):
        return cls("ReceiverVaultIdRequired")
    
    @schemas.classproperty
    def EXPIRATION_TIMESTAMP_REQUIRED(cls):
        return cls("ExpirationTimestampRequired")
    
    @schemas.classproperty
    def NONCE_REQUIRED(cls):
        return cls("NonceRequired")
    
    @schemas.classproperty
    def TRANSACTION_ID_NOT_FOUND(cls):
        return cls("TransactionIdNotFound")
    
    @schemas.classproperty
    def ASSET_TYPE_REQUIRED(cls):
        return cls("AssetTypeRequired")
    
    @schemas.classproperty
    def SENDER_DATA_AVAILABILITY_MODE_REQUIRED(cls):
        return cls("SenderDataAvailabilityModeRequired")
    
    @schemas.classproperty
    def RECEIVER_DATA_AVAILABILITY_MODE_REQUIRED(cls):
        return cls("ReceiverDataAvailabilityModeRequired")
    
    @schemas.classproperty
    def MINTING_BLOB_NOT_FOUND(cls):
        return cls("MintingBlobNotFound")
    
    @schemas.classproperty
    def INVALID_HEX_STRING(cls):
        return cls("InvalidHexString")
    
    @schemas.classproperty
    def TENANT_NAME_ALREADY_REGISTERED(cls):
        return cls("TenantNameAlreadyRegistered")
    
    @schemas.classproperty
    def TENANT_ID_NOT_FOUND(cls):
        return cls("TenantIdNotFound")
    
    @schemas.classproperty
    def TENANT_OWNER_REQUIRED(cls):
        return cls("TenantOwnerRequired")
    
    @schemas.classproperty
    def STARK_EX_INSTANCE_NOT_FOUND(cls):
        return cls("StarkExInstanceNotFound")
    
    @schemas.classproperty
    def STARK_EX_CONTRACT_ALREADY_REGISTERED(cls):
        return cls("StarkExContractAlreadyRegistered")
    
    @schemas.classproperty
    def STARK_EX_NAME_ALREADY_REGISTERED(cls):
        return cls("StarkExNameAlreadyRegistered")
    
    @schemas.classproperty
    def STARK_EX_ADDRESS_REQUIRED(cls):
        return cls("StarkExAddressRequired")
    
    @schemas.classproperty
    def STARK_EX_CONTRACT_TOKENS_ADMIN_KEY_REQUIRED(cls):
        return cls("StarkExContractTokensAdminKeyRequired")
    
    @schemas.classproperty
    def STARK_EX_INSTANCE_NAME_REQUIRED(cls):
        return cls("StarkExInstanceNameRequired")
    
    @schemas.classproperty
    def VALIDIUM_TREE_HEIGHT_REQUIRED(cls):
        return cls("ValidiumTreeHeightRequired")
    
    @schemas.classproperty
    def ZK_ROLLUP_TREE_HEIGHT_REQUIRED(cls):
        return cls("ZkRollupTreeHeightRequired")
    
    @schemas.classproperty
    def VALIDIUM_TREE_HEIGHT_OUT_OF_RANGE(cls):
        return cls("ValidiumTreeHeightOutOfRange")
    
    @schemas.classproperty
    def ZK_ROLLUP_TREE_HEIGHT_OUT_OF_RANGE(cls):
        return cls("ZkRollupTreeHeightOutOfRange")
    
    @schemas.classproperty
    def STARK_EX_HOSTNAME_REQUIRED(cls):
        return cls("StarkExHostnameRequired")
    
    @schemas.classproperty
    def STARK_EX_VERSION_REQUIRED(cls):
        return cls("StarkExVersionRequired")
    
    @schemas.classproperty
    def STARK_EX_HOSTNAME_INVALID(cls):
        return cls("StarkExHostnameInvalid")
    
    @schemas.classproperty
    def STARK_EX_VERSION_NOT_SUPPORTED(cls):
        return cls("StarkExVersionNotSupported")
    
    @schemas.classproperty
    def IS_UNIQUE_MINTING_ENABLED_REQUIRED(cls):
        return cls("IsUniqueMintingEnabledRequired")
    
    @schemas.classproperty
    def STARK_EX_CERTIFICATE_REQUIRED(cls):
        return cls("StarkExCertificateRequired")
    
    @schemas.classproperty
    def STARK_EX_CERTIFICATE_IS_INVALID(cls):
        return cls("StarkExCertificateIsInvalid")
    
    @schemas.classproperty
    def STARK_EX_INSTANCE_TOKEN_ADMIN_PRIVATE_KEY_SECRET_NOT_FOUND(cls):
        return cls("StarkExInstanceTokenAdminPrivateKeySecretNotFound")
    
    @schemas.classproperty
    def STARK_EX_DEPLOYMENT_BLOCK_MISSING(cls):
        return cls("StarkExDeploymentBlockMissing")
    
    @schemas.classproperty
    def STARK_EX_DEPLOYMENT_BLOCK_OUT_OF_RANGE(cls):
        return cls("StarkExDeploymentBlockOutOfRange")
    
    @schemas.classproperty
    def ORDERBOOK_ID_REQUIRED(cls):
        return cls("OrderbookIdRequired")
    
    @schemas.classproperty
    def BASE_ASSET_ID_REQUIRED(cls):
        return cls("BaseAssetIdRequired")
    
    @schemas.classproperty
    def QUOTE_ASSET_ID_REQUIRED(cls):
        return cls("QuoteAssetIdRequired")
    
    @schemas.classproperty
    def BASE_ASSET_PRECISION_REQUIRED(cls):
        return cls("BaseAssetPrecisionRequired")
    
    @schemas.classproperty
    def QUOTE_ASSET_PRECISION_REQUIRED(cls):
        return cls("QuoteAssetPrecisionRequired")
    
    @schemas.classproperty
    def ORDER_ID_REQUIRED(cls):
        return cls("OrderIdRequired")
    
    @schemas.classproperty
    def ORDER_SIDE_REQUIRED(cls):
        return cls("OrderSideRequired")
    
    @schemas.classproperty
    def ORDER_PRICE_REQUIRED(cls):
        return cls("OrderPriceRequired")
    
    @schemas.classproperty
    def ORDER_AMOUNT_REQUIRED(cls):
        return cls("OrderAmountRequired")
    
    @schemas.classproperty
    def INSUFFICIENT_BALANCE(cls):
        return cls("InsufficientBalance")
    
    @schemas.classproperty
    def TIMESTAMP_OUTSIDE_VALID_RANGE(cls):
        return cls("TimestampOutsideValidRange")
    
    @schemas.classproperty
    def TRANSFER_INTO_SAME_VAULT(cls):
        return cls("TransferIntoSameVault")
    
    @schemas.classproperty
    def CONFLICTING_VAULT_ASSETS(cls):
        return cls("ConflictingVaultAssets")
    
    @schemas.classproperty
    def FEE_ALREADY_CONFIGURED(cls):
        return cls("FeeAlreadyConfigured")
    
    @schemas.classproperty
    def MINTING_BLOB_INVALID(cls):
        return cls("MintingBlobInvalid")
    
    @schemas.classproperty
    def TOKEN_ID_INVALID(cls):
        return cls("TokenIdInvalid")
    
    @schemas.classproperty
    def TENANT_OWNER_UNAUTHORIZED(cls):
        return cls("TenantOwnerUnauthorized")
    
    @schemas.classproperty
    def INTERNAL_ERROR(cls):
        return cls("InternalError")
