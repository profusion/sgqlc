import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


shopify_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
shopify_schema -= sgqlc.types.relay.Node
shopify_schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class ARN(sgqlc.types.Scalar):
    __schema__ = shopify_schema


class AppInstallationCategory(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CHANNEL', 'POS_EMBEDDED')


class AppInstallationPrivacy(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('PRIVATE', 'PUBLIC')


class AppInstallationSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('APP_TITLE', 'ID', 'INSTALLED_AT', 'RELEVANCE')


class AppPricingInterval(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ANNUAL', 'EVERY_30_DAYS')


class AppPurchaseStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACCEPTED', 'ACTIVE', 'DECLINED', 'EXPIRED', 'PENDING')


class AppSubscriptionSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE')


class AppSubscriptionStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACCEPTED', 'ACTIVE', 'CANCELLED', 'DECLINED', 'EXPIRED', 'FROZEN', 'PENDING')


class AppTransactionSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE')


class AppUsageRecordSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE')


class AutomaticDiscountSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE')


Boolean = sgqlc.types.Boolean

class BulkOperationErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACCESS_DENIED', 'INTERNAL_SERVER_ERROR', 'TIMEOUT')


class BulkOperationStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'EXPIRED', 'FAILED', 'RUNNING')


class CodeDiscountSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ENDS_AT', 'ID', 'RELEVANCE', 'STARTS_AT', 'TITLE', 'UPDATED_AT')


class CollectionRuleColumn(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('IS_PRICE_REDUCED', 'TAG', 'TITLE', 'TYPE', 'VARIANT_COMPARE_AT_PRICE', 'VARIANT_INVENTORY', 'VARIANT_PRICE', 'VARIANT_TITLE', 'VARIANT_WEIGHT', 'VENDOR')


class CollectionRuleRelation(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CONTAINS', 'ENDS_WITH', 'EQUALS', 'GREATER_THAN', 'IS_NOT_SET', 'IS_SET', 'LESS_THAN', 'NOT_CONTAINS', 'NOT_EQUALS', 'STARTS_WITH')


class CollectionSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ID', 'RELEVANCE', 'TITLE', 'UPDATED_AT')


class CollectionSortOrder(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ALPHA_ASC', 'ALPHA_DESC', 'BEST_SELLING', 'CREATED', 'CREATED_DESC', 'MANUAL', 'PRICE_ASC', 'PRICE_DESC')


class CountryCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AN', 'AO', 'AR', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MK', 'ML', 'MM', 'MN', 'MO', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PS', 'PT', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VN', 'VU', 'WF', 'WS', 'XK', 'YE', 'YT', 'ZA', 'ZM', 'ZW')


class CropRegion(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('BOTTOM', 'CENTER', 'LEFT', 'RIGHT', 'TOP')


class CurrencyCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW')


class CustomerMarketingOptInLevel(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CONFIRMED_OPT_IN', 'SINGLE_OPT_IN', 'UNKNOWN')


class CustomerSavedSearchSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ID', 'NAME', 'RELEVANCE')


class CustomerSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ID', 'LAST_ORDER_DATE', 'LOCATION', 'NAME', 'ORDERS_COUNT', 'RELEVANCE', 'TOTAL_SPENT', 'UPDATED_AT')


class CustomerState(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('DECLINED', 'DISABLED', 'ENABLED', 'INVITED')


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

class DayOfTheWeek(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY')


class Decimal(sgqlc.types.Scalar):
    __schema__ = shopify_schema


class DeletionEventSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE')


class DeletionEventSubjectType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('COLLECTION', 'PRODUCT')


class DeliveryConditionField(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('TOTAL_PRICE', 'TOTAL_WEIGHT')


class DeliveryConditionOperator(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN_OR_EQUAL_TO')


class DeliveryLegacyModeBlockedReason(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('MULTI_LOCATION_DISABLED', 'NO_LOCATIONS_FULFILLING_ONLINE_ORDERS')


class DeliveryMethodDefinitionType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('MERCHANT', 'PARTICIPANT')


class DeliveryMethodType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('LOCAL', 'NONE', 'PICK_UP', 'RETAIL', 'SHIPPING')


class DigitalWallet(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ANDROID_PAY', 'APPLE_PAY', 'GOOGLE_PAY', 'SHOPIFY_PAY')


class DiscountApplicationAllocationMethod(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACROSS', 'EACH')


class DiscountApplicationLevel(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('LINE', 'ORDER')


class DiscountApplicationTargetSelection(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ALL', 'ENTITLED', 'EXPLICIT')


class DiscountApplicationTargetType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('LINE_ITEM', 'SHIPPING_LINE')


class DiscountCodeSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CODE', 'CREATED_AT', 'ID', 'RELEVANCE')


class DiscountErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACTIVE_PERIOD_OVERLAP', 'BLANK', 'CONFLICT', 'DUPLICATE', 'EQUAL_TO', 'EXCEEDED_MAX', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'IMPLICIT_DUPLICATE', 'INCLUSION', 'INTERNAL_ERROR', 'INVALID', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MINIMUM_SUBTOTAL_AND_QUANTITY_RANGE_BOTH_PRESENT', 'MISSING_ARGUMENT', 'PRESENT', 'TAKEN', 'TOO_LONG', 'TOO_MANY_ARGUMENTS', 'TOO_SHORT', 'VALUE_OUTSIDE_RANGE')


class DiscountShareableUrlTargetType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('COLLECTION', 'HOME', 'PRODUCT')


class DiscountStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACTIVE', 'EXPIRED', 'SCHEDULED')


class DisputeStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACCEPTED', 'CHARGE_REFUNDED', 'LOST', 'NEEDS_RESPONSE', 'UNDER_REVIEW', 'WON')


class DisputeType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CHARGEBACK', 'INQUIRY')


class DraftOrderAppliedDiscountType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('FIXED_AMOUNT', 'PERCENTAGE')


class DraftOrderSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CUSTOMER_NAME', 'ID', 'NUMBER', 'RELEVANCE', 'STATUS', 'TOTAL_PRICE', 'UPDATED_AT')


class DraftOrderStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('COMPLETED', 'INVOICE_SENT', 'OPEN')


class EventSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE')


Float = sgqlc.types.Float

class FormattedString(sgqlc.types.Scalar):
    __schema__ = shopify_schema


class FulfillmentDisplayStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ATTEMPTED_DELIVERY', 'CANCELED', 'CONFIRMED', 'DELIVERED', 'FAILURE', 'FULFILLED', 'IN_TRANSIT', 'LABEL_PRINTED', 'LABEL_PURCHASED', 'LABEL_VOIDED', 'MARKED_AS_FULFILLED', 'NOT_DELIVERED', 'OUT_FOR_DELIVERY', 'READY_FOR_PICKUP', 'SUBMITTED')


class FulfillmentEventSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('HAPPENED_AT', 'ID', 'RELEVANCE')


class FulfillmentEventStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ATTEMPTED_DELIVERY', 'CONFIRMED', 'DELIVERED', 'FAILURE', 'IN_TRANSIT', 'LABEL_PRINTED', 'LABEL_PURCHASED', 'OUT_FOR_DELIVERY', 'READY_FOR_PICKUP')


class FulfillmentOrderAction(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CANCEL_FULFILLMENT_ORDER', 'CREATE_FULFILLMENT', 'EXTERNAL', 'MOVE', 'REQUEST_CANCELLATION', 'REQUEST_FULFILLMENT')


class FulfillmentOrderAssignmentStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CANCELLATION_REQUESTED', 'FULFILLMENT_ACCEPTED', 'FULFILLMENT_REQUESTED')


class FulfillmentOrderMerchantRequestKind(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CANCELLATION_REQUEST', 'FULFILLMENT_REQUEST')


class FulfillmentOrderRequestStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACCEPTED', 'CANCELLATION_ACCEPTED', 'CANCELLATION_REJECTED', 'CANCELLATION_REQUESTED', 'CLOSED', 'REJECTED', 'SUBMITTED', 'UNSUBMITTED')


class FulfillmentOrderSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ID', 'RELEVANCE')


class FulfillmentOrderStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CANCELLED', 'CLOSED', 'INCOMPLETE', 'IN_PROGRESS', 'OPEN')


class FulfillmentServiceType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('GIFT_CARD', 'MANUAL', 'THIRD_PARTY')


class FulfillmentStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CANCELLED', 'ERROR', 'FAILURE', 'OPEN', 'PENDING', 'SUCCESS')


class HTML(sgqlc.types.Scalar):
    __schema__ = shopify_schema


ID = sgqlc.types.ID

class ImageContentType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('JPG', 'PNG', 'WEBP')


Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    __schema__ = shopify_schema


class KitSkillLocale(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('EN',)


class LocalizationExtensionPurpose(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('SHIPPING', 'TAX')


class LocationSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ID', 'NAME', 'RELEVANCE')


class MarketingActivityExtensionAppErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('API_ERROR', 'INSTALL_REQUIRED_ERROR', 'NOT_ONBOARDED_ERROR', 'PLATFORM_ERROR', 'VALIDATION_ERROR')


class MarketingActivitySortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE', 'TITLE')


class MarketingActivityStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACTIVE', 'DELETED', 'DELETED_EXTERNALLY', 'DISCONNECTED', 'DRAFT', 'FAILED', 'INACTIVE', 'PAUSED', 'PENDING', 'SCHEDULED', 'UNDEFINED')


class MarketingActivityStatusBadgeType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ATTENTION', 'DEFAULT', 'INFO', 'SUCCESS', 'WARNING')


class MarketingBudgetBudgetType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('DAILY', 'LIFETIME')


class MarketingChannel(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('DISPLAY', 'EMAIL', 'REFERRAL', 'SEARCH', 'SOCIAL')


class MarketingEventSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ID', 'RELEVANCE', 'STARTED_AT')


class MarketingTactic(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ABANDONED_CART', 'AD', 'AFFILIATE', 'DIRECT', 'LINK', 'LOYALTY', 'MESSAGE', 'NEWSLETTER', 'NOTIFICATION', 'POST', 'RETARGETING', 'SEO', 'STOREFRONT_APP', 'TRANSACTIONAL')


class MediaContentType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('EXTERNAL_VIDEO', 'IMAGE', 'MODEL_3D', 'VIDEO')


class MediaErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('EXTERNAL_VIDEO_INVALID_ASPECT_RATIO', 'EXTERNAL_VIDEO_NOT_FOUND', 'EXTERNAL_VIDEO_UNLISTED', 'IMAGE_DOWNLOAD_FAILURE', 'IMAGE_PROCESSING_FAILURE', 'INVALID_IMAGE_FILE_SIZE', 'INVALID_SIGNED_URL', 'MEDIA_TIMEOUT_ERROR', 'MODEL3D_GLB_OUTPUT_CREATION_ERROR', 'MODEL3D_GLB_TO_USDZ_CONVERSION_ERROR', 'MODEL3D_THUMBNAIL_GENERATION_ERROR', 'MODEL3D_VALIDATION_ERROR', 'UNKNOWN', 'UNSUPPORTED_IMAGE_FILE_TYPE', 'VIDEO_INVALID_FILETYPE_ERROR', 'VIDEO_MAX_DURATION_ERROR', 'VIDEO_MAX_HEIGHT_ERROR', 'VIDEO_MAX_WIDTH_ERROR', 'VIDEO_METADATA_READ_ERROR', 'VIDEO_MIN_DURATION_ERROR', 'VIDEO_MIN_HEIGHT_ERROR', 'VIDEO_MIN_WIDTH_ERROR', 'VIDEO_VALIDATION_ERROR')


class MediaPreviewImageStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('FAILED', 'PROCESSING', 'READY', 'UPLOADED')


class MediaStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('FAILED', 'PROCESSING', 'READY', 'UPLOADED')


class MediaUserErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('BLANK', 'INVALID', 'INVALID_MEDIA_TYPE', 'MAXIMUM_VARIANT_MEDIA_PAIRS_EXCEEDED', 'MEDIA_CANNOT_BE_MODIFIED', 'MEDIA_DOES_NOT_EXIST', 'MEDIA_DOES_NOT_EXIST_ON_PRODUCT', 'MEDIA_IS_NOT_ATTACHED_TO_VARIANT', 'MODEL3D_THROTTLE_EXCEEDED', 'MODEL3D_VALIDATION_ERROR', 'NON_READY_MEDIA', 'PRODUCT_DOES_NOT_EXIST', 'PRODUCT_MEDIA_LIMIT_EXCEEDED', 'PRODUCT_VARIANT_ALREADY_HAS_MEDIA', 'PRODUCT_VARIANT_DOES_NOT_EXIST_ON_PRODUCT', 'PRODUCT_VARIANT_SPECIFIED_MULTIPLE_TIMES', 'SHOP_MEDIA_LIMIT_EXCEEDED', 'TOO_MANY_MEDIA_PER_INPUT_PAIR', 'VIDEO_THROTTLE_EXCEEDED', 'VIDEO_VALIDATION_ERROR')


class MetafieldOwnerType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ARTICLE', 'BLOG', 'COLLECTION', 'CUSTOMER', 'DRAFTORDER', 'ORDER', 'PAGE', 'PRODUCT', 'PRODUCTIMAGE', 'PRODUCTVARIANT', 'SHOP')


class MetafieldValueType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('INTEGER', 'JSON_STRING', 'STRING')


class MethodDefinitionSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ID', 'RATE_PROVIDER_TYPE', 'RELEVANCE')


class Money(sgqlc.types.Scalar):
    __schema__ = shopify_schema


class OrderCancelReason(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CUSTOMER', 'DECLINED', 'FRAUD', 'INVENTORY', 'OTHER')


class OrderDisplayFinancialStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('AUTHORIZED', 'PAID', 'PARTIALLY_PAID', 'PARTIALLY_REFUNDED', 'PENDING', 'REFUNDED', 'VOIDED')


class OrderDisplayFulfillmentStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('FULFILLED', 'IN_PROGRESS', 'OPEN', 'PARTIALLY_FULFILLED', 'PENDING_FULFILLMENT', 'RESTOCKED', 'UNFULFILLED')


class OrderRiskLevel(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('HIGH', 'LOW', 'MEDIUM')


class OrderSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'CUSTOMER_NAME', 'FINANCIAL_STATUS', 'FULFILLMENT_STATUS', 'ID', 'ORDER_NUMBER', 'PROCESSED_AT', 'RELEVANCE', 'TOTAL_PRICE', 'UPDATED_AT')


class OrderTransactionErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('AMAZON_PAYMENTS_INVALID_PAYMENT_METHOD', 'AMAZON_PAYMENTS_MAX_AMOUNT_CHARGED', 'AMAZON_PAYMENTS_MAX_AMOUNT_REFUNDED', 'AMAZON_PAYMENTS_MAX_AUTHORIZATIONS_CAPTURED', 'AMAZON_PAYMENTS_MAX_REFUNDS_PROCESSED', 'AMAZON_PAYMENTS_ORDER_REFERENCE_CANCELED', 'AMAZON_PAYMENTS_STALE', 'CALL_ISSUER', 'CARD_DECLINED', 'CONFIG_ERROR', 'EXPIRED_CARD', 'GENERIC_ERROR', 'INCORRECT_ADDRESS', 'INCORRECT_CVC', 'INCORRECT_NUMBER', 'INCORRECT_PIN', 'INCORRECT_ZIP', 'INVALID_AMOUNT', 'INVALID_COUNTRY', 'INVALID_CVC', 'INVALID_EXPIRY_DATE', 'INVALID_NUMBER', 'PAYMENT_METHOD_UNAVAILABLE', 'PICK_UP_CARD', 'PROCESSING_ERROR', 'TEST_MODE_LIVE_CARD', 'UNSUPPORTED_FEATURE')


class OrderTransactionKind(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('AUTHORIZATION', 'CAPTURE', 'CHANGE', 'EMV_AUTHORIZATION', 'REFUND', 'SALE', 'SUGGESTED_REFUND', 'VOID')


class OrderTransactionStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('AWAITING_RESPONSE', 'ERROR', 'FAILURE', 'PENDING', 'SUCCESS', 'UNKNOWN')


class PaymentMethods(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('AMERICAN_EXPRESS', 'BITCOIN', 'BOGUS', 'DANKORT', 'DINERS_CLUB', 'DISCOVER', 'DOGECOIN', 'FORBRUGSFORENINGEN', 'JCB', 'LITECOIN', 'MAESTRO', 'MASTERCARD', 'PAYPAL', 'VISA')


class PriceRuleAllocationMethod(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACROSS', 'EACH')


class PriceRuleErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ALLOCATION_METHOD_MUST_BE_ACROSS_FOR_GIVEN_TARGET_SELECTION', 'BLANK', 'BOGO_INVALID_TARGET_SELECTION', 'BOGO_INVALID_TARGET_TYPE', 'BOGO_INVALID_VALUE_TYPE', 'BOTH_CUSTOMER_AND_SAVED_SEARCH_PREREQUISITES_SELECTED', 'CANNOT_ENTITLE_COLLECTIONS_WITH_PRODUCTS_OR_VARIANTS', 'CANNOT_PREREQUISITE_COLLECTION_WITH_PRODUCT_OR_VARIANTS', 'CUSTOMER_PREREQUISITES_EXCEEDED_MAX', 'CUSTOMER_PREREQUISITES_INVALID_SELECTION', 'CUSTOMER_PREREQUISITES_MISSING', 'CUSTOMER_PREREQUISITE_DUPLICATE', 'CUSTOMER_SAVED_SEARCH_DUPLICATE', 'CUSTOMER_SAVED_SEARCH_EXCEEDED_MAX', 'CUSTOMER_SAVED_SEARCH_INVALID', 'DISCOUNT_CODE_DUPLICATE', 'END_DATE_BEFORE_START_DATE', 'EQUAL_TO', 'EXCEEDED_MAX', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'INTERNAL_ERROR', 'INVALID', 'INVALID_TARGET_TYPE_PREREQUISITE_SHIPPING_PRICE_RANGE', 'ITEM_ENTITLEMENTS_DUPLICATE_COLLECTION', 'ITEM_ENTITLEMENTS_DUPLICATE_PRODUCT', 'ITEM_ENTITLEMENTS_DUPLICATE_VARIANT', 'ITEM_ENTITLEMENTS_EXCEEDED_MAX_COLLECTION', 'ITEM_ENTITLEMENTS_EXCEEDED_MAX_PRODUCT', 'ITEM_ENTITLEMENTS_EXCEEDED_MAX_VARIANT', 'ITEM_ENTITLEMENTS_INVALID_COLLECTION', 'ITEM_ENTITLEMENTS_INVALID_PRODUCT', 'ITEM_ENTITLEMENTS_INVALID_TARGET_TYPE_OR_SELECTION', 'ITEM_ENTITLEMENTS_INVALID_VARIANT', 'ITEM_ENTITLEMENTS_MISSING', 'ITEM_ENTITLEMENT_INVALID_TYPE', 'ITEM_PREREQUISITES_DUPLICATE_COLLECTION', 'ITEM_PREREQUISITES_DUPLICATE_PRODUCT', 'ITEM_PREREQUISITES_DUPLICATE_VARIANT', 'ITEM_PREREQUISITES_EXCEEDED_MAX', 'ITEM_PREREQUISITES_INVALID_COLLECTION', 'ITEM_PREREQUISITES_INVALID_PRODUCT', 'ITEM_PREREQUISITES_INVALID_TYPE', 'ITEM_PREREQUISITES_INVALID_VARIANT', 'ITEM_PREREQUISITES_MISSING', 'ITEM_PREREQUISITES_MUST_BE_EMPTY', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MISSING_ARGUMENT', 'PREREQUISITE_SUBTOTAL_AND_QUANTITY_RANGE_BOTH_PRESENT', 'PRICE_RULE_ALLOCATION_LIMIT_IS_ZERO', 'PRICE_RULE_ALLOCATION_LIMIT_ON_NON_BOGO', 'PRICE_RULE_EXCEEDED_MAX_DISCOUNT_CODE', 'PRICE_RULE_PERCENTAGE_VALUE_OUTSIDE_RANGE', 'SHIPPING_ENTITLEMENTS_DUPLICATE_COUNTRY', 'SHIPPING_ENTITLEMENTS_EXCEEDED_MAX', 'SHIPPING_ENTITLEMENTS_INVALID_COUNTRY', 'SHIPPING_ENTITLEMENTS_INVALID_TARGET_TYPE_OR_SELECTION', 'SHIPPING_ENTITLEMENTS_MISSING', 'SHIPPING_ENTITLEMENTS_UNSUPPORTED_DESTINATION_TYPE', 'SHOP_EXCEEDED_MAX_PRICE_RULES', 'TAKEN', 'TOO_LONG', 'TOO_MANY_ARGUMENTS', 'TOO_SHORT', 'VARIANT_ALREADY_ENTITLED_THROUGH_PRODUCT')


class PriceRuleFeature(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('BULK', 'BUY_ONE_GET_ONE', 'BUY_ONE_GET_ONE_WITH_ALLOCATION_LIMIT', 'QUANTITY_DISCOUNTS', 'SPECIFIC_CUSTOMERS')


class PriceRuleShareableUrlTargetType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('COLLECTION', 'HOME', 'PRODUCT')


class PriceRuleSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ENDS_AT', 'ID', 'RELEVANCE', 'STARTS_AT', 'TITLE', 'UPDATED_AT')


class PriceRuleStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACTIVE', 'EXPIRED', 'SCHEDULED')


class PriceRuleTarget(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('LINE_ITEM', 'SHIPPING_LINE')


class PriceRuleTrait(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('BULK', 'BUY_ONE_GET_ONE', 'BUY_ONE_GET_ONE_WITH_ALLOCATION_LIMIT', 'QUANTITY_DISCOUNTS', 'SPECIFIC_CUSTOMERS')


class PrivateMetafieldValueType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('INTEGER', 'JSON_STRING', 'STRING')


class ProductChangeStatusUserErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('PRODUCT_NOT_FOUND',)


class ProductCollectionSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('BEST_SELLING', 'COLLECTION_DEFAULT', 'CREATED', 'ID', 'MANUAL', 'PRICE', 'RELEVANCE', 'TITLE')


class ProductImageSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'POSITION', 'RELEVANCE')


class ProductMediaSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ID', 'POSITION', 'RELEVANCE')


class ProductSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'INVENTORY_TOTAL', 'PRODUCT_TYPE', 'PUBLISHED_AT', 'RELEVANCE', 'TITLE', 'UPDATED_AT', 'VENDOR')


class ProductStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ACTIVE', 'ARCHIVED', 'DRAFT')


class ProductVariantInventoryManagement(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('FULFILLMENT_SERVICE', 'NOT_MANAGED', 'SHOPIFY')


class ProductVariantInventoryPolicy(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CONTINUE', 'DENY')


class ProductVariantSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('FULL_TITLE', 'ID', 'INVENTORY_LEVELS_AVAILABLE', 'INVENTORY_MANAGEMENT', 'INVENTORY_POLICY', 'INVENTORY_QUANTITY', 'NAME', 'POPULAR', 'POSITION', 'RELEVANCE', 'SKU', 'TITLE')


class ProfileItemSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'INVENTORY_TOTAL', 'PRODUCT_TYPE', 'PUBLISHED_AT', 'RELEVANCE', 'TITLE', 'UPDATED_AT', 'VENDOR')


class RefundDutyRefundType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('FULL', 'PROPORTIONAL')


class RefundLineItemRestockType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CANCEL', 'LEGACY_RESTOCK', 'NO_RESTOCK', 'RETURN')


class ResourceAlertIcon(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CHECKMARK_CIRCLE', 'INFORMATION_CIRCLE')


class ResourceAlertSeverity(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CRITICAL', 'DEFAULT', 'INFO', 'SUCCESS', 'WARNING')


class ScriptTagDisplayScope(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ALL', 'ONLINE_STORE', 'ORDER_STATUS')


class SearchResultType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('COLLECTION', 'CUSTOMER', 'DISCOUNT_REDEEM_CODE', 'DRAFT_ORDER', 'ONLINE_STORE_ARTICLE', 'ONLINE_STORE_BLOG', 'ONLINE_STORE_PAGE', 'ORDER', 'PRICE_RULE', 'PRODUCT')


class ShopBranding(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ROGERS', 'SHOPIFY', 'SHOPIFY_GOLD', 'SHOPIFY_PLUS')


class ShopCustomerAccountsSetting(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('DISABLED', 'OPTIONAL', 'REQUIRED')


class ShopImageSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE')


class ShopPolicyErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('TOO_BIG',)


class ShopPolicyType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('LEGAL_NOTICE', 'PRIVACY_POLICY', 'REFUND_POLICY', 'SHIPPING_POLICY', 'TERMS_OF_SALE', 'TERMS_OF_SERVICE')


class ShopTagSort(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ALPHABETICAL', 'POPULAR')


class ShopifyPaymentsBankAccountStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('ERRORED', 'NEW', 'VALIDATED', 'VERIFIED')


class ShopifyPaymentsDisputeReason(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('BANK_CANNOT_PROCESS', 'CREDIT_NOT_PROCESSED', 'CUSTOMER_INITIATED', 'DEBIT_NOT_AUTHORIZED', 'DUPLICATE', 'FRAUDULENT', 'GENERAL', 'INCORRECT_ACCOUNT_DETAILS', 'INSUFFICIENT_FUNDS', 'PRODUCT_NOT_RECEIVED', 'PRODUCT_UNACCEPTABLE', 'SUBSCRIPTION_CANCELLED', 'UNRECOGNIZED')


class ShopifyPaymentsPayoutInterval(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('DAILY', 'MANUAL', 'MONTHLY', 'WEEKLY')


class ShopifyPaymentsPayoutStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CANCELED', 'FAILED', 'IN_TRANSIT', 'PAID', 'SCHEDULED')


class ShopifyPaymentsPayoutTransactionType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('DEPOSIT', 'WITHDRAWAL')


class ShopifyPaymentsVerificationDocumentType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('DRIVERS_LICENSE', 'GOVERNMENT_IDENTIFICATION', 'PASSPORT')


class ShopifyPaymentsVerificationStatus(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('PENDING', 'UNVERIFIED', 'VERIFIED')


class StagedUploadHttpMethodType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('POST', 'PUT')


class StagedUploadTargetGenerateUploadResource(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('COLLECTION_IMAGE', 'IMAGE', 'MODEL_3D', 'PRODUCT_IMAGE', 'SHOP_IMAGE', 'TIMELINE', 'VIDEO')


class StorefrontID(sgqlc.types.Scalar):
    __schema__ = shopify_schema


String = sgqlc.types.String

class SuggestedOrderTransactionKind(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('SUGGESTED_REFUND',)


class TaxExemption(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CA_BC_COMMERCIAL_FISHERY_EXEMPTION', 'CA_BC_CONTRACTOR_EXEMPTION', 'CA_BC_PRODUCTION_AND_MACHINERY_EXEMPTION', 'CA_BC_RESELLER_EXEMPTION', 'CA_BC_SUB_CONTRACTOR_EXEMPTION', 'CA_DIPLOMAT_EXEMPTION', 'CA_MB_COMMERCIAL_FISHERY_EXEMPTION', 'CA_MB_FARMER_EXEMPTION', 'CA_MB_RESELLER_EXEMPTION', 'CA_NS_COMMERCIAL_FISHERY_EXEMPTION', 'CA_NS_FARMER_EXEMPTION', 'CA_ON_PURCHASE_EXEMPTION', 'CA_PE_COMMERCIAL_FISHERY_EXEMPTION', 'CA_SK_COMMERCIAL_FISHERY_EXEMPTION', 'CA_SK_CONTRACTOR_EXEMPTION', 'CA_SK_FARMER_EXEMPTION', 'CA_SK_PRODUCTION_AND_MACHINERY_EXEMPTION', 'CA_SK_RESELLER_EXEMPTION', 'CA_SK_SUB_CONTRACTOR_EXEMPTION', 'CA_STATUS_CARD_EXEMPTION')


class TranslatableResourceType(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('COLLECTION', 'DELIVERY_METHOD_DEFINITION', 'EMAIL_TEMPLATE', 'LINK', 'METAFIELD', 'ONLINE_STORE_ARTICLE', 'ONLINE_STORE_BLOG', 'ONLINE_STORE_PAGE', 'ONLINE_STORE_THEME', 'PAYMENT_GATEWAY', 'PRODUCT', 'PRODUCT_OPTION', 'PRODUCT_VARIANT', 'SHOP', 'SHOP_POLICY', 'SMS_TEMPLATE')


class TranslationErrorCode(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('BLANK', 'FAILS_RESOURCE_VALIDATION', 'INVALID', 'INVALID_CODE', 'INVALID_FORMAT', 'INVALID_KEY_FOR_MODEL', 'INVALID_LOCALE_FOR_SHOP', 'INVALID_TRANSLATABLE_CONTENT', 'RESOURCE_NOT_FOUND', 'TOO_MANY_KEYS_FOR_RESOURCE')


class URL(sgqlc.types.Scalar):
    __schema__ = shopify_schema


class UnitSystem(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('IMPERIAL_SYSTEM', 'METRIC_SYSTEM')


class UnsignedInt64(sgqlc.types.Scalar):
    __schema__ = shopify_schema


class UtcOffset(sgqlc.types.Scalar):
    __schema__ = shopify_schema


class WebhookSubscriptionFormat(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('JSON', 'XML')


class WebhookSubscriptionSortKeys(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('CREATED_AT', 'ID', 'RELEVANCE')


class WebhookSubscriptionTopic(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('APP_PURCHASES_ONE_TIME_UPDATE', 'APP_SUBSCRIPTIONS_UPDATE', 'APP_UNINSTALLED', 'ATTRIBUTED_SESSIONS_FIRST', 'ATTRIBUTED_SESSIONS_LAST', 'ATTRIBUTION_RISK', 'CARTS_CREATE', 'CARTS_UPDATE', 'CHANNELS_DELETE', 'CHECKOUTS_CREATE', 'CHECKOUTS_DELETE', 'CHECKOUTS_UPDATE', 'COLLECTIONS_CREATE', 'COLLECTIONS_DELETE', 'COLLECTIONS_UPDATE', 'COLLECTION_LISTINGS_ADD', 'COLLECTION_LISTINGS_REMOVE', 'COLLECTION_LISTINGS_UPDATE', 'COLLECTION_PUBLICATIONS_CREATE', 'COLLECTION_PUBLICATIONS_DELETE', 'COLLECTION_PUBLICATIONS_UPDATE', 'CUSTOMERS_CREATE', 'CUSTOMERS_DELETE', 'CUSTOMERS_DISABLE', 'CUSTOMERS_ENABLE', 'CUSTOMERS_UPDATE', 'CUSTOMER_GROUPS_CREATE', 'CUSTOMER_GROUPS_DELETE', 'CUSTOMER_GROUPS_UPDATE', 'DISPUTES_CREATE', 'DISPUTES_UPDATE', 'DOMAINS_CREATE', 'DOMAINS_DESTROY', 'DOMAINS_UPDATE', 'DRAFT_ORDERS_CREATE', 'DRAFT_ORDERS_DELETE', 'DRAFT_ORDERS_UPDATE', 'FULFILLMENTS_CREATE', 'FULFILLMENTS_UPDATE', 'FULFILLMENT_EVENTS_CREATE', 'FULFILLMENT_EVENTS_DELETE', 'INVENTORY_ITEMS_CREATE', 'INVENTORY_ITEMS_DELETE', 'INVENTORY_ITEMS_UPDATE', 'INVENTORY_LEVELS_CONNECT', 'INVENTORY_LEVELS_DISCONNECT', 'INVENTORY_LEVELS_UPDATE', 'LOCALES_CREATE', 'LOCALES_UPDATE', 'LOCATIONS_CREATE', 'LOCATIONS_DELETE', 'LOCATIONS_UPDATE', 'ORDERS_CANCELLED', 'ORDERS_CREATE', 'ORDERS_DELETE', 'ORDERS_EDITED', 'ORDERS_FULFILLED', 'ORDERS_PAID', 'ORDERS_PARTIALLY_FULFILLED', 'ORDERS_UPDATED', 'ORDER_TRANSACTIONS_CREATE', 'PRODUCTS_CREATE', 'PRODUCTS_DELETE', 'PRODUCTS_UPDATE', 'PRODUCT_LISTINGS_ADD', 'PRODUCT_LISTINGS_REMOVE', 'PRODUCT_LISTINGS_UPDATE', 'PRODUCT_PUBLICATIONS_CREATE', 'PRODUCT_PUBLICATIONS_DELETE', 'PRODUCT_PUBLICATIONS_UPDATE', 'PROFILES_CREATE', 'PROFILES_DELETE', 'PROFILES_UPDATE', 'REFUNDS_CREATE', 'SHIPPING_ADDRESSES_CREATE', 'SHIPPING_ADDRESSES_UPDATE', 'SHOP_UPDATE', 'TAX_SERVICES_CREATE', 'TAX_SERVICES_UPDATE', 'TENDER_TRANSACTIONS_CREATE', 'THEMES_CREATE', 'THEMES_DELETE', 'THEMES_PUBLISH', 'THEMES_UPDATE', 'VARIANTS_IN_STOCK', 'VARIANTS_OUT_OF_STOCK')


class WeightUnit(sgqlc.types.Enum):
    __schema__ = shopify_schema
    __choices__ = ('GRAMS', 'KILOGRAMS', 'OUNCES', 'POUNDS')



########################################################################
# Input Objects
########################################################################
class AppPlanInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('app_usage_pricing_details', 'app_recurring_pricing_details')
    app_usage_pricing_details = sgqlc.types.Field('AppUsagePricingInput', graphql_name='appUsagePricingDetails')
    app_recurring_pricing_details = sgqlc.types.Field('AppRecurringPricingInput', graphql_name='appRecurringPricingDetails')


class AppRecurringPricingInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('interval', 'price')
    interval = sgqlc.types.Field(AppPricingInterval, graphql_name='interval')
    price = sgqlc.types.Field(sgqlc.types.non_null('MoneyInput'), graphql_name='price')


class AppSubscriptionLineItemInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('plan',)
    plan = sgqlc.types.Field(sgqlc.types.non_null(AppPlanInput), graphql_name='plan')


class AppUsagePricingInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('capped_amount', 'terms')
    capped_amount = sgqlc.types.Field(sgqlc.types.non_null('MoneyInput'), graphql_name='cappedAmount')
    terms = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='terms')


class AttributeInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class CollectionDeleteInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class CollectionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('description_html', 'handle', 'id', 'image', 'products', 'publications', 'private_metafields', 'rule_set', 'template_suffix', 'sort_order', 'title', 'metafields', 'seo', 'redirect_new_handle')
    description_html = sgqlc.types.Field(String, graphql_name='descriptionHtml')
    handle = sgqlc.types.Field(String, graphql_name='handle')
    id = sgqlc.types.Field(ID, graphql_name='id')
    image = sgqlc.types.Field('ImageInput', graphql_name='image')
    products = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='products')
    publications = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CollectionPublicationInput')), graphql_name='publications')
    private_metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PrivateMetafieldInput')), graphql_name='privateMetafields')
    rule_set = sgqlc.types.Field('CollectionRuleSetInput', graphql_name='ruleSet')
    template_suffix = sgqlc.types.Field(String, graphql_name='templateSuffix')
    sort_order = sgqlc.types.Field(CollectionSortOrder, graphql_name='sortOrder')
    title = sgqlc.types.Field(String, graphql_name='title')
    metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MetafieldInput')), graphql_name='metafields')
    seo = sgqlc.types.Field('SEOInput', graphql_name='seo')
    redirect_new_handle = sgqlc.types.Field(Boolean, graphql_name='redirectNewHandle')


class CollectionPublicationInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('publication_id', 'channel_id', 'channel_handle')
    publication_id = sgqlc.types.Field(ID, graphql_name='publicationId')
    channel_id = sgqlc.types.Field(ID, graphql_name='channelId')
    channel_handle = sgqlc.types.Field(String, graphql_name='channelHandle')


class CollectionPublishInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'collection_publications')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    collection_publications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CollectionPublicationInput))), graphql_name='collectionPublications')


class CollectionRuleInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('column', 'relation', 'condition')
    column = sgqlc.types.Field(sgqlc.types.non_null(CollectionRuleColumn), graphql_name='column')
    relation = sgqlc.types.Field(sgqlc.types.non_null(CollectionRuleRelation), graphql_name='relation')
    condition = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='condition')


class CollectionRuleSetInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('applied_disjunctively', 'rules')
    applied_disjunctively = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='appliedDisjunctively')
    rules = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CollectionRuleInput)), graphql_name='rules')


class CollectionUnpublishInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'collection_publications')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    collection_publications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CollectionPublicationInput))), graphql_name='collectionPublications')


class CountryHarmonizedSystemCodeInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('harmonized_system_code', 'country_code')
    harmonized_system_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='harmonizedSystemCode')
    country_code = sgqlc.types.Field(sgqlc.types.non_null(CountryCode), graphql_name='countryCode')


class CreateMediaInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('original_source', 'alt', 'media_content_type')
    original_source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='originalSource')
    alt = sgqlc.types.Field(String, graphql_name='alt')
    media_content_type = sgqlc.types.Field(sgqlc.types.non_null(MediaContentType), graphql_name='mediaContentType')


class CustomerDeleteInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class CustomerInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('accepts_marketing', 'accepts_marketing_updated_at', 'addresses', 'email', 'first_name', 'id', 'last_name', 'locale', 'marketing_opt_in_level', 'metafields', 'note', 'phone', 'private_metafields', 'tags', 'tax_exempt', 'tax_exemptions')
    accepts_marketing = sgqlc.types.Field(Boolean, graphql_name='acceptsMarketing')
    accepts_marketing_updated_at = sgqlc.types.Field(DateTime, graphql_name='acceptsMarketingUpdatedAt')
    addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MailingAddressInput')), graphql_name='addresses')
    email = sgqlc.types.Field(String, graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    id = sgqlc.types.Field(ID, graphql_name='id')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    locale = sgqlc.types.Field(String, graphql_name='locale')
    marketing_opt_in_level = sgqlc.types.Field(CustomerMarketingOptInLevel, graphql_name='marketingOptInLevel')
    metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MetafieldInput')), graphql_name='metafields')
    note = sgqlc.types.Field(String, graphql_name='note')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    private_metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PrivateMetafieldInput')), graphql_name='privateMetafields')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    tax_exempt = sgqlc.types.Field(Boolean, graphql_name='taxExempt')
    tax_exemptions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TaxExemption)), graphql_name='taxExemptions')


class DeliveryCountryInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('code', 'rest_of_world', 'provinces', 'include_all_provinces')
    code = sgqlc.types.Field(CountryCode, graphql_name='code')
    rest_of_world = sgqlc.types.Field(Boolean, graphql_name='restOfWorld')
    provinces = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryProvinceInput')), graphql_name='provinces')
    include_all_provinces = sgqlc.types.Field(Boolean, graphql_name='includeAllProvinces')


class DeliveryLocationGroupZoneInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'name', 'countries', 'method_definitions_to_create', 'method_definitions_to_update')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryCountryInput)), graphql_name='countries')
    method_definitions_to_create = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryMethodDefinitionInput')), graphql_name='methodDefinitionsToCreate')
    method_definitions_to_update = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryMethodDefinitionInput')), graphql_name='methodDefinitionsToUpdate')


class DeliveryMethodDefinitionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'name', 'description', 'active', 'rate_definition', 'participant', 'weight_conditions_to_create', 'price_conditions_to_create', 'conditions_to_update')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    rate_definition = sgqlc.types.Field('DeliveryRateDefinitionInput', graphql_name='rateDefinition')
    participant = sgqlc.types.Field('DeliveryParticipantInput', graphql_name='participant')
    weight_conditions_to_create = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryWeightConditionInput')), graphql_name='weightConditionsToCreate')
    price_conditions_to_create = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryPriceConditionInput')), graphql_name='priceConditionsToCreate')
    conditions_to_update = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryUpdateConditionInput')), graphql_name='conditionsToUpdate')


class DeliveryParticipantInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'carrier_service_id', 'fixed_fee', 'percentage_of_rate_fee', 'participant_services', 'adapt_to_new_services')
    id = sgqlc.types.Field(ID, graphql_name='id')
    carrier_service_id = sgqlc.types.Field(ID, graphql_name='carrierServiceId')
    fixed_fee = sgqlc.types.Field('MoneyInput', graphql_name='fixedFee')
    percentage_of_rate_fee = sgqlc.types.Field(Float, graphql_name='percentageOfRateFee')
    participant_services = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryParticipantServiceInput')), graphql_name='participantServices')
    adapt_to_new_services = sgqlc.types.Field(Boolean, graphql_name='adaptToNewServices')


class DeliveryParticipantServiceInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('name', 'active')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')


class DeliveryPriceConditionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('criteria', 'operator')
    criteria = sgqlc.types.Field('MoneyInput', graphql_name='criteria')
    operator = sgqlc.types.Field(DeliveryConditionOperator, graphql_name='operator')


class DeliveryProfileInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('name', 'profile_location_groups', 'location_groups_to_create', 'location_groups_to_update', 'location_groups_to_delete', 'variants_to_associate', 'variants_to_dissociate', 'zones_to_delete', 'method_definitions_to_delete', 'conditions_to_delete')
    name = sgqlc.types.Field(String, graphql_name='name')
    profile_location_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryProfileLocationGroupInput')), graphql_name='profileLocationGroups')
    location_groups_to_create = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryProfileLocationGroupInput')), graphql_name='locationGroupsToCreate')
    location_groups_to_update = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryProfileLocationGroupInput')), graphql_name='locationGroupsToUpdate')
    location_groups_to_delete = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='locationGroupsToDelete')
    variants_to_associate = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='variantsToAssociate')
    variants_to_dissociate = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='variantsToDissociate')
    zones_to_delete = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='zonesToDelete')
    method_definitions_to_delete = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='methodDefinitionsToDelete')
    conditions_to_delete = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='conditionsToDelete')


class DeliveryProfileLocationGroupInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'locations', 'zones_to_create', 'zones_to_update')
    id = sgqlc.types.Field(ID, graphql_name='id')
    locations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='locations')
    zones_to_create = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryLocationGroupZoneInput)), graphql_name='zonesToCreate')
    zones_to_update = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryLocationGroupZoneInput)), graphql_name='zonesToUpdate')


class DeliveryProvinceInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')


class DeliveryRateDefinitionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'price')
    id = sgqlc.types.Field(ID, graphql_name='id')
    price = sgqlc.types.Field(sgqlc.types.non_null('MoneyInput'), graphql_name='price')


class DeliverySettingInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('legacy_mode_profiles',)
    legacy_mode_profiles = sgqlc.types.Field(Boolean, graphql_name='legacyModeProfiles')


class DeliveryUpdateConditionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'criteria', 'criteria_unit', 'field', 'operator')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    criteria = sgqlc.types.Field(Float, graphql_name='criteria')
    criteria_unit = sgqlc.types.Field(String, graphql_name='criteriaUnit')
    field = sgqlc.types.Field(DeliveryConditionField, graphql_name='field')
    operator = sgqlc.types.Field(DeliveryConditionOperator, graphql_name='operator')


class DeliveryWeightConditionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('criteria', 'operator')
    criteria = sgqlc.types.Field('WeightInput', graphql_name='criteria')
    operator = sgqlc.types.Field(DeliveryConditionOperator, graphql_name='operator')


class DiscountAmountInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'applies_on_each_item')
    amount = sgqlc.types.Field(Decimal, graphql_name='amount')
    applies_on_each_item = sgqlc.types.Field(Boolean, graphql_name='appliesOnEachItem')


class DiscountAutomaticBasicInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('title', 'starts_at', 'ends_at', 'minimum_requirement', 'customer_gets')
    title = sgqlc.types.Field(String, graphql_name='title')
    starts_at = sgqlc.types.Field(DateTime, graphql_name='startsAt')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    minimum_requirement = sgqlc.types.Field('DiscountMinimumRequirementInput', graphql_name='minimumRequirement')
    customer_gets = sgqlc.types.Field('DiscountCustomerGetsInput', graphql_name='customerGets')


class DiscountAutomaticBxgyInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('starts_at', 'ends_at', 'title', 'uses_per_order_limit', 'customer_buys', 'customer_gets')
    starts_at = sgqlc.types.Field(DateTime, graphql_name='startsAt')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    title = sgqlc.types.Field(String, graphql_name='title')
    uses_per_order_limit = sgqlc.types.Field(UnsignedInt64, graphql_name='usesPerOrderLimit')
    customer_buys = sgqlc.types.Field('DiscountCustomerBuysInput', graphql_name='customerBuys')
    customer_gets = sgqlc.types.Field('DiscountCustomerGetsInput', graphql_name='customerGets')


class DiscountCodeBasicInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('title', 'starts_at', 'ends_at', 'usage_limit', 'applies_once_per_customer', 'minimum_requirement', 'customer_gets', 'customer_selection', 'code')
    title = sgqlc.types.Field(String, graphql_name='title')
    starts_at = sgqlc.types.Field(DateTime, graphql_name='startsAt')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    usage_limit = sgqlc.types.Field(Int, graphql_name='usageLimit')
    applies_once_per_customer = sgqlc.types.Field(Boolean, graphql_name='appliesOncePerCustomer')
    minimum_requirement = sgqlc.types.Field('DiscountMinimumRequirementInput', graphql_name='minimumRequirement')
    customer_gets = sgqlc.types.Field('DiscountCustomerGetsInput', graphql_name='customerGets')
    customer_selection = sgqlc.types.Field('DiscountCustomerSelectionInput', graphql_name='customerSelection')
    code = sgqlc.types.Field(String, graphql_name='code')


class DiscountCodeBxgyInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('title', 'starts_at', 'ends_at', 'customer_buys', 'customer_gets', 'customer_selection', 'code', 'usage_limit', 'uses_per_order_limit', 'applies_once_per_customer')
    title = sgqlc.types.Field(String, graphql_name='title')
    starts_at = sgqlc.types.Field(DateTime, graphql_name='startsAt')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    customer_buys = sgqlc.types.Field('DiscountCustomerBuysInput', graphql_name='customerBuys')
    customer_gets = sgqlc.types.Field('DiscountCustomerGetsInput', graphql_name='customerGets')
    customer_selection = sgqlc.types.Field('DiscountCustomerSelectionInput', graphql_name='customerSelection')
    code = sgqlc.types.Field(String, graphql_name='code')
    usage_limit = sgqlc.types.Field(Int, graphql_name='usageLimit')
    uses_per_order_limit = sgqlc.types.Field(Int, graphql_name='usesPerOrderLimit')
    applies_once_per_customer = sgqlc.types.Field(Boolean, graphql_name='appliesOncePerCustomer')


class DiscountCodeFreeShippingInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('title', 'starts_at', 'ends_at', 'code', 'usage_limit', 'applies_once_per_customer', 'minimum_requirement', 'customer_selection', 'destination', 'maximum_shipping_price')
    title = sgqlc.types.Field(String, graphql_name='title')
    starts_at = sgqlc.types.Field(DateTime, graphql_name='startsAt')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    code = sgqlc.types.Field(String, graphql_name='code')
    usage_limit = sgqlc.types.Field(Int, graphql_name='usageLimit')
    applies_once_per_customer = sgqlc.types.Field(Boolean, graphql_name='appliesOncePerCustomer')
    minimum_requirement = sgqlc.types.Field('DiscountMinimumRequirementInput', graphql_name='minimumRequirement')
    customer_selection = sgqlc.types.Field('DiscountCustomerSelectionInput', graphql_name='customerSelection')
    destination = sgqlc.types.Field('DiscountShippingDestinationSelectionInput', graphql_name='destination')
    maximum_shipping_price = sgqlc.types.Field(Decimal, graphql_name='maximumShippingPrice')


class DiscountCollectionsInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('add', 'remove')
    add = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='add')
    remove = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='remove')


class DiscountCountriesInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('add', 'remove', 'include_rest_of_world')
    add = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode)), graphql_name='add')
    remove = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode)), graphql_name='remove')
    include_rest_of_world = sgqlc.types.Field(Boolean, graphql_name='includeRestOfWorld')


class DiscountCustomerBuysInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('value', 'items')
    value = sgqlc.types.Field('DiscountCustomerBuysValueInput', graphql_name='value')
    items = sgqlc.types.Field('DiscountItemsInput', graphql_name='items')


class DiscountCustomerBuysValueInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('quantity', 'amount')
    quantity = sgqlc.types.Field(UnsignedInt64, graphql_name='quantity')
    amount = sgqlc.types.Field(Decimal, graphql_name='amount')


class DiscountCustomerGetsInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('value', 'items')
    value = sgqlc.types.Field('DiscountCustomerGetsValueInput', graphql_name='value')
    items = sgqlc.types.Field('DiscountItemsInput', graphql_name='items')


class DiscountCustomerGetsValueInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('discount_on_quantity', 'percentage', 'discount_amount')
    discount_on_quantity = sgqlc.types.Field('DiscountOnQuantityInput', graphql_name='discountOnQuantity')
    percentage = sgqlc.types.Field(Float, graphql_name='percentage')
    discount_amount = sgqlc.types.Field(DiscountAmountInput, graphql_name='discountAmount')


class DiscountCustomerSavedSearchesInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('add', 'remove')
    add = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='add')
    remove = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='remove')


class DiscountCustomerSelectionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('all', 'customers', 'customer_saved_searches')
    all = sgqlc.types.Field(Boolean, graphql_name='all')
    customers = sgqlc.types.Field('DiscountCustomersInput', graphql_name='customers')
    customer_saved_searches = sgqlc.types.Field(DiscountCustomerSavedSearchesInput, graphql_name='customerSavedSearches')


class DiscountCustomersInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('add', 'remove')
    add = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='add')
    remove = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='remove')


class DiscountEffectInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('percentage',)
    percentage = sgqlc.types.Field(Float, graphql_name='percentage')


class DiscountItemsInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('products', 'collections', 'all')
    products = sgqlc.types.Field('DiscountProductsInput', graphql_name='products')
    collections = sgqlc.types.Field(DiscountCollectionsInput, graphql_name='collections')
    all = sgqlc.types.Field(Boolean, graphql_name='all')


class DiscountMinimumQuantityInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('greater_than_or_equal_to_quantity',)
    greater_than_or_equal_to_quantity = sgqlc.types.Field(UnsignedInt64, graphql_name='greaterThanOrEqualToQuantity')


class DiscountMinimumRequirementInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('quantity', 'subtotal')
    quantity = sgqlc.types.Field(DiscountMinimumQuantityInput, graphql_name='quantity')
    subtotal = sgqlc.types.Field('DiscountMinimumSubtotalInput', graphql_name='subtotal')


class DiscountMinimumSubtotalInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('greater_than_or_equal_to_subtotal',)
    greater_than_or_equal_to_subtotal = sgqlc.types.Field(Decimal, graphql_name='greaterThanOrEqualToSubtotal')


class DiscountOnQuantityInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('quantity', 'effect')
    quantity = sgqlc.types.Field(UnsignedInt64, graphql_name='quantity')
    effect = sgqlc.types.Field(DiscountEffectInput, graphql_name='effect')


class DiscountProductsInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('products_to_add', 'products_to_remove', 'product_variants_to_add', 'product_variants_to_remove')
    products_to_add = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='productsToAdd')
    products_to_remove = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='productsToRemove')
    product_variants_to_add = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='productVariantsToAdd')
    product_variants_to_remove = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='productVariantsToRemove')


class DiscountShippingDestinationSelectionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('all', 'countries')
    all = sgqlc.types.Field(Boolean, graphql_name='all')
    countries = sgqlc.types.Field(DiscountCountriesInput, graphql_name='countries')


class DraftOrderAppliedDiscountInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'description', 'title', 'value', 'value_type')
    amount = sgqlc.types.Field(Money, graphql_name='amount')
    description = sgqlc.types.Field(String, graphql_name='description')
    title = sgqlc.types.Field(String, graphql_name='title')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(DraftOrderAppliedDiscountType), graphql_name='valueType')


class DraftOrderDeleteInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DraftOrderInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('applied_discount', 'billing_address', 'customer_id', 'custom_attributes', 'email', 'line_items', 'metafields', 'private_metafields', 'note', 'shipping_address', 'shipping_line', 'tags', 'tax_exempt', 'use_customer_default_address')
    applied_discount = sgqlc.types.Field(DraftOrderAppliedDiscountInput, graphql_name='appliedDiscount')
    billing_address = sgqlc.types.Field('MailingAddressInput', graphql_name='billingAddress')
    customer_id = sgqlc.types.Field(ID, graphql_name='customerId')
    custom_attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AttributeInput)), graphql_name='customAttributes')
    email = sgqlc.types.Field(String, graphql_name='email')
    line_items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DraftOrderLineItemInput')), graphql_name='lineItems')
    metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MetafieldInput')), graphql_name='metafields')
    private_metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PrivateMetafieldInput')), graphql_name='privateMetafields')
    note = sgqlc.types.Field(String, graphql_name='note')
    shipping_address = sgqlc.types.Field('MailingAddressInput', graphql_name='shippingAddress')
    shipping_line = sgqlc.types.Field('ShippingLineInput', graphql_name='shippingLine')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    tax_exempt = sgqlc.types.Field(Boolean, graphql_name='taxExempt')
    use_customer_default_address = sgqlc.types.Field(Boolean, graphql_name='useCustomerDefaultAddress')


class DraftOrderLineItemInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('applied_discount', 'custom_attributes', 'grams', 'original_unit_price', 'quantity', 'requires_shipping', 'sku', 'taxable', 'title', 'variant_id', 'weight')
    applied_discount = sgqlc.types.Field(DraftOrderAppliedDiscountInput, graphql_name='appliedDiscount')
    custom_attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AttributeInput)), graphql_name='customAttributes')
    grams = sgqlc.types.Field(Int, graphql_name='grams')
    original_unit_price = sgqlc.types.Field(Money, graphql_name='originalUnitPrice')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    requires_shipping = sgqlc.types.Field(Boolean, graphql_name='requiresShipping')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    taxable = sgqlc.types.Field(Boolean, graphql_name='taxable')
    title = sgqlc.types.Field(String, graphql_name='title')
    variant_id = sgqlc.types.Field(ID, graphql_name='variantId')
    weight = sgqlc.types.Field('WeightInput', graphql_name='weight')


class EmailInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('subject', 'to', 'from_', 'body', 'bcc', 'custom_message')
    subject = sgqlc.types.Field(String, graphql_name='subject')
    to = sgqlc.types.Field(String, graphql_name='to')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    body = sgqlc.types.Field(String, graphql_name='body')
    bcc = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='bcc')
    custom_message = sgqlc.types.Field(String, graphql_name='customMessage')


class EventBridgeWebhookSubscriptionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('arn', 'format', 'include_fields', 'metafield_namespaces')
    arn = sgqlc.types.Field(ARN, graphql_name='arn')
    format = sgqlc.types.Field(WebhookSubscriptionFormat, graphql_name='format')
    include_fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='includeFields')
    metafield_namespaces = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metafieldNamespaces')


class FulfillmentInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('order_id', 'line_items', 'tracking_numbers', 'tracking_urls', 'tracking_company', 'notify_customer', 'shipping_method', 'location_id')
    order_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='orderId')
    line_items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('FulfillmentLineItemInput')), graphql_name='lineItems')
    tracking_numbers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='trackingNumbers')
    tracking_urls = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='trackingUrls')
    tracking_company = sgqlc.types.Field(String, graphql_name='trackingCompany')
    notify_customer = sgqlc.types.Field(Boolean, graphql_name='notifyCustomer')
    shipping_method = sgqlc.types.Field(String, graphql_name='shippingMethod')
    location_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='locationId')


class FulfillmentLineItemInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'quantity')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    quantity = sgqlc.types.Field(Int, graphql_name='quantity')


class FulfillmentOrderLineItemInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'quantity')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')


class FulfillmentOrderLineItemsInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_order_id', 'fulfillment_order_line_items')
    fulfillment_order_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='fulfillmentOrderId')
    fulfillment_order_line_items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FulfillmentOrderLineItemInput)), graphql_name='fulfillmentOrderLineItems')


class FulfillmentTrackingInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('number', 'url', 'company')
    number = sgqlc.types.Field(String, graphql_name='number')
    url = sgqlc.types.Field(URL, graphql_name='url')
    company = sgqlc.types.Field(String, graphql_name='company')


class FulfillmentV2Input(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('tracking_info', 'notify_customer', 'line_items_by_fulfillment_order')
    tracking_info = sgqlc.types.Field(FulfillmentTrackingInput, graphql_name='trackingInfo')
    notify_customer = sgqlc.types.Field(Boolean, graphql_name='notifyCustomer')
    line_items_by_fulfillment_order = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FulfillmentOrderLineItemsInput))), graphql_name='lineItemsByFulfillmentOrder')


class ImageInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'alt_text', 'src')
    id = sgqlc.types.Field(ID, graphql_name='id')
    alt_text = sgqlc.types.Field(String, graphql_name='altText')
    src = sgqlc.types.Field(String, graphql_name='src')


class InventoryAdjustItemInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('inventory_item_id', 'available_delta')
    inventory_item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='inventoryItemId')
    available_delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='availableDelta')


class InventoryAdjustQuantityInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('inventory_level_id', 'available_delta')
    inventory_level_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='inventoryLevelId')
    available_delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='availableDelta')


class InventoryItemInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('cost', 'tracked')
    cost = sgqlc.types.Field(Decimal, graphql_name='cost')
    tracked = sgqlc.types.Field(Boolean, graphql_name='tracked')


class InventoryItemUpdateInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('cost', 'tracked', 'country_code_of_origin', 'province_code_of_origin', 'harmonized_system_code', 'country_harmonized_system_codes')
    cost = sgqlc.types.Field(Decimal, graphql_name='cost')
    tracked = sgqlc.types.Field(Boolean, graphql_name='tracked')
    country_code_of_origin = sgqlc.types.Field(CountryCode, graphql_name='countryCodeOfOrigin')
    province_code_of_origin = sgqlc.types.Field(String, graphql_name='provinceCodeOfOrigin')
    harmonized_system_code = sgqlc.types.Field(String, graphql_name='harmonizedSystemCode')
    country_harmonized_system_codes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CountryHarmonizedSystemCodeInput)), graphql_name='countryHarmonizedSystemCodes')


class InventoryLevelInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('available_quantity', 'location_id')
    available_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='availableQuantity')
    location_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='locationId')


class MailingAddressInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('address1', 'address2', 'city', 'company', 'country', 'country_code', 'first_name', 'id', 'last_name', 'phone', 'province', 'province_code', 'zip')
    address1 = sgqlc.types.Field(String, graphql_name='address1')
    address2 = sgqlc.types.Field(String, graphql_name='address2')
    city = sgqlc.types.Field(String, graphql_name='city')
    company = sgqlc.types.Field(String, graphql_name='company')
    country = sgqlc.types.Field(String, graphql_name='country')
    country_code = sgqlc.types.Field(CountryCode, graphql_name='countryCode')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    id = sgqlc.types.Field(ID, graphql_name='id')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    province_code = sgqlc.types.Field(String, graphql_name='provinceCode')
    zip = sgqlc.types.Field(String, graphql_name='zip')


class MarketingActivityBudgetInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('budget_type', 'total')
    budget_type = sgqlc.types.Field(MarketingBudgetBudgetType, graphql_name='budgetType')
    total = sgqlc.types.Field('MoneyInput', graphql_name='total')


class MarketingActivityCreateInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('marketing_activity_title', 'form_data', 'marketing_activity_extension_id', 'context', 'utm', 'status', 'budget')
    marketing_activity_title = sgqlc.types.Field(String, graphql_name='marketingActivityTitle')
    form_data = sgqlc.types.Field(String, graphql_name='formData')
    marketing_activity_extension_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='marketingActivityExtensionId')
    context = sgqlc.types.Field(String, graphql_name='context')
    utm = sgqlc.types.Field('UTMInput', graphql_name='utm')
    status = sgqlc.types.Field(sgqlc.types.non_null(MarketingActivityStatus), graphql_name='status')
    budget = sgqlc.types.Field(MarketingActivityBudgetInput, graphql_name='budget')


class MarketingActivityUpdateInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'marketing_recommendation_id', 'title', 'budget', 'ad_spend', 'status', 'target_status', 'form_data', 'utm', 'marketed_resources', 'context', 'errors')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    marketing_recommendation_id = sgqlc.types.Field(ID, graphql_name='marketingRecommendationId')
    title = sgqlc.types.Field(String, graphql_name='title')
    budget = sgqlc.types.Field(MarketingActivityBudgetInput, graphql_name='budget')
    ad_spend = sgqlc.types.Field('MoneyInput', graphql_name='adSpend')
    status = sgqlc.types.Field(MarketingActivityStatus, graphql_name='status')
    target_status = sgqlc.types.Field(MarketingActivityStatus, graphql_name='targetStatus')
    form_data = sgqlc.types.Field(String, graphql_name='formData')
    utm = sgqlc.types.Field('UTMInput', graphql_name='utm')
    marketed_resources = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='marketedResources')
    context = sgqlc.types.Field(String, graphql_name='context')
    errors = sgqlc.types.Field(JSON, graphql_name='errors')


class MarketingEngagementInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('occurred_on', 'impressions_count', 'views_count', 'clicks_count', 'shares_count', 'favorites_count', 'comments_count', 'unsubscribes_count', 'complaints_count', 'fails_count', 'sends_count', 'unique_views_count', 'unique_clicks_count', 'ad_spend', 'is_cumulative', 'utc_offset', 'fetched_at')
    occurred_on = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='occurredOn')
    impressions_count = sgqlc.types.Field(Int, graphql_name='impressionsCount')
    views_count = sgqlc.types.Field(Int, graphql_name='viewsCount')
    clicks_count = sgqlc.types.Field(Int, graphql_name='clicksCount')
    shares_count = sgqlc.types.Field(Int, graphql_name='sharesCount')
    favorites_count = sgqlc.types.Field(Int, graphql_name='favoritesCount')
    comments_count = sgqlc.types.Field(Int, graphql_name='commentsCount')
    unsubscribes_count = sgqlc.types.Field(Int, graphql_name='unsubscribesCount')
    complaints_count = sgqlc.types.Field(Int, graphql_name='complaintsCount')
    fails_count = sgqlc.types.Field(Int, graphql_name='failsCount')
    sends_count = sgqlc.types.Field(Int, graphql_name='sendsCount')
    unique_views_count = sgqlc.types.Field(Int, graphql_name='uniqueViewsCount')
    unique_clicks_count = sgqlc.types.Field(Int, graphql_name='uniqueClicksCount')
    ad_spend = sgqlc.types.Field('MoneyInput', graphql_name='adSpend')
    is_cumulative = sgqlc.types.Field(Boolean, graphql_name='isCumulative')
    utc_offset = sgqlc.types.Field(UtcOffset, graphql_name='utcOffset')
    fetched_at = sgqlc.types.Field(DateTime, graphql_name='fetchedAt')


class MetafieldDeleteInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class MetafieldInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('description', 'id', 'key', 'namespace', 'value', 'value_type')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    key = sgqlc.types.Field(String, graphql_name='key')
    namespace = sgqlc.types.Field(String, graphql_name='namespace')
    value = sgqlc.types.Field(String, graphql_name='value')
    value_type = sgqlc.types.Field(MetafieldValueType, graphql_name='valueType')


class MetafieldStorefrontVisibilityInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('namespace', 'key', 'owner_type')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    owner_type = sgqlc.types.Field(sgqlc.types.non_null(MetafieldOwnerType), graphql_name='ownerType')


class MoneyInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'currency_code')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Decimal), graphql_name='amount')
    currency_code = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='currencyCode')


class MoveInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'new_position')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    new_position = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='newPosition')


class OrderCaptureInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'parent_transaction_id', 'amount', 'currency')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent_transaction_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='parentTransactionId')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='amount')
    currency = sgqlc.types.Field(CurrencyCode, graphql_name='currency')


class OrderCloseInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OrderEditAppliedDiscountInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('description', 'fixed_value', 'percent_value')
    description = sgqlc.types.Field(String, graphql_name='description')
    fixed_value = sgqlc.types.Field(MoneyInput, graphql_name='fixedValue')
    percent_value = sgqlc.types.Field(Float, graphql_name='percentValue')


class OrderInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('email', 'id', 'note', 'tags', 'shipping_address', 'custom_attributes', 'metafields')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    note = sgqlc.types.Field(String, graphql_name='note')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    shipping_address = sgqlc.types.Field(MailingAddressInput, graphql_name='shippingAddress')
    custom_attributes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AttributeInput)), graphql_name='customAttributes')
    metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MetafieldInput)), graphql_name='metafields')


class OrderMarkAsPaidInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OrderOpenInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OrderTransactionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'gateway', 'kind', 'order_id', 'parent_id')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='amount')
    gateway = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='gateway')
    kind = sgqlc.types.Field(sgqlc.types.non_null(OrderTransactionKind), graphql_name='kind')
    order_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='orderId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')


class PriceRuleCustomerSelectionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('for_all_customers', 'saved_search_ids', 'customer_ids_to_add', 'customer_ids_to_remove')
    for_all_customers = sgqlc.types.Field(Boolean, graphql_name='forAllCustomers')
    saved_search_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='savedSearchIds')
    customer_ids_to_add = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='customerIdsToAdd')
    customer_ids_to_remove = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='customerIdsToRemove')


class PriceRuleDiscountCodeInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(String, graphql_name='code')


class PriceRuleEntitlementToPrerequisiteQuantityRatioInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('entitlement_quantity', 'prerequisite_quantity')
    entitlement_quantity = sgqlc.types.Field(Int, graphql_name='entitlementQuantity')
    prerequisite_quantity = sgqlc.types.Field(Int, graphql_name='prerequisiteQuantity')


class PriceRuleInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('validity_period', 'once_per_customer', 'customer_selection', 'usage_limit', 'title', 'allocation_limit', 'allocation_method', 'value', 'target', 'prerequisite_subtotal_range', 'prerequisite_quantity_range', 'prerequisite_shipping_price_range', 'item_entitlements', 'item_prerequisites', 'shipping_entitlements', 'entitlement_to_prerequisite_quantity_ratio', 'prerequisite_to_entitlement_quantity_ratio')
    validity_period = sgqlc.types.Field('PriceRuleValidityPeriodInput', graphql_name='validityPeriod')
    once_per_customer = sgqlc.types.Field(Boolean, graphql_name='oncePerCustomer')
    customer_selection = sgqlc.types.Field(PriceRuleCustomerSelectionInput, graphql_name='customerSelection')
    usage_limit = sgqlc.types.Field(Int, graphql_name='usageLimit')
    title = sgqlc.types.Field(String, graphql_name='title')
    allocation_limit = sgqlc.types.Field(Int, graphql_name='allocationLimit')
    allocation_method = sgqlc.types.Field(PriceRuleAllocationMethod, graphql_name='allocationMethod')
    value = sgqlc.types.Field('PriceRuleValueInput', graphql_name='value')
    target = sgqlc.types.Field(PriceRuleTarget, graphql_name='target')
    prerequisite_subtotal_range = sgqlc.types.Field('PriceRuleMoneyRangeInput', graphql_name='prerequisiteSubtotalRange')
    prerequisite_quantity_range = sgqlc.types.Field('PriceRuleQuantityRangeInput', graphql_name='prerequisiteQuantityRange')
    prerequisite_shipping_price_range = sgqlc.types.Field('PriceRuleMoneyRangeInput', graphql_name='prerequisiteShippingPriceRange')
    item_entitlements = sgqlc.types.Field('PriceRuleItemEntitlementsInput', graphql_name='itemEntitlements')
    item_prerequisites = sgqlc.types.Field('PriceRuleItemPrerequisitesInput', graphql_name='itemPrerequisites')
    shipping_entitlements = sgqlc.types.Field('PriceRuleShippingEntitlementsInput', graphql_name='shippingEntitlements')
    entitlement_to_prerequisite_quantity_ratio = sgqlc.types.Field(PriceRuleEntitlementToPrerequisiteQuantityRatioInput, graphql_name='entitlementToPrerequisiteQuantityRatio')
    prerequisite_to_entitlement_quantity_ratio = sgqlc.types.Field('PriceRulePrerequisiteToEntitlementQuantityRatioInput', graphql_name='prerequisiteToEntitlementQuantityRatio')


class PriceRuleItemEntitlementsInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('target_all_line_items', 'product_ids', 'product_variant_ids', 'collection_ids')
    target_all_line_items = sgqlc.types.Field(Boolean, graphql_name='targetAllLineItems')
    product_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='productIds')
    product_variant_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='productVariantIds')
    collection_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='collectionIds')


class PriceRuleItemPrerequisitesInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('product_ids', 'product_variant_ids', 'collection_ids')
    product_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='productIds')
    product_variant_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='productVariantIds')
    collection_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='collectionIds')


class PriceRuleMoneyRangeInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    less_than = sgqlc.types.Field(Money, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(Money, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(Money, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(Money, graphql_name='greaterThanOrEqualTo')


class PriceRulePrerequisiteToEntitlementQuantityRatioInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('entitlement_quantity', 'prerequisite_quantity')
    entitlement_quantity = sgqlc.types.Field(Int, graphql_name='entitlementQuantity')
    prerequisite_quantity = sgqlc.types.Field(Int, graphql_name='prerequisiteQuantity')


class PriceRuleQuantityRangeInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('less_than', 'less_than_or_equal_to', 'greater_than', 'greater_than_or_equal_to')
    less_than = sgqlc.types.Field(Int, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(Int, graphql_name='lessThanOrEqualTo')
    greater_than = sgqlc.types.Field(Int, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(Int, graphql_name='greaterThanOrEqualTo')


class PriceRuleShippingEntitlementsInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('target_all_shipping_lines', 'country_codes', 'include_rest_of_world')
    target_all_shipping_lines = sgqlc.types.Field(Boolean, graphql_name='targetAllShippingLines')
    country_codes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode)), graphql_name='countryCodes')
    include_rest_of_world = sgqlc.types.Field(Boolean, graphql_name='includeRestOfWorld')


class PriceRuleValidityPeriodInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('start', 'end')
    start = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='start')
    end = sgqlc.types.Field(DateTime, graphql_name='end')


class PriceRuleValueInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('percentage_value', 'fixed_amount_value')
    percentage_value = sgqlc.types.Field(Float, graphql_name='percentageValue')
    fixed_amount_value = sgqlc.types.Field(Money, graphql_name='fixedAmountValue')


class PrivateMetafieldDeleteInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('owner', 'namespace', 'key')
    owner = sgqlc.types.Field(ID, graphql_name='owner')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')


class PrivateMetafieldInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('owner', 'namespace', 'key', 'value_input')
    owner = sgqlc.types.Field(ID, graphql_name='owner')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value_input = sgqlc.types.Field(sgqlc.types.non_null('PrivateMetafieldValueInput'), graphql_name='valueInput')


class PrivateMetafieldValueInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('value', 'value_type')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(PrivateMetafieldValueType), graphql_name='valueType')


class ProductAppendImagesInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'images')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    images = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ImageInput))), graphql_name='images')


class ProductDeleteInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ProductInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('description_html', 'handle', 'redirect_new_handle', 'seo', 'product_type', 'tags', 'template_suffix', 'gift_card', 'gift_card_template_suffix', 'title', 'vendor', 'body_html', 'collections_to_join', 'collections_to_leave', 'id', 'images', 'metafields', 'private_metafields', 'options', 'product_publications', 'publications', 'publish_date', 'publish_on', 'published', 'published_at', 'variants', 'status')
    description_html = sgqlc.types.Field(String, graphql_name='descriptionHtml')
    handle = sgqlc.types.Field(String, graphql_name='handle')
    redirect_new_handle = sgqlc.types.Field(Boolean, graphql_name='redirectNewHandle')
    seo = sgqlc.types.Field('SEOInput', graphql_name='seo')
    product_type = sgqlc.types.Field(String, graphql_name='productType')
    tags = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tags')
    template_suffix = sgqlc.types.Field(String, graphql_name='templateSuffix')
    gift_card = sgqlc.types.Field(Boolean, graphql_name='giftCard')
    gift_card_template_suffix = sgqlc.types.Field(String, graphql_name='giftCardTemplateSuffix')
    title = sgqlc.types.Field(String, graphql_name='title')
    vendor = sgqlc.types.Field(String, graphql_name='vendor')
    body_html = sgqlc.types.Field(String, graphql_name='bodyHtml')
    collections_to_join = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='collectionsToJoin')
    collections_to_leave = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='collectionsToLeave')
    id = sgqlc.types.Field(ID, graphql_name='id')
    images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ImageInput)), graphql_name='images')
    metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MetafieldInput)), graphql_name='metafields')
    private_metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PrivateMetafieldInput)), graphql_name='privateMetafields')
    options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='options')
    product_publications = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProductPublicationInput')), graphql_name='productPublications')
    publications = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProductPublicationInput')), graphql_name='publications')
    publish_date = sgqlc.types.Field(DateTime, graphql_name='publishDate')
    publish_on = sgqlc.types.Field(DateTime, graphql_name='publishOn')
    published = sgqlc.types.Field(Boolean, graphql_name='published')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    variants = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProductVariantInput')), graphql_name='variants')
    status = sgqlc.types.Field(ProductStatus, graphql_name='status')


class ProductPublicationInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('publication_id', 'channel_id', 'channel_handle', 'publish_date')
    publication_id = sgqlc.types.Field(ID, graphql_name='publicationId')
    channel_id = sgqlc.types.Field(ID, graphql_name='channelId')
    channel_handle = sgqlc.types.Field(String, graphql_name='channelHandle')
    publish_date = sgqlc.types.Field(DateTime, graphql_name='publishDate')


class ProductPublishInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'product_publications')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    product_publications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductPublicationInput))), graphql_name='productPublications')


class ProductUnpublishInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'product_publications')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    product_publications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductPublicationInput))), graphql_name='productPublications')


class ProductVariantAppendMediaInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('variant_id', 'media_ids')
    variant_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='variantId')
    media_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='mediaIds')


class ProductVariantDetachMediaInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('variant_id', 'media_ids')
    variant_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='variantId')
    media_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='mediaIds')


class ProductVariantInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('barcode', 'compare_at_price', 'fulfillment_service_id', 'harmonized_system_code', 'id', 'image_id', 'image_src', 'media_src', 'inventory_management', 'inventory_policy', 'inventory_quantities', 'inventory_item', 'metafields', 'private_metafields', 'options', 'position', 'price', 'product_id', 'requires_shipping', 'sku', 'taxable', 'title', 'tax_code', 'weight', 'weight_unit')
    barcode = sgqlc.types.Field(String, graphql_name='barcode')
    compare_at_price = sgqlc.types.Field(Money, graphql_name='compareAtPrice')
    fulfillment_service_id = sgqlc.types.Field(ID, graphql_name='fulfillmentServiceId')
    harmonized_system_code = sgqlc.types.Field(String, graphql_name='harmonizedSystemCode')
    id = sgqlc.types.Field(ID, graphql_name='id')
    image_id = sgqlc.types.Field(ID, graphql_name='imageId')
    image_src = sgqlc.types.Field(String, graphql_name='imageSrc')
    media_src = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='mediaSrc')
    inventory_management = sgqlc.types.Field(ProductVariantInventoryManagement, graphql_name='inventoryManagement')
    inventory_policy = sgqlc.types.Field(ProductVariantInventoryPolicy, graphql_name='inventoryPolicy')
    inventory_quantities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(InventoryLevelInput)), graphql_name='inventoryQuantities')
    inventory_item = sgqlc.types.Field(InventoryItemInput, graphql_name='inventoryItem')
    metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MetafieldInput)), graphql_name='metafields')
    private_metafields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PrivateMetafieldInput)), graphql_name='privateMetafields')
    options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='options')
    position = sgqlc.types.Field(Int, graphql_name='position')
    price = sgqlc.types.Field(Money, graphql_name='price')
    product_id = sgqlc.types.Field(ID, graphql_name='productId')
    requires_shipping = sgqlc.types.Field(Boolean, graphql_name='requiresShipping')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    taxable = sgqlc.types.Field(Boolean, graphql_name='taxable')
    title = sgqlc.types.Field(String, graphql_name='title')
    tax_code = sgqlc.types.Field(String, graphql_name='taxCode')
    weight = sgqlc.types.Field(Float, graphql_name='weight')
    weight_unit = sgqlc.types.Field(WeightUnit, graphql_name='weightUnit')


class PublicationInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('channel_id', 'publication_id', 'publish_date')
    channel_id = sgqlc.types.Field(ID, graphql_name='channelId')
    publication_id = sgqlc.types.Field(ID, graphql_name='publicationId')
    publish_date = sgqlc.types.Field(DateTime, graphql_name='publishDate')


class RefundDutyInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('duty_id', 'refund_type')
    duty_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='dutyId')
    refund_type = sgqlc.types.Field(RefundDutyRefundType, graphql_name='refundType')


class RefundInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('currency', 'order_id', 'note', 'notify', 'shipping', 'refund_line_items', 'refund_duties', 'transactions')
    currency = sgqlc.types.Field(CurrencyCode, graphql_name='currency')
    order_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='orderId')
    note = sgqlc.types.Field(String, graphql_name='note')
    notify = sgqlc.types.Field(Boolean, graphql_name='notify')
    shipping = sgqlc.types.Field('ShippingRefundInput', graphql_name='shipping')
    refund_line_items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RefundLineItemInput')), graphql_name='refundLineItems')
    refund_duties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RefundDutyInput)), graphql_name='refundDuties')
    transactions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OrderTransactionInput)), graphql_name='transactions')


class RefundLineItemInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('line_item_id', 'quantity', 'restock_type', 'location_id')
    line_item_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='lineItemId')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    restock_type = sgqlc.types.Field(RefundLineItemRestockType, graphql_name='restockType')
    location_id = sgqlc.types.Field(ID, graphql_name='locationId')


class SEOInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('title', 'description')
    title = sgqlc.types.Field(String, graphql_name='title')
    description = sgqlc.types.Field(String, graphql_name='description')


class SavedSearchCreateInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('resource_type', 'name', 'query')
    resource_type = sgqlc.types.Field(sgqlc.types.non_null(SearchResultType), graphql_name='resourceType')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')


class SavedSearchDeleteInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class SavedSearchUpdateInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'name', 'query')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    query = sgqlc.types.Field(String, graphql_name='query')


class ScriptTagInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('src', 'display_scope')
    src = sgqlc.types.Field(URL, graphql_name='src')
    display_scope = sgqlc.types.Field(ScriptTagDisplayScope, graphql_name='displayScope')


class ShippingLineInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('price', 'shipping_rate_handle', 'title')
    price = sgqlc.types.Field(Money, graphql_name='price')
    shipping_rate_handle = sgqlc.types.Field(String, graphql_name='shippingRateHandle')
    title = sgqlc.types.Field(String, graphql_name='title')


class ShippingRefundInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'full_refund')
    amount = sgqlc.types.Field(Money, graphql_name='amount')
    full_refund = sgqlc.types.Field(Boolean, graphql_name='fullRefund')


class ShopLocaleInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('published',)
    published = sgqlc.types.Field(Boolean, graphql_name='published')


class ShopPolicyInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('type', 'body')
    type = sgqlc.types.Field(sgqlc.types.non_null(ShopPolicyType), graphql_name='type')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class StageImageInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('resource', 'filename', 'mime_type', 'http_method')
    resource = sgqlc.types.Field(sgqlc.types.non_null(StagedUploadTargetGenerateUploadResource), graphql_name='resource')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    mime_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mimeType')
    http_method = sgqlc.types.Field(StagedUploadHttpMethodType, graphql_name='httpMethod')


class StagedUploadInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('resource', 'filename', 'mime_type', 'http_method', 'file_size')
    resource = sgqlc.types.Field(sgqlc.types.non_null(StagedUploadTargetGenerateUploadResource), graphql_name='resource')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    mime_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mimeType')
    http_method = sgqlc.types.Field(StagedUploadHttpMethodType, graphql_name='httpMethod')
    file_size = sgqlc.types.Field(UnsignedInt64, graphql_name='fileSize')


class StagedUploadTargetGenerateInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('resource', 'filename', 'mime_type', 'http_method', 'file_size')
    resource = sgqlc.types.Field(sgqlc.types.non_null(StagedUploadTargetGenerateUploadResource), graphql_name='resource')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    mime_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mimeType')
    http_method = sgqlc.types.Field(StagedUploadHttpMethodType, graphql_name='httpMethod')
    file_size = sgqlc.types.Field(UnsignedInt64, graphql_name='fileSize')


class StorefrontAccessTokenDeleteInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class StorefrontAccessTokenInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('title',)
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class TrackingInfoInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('number', 'url')
    number = sgqlc.types.Field(String, graphql_name='number')
    url = sgqlc.types.Field(String, graphql_name='url')


class TrackingInfoUpdateInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('tracking_details', 'tracking_company', 'notify_customer')
    tracking_details = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TrackingInfoInput)), graphql_name='trackingDetails')
    tracking_company = sgqlc.types.Field(String, graphql_name='trackingCompany')
    notify_customer = sgqlc.types.Field(Boolean, graphql_name='notifyCustomer')


class TranslationInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('locale', 'key', 'value', 'translatable_content_digest')
    locale = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='locale')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    translatable_content_digest = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='translatableContentDigest')


class UTMInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('campaign', 'source', 'medium')
    campaign = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='campaign')
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='source')
    medium = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='medium')


class UpdateMediaInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'preview_image_source', 'alt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    preview_image_source = sgqlc.types.Field(String, graphql_name='previewImageSource')
    alt = sgqlc.types.Field(String, graphql_name='alt')


class WebhookSubscriptionInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('callback_url', 'format', 'include_fields', 'metafield_namespaces')
    callback_url = sgqlc.types.Field(URL, graphql_name='callbackUrl')
    format = sgqlc.types.Field(WebhookSubscriptionFormat, graphql_name='format')
    include_fields = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='includeFields')
    metafield_namespaces = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='metafieldNamespaces')


class WeightInput(sgqlc.types.Input):
    __schema__ = shopify_schema
    __field_names__ = ('value', 'unit')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    unit = sgqlc.types.Field(sgqlc.types.non_null(WeightUnit), graphql_name='unit')



########################################################################
# Output Objects and Interfaces
########################################################################
class AccessScope(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('description', 'handle')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    handle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='handle')


class AllDiscountItems(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('all_items',)
    all_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allItems')


class ApiVersion(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('display_name', 'handle', 'supported')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    handle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='handle')
    supported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='supported')


class AppConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AppCreditConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppCreditEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AppCreditCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app_credit', 'user_errors')
    app_credit = sgqlc.types.Field('AppCredit', graphql_name='appCredit')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class AppCreditEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AppCredit'), graphql_name='node')


class AppEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('App'), graphql_name='node')


class AppFeedback(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app', 'link', 'messages')
    app = sgqlc.types.Field(sgqlc.types.non_null('App'), graphql_name='app')
    link = sgqlc.types.Field('Link', graphql_name='link')
    messages = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='messages')


class AppInstallationConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppInstallationEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AppInstallationEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AppInstallation'), graphql_name='node')


class AppPlanV2(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('pricing_details',)
    pricing_details = sgqlc.types.Field(sgqlc.types.non_null('AppPricingDetails'), graphql_name='pricingDetails')


class AppPurchase(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'name', 'price', 'status', 'test')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    price = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='price')
    status = sgqlc.types.Field(sgqlc.types.non_null(AppPurchaseStatus), graphql_name='status')
    test = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='test')


class AppPurchaseOneTimeConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppPurchaseOneTimeEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AppPurchaseOneTimeCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app_purchase_one_time', 'confirmation_url', 'user_errors')
    app_purchase_one_time = sgqlc.types.Field('AppPurchaseOneTime', graphql_name='appPurchaseOneTime')
    confirmation_url = sgqlc.types.Field(URL, graphql_name='confirmationUrl')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class AppPurchaseOneTimeEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AppPurchaseOneTime'), graphql_name='node')


class AppRecurringPricing(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('interval', 'price')
    interval = sgqlc.types.Field(sgqlc.types.non_null(AppPricingInterval), graphql_name='interval')
    price = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='price')


class AppSubscriptionCancelPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app_subscription', 'user_errors')
    app_subscription = sgqlc.types.Field('AppSubscription', graphql_name='appSubscription')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class AppSubscriptionConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppSubscriptionEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AppSubscriptionCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app_subscription', 'confirmation_url', 'user_errors')
    app_subscription = sgqlc.types.Field('AppSubscription', graphql_name='appSubscription')
    confirmation_url = sgqlc.types.Field(URL, graphql_name='confirmationUrl')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class AppSubscriptionEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AppSubscription'), graphql_name='node')


class AppSubscriptionLineItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'plan', 'usage_records')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    plan = sgqlc.types.Field(sgqlc.types.non_null(AppPlanV2), graphql_name='plan')
    usage_records = sgqlc.types.Field(sgqlc.types.non_null('AppUsageRecordConnection'), graphql_name='usageRecords', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(AppUsageRecordSortKeys, graphql_name='sortKey', default='CREATED_AT')),
))
    )


class AppSubscriptionLineItemUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app_subscription', 'confirmation_url', 'user_errors')
    app_subscription = sgqlc.types.Field('AppSubscription', graphql_name='appSubscription')
    confirmation_url = sgqlc.types.Field(URL, graphql_name='confirmationUrl')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class AppUsagePricing(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('balance_used', 'capped_amount', 'interval', 'terms')
    balance_used = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='balanceUsed')
    capped_amount = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='cappedAmount')
    interval = sgqlc.types.Field(sgqlc.types.non_null(AppPricingInterval), graphql_name='interval')
    terms = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='terms')


class AppUsageRecordConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppUsageRecordEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class AppUsageRecordCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app_usage_record', 'user_errors')
    app_usage_record = sgqlc.types.Field('AppUsageRecord', graphql_name='appUsageRecord')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class AppUsageRecordEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AppUsageRecord'), graphql_name='node')


class Attribute(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(String, graphql_name='value')


class BulkOperationCancelPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('bulk_operation', 'user_errors')
    bulk_operation = sgqlc.types.Field('BulkOperation', graphql_name='bulkOperation')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class BulkOperationRunQueryPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('bulk_operation', 'user_errors')
    bulk_operation = sgqlc.types.Field('BulkOperation', graphql_name='bulkOperation')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CalculatedDiscountAllocation(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('allocated_amount_set', 'discount_application')
    allocated_amount_set = sgqlc.types.Field(sgqlc.types.non_null('MoneyBag'), graphql_name='allocatedAmountSet')
    discount_application = sgqlc.types.Field(sgqlc.types.non_null('CalculatedDiscountApplication'), graphql_name='discountApplication')


class CalculatedDiscountApplication(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('allocation_method', 'applied_to', 'description', 'id', 'target_selection', 'target_type', 'value')
    allocation_method = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplicationAllocationMethod), graphql_name='allocationMethod')
    applied_to = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplicationLevel), graphql_name='appliedTo')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    target_selection = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplicationTargetSelection), graphql_name='targetSelection')
    target_type = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplicationTargetType), graphql_name='targetType')
    value = sgqlc.types.Field(sgqlc.types.non_null('PricingValue'), graphql_name='value')


class CalculatedDiscountApplicationConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CalculatedDiscountApplicationEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CalculatedDiscountApplicationEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(CalculatedDiscountApplication), graphql_name='node')


class CalculatedDraftOrder(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('applied_discount', 'available_shipping_rates', 'customer', 'line_items', 'shipping_line', 'subtotal_price', 'tax_lines', 'total_price', 'total_shipping_price', 'total_tax')
    applied_discount = sgqlc.types.Field('DraftOrderAppliedDiscount', graphql_name='appliedDiscount')
    available_shipping_rates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShippingRate'))), graphql_name='availableShippingRates')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CalculatedDraftOrderLineItem'))), graphql_name='lineItems')
    shipping_line = sgqlc.types.Field('ShippingLine', graphql_name='shippingLine')
    subtotal_price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='subtotalPrice')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TaxLine'))), graphql_name='taxLines')
    total_price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='totalPrice')
    total_shipping_price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='totalShippingPrice')
    total_tax = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='totalTax')


class CalculatedDraftOrderLineItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('applied_discount', 'custom', 'custom_attributes', 'discounted_total', 'discounted_unit_price', 'fulfillment_service', 'image', 'is_gift_card', 'name', 'original_total', 'original_unit_price', 'product', 'quantity', 'requires_shipping', 'sku', 'taxable', 'title', 'total_discount', 'variant', 'variant_title', 'vendor', 'weight')
    applied_discount = sgqlc.types.Field('DraftOrderAppliedDiscount', graphql_name='appliedDiscount')
    custom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='custom')
    custom_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='customAttributes')
    discounted_total = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='discountedTotal')
    discounted_unit_price = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='discountedUnitPrice')
    fulfillment_service = sgqlc.types.Field(sgqlc.types.non_null('FulfillmentService'), graphql_name='fulfillmentService')
    image = sgqlc.types.Field('Image', graphql_name='image')
    is_gift_card = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGiftCard')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    original_total = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='originalTotal')
    original_unit_price = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='originalUnitPrice')
    product = sgqlc.types.Field('Product', graphql_name='product')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    requires_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresShipping')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    taxable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxable')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_discount = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='totalDiscount')
    variant = sgqlc.types.Field('ProductVariant', graphql_name='variant')
    variant_title = sgqlc.types.Field(String, graphql_name='variantTitle')
    vendor = sgqlc.types.Field(String, graphql_name='vendor')
    weight = sgqlc.types.Field('Weight', graphql_name='weight')


class CalculatedLineItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('calculated_discount_allocations', 'custom_attributes', 'discounted_unit_price_set', 'editable_quantity', 'editable_quantity_before_changes', 'editable_subtotal_set', 'has_staged_line_item_discount', 'id', 'image', 'original_unit_price_set', 'quantity', 'restockable', 'restocking', 'sku', 'staged_changes', 'title', 'uneditable_subtotal_set', 'variant', 'variant_title')
    calculated_discount_allocations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CalculatedDiscountAllocation))), graphql_name='calculatedDiscountAllocations')
    custom_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='customAttributes')
    discounted_unit_price_set = sgqlc.types.Field(sgqlc.types.non_null('MoneyBag'), graphql_name='discountedUnitPriceSet')
    editable_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='editableQuantity')
    editable_quantity_before_changes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='editableQuantityBeforeChanges')
    editable_subtotal_set = sgqlc.types.Field(sgqlc.types.non_null('MoneyBag'), graphql_name='editableSubtotalSet')
    has_staged_line_item_discount = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasStagedLineItemDiscount')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field('Image', graphql_name='image')
    original_unit_price_set = sgqlc.types.Field(sgqlc.types.non_null('MoneyBag'), graphql_name='originalUnitPriceSet')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    restockable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restockable')
    restocking = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restocking')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    staged_changes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrderStagedChange'))), graphql_name='stagedChanges')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    uneditable_subtotal_set = sgqlc.types.Field(sgqlc.types.non_null('MoneyBag'), graphql_name='uneditableSubtotalSet')
    variant = sgqlc.types.Field('ProductVariant', graphql_name='variant')
    variant_title = sgqlc.types.Field(String, graphql_name='variantTitle')


class CalculatedLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CalculatedLineItemEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CalculatedLineItemEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(CalculatedLineItem), graphql_name='node')


class ChannelConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ChannelEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class ChannelEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Channel'), graphql_name='node')


class CollectionAddProductsPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collection', 'user_errors')
    collection = sgqlc.types.Field('Collection', graphql_name='collection')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CollectionConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CollectionEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CollectionCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collection', 'user_errors')
    collection = sgqlc.types.Field('Collection', graphql_name='collection')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CollectionDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_collection_id', 'shop', 'user_errors')
    deleted_collection_id = sgqlc.types.Field(ID, graphql_name='deletedCollectionId')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CollectionEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Collection'), graphql_name='node')


class CollectionPublication(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collection', 'is_published', 'publication', 'publish_date')
    collection = sgqlc.types.Field(sgqlc.types.non_null('Collection'), graphql_name='collection')
    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')
    publication = sgqlc.types.Field(sgqlc.types.non_null('Publication'), graphql_name='publication')
    publish_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='publishDate')


class CollectionPublicationConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CollectionPublicationEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CollectionPublicationEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(CollectionPublication), graphql_name='node')


class CollectionPublishPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collection', 'collection_publications', 'shop', 'user_errors')
    collection = sgqlc.types.Field('Collection', graphql_name='collection')
    collection_publications = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CollectionPublication)), graphql_name='collectionPublications')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CollectionRemoveProductsPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field('Job', graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CollectionReorderProductsPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field('Job', graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CollectionRule(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('column', 'condition', 'relation')
    column = sgqlc.types.Field(sgqlc.types.non_null(CollectionRuleColumn), graphql_name='column')
    condition = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='condition')
    relation = sgqlc.types.Field(sgqlc.types.non_null(CollectionRuleRelation), graphql_name='relation')


class CollectionRuleConditions(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('allowed_relations', 'default_relation', 'rule_type')
    allowed_relations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CollectionRuleRelation))), graphql_name='allowedRelations')
    default_relation = sgqlc.types.Field(sgqlc.types.non_null(CollectionRuleRelation), graphql_name='defaultRelation')
    rule_type = sgqlc.types.Field(sgqlc.types.non_null(CollectionRuleColumn), graphql_name='ruleType')


class CollectionRuleSet(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('applied_disjunctively', 'rules')
    applied_disjunctively = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='appliedDisjunctively')
    rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CollectionRule))), graphql_name='rules')


class CollectionUnpublishPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collection', 'shop', 'user_errors')
    collection = sgqlc.types.Field('Collection', graphql_name='collection')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CollectionUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collection', 'job', 'user_errors')
    collection = sgqlc.types.Field('Collection', graphql_name='collection')
    job = sgqlc.types.Field('Job', graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CommentEventAttachment(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('file_extension', 'id', 'image', 'name', 'size', 'url')
    file_extension = sgqlc.types.Field(String, graphql_name='fileExtension')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field('Image', graphql_name='image', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class CommentEventSubject(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('has_timeline_comment', 'id')
    has_timeline_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTimelineComment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class CountriesInShippingZones(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('country_codes', 'include_rest_of_world')
    country_codes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode))), graphql_name='countryCodes')
    include_rest_of_world = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includeRestOfWorld')


class CountryHarmonizedSystemCode(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('country_code', 'harmonized_system_code')
    country_code = sgqlc.types.Field(sgqlc.types.non_null(CountryCode), graphql_name='countryCode')
    harmonized_system_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='harmonizedSystemCode')


class CountryHarmonizedSystemCodeConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CountryHarmonizedSystemCodeEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CountryHarmonizedSystemCodeEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(CountryHarmonizedSystemCode), graphql_name='node')


class CurrencyFormats(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('money_format', 'money_in_emails_format', 'money_with_currency_format', 'money_with_currency_in_emails_format')
    money_format = sgqlc.types.Field(sgqlc.types.non_null(FormattedString), graphql_name='moneyFormat')
    money_in_emails_format = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='moneyInEmailsFormat')
    money_with_currency_format = sgqlc.types.Field(sgqlc.types.non_null(FormattedString), graphql_name='moneyWithCurrencyFormat')
    money_with_currency_in_emails_format = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='moneyWithCurrencyInEmailsFormat')


class CurrencySetting(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('currency_code', 'currency_name', 'enabled', 'rate_updated_at')
    currency_code = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='currencyCode')
    currency_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currencyName')
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enabled')
    rate_updated_at = sgqlc.types.Field(DateTime, graphql_name='rateUpdatedAt')


class CurrencySettingConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CurrencySettingEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CurrencySettingEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(CurrencySetting), graphql_name='node')


class CustomerAddTaxExemptionsPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customer', 'user_errors')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CustomerConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CustomerCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customer', 'user_errors')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CustomerDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_customer_id', 'shop', 'user_errors')
    deleted_customer_id = sgqlc.types.Field(ID, graphql_name='deletedCustomerId')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CustomerEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Customer'), graphql_name='node')


class CustomerGenerateAccountActivationUrlPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('account_activation_url', 'user_errors')
    account_activation_url = sgqlc.types.Field(URL, graphql_name='accountActivationUrl')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CustomerJourney(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customer_order_index', 'days_to_conversion', 'first_visit', 'last_visit', 'moments')
    customer_order_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='customerOrderIndex')
    days_to_conversion = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='daysToConversion')
    first_visit = sgqlc.types.Field(sgqlc.types.non_null('CustomerVisit'), graphql_name='firstVisit')
    last_visit = sgqlc.types.Field('CustomerVisit', graphql_name='lastVisit')
    moments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerMoment'))), graphql_name='moments')


class CustomerJourneySummary(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customer_order_index', 'days_to_conversion', 'first_visit', 'last_visit', 'moments', 'moments_count', 'ready')
    customer_order_index = sgqlc.types.Field(Int, graphql_name='customerOrderIndex')
    days_to_conversion = sgqlc.types.Field(Int, graphql_name='daysToConversion')
    first_visit = sgqlc.types.Field('CustomerVisit', graphql_name='firstVisit')
    last_visit = sgqlc.types.Field('CustomerVisit', graphql_name='lastVisit')
    moments = sgqlc.types.Field('CustomerMomentConnection', graphql_name='moments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    moments_count = sgqlc.types.Field(Int, graphql_name='momentsCount')
    ready = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='ready')


class CustomerMoment(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('occurred_at',)
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')


class CustomerMomentConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CustomerMomentEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class CustomerMomentEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(CustomerMoment), graphql_name='node')


class CustomerRemoveTaxExemptionsPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customer', 'user_errors')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CustomerReplaceTaxExemptionsPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customer', 'user_errors')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CustomerUpdateDefaultAddressPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customer', 'user_errors')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class CustomerUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customer', 'user_errors')
    customer = sgqlc.types.Field('Customer', graphql_name='customer')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DeletionEvent(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('occurred_at', 'subject_id', 'subject_type')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    subject_type = sgqlc.types.Field(sgqlc.types.non_null(DeletionEventSubjectType), graphql_name='subjectType')


class DeletionEventConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DeletionEventEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DeletionEventEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(DeletionEvent), graphql_name='node')


class DeliveryAvailableService(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('countries', 'name')
    countries = sgqlc.types.Field(sgqlc.types.non_null('DeliveryCountryCodesOrRestOfWorld'), graphql_name='countries')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DeliveryCarrierServiceAndLocations(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('carrier_service', 'locations')
    carrier_service = sgqlc.types.Field(sgqlc.types.non_null('DeliveryCarrierService'), graphql_name='carrierService')
    locations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Location'))), graphql_name='locations')


class DeliveryCountryAndZone(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('country', 'zone')
    country = sgqlc.types.Field(sgqlc.types.non_null('DeliveryCountry'), graphql_name='country')
    zone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='zone')


class DeliveryCountryCodeOrRestOfWorld(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('country_code', 'rest_of_world')
    country_code = sgqlc.types.Field(CountryCode, graphql_name='countryCode')
    rest_of_world = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restOfWorld')


class DeliveryCountryCodesOrRestOfWorld(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('country_codes', 'rest_of_world')
    country_codes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode))), graphql_name='countryCodes')
    rest_of_world = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restOfWorld')


class DeliveryLegacyModeBlocked(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('blocked', 'reasons')
    blocked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='blocked')
    reasons = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryLegacyModeBlockedReason)), graphql_name='reasons')


class DeliveryLocationGroupZone(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('method_definition_counts', 'method_definitions', 'zone')
    method_definition_counts = sgqlc.types.Field(sgqlc.types.non_null('DeliveryMethodDefinitionCounts'), graphql_name='methodDefinitionCounts')
    method_definitions = sgqlc.types.Field(sgqlc.types.non_null('DeliveryMethodDefinitionConnection'), graphql_name='methodDefinitions', args=sgqlc.types.ArgDict((
        ('eligible', sgqlc.types.Arg(Boolean, graphql_name='eligible', default=None)),
        ('type', sgqlc.types.Arg(DeliveryMethodDefinitionType, graphql_name='type', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(MethodDefinitionSortKeys, graphql_name='sortKey', default='ID')),
))
    )
    zone = sgqlc.types.Field(sgqlc.types.non_null('DeliveryZone'), graphql_name='zone')


class DeliveryLocationGroupZoneConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryLocationGroupZoneEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DeliveryLocationGroupZoneEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(DeliveryLocationGroupZone), graphql_name='node')


class DeliveryMethodDefinitionConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryMethodDefinitionEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DeliveryMethodDefinitionCounts(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('participant_definitions_count', 'rate_definitions_count')
    participant_definitions_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='participantDefinitionsCount')
    rate_definitions_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rateDefinitionsCount')


class DeliveryMethodDefinitionEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('DeliveryMethodDefinition'), graphql_name='node')


class DeliveryParticipantService(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('active', 'name')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DeliveryProductVariantsCount(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('capped', 'count')
    capped = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='capped')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class DeliveryProfileConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryProfileEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DeliveryProfileEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('DeliveryProfile'), graphql_name='node')


class DeliveryProfileItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'variants')
    product = sgqlc.types.Field(sgqlc.types.non_null('Product'), graphql_name='product')
    variants = sgqlc.types.Field(sgqlc.types.non_null('ProductVariantConnection'), graphql_name='variants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProductVariantSortKeys, graphql_name='sortKey', default='ID')),
))
    )


class DeliveryProfileItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryProfileItemEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DeliveryProfileItemEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(DeliveryProfileItem), graphql_name='node')


class DeliveryProfileLocationGroup(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('countries_in_any_zone', 'location_group', 'location_group_zones')
    countries_in_any_zone = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryCountryAndZone))), graphql_name='countriesInAnyZone')
    location_group = sgqlc.types.Field(sgqlc.types.non_null('DeliveryLocationGroup'), graphql_name='locationGroup')
    location_group_zones = sgqlc.types.Field(sgqlc.types.non_null(DeliveryLocationGroupZoneConnection), graphql_name='locationGroupZones', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )


class DeliverySetting(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('legacy_mode_blocked', 'legacy_mode_profiles')
    legacy_mode_blocked = sgqlc.types.Field(sgqlc.types.non_null(DeliveryLegacyModeBlocked), graphql_name='legacyModeBlocked')
    legacy_mode_profiles = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='legacyModeProfiles')


class DeliverySettingUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('setting', 'user_errors')
    setting = sgqlc.types.Field(DeliverySetting, graphql_name='setting')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DeliveryShippingOriginAssignPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors',)
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DiscountAllocation(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('allocated_amount_set', 'discount_application')
    allocated_amount_set = sgqlc.types.Field(sgqlc.types.non_null('MoneyBag'), graphql_name='allocatedAmountSet')
    discount_application = sgqlc.types.Field(sgqlc.types.non_null('DiscountApplication'), graphql_name='discountApplication')


class DiscountAmount(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'applies_on_each_item')
    amount = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='amount')
    applies_on_each_item = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='appliesOnEachItem')


class DiscountApplication(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('allocation_method', 'index', 'target_selection', 'target_type', 'value')
    allocation_method = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplicationAllocationMethod), graphql_name='allocationMethod')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    target_selection = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplicationTargetSelection), graphql_name='targetSelection')
    target_type = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplicationTargetType), graphql_name='targetType')
    value = sgqlc.types.Field(sgqlc.types.non_null('PricingValue'), graphql_name='value')


class DiscountApplicationConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountApplicationEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DiscountApplicationEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplication), graphql_name='node')


class DiscountAutomaticActivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('automatic_discount_node', 'user_errors')
    automatic_discount_node = sgqlc.types.Field('DiscountAutomaticNode', graphql_name='automaticDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountAutomaticBasic(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('async_usage_count', 'created_at', 'customer_gets', 'ends_at', 'minimum_requirement', 'short_summary', 'starts_at', 'status', 'summary', 'title')
    async_usage_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='asyncUsageCount')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_gets = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerGets'), graphql_name='customerGets')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    minimum_requirement = sgqlc.types.Field(sgqlc.types.non_null('DiscountMinimumRequirement'), graphql_name='minimumRequirement')
    short_summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortSummary')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(DiscountStatus), graphql_name='status')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class DiscountAutomaticBasicCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('automatic_discount_node', 'user_errors')
    automatic_discount_node = sgqlc.types.Field('DiscountAutomaticNode', graphql_name='automaticDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountAutomaticBasicUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('automatic_discount_node', 'user_errors')
    automatic_discount_node = sgqlc.types.Field('DiscountAutomaticNode', graphql_name='automaticDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountAutomaticBulkDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field('Job', graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountAutomaticBxgyCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('automatic_discount_node', 'user_errors')
    automatic_discount_node = sgqlc.types.Field('DiscountAutomaticNode', graphql_name='automaticDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountAutomaticBxgyUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('automatic_discount_node', 'user_errors')
    automatic_discount_node = sgqlc.types.Field('DiscountAutomaticNode', graphql_name='automaticDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountAutomaticConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountAutomaticEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DiscountAutomaticDeactivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('automatic_discount_node', 'user_errors')
    automatic_discount_node = sgqlc.types.Field('DiscountAutomaticNode', graphql_name='automaticDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountAutomaticDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_automatic_discount_id', 'user_errors')
    deleted_automatic_discount_id = sgqlc.types.Field(ID, graphql_name='deletedAutomaticDiscountId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountAutomaticEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('DiscountAutomatic'), graphql_name='node')


class DiscountAutomaticNodeConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountAutomaticNodeEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DiscountAutomaticNodeEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('DiscountAutomaticNode'), graphql_name='node')


class DiscountCodeActivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount_node', 'user_errors')
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeBasic(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('applies_once_per_customer', 'async_usage_count', 'code_count', 'codes', 'created_at', 'customer_gets', 'customer_selection', 'ends_at', 'has_timeline_comment', 'minimum_requirement', 'shareable_urls', 'short_summary', 'starts_at', 'status', 'summary', 'title', 'total_sales', 'usage_limit')
    applies_once_per_customer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='appliesOncePerCustomer')
    async_usage_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='asyncUsageCount')
    code_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='codeCount')
    codes = sgqlc.types.Field(sgqlc.types.non_null('DiscountRedeemCodeConnection'), graphql_name='codes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(DiscountCodeSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_gets = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerGets'), graphql_name='customerGets')
    customer_selection = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerSelection'), graphql_name='customerSelection')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    has_timeline_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTimelineComment')
    minimum_requirement = sgqlc.types.Field('DiscountMinimumRequirement', graphql_name='minimumRequirement')
    shareable_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountShareableUrl'))), graphql_name='shareableUrls')
    short_summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortSummary')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(DiscountStatus), graphql_name='status')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_sales = sgqlc.types.Field('MoneyV2', graphql_name='totalSales')
    usage_limit = sgqlc.types.Field(Int, graphql_name='usageLimit')


class DiscountCodeBasicCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount_node', 'user_errors')
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeBasicUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount_node', 'user_errors')
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeBulkActivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field('Job', graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeBulkDeactivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field('Job', graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeBulkDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field('Job', graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeBxgy(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('applies_once_per_customer', 'async_usage_count', 'code_count', 'codes', 'created_at', 'customer_buys', 'customer_gets', 'customer_selection', 'ends_at', 'has_timeline_comment', 'shareable_urls', 'starts_at', 'status', 'summary', 'title', 'total_sales', 'usage_limit', 'uses_per_order_limit')
    applies_once_per_customer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='appliesOncePerCustomer')
    async_usage_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='asyncUsageCount')
    code_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='codeCount')
    codes = sgqlc.types.Field(sgqlc.types.non_null('DiscountRedeemCodeConnection'), graphql_name='codes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(DiscountCodeSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_buys = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerBuys'), graphql_name='customerBuys')
    customer_gets = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerGets'), graphql_name='customerGets')
    customer_selection = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerSelection'), graphql_name='customerSelection')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    has_timeline_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTimelineComment')
    shareable_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountShareableUrl'))), graphql_name='shareableUrls')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(DiscountStatus), graphql_name='status')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_sales = sgqlc.types.Field('MoneyV2', graphql_name='totalSales')
    usage_limit = sgqlc.types.Field(Int, graphql_name='usageLimit')
    uses_per_order_limit = sgqlc.types.Field(Int, graphql_name='usesPerOrderLimit')


class DiscountCodeBxgyCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount_node', 'user_errors')
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeBxgyUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount_node', 'user_errors')
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeDeactivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount_node', 'user_errors')
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_code_discount_id', 'user_errors')
    deleted_code_discount_id = sgqlc.types.Field(ID, graphql_name='deletedCodeDiscountId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeFreeShipping(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('applies_once_per_customer', 'async_usage_count', 'code_count', 'codes', 'created_at', 'customer_selection', 'destination_selection', 'ends_at', 'has_timeline_comment', 'maximum_shipping_price', 'minimum_requirement', 'shareable_urls', 'short_summary', 'starts_at', 'status', 'summary', 'title', 'total_sales', 'usage_limit')
    applies_once_per_customer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='appliesOncePerCustomer')
    async_usage_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='asyncUsageCount')
    code_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='codeCount')
    codes = sgqlc.types.Field(sgqlc.types.non_null('DiscountRedeemCodeConnection'), graphql_name='codes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(DiscountCodeSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_selection = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerSelection'), graphql_name='customerSelection')
    destination_selection = sgqlc.types.Field(sgqlc.types.non_null('DiscountShippingDestinationSelection'), graphql_name='destinationSelection')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    has_timeline_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTimelineComment')
    maximum_shipping_price = sgqlc.types.Field('MoneyV2', graphql_name='maximumShippingPrice')
    minimum_requirement = sgqlc.types.Field('DiscountMinimumRequirement', graphql_name='minimumRequirement')
    shareable_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountShareableUrl'))), graphql_name='shareableUrls')
    short_summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortSummary')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(DiscountStatus), graphql_name='status')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_sales = sgqlc.types.Field('MoneyV2', graphql_name='totalSales')
    usage_limit = sgqlc.types.Field(Int, graphql_name='usageLimit')


class DiscountCodeFreeShippingCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount_node', 'user_errors')
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeFreeShippingUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount_node', 'user_errors')
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCodeNodeConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountCodeNodeEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DiscountCodeNodeEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('DiscountCodeNode'), graphql_name='node')


class DiscountCodeRedeemCodeBulkDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field('Job', graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountUserError'))), graphql_name='userErrors')


class DiscountCollections(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collections',)
    collections = sgqlc.types.Field(sgqlc.types.non_null(CollectionConnection), graphql_name='collections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )


class DiscountCountries(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('countries', 'include_rest_of_world')
    countries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode))), graphql_name='countries')
    include_rest_of_world = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includeRestOfWorld')


class DiscountCountryAll(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('all_countries',)
    all_countries = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allCountries')


class DiscountCustomerAll(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('all_customers',)
    all_customers = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allCustomers')


class DiscountCustomerBuys(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('items', 'value')
    items = sgqlc.types.Field(sgqlc.types.non_null('DiscountItems'), graphql_name='items')
    value = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerBuysValue'), graphql_name='value')


class DiscountCustomerGets(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('items', 'value')
    items = sgqlc.types.Field(sgqlc.types.non_null('DiscountItems'), graphql_name='items')
    value = sgqlc.types.Field(sgqlc.types.non_null('DiscountCustomerGetsValue'), graphql_name='value')


class DiscountCustomerSavedSearches(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('saved_searches',)
    saved_searches = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SavedSearch'))), graphql_name='savedSearches')


class DiscountCustomers(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customers',)
    customers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Customer'))), graphql_name='customers')


class DiscountMinimumQuantity(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('greater_than_or_equal_to_quantity',)
    greater_than_or_equal_to_quantity = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='greaterThanOrEqualToQuantity')


class DiscountMinimumSubtotal(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('greater_than_or_equal_to_subtotal',)
    greater_than_or_equal_to_subtotal = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='greaterThanOrEqualToSubtotal')


class DiscountOnQuantity(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('effect', 'quantity')
    effect = sgqlc.types.Field(sgqlc.types.non_null('DiscountEffect'), graphql_name='effect')
    quantity = sgqlc.types.Field(sgqlc.types.non_null('DiscountQuantity'), graphql_name='quantity')


class DiscountPercentage(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('percentage',)
    percentage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='percentage')


class DiscountProducts(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product_variants', 'products')
    product_variants = sgqlc.types.Field(sgqlc.types.non_null('ProductVariantConnection'), graphql_name='productVariants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    products = sgqlc.types.Field(sgqlc.types.non_null('ProductConnection'), graphql_name='products', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )


class DiscountPurchaseAmount(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('amount',)
    amount = sgqlc.types.Field(sgqlc.types.non_null(Decimal), graphql_name='amount')


class DiscountQuantity(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('quantity',)
    quantity = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='quantity')


class DiscountRedeemCode(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('async_usage_count', 'code', 'created_by', 'id')
    async_usage_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='asyncUsageCount')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_by = sgqlc.types.Field('App', graphql_name='createdBy')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DiscountRedeemCodeConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DiscountRedeemCodeEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DiscountRedeemCodeEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(DiscountRedeemCode), graphql_name='node')


class DiscountShareableUrl(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('target_item_image', 'target_type', 'title', 'url')
    target_item_image = sgqlc.types.Field('Image', graphql_name='targetItemImage')
    target_type = sgqlc.types.Field(sgqlc.types.non_null(DiscountShareableUrlTargetType), graphql_name='targetType')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class DisplayableError(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('field', 'message')
    field = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='field')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')


class DomainLocalization(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('alternate_locales', 'country', 'default_locale')
    alternate_locales = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='alternateLocales')
    country = sgqlc.types.Field(String, graphql_name='country')
    default_locale = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='defaultLocale')


class DraftFulfillment(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('allow_label_purchase', 'line_items', 'requires_shipping', 'service')
    allow_label_purchase = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='allowLabelPurchase')
    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LineItem'))), graphql_name='lineItems')
    requires_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresShipping')
    service = sgqlc.types.Field(sgqlc.types.non_null('FulfillmentService'), graphql_name='service')


class DraftOrderAppliedDiscount(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('amount_v2', 'description', 'title', 'value', 'value_type')
    amount_v2 = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='amountV2')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    title = sgqlc.types.Field(String, graphql_name='title')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(DraftOrderAppliedDiscountType), graphql_name='valueType')


class DraftOrderCalculatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('calculated_draft_order', 'user_errors')
    calculated_draft_order = sgqlc.types.Field(CalculatedDraftOrder, graphql_name='calculatedDraftOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DraftOrderCompletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('draft_order', 'user_errors')
    draft_order = sgqlc.types.Field('DraftOrder', graphql_name='draftOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DraftOrderConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DraftOrderEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DraftOrderCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('draft_order', 'user_errors')
    draft_order = sgqlc.types.Field('DraftOrder', graphql_name='draftOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DraftOrderDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_id', 'user_errors')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DraftOrderEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('DraftOrder'), graphql_name='node')


class DraftOrderInvoicePreviewPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('preview_html', 'user_errors')
    preview_html = sgqlc.types.Field(HTML, graphql_name='previewHtml')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DraftOrderInvoiceSendPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('draft_order', 'user_errors')
    draft_order = sgqlc.types.Field('DraftOrder', graphql_name='draftOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class DraftOrderLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DraftOrderLineItemEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class DraftOrderLineItemEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('DraftOrderLineItem'), graphql_name='node')


class DraftOrderUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('draft_order', 'user_errors')
    draft_order = sgqlc.types.Field('DraftOrder', graphql_name='draftOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class EditableProperty(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('locked', 'reason')
    locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='locked')
    reason = sgqlc.types.Field(FormattedString, graphql_name='reason')


class Event(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('app_title', 'attribute_to_app', 'attribute_to_user', 'created_at', 'critical_alert', 'id', 'message')
    app_title = sgqlc.types.Field(String, graphql_name='appTitle')
    attribute_to_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='attributeToApp')
    attribute_to_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='attributeToUser')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    critical_alert = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='criticalAlert')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    message = sgqlc.types.Field(sgqlc.types.non_null(FormattedString), graphql_name='message')


class EventBridgeWebhookSubscriptionCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors', 'webhook_subscription')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')
    webhook_subscription = sgqlc.types.Field('WebhookSubscription', graphql_name='webhookSubscription')


class EventBridgeWebhookSubscriptionUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors', 'webhook_subscription')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')
    webhook_subscription = sgqlc.types.Field('WebhookSubscription', graphql_name='webhookSubscription')


class EventConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class EventEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(Event), graphql_name='node')


class FailedRequirement(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('action', 'message')
    action = sgqlc.types.Field('NavigationItem', graphql_name='action')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')


class FilterOption(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('label', 'value')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class FlowTriggerReceivePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors',)
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentCancelPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment', 'user_errors')
    fulfillment = sgqlc.types.Field('Fulfillment', graphql_name='fulfillment')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FulfillmentEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class FulfillmentCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment', 'order', 'user_errors')
    fulfillment = sgqlc.types.Field('Fulfillment', graphql_name='fulfillment')
    order = sgqlc.types.Field('Order', graphql_name='order')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentCreateV2Payload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment', 'user_errors')
    fulfillment = sgqlc.types.Field('Fulfillment', graphql_name='fulfillment')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Fulfillment'), graphql_name='node')


class FulfillmentEventConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FulfillmentEventEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class FulfillmentEventEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('FulfillmentEvent'), graphql_name='node')


class FulfillmentLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FulfillmentLineItemEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class FulfillmentLineItemEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('FulfillmentLineItem'), graphql_name='node')


class FulfillmentOrderAcceptCancellationRequestPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_order', 'user_errors')
    fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='fulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderAcceptFulfillmentRequestPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_order', 'user_errors')
    fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='fulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderAssignedLocation(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('address1', 'address2', 'city', 'country_code', 'location', 'name', 'phone', 'province', 'zip')
    address1 = sgqlc.types.Field(String, graphql_name='address1')
    address2 = sgqlc.types.Field(String, graphql_name='address2')
    city = sgqlc.types.Field(String, graphql_name='city')
    country_code = sgqlc.types.Field(sgqlc.types.non_null(CountryCode), graphql_name='countryCode')
    location = sgqlc.types.Field('Location', graphql_name='location')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    zip = sgqlc.types.Field(String, graphql_name='zip')


class FulfillmentOrderCancelPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_order', 'replacement_fulfillment_order', 'user_errors')
    fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='fulfillmentOrder')
    replacement_fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='replacementFulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderClosePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_order', 'user_errors')
    fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='fulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FulfillmentOrderEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class FulfillmentOrderEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('FulfillmentOrder'), graphql_name='node')


class FulfillmentOrderLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FulfillmentOrderLineItemEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class FulfillmentOrderLineItemEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('FulfillmentOrderLineItem'), graphql_name='node')


class FulfillmentOrderLocationForMove(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('location', 'message', 'movable')
    location = sgqlc.types.Field(sgqlc.types.non_null('Location'), graphql_name='location')
    message = sgqlc.types.Field(String, graphql_name='message')
    movable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='movable')


class FulfillmentOrderLocationForMoveConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FulfillmentOrderLocationForMoveEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class FulfillmentOrderLocationForMoveEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderLocationForMove), graphql_name='node')


class FulfillmentOrderMerchantRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FulfillmentOrderMerchantRequestEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class FulfillmentOrderMerchantRequestEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('FulfillmentOrderMerchantRequest'), graphql_name='node')


class FulfillmentOrderMovePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('moved_fulfillment_order', 'original_fulfillment_order', 'remaining_fulfillment_order', 'user_errors')
    moved_fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='movedFulfillmentOrder')
    original_fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='originalFulfillmentOrder')
    remaining_fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='remainingFulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderRejectCancellationRequestPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_order', 'user_errors')
    fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='fulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderRejectFulfillmentRequestPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_order', 'user_errors')
    fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='fulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderSubmitCancellationRequestPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_order', 'user_errors')
    fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='fulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderSubmitFulfillmentRequestPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('original_fulfillment_order', 'submitted_fulfillment_order', 'unsubmitted_fulfillment_order', 'user_errors')
    original_fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='originalFulfillmentOrder')
    submitted_fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='submittedFulfillmentOrder')
    unsubmitted_fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='unsubmittedFulfillmentOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentOrderSupportedAction(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('action', 'external_url')
    action = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderAction), graphql_name='action')
    external_url = sgqlc.types.Field(URL, graphql_name='externalUrl')


class FulfillmentService(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('callback_url', 'fulfillment_orders_opt_in', 'handle', 'id', 'inventory_management', 'location', 'product_based', 'service_name', 'shipping_methods', 'type')
    callback_url = sgqlc.types.Field(URL, graphql_name='callbackUrl')
    fulfillment_orders_opt_in = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fulfillmentOrdersOptIn')
    handle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='handle')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    inventory_management = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='inventoryManagement')
    location = sgqlc.types.Field('Location', graphql_name='location')
    product_based = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='productBased')
    service_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='serviceName')
    shipping_methods = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShippingMethod'))), graphql_name='shippingMethods')
    type = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentServiceType), graphql_name='type')


class FulfillmentServiceCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_service', 'user_errors')
    fulfillment_service = sgqlc.types.Field(FulfillmentService, graphql_name='fulfillmentService')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentServiceDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_id', 'user_errors')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentServiceUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment_service', 'user_errors')
    fulfillment_service = sgqlc.types.Field(FulfillmentService, graphql_name='fulfillmentService')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentTrackingInfo(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('company', 'number', 'url')
    company = sgqlc.types.Field(String, graphql_name='company')
    number = sgqlc.types.Field(String, graphql_name='number')
    url = sgqlc.types.Field(URL, graphql_name='url')


class FulfillmentTrackingInfoUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment', 'user_errors')
    fulfillment = sgqlc.types.Field('Fulfillment', graphql_name='fulfillment')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class FulfillmentTrackingInfoUpdateV2Payload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('fulfillment', 'user_errors')
    fulfillment = sgqlc.types.Field('Fulfillment', graphql_name='fulfillment')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class HasEvents(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('events',)
    events = sgqlc.types.Field(sgqlc.types.non_null(EventConnection), graphql_name='events', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(EventSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )


class HasLocalizationExtensions(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('localization_extensions',)
    localization_extensions = sgqlc.types.Field(sgqlc.types.non_null('LocalizationExtensionConnection'), graphql_name='localizationExtensions', args=sgqlc.types.ArgDict((
        ('country_codes', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode)), graphql_name='countryCodes', default=None)),
        ('purposes', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(LocalizationExtensionPurpose)), graphql_name='purposes', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )


class HasMetafields(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('metafield', 'metafields', 'private_metafield', 'private_metafields')
    metafield = sgqlc.types.Field('Metafield', graphql_name='metafield', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='namespace', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    metafields = sgqlc.types.Field(sgqlc.types.non_null('MetafieldConnection'), graphql_name='metafields', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    private_metafield = sgqlc.types.Field('PrivateMetafield', graphql_name='privateMetafield', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='namespace', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    private_metafields = sgqlc.types.Field(sgqlc.types.non_null('PrivateMetafieldConnection'), graphql_name='privateMetafields', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )


class HasPublishedTranslations(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('translations',)
    translations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PublishedTranslation'))), graphql_name='translations', args=sgqlc.types.ArgDict((
        ('locale', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='locale', default=None)),
))
    )


class ImageConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ImageEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class ImageEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Image'), graphql_name='node')


class ImageUploadParameter(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class InventoryActivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('inventory_level', 'user_errors')
    inventory_level = sgqlc.types.Field('InventoryLevel', graphql_name='inventoryLevel')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class InventoryAdjustQuantityPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('inventory_level', 'user_errors')
    inventory_level = sgqlc.types.Field('InventoryLevel', graphql_name='inventoryLevel')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class InventoryBulkAdjustQuantityAtLocationPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('inventory_levels', 'user_errors')
    inventory_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('InventoryLevel')), graphql_name='inventoryLevels')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class InventoryDeactivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors',)
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class InventoryItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InventoryItemEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class InventoryItemEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('InventoryItem'), graphql_name='node')


class InventoryItemUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('inventory_item', 'user_errors')
    inventory_item = sgqlc.types.Field('InventoryItem', graphql_name='inventoryItem')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class InventoryLevelConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InventoryLevelEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class InventoryLevelEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('InventoryLevel'), graphql_name='node')


class Job(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('done', 'id', 'query')
    done = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='done')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    query = sgqlc.types.Field('QueryRoot', graphql_name='query')


class KitSkillTriggerRequestPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('conversation_uid', 'user_errors')
    conversation_uid = sgqlc.types.Field(String, graphql_name='conversationUid')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class LegacyInteroperability(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('legacy_resource_id',)
    legacy_resource_id = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='legacyResourceId')


class LimitedPendingOrderCount(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('at_max', 'count')
    at_max = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='atMax')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')


class LineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LineItemEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class LineItemEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('LineItem'), graphql_name='node')


class LineItemMutableConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LineItemMutableEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class LineItemMutableEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('LineItemMutable'), graphql_name='node')


class Locale(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('iso_code', 'name')
    iso_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='isoCode')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class LocalizationExtension(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('country_code', 'purpose', 'title', 'value')
    country_code = sgqlc.types.Field(sgqlc.types.non_null(CountryCode), graphql_name='countryCode')
    purpose = sgqlc.types.Field(sgqlc.types.non_null(LocalizationExtensionPurpose), graphql_name='purpose')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class LocalizationExtensionConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LocalizationExtensionEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class LocalizationExtensionEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(LocalizationExtension), graphql_name='node')


class LocationAddress(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('address1', 'address2', 'city', 'country', 'country_code', 'formatted', 'latitude', 'longitude', 'phone', 'province', 'province_code', 'zip')
    address1 = sgqlc.types.Field(String, graphql_name='address1')
    address2 = sgqlc.types.Field(String, graphql_name='address2')
    city = sgqlc.types.Field(String, graphql_name='city')
    country = sgqlc.types.Field(String, graphql_name='country')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    formatted = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='formatted')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    province_code = sgqlc.types.Field(String, graphql_name='provinceCode')
    zip = sgqlc.types.Field(String, graphql_name='zip')


class LocationConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LocationEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class LocationEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Location'), graphql_name='node')


class LocationSuggestedAddress(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('address1', 'address2', 'city', 'country', 'country_code', 'formatted', 'province', 'province_code', 'zip')
    address1 = sgqlc.types.Field(String, graphql_name='address1')
    address2 = sgqlc.types.Field(String, graphql_name='address2')
    city = sgqlc.types.Field(String, graphql_name='city')
    country = sgqlc.types.Field(String, graphql_name='country')
    country_code = sgqlc.types.Field(CountryCode, graphql_name='countryCode')
    formatted = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='formatted')
    province = sgqlc.types.Field(String, graphql_name='province')
    province_code = sgqlc.types.Field(String, graphql_name='provinceCode')
    zip = sgqlc.types.Field(String, graphql_name='zip')


class MarketingActivityConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MarketingActivityEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class MarketingActivityCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('marketing_activity', 'redirect_path', 'user_errors')
    marketing_activity = sgqlc.types.Field('MarketingActivity', graphql_name='marketingActivity')
    redirect_path = sgqlc.types.Field(String, graphql_name='redirectPath')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class MarketingActivityEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('MarketingActivity'), graphql_name='node')


class MarketingActivityExtensionAppErrors(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code', 'user_errors')
    code = sgqlc.types.Field(sgqlc.types.non_null(MarketingActivityExtensionAppErrorCode), graphql_name='code')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class MarketingActivityUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('marketing_activity', 'redirect_path', 'user_errors')
    marketing_activity = sgqlc.types.Field('MarketingActivity', graphql_name='marketingActivity')
    redirect_path = sgqlc.types.Field(String, graphql_name='redirectPath')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class MarketingBudget(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('budget_type', 'total')
    budget_type = sgqlc.types.Field(sgqlc.types.non_null(MarketingBudgetBudgetType), graphql_name='budgetType')
    total = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='total')


class MarketingEngagement(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('ad_spend', 'clicks_count', 'comments_count', 'complaints_count', 'fails_count', 'favorites_count', 'fetched_at', 'impressions_count', 'is_cumulative', 'marketing_activity', 'occurred_on', 'sends_count', 'shares_count', 'unique_clicks_count', 'unique_views_count', 'unsubscribes_count', 'utc_offset', 'views_count')
    ad_spend = sgqlc.types.Field('MoneyV2', graphql_name='adSpend')
    clicks_count = sgqlc.types.Field(Int, graphql_name='clicksCount')
    comments_count = sgqlc.types.Field(Int, graphql_name='commentsCount')
    complaints_count = sgqlc.types.Field(Int, graphql_name='complaintsCount')
    fails_count = sgqlc.types.Field(Int, graphql_name='failsCount')
    favorites_count = sgqlc.types.Field(Int, graphql_name='favoritesCount')
    fetched_at = sgqlc.types.Field(DateTime, graphql_name='fetchedAt')
    impressions_count = sgqlc.types.Field(Int, graphql_name='impressionsCount')
    is_cumulative = sgqlc.types.Field(Boolean, graphql_name='isCumulative')
    marketing_activity = sgqlc.types.Field(sgqlc.types.non_null('MarketingActivity'), graphql_name='marketingActivity')
    occurred_on = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='occurredOn')
    sends_count = sgqlc.types.Field(Int, graphql_name='sendsCount')
    shares_count = sgqlc.types.Field(Int, graphql_name='sharesCount')
    unique_clicks_count = sgqlc.types.Field(Int, graphql_name='uniqueClicksCount')
    unique_views_count = sgqlc.types.Field(Int, graphql_name='uniqueViewsCount')
    unsubscribes_count = sgqlc.types.Field(Int, graphql_name='unsubscribesCount')
    utc_offset = sgqlc.types.Field(UtcOffset, graphql_name='utcOffset')
    views_count = sgqlc.types.Field(Int, graphql_name='viewsCount')


class MarketingEngagementCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('marketing_engagement', 'user_errors')
    marketing_engagement = sgqlc.types.Field(MarketingEngagement, graphql_name='marketingEngagement')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class MarketingEventConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MarketingEventEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class MarketingEventEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('MarketingEvent'), graphql_name='node')


class Media(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('alt', 'media_content_type', 'media_errors', 'preview', 'status')
    alt = sgqlc.types.Field(String, graphql_name='alt')
    media_content_type = sgqlc.types.Field(sgqlc.types.non_null(MediaContentType), graphql_name='mediaContentType')
    media_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaError'))), graphql_name='mediaErrors')
    preview = sgqlc.types.Field('MediaPreviewImage', graphql_name='preview')
    status = sgqlc.types.Field(sgqlc.types.non_null(MediaStatus), graphql_name='status')


class MediaConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class MediaEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(Media), graphql_name='node')


class MediaError(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code', 'details', 'message')
    code = sgqlc.types.Field(sgqlc.types.non_null(MediaErrorCode), graphql_name='code')
    details = sgqlc.types.Field(String, graphql_name='details')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')


class MediaPreviewImage(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('image', 'status')
    image = sgqlc.types.Field('Image', graphql_name='image')
    status = sgqlc.types.Field(sgqlc.types.non_null(MediaPreviewImageStatus), graphql_name='status')


class MetafieldConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MetafieldEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class MetafieldDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_id', 'user_errors')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class MetafieldEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Metafield'), graphql_name='node')


class MetafieldStorefrontVisibilityConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MetafieldStorefrontVisibilityEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class MetafieldStorefrontVisibilityCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('metafield_storefront_visibility', 'user_errors')
    metafield_storefront_visibility = sgqlc.types.Field('MetafieldStorefrontVisibility', graphql_name='metafieldStorefrontVisibility')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class MetafieldStorefrontVisibilityDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_metafield_storefront_visibility_id', 'user_errors')
    deleted_metafield_storefront_visibility_id = sgqlc.types.Field(ID, graphql_name='deletedMetafieldStorefrontVisibilityId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class MetafieldStorefrontVisibilityEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('MetafieldStorefrontVisibility'), graphql_name='node')


class Model3dSource(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('filesize', 'format', 'mime_type', 'url')
    filesize = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='filesize')
    format = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='format')
    mime_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mimeType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class MoneyBag(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('presentment_money', 'shop_money')
    presentment_money = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='presentmentMoney')
    shop_money = sgqlc.types.Field(sgqlc.types.non_null('MoneyV2'), graphql_name='shopMoney')


class MoneyV2(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'currency_code')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Decimal), graphql_name='amount')
    currency_code = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='currencyCode')


class Mutation(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app_credit_create', 'app_purchase_one_time_create', 'app_subscription_cancel', 'app_subscription_create', 'app_subscription_line_item_update', 'app_usage_record_create', 'bulk_operation_cancel', 'bulk_operation_run_query', 'collection_add_products', 'collection_create', 'collection_delete', 'collection_remove_products', 'collection_reorder_products', 'collection_update', 'customer_add_tax_exemptions', 'customer_create', 'customer_delete', 'customer_generate_account_activation_url', 'customer_remove_tax_exemptions', 'customer_replace_tax_exemptions', 'customer_update', 'customer_update_default_address', 'delivery_profile_create', 'delivery_profile_remove', 'delivery_profile_update', 'delivery_setting_update', 'delivery_shipping_origin_assign', 'discount_automatic_activate', 'discount_automatic_basic_create', 'discount_automatic_basic_update', 'discount_automatic_bulk_delete', 'discount_automatic_bxgy_create', 'discount_automatic_bxgy_update', 'discount_automatic_deactivate', 'discount_automatic_delete', 'discount_code_activate', 'discount_code_basic_create', 'discount_code_basic_update', 'discount_code_bulk_activate', 'discount_code_bulk_deactivate', 'discount_code_bulk_delete', 'discount_code_bxgy_create', 'discount_code_bxgy_update', 'discount_code_deactivate', 'discount_code_delete', 'discount_code_free_shipping_create', 'discount_code_free_shipping_update', 'discount_code_redeem_code_bulk_delete', 'draft_order_calculate', 'draft_order_complete', 'draft_order_create', 'draft_order_delete', 'draft_order_invoice_preview', 'draft_order_invoice_send', 'draft_order_update', 'event_bridge_webhook_subscription_create', 'event_bridge_webhook_subscription_update', 'flow_trigger_receive', 'fulfillment_cancel', 'fulfillment_create_v2', 'fulfillment_order_accept_cancellation_request', 'fulfillment_order_accept_fulfillment_request', 'fulfillment_order_cancel', 'fulfillment_order_close', 'fulfillment_order_move', 'fulfillment_order_reject_cancellation_request', 'fulfillment_order_reject_fulfillment_request', 'fulfillment_order_submit_cancellation_request', 'fulfillment_order_submit_fulfillment_request', 'fulfillment_service_create', 'fulfillment_service_delete', 'fulfillment_service_update', 'fulfillment_tracking_info_update_v2', 'inventory_activate', 'inventory_adjust_quantity', 'inventory_bulk_adjust_quantity_at_location', 'inventory_deactivate', 'inventory_item_update', 'kit_skill_trigger_request', 'marketing_activity_create', 'marketing_activity_update', 'marketing_engagement_create', 'metafield_delete', 'metafield_storefront_visibility_create', 'metafield_storefront_visibility_delete', 'order_capture', 'order_close', 'order_edit_add_custom_item', 'order_edit_add_line_item_discount', 'order_edit_add_variant', 'order_edit_begin', 'order_edit_commit', 'order_edit_remove_line_item_discount', 'order_edit_set_quantity', 'order_mark_as_paid', 'order_open', 'order_update', 'price_rule_activate', 'price_rule_create', 'price_rule_deactivate', 'price_rule_delete', 'price_rule_discount_code_create', 'price_rule_discount_code_update', 'price_rule_update', 'private_metafield_delete', 'private_metafield_upsert', 'product_append_images', 'product_change_status', 'product_create', 'product_create_media', 'product_delete', 'product_delete_images', 'product_delete_media', 'product_duplicate', 'product_image_update', 'product_reorder_images', 'product_reorder_media', 'product_update', 'product_update_media', 'product_variant_append_media', 'product_variant_create', 'product_variant_delete', 'product_variant_detach_media', 'product_variant_update', 'publishable_publish', 'publishable_publish_to_current_channel', 'publishable_unpublish', 'publishable_unpublish_to_current_channel', 'refund_create', 'saved_search_create', 'saved_search_delete', 'saved_search_update', 'script_tag_create', 'script_tag_delete', 'script_tag_update', 'shipping_package_delete', 'shipping_package_make_default', 'shipping_package_update', 'shop_locale_disable', 'shop_locale_enable', 'shop_locale_update', 'shop_policy_update', 'staged_uploads_create', 'storefront_access_token_create', 'storefront_access_token_delete', 'tags_add', 'tags_remove', 'translations_register', 'translations_remove', 'webhook_subscription_create', 'webhook_subscription_delete', 'webhook_subscription_update')
    app_credit_create = sgqlc.types.Field(AppCreditCreatePayload, graphql_name='appCreditCreate', args=sgqlc.types.ArgDict((
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
        ('amount', sgqlc.types.Arg(sgqlc.types.non_null(MoneyInput), graphql_name='amount', default=None)),
        ('test', sgqlc.types.Arg(Boolean, graphql_name='test', default=False)),
))
    )
    app_purchase_one_time_create = sgqlc.types.Field(AppPurchaseOneTimeCreatePayload, graphql_name='appPurchaseOneTimeCreate', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('price', sgqlc.types.Arg(sgqlc.types.non_null(MoneyInput), graphql_name='price', default=None)),
        ('return_url', sgqlc.types.Arg(sgqlc.types.non_null(URL), graphql_name='returnUrl', default=None)),
        ('test', sgqlc.types.Arg(Boolean, graphql_name='test', default=False)),
))
    )
    app_subscription_cancel = sgqlc.types.Field(AppSubscriptionCancelPayload, graphql_name='appSubscriptionCancel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    app_subscription_create = sgqlc.types.Field(AppSubscriptionCreatePayload, graphql_name='appSubscriptionCreate', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('line_items', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AppSubscriptionLineItemInput))), graphql_name='lineItems', default=None)),
        ('test', sgqlc.types.Arg(Boolean, graphql_name='test', default=None)),
        ('trial_days', sgqlc.types.Arg(Int, graphql_name='trialDays', default=None)),
        ('return_url', sgqlc.types.Arg(sgqlc.types.non_null(URL), graphql_name='returnUrl', default=None)),
))
    )
    app_subscription_line_item_update = sgqlc.types.Field(AppSubscriptionLineItemUpdatePayload, graphql_name='appSubscriptionLineItemUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('capped_amount', sgqlc.types.Arg(sgqlc.types.non_null(MoneyInput), graphql_name='cappedAmount', default=None)),
))
    )
    app_usage_record_create = sgqlc.types.Field(AppUsageRecordCreatePayload, graphql_name='appUsageRecordCreate', args=sgqlc.types.ArgDict((
        ('subscription_line_item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='subscriptionLineItemId', default=None)),
        ('price', sgqlc.types.Arg(sgqlc.types.non_null(MoneyInput), graphql_name='price', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
))
    )
    bulk_operation_cancel = sgqlc.types.Field(BulkOperationCancelPayload, graphql_name='bulkOperationCancel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    bulk_operation_run_query = sgqlc.types.Field(BulkOperationRunQueryPayload, graphql_name='bulkOperationRunQuery', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
))
    )
    collection_add_products = sgqlc.types.Field(CollectionAddProductsPayload, graphql_name='collectionAddProducts', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('product_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='productIds', default=None)),
))
    )
    collection_create = sgqlc.types.Field(CollectionCreatePayload, graphql_name='collectionCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CollectionInput), graphql_name='input', default=None)),
))
    )
    collection_delete = sgqlc.types.Field(CollectionDeletePayload, graphql_name='collectionDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CollectionDeleteInput), graphql_name='input', default=None)),
))
    )
    collection_remove_products = sgqlc.types.Field(CollectionRemoveProductsPayload, graphql_name='collectionRemoveProducts', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('product_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='productIds', default=None)),
))
    )
    collection_reorder_products = sgqlc.types.Field(CollectionReorderProductsPayload, graphql_name='collectionReorderProducts', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('moves', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MoveInput))), graphql_name='moves', default=None)),
))
    )
    collection_update = sgqlc.types.Field(CollectionUpdatePayload, graphql_name='collectionUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CollectionInput), graphql_name='input', default=None)),
))
    )
    customer_add_tax_exemptions = sgqlc.types.Field(CustomerAddTaxExemptionsPayload, graphql_name='customerAddTaxExemptions', args=sgqlc.types.ArgDict((
        ('customer_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='customerId', default=None)),
        ('tax_exemptions', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxExemption))), graphql_name='taxExemptions', default=None)),
))
    )
    customer_create = sgqlc.types.Field(CustomerCreatePayload, graphql_name='customerCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerInput), graphql_name='input', default=None)),
))
    )
    customer_delete = sgqlc.types.Field(CustomerDeletePayload, graphql_name='customerDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerDeleteInput), graphql_name='input', default=None)),
))
    )
    customer_generate_account_activation_url = sgqlc.types.Field(CustomerGenerateAccountActivationUrlPayload, graphql_name='customerGenerateAccountActivationUrl', args=sgqlc.types.ArgDict((
        ('customer_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='customerId', default=None)),
))
    )
    customer_remove_tax_exemptions = sgqlc.types.Field(CustomerRemoveTaxExemptionsPayload, graphql_name='customerRemoveTaxExemptions', args=sgqlc.types.ArgDict((
        ('customer_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='customerId', default=None)),
        ('tax_exemptions', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxExemption))), graphql_name='taxExemptions', default=None)),
))
    )
    customer_replace_tax_exemptions = sgqlc.types.Field(CustomerReplaceTaxExemptionsPayload, graphql_name='customerReplaceTaxExemptions', args=sgqlc.types.ArgDict((
        ('customer_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='customerId', default=None)),
        ('tax_exemptions', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxExemption))), graphql_name='taxExemptions', default=None)),
))
    )
    customer_update = sgqlc.types.Field(CustomerUpdatePayload, graphql_name='customerUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CustomerInput), graphql_name='input', default=None)),
))
    )
    customer_update_default_address = sgqlc.types.Field(CustomerUpdateDefaultAddressPayload, graphql_name='customerUpdateDefaultAddress', args=sgqlc.types.ArgDict((
        ('customer_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='customerId', default=None)),
        ('address_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='addressId', default=None)),
))
    )
    delivery_profile_create = sgqlc.types.Field('deliveryProfileCreatePayload', graphql_name='deliveryProfileCreate', args=sgqlc.types.ArgDict((
        ('profile', sgqlc.types.Arg(sgqlc.types.non_null(DeliveryProfileInput), graphql_name='profile', default=None)),
))
    )
    delivery_profile_remove = sgqlc.types.Field('deliveryProfileRemovePayload', graphql_name='deliveryProfileRemove', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delivery_profile_update = sgqlc.types.Field('deliveryProfileUpdatePayload', graphql_name='deliveryProfileUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('profile', sgqlc.types.Arg(sgqlc.types.non_null(DeliveryProfileInput), graphql_name='profile', default=None)),
        ('leave_legacy_mode_profiles', sgqlc.types.Arg(Boolean, graphql_name='leaveLegacyModeProfiles', default=None)),
))
    )
    delivery_setting_update = sgqlc.types.Field(DeliverySettingUpdatePayload, graphql_name='deliverySettingUpdate', args=sgqlc.types.ArgDict((
        ('setting', sgqlc.types.Arg(sgqlc.types.non_null(DeliverySettingInput), graphql_name='setting', default=None)),
))
    )
    delivery_shipping_origin_assign = sgqlc.types.Field(DeliveryShippingOriginAssignPayload, graphql_name='deliveryShippingOriginAssign', args=sgqlc.types.ArgDict((
        ('location_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='locationId', default=None)),
))
    )
    discount_automatic_activate = sgqlc.types.Field(DiscountAutomaticActivatePayload, graphql_name='discountAutomaticActivate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    discount_automatic_basic_create = sgqlc.types.Field(DiscountAutomaticBasicCreatePayload, graphql_name='discountAutomaticBasicCreate', args=sgqlc.types.ArgDict((
        ('automatic_basic_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountAutomaticBasicInput), graphql_name='automaticBasicDiscount', default=None)),
))
    )
    discount_automatic_basic_update = sgqlc.types.Field(DiscountAutomaticBasicUpdatePayload, graphql_name='discountAutomaticBasicUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('automatic_basic_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountAutomaticBasicInput), graphql_name='automaticBasicDiscount', default=None)),
))
    )
    discount_automatic_bulk_delete = sgqlc.types.Field(DiscountAutomaticBulkDeletePayload, graphql_name='discountAutomaticBulkDelete', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    discount_automatic_bxgy_create = sgqlc.types.Field(DiscountAutomaticBxgyCreatePayload, graphql_name='discountAutomaticBxgyCreate', args=sgqlc.types.ArgDict((
        ('automatic_bxgy_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountAutomaticBxgyInput), graphql_name='automaticBxgyDiscount', default=None)),
))
    )
    discount_automatic_bxgy_update = sgqlc.types.Field(DiscountAutomaticBxgyUpdatePayload, graphql_name='discountAutomaticBxgyUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('automatic_bxgy_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountAutomaticBxgyInput), graphql_name='automaticBxgyDiscount', default=None)),
))
    )
    discount_automatic_deactivate = sgqlc.types.Field(DiscountAutomaticDeactivatePayload, graphql_name='discountAutomaticDeactivate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    discount_automatic_delete = sgqlc.types.Field(DiscountAutomaticDeletePayload, graphql_name='discountAutomaticDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    discount_code_activate = sgqlc.types.Field(DiscountCodeActivatePayload, graphql_name='discountCodeActivate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    discount_code_basic_create = sgqlc.types.Field(DiscountCodeBasicCreatePayload, graphql_name='discountCodeBasicCreate', args=sgqlc.types.ArgDict((
        ('basic_code_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountCodeBasicInput), graphql_name='basicCodeDiscount', default=None)),
))
    )
    discount_code_basic_update = sgqlc.types.Field(DiscountCodeBasicUpdatePayload, graphql_name='discountCodeBasicUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('basic_code_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountCodeBasicInput), graphql_name='basicCodeDiscount', default=None)),
))
    )
    discount_code_bulk_activate = sgqlc.types.Field(DiscountCodeBulkActivatePayload, graphql_name='discountCodeBulkActivate', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    discount_code_bulk_deactivate = sgqlc.types.Field(DiscountCodeBulkDeactivatePayload, graphql_name='discountCodeBulkDeactivate', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    discount_code_bulk_delete = sgqlc.types.Field(DiscountCodeBulkDeletePayload, graphql_name='discountCodeBulkDelete', args=sgqlc.types.ArgDict((
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    discount_code_bxgy_create = sgqlc.types.Field(DiscountCodeBxgyCreatePayload, graphql_name='discountCodeBxgyCreate', args=sgqlc.types.ArgDict((
        ('bxgy_code_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountCodeBxgyInput), graphql_name='bxgyCodeDiscount', default=None)),
))
    )
    discount_code_bxgy_update = sgqlc.types.Field(DiscountCodeBxgyUpdatePayload, graphql_name='discountCodeBxgyUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('bxgy_code_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountCodeBxgyInput), graphql_name='bxgyCodeDiscount', default=None)),
))
    )
    discount_code_deactivate = sgqlc.types.Field(DiscountCodeDeactivatePayload, graphql_name='discountCodeDeactivate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    discount_code_delete = sgqlc.types.Field(DiscountCodeDeletePayload, graphql_name='discountCodeDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    discount_code_free_shipping_create = sgqlc.types.Field(DiscountCodeFreeShippingCreatePayload, graphql_name='discountCodeFreeShippingCreate', args=sgqlc.types.ArgDict((
        ('free_shipping_code_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountCodeFreeShippingInput), graphql_name='freeShippingCodeDiscount', default=None)),
))
    )
    discount_code_free_shipping_update = sgqlc.types.Field(DiscountCodeFreeShippingUpdatePayload, graphql_name='discountCodeFreeShippingUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('free_shipping_code_discount', sgqlc.types.Arg(sgqlc.types.non_null(DiscountCodeFreeShippingInput), graphql_name='freeShippingCodeDiscount', default=None)),
))
    )
    discount_code_redeem_code_bulk_delete = sgqlc.types.Field(DiscountCodeRedeemCodeBulkDeletePayload, graphql_name='discountCodeRedeemCodeBulkDelete', args=sgqlc.types.ArgDict((
        ('discount_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='discountId', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    draft_order_calculate = sgqlc.types.Field(DraftOrderCalculatePayload, graphql_name='draftOrderCalculate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DraftOrderInput), graphql_name='input', default=None)),
))
    )
    draft_order_complete = sgqlc.types.Field(DraftOrderCompletePayload, graphql_name='draftOrderComplete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('payment_pending', sgqlc.types.Arg(Boolean, graphql_name='paymentPending', default=False)),
))
    )
    draft_order_create = sgqlc.types.Field(DraftOrderCreatePayload, graphql_name='draftOrderCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DraftOrderInput), graphql_name='input', default=None)),
))
    )
    draft_order_delete = sgqlc.types.Field(DraftOrderDeletePayload, graphql_name='draftOrderDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DraftOrderDeleteInput), graphql_name='input', default=None)),
))
    )
    draft_order_invoice_preview = sgqlc.types.Field(DraftOrderInvoicePreviewPayload, graphql_name='draftOrderInvoicePreview', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('email', sgqlc.types.Arg(EmailInput, graphql_name='email', default=None)),
))
    )
    draft_order_invoice_send = sgqlc.types.Field(DraftOrderInvoiceSendPayload, graphql_name='draftOrderInvoiceSend', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('email', sgqlc.types.Arg(EmailInput, graphql_name='email', default=None)),
))
    )
    draft_order_update = sgqlc.types.Field(DraftOrderUpdatePayload, graphql_name='draftOrderUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DraftOrderInput), graphql_name='input', default=None)),
))
    )
    event_bridge_webhook_subscription_create = sgqlc.types.Field(EventBridgeWebhookSubscriptionCreatePayload, graphql_name='eventBridgeWebhookSubscriptionCreate', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(WebhookSubscriptionTopic), graphql_name='topic', default=None)),
        ('webhook_subscription', sgqlc.types.Arg(sgqlc.types.non_null(EventBridgeWebhookSubscriptionInput), graphql_name='webhookSubscription', default=None)),
))
    )
    event_bridge_webhook_subscription_update = sgqlc.types.Field(EventBridgeWebhookSubscriptionUpdatePayload, graphql_name='eventBridgeWebhookSubscriptionUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('webhook_subscription', sgqlc.types.Arg(sgqlc.types.non_null(EventBridgeWebhookSubscriptionInput), graphql_name='webhookSubscription', default=None)),
))
    )
    flow_trigger_receive = sgqlc.types.Field(FlowTriggerReceivePayload, graphql_name='flowTriggerReceive', args=sgqlc.types.ArgDict((
        ('body', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='body', default=None)),
))
    )
    fulfillment_cancel = sgqlc.types.Field(FulfillmentCancelPayload, graphql_name='fulfillmentCancel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    fulfillment_create_v2 = sgqlc.types.Field(FulfillmentCreateV2Payload, graphql_name='fulfillmentCreateV2', args=sgqlc.types.ArgDict((
        ('fulfillment', sgqlc.types.Arg(sgqlc.types.non_null(FulfillmentV2Input), graphql_name='fulfillment', default=None)),
        ('message', sgqlc.types.Arg(String, graphql_name='message', default=None)),
))
    )
    fulfillment_order_accept_cancellation_request = sgqlc.types.Field(FulfillmentOrderAcceptCancellationRequestPayload, graphql_name='fulfillmentOrderAcceptCancellationRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('message', sgqlc.types.Arg(String, graphql_name='message', default=None)),
))
    )
    fulfillment_order_accept_fulfillment_request = sgqlc.types.Field(FulfillmentOrderAcceptFulfillmentRequestPayload, graphql_name='fulfillmentOrderAcceptFulfillmentRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('message', sgqlc.types.Arg(String, graphql_name='message', default=None)),
))
    )
    fulfillment_order_cancel = sgqlc.types.Field(FulfillmentOrderCancelPayload, graphql_name='fulfillmentOrderCancel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    fulfillment_order_close = sgqlc.types.Field(FulfillmentOrderClosePayload, graphql_name='fulfillmentOrderClose', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('message', sgqlc.types.Arg(String, graphql_name='message', default=None)),
))
    )
    fulfillment_order_move = sgqlc.types.Field(FulfillmentOrderMovePayload, graphql_name='fulfillmentOrderMove', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('new_location_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='newLocationId', default=None)),
))
    )
    fulfillment_order_reject_cancellation_request = sgqlc.types.Field(FulfillmentOrderRejectCancellationRequestPayload, graphql_name='fulfillmentOrderRejectCancellationRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('message', sgqlc.types.Arg(String, graphql_name='message', default=None)),
))
    )
    fulfillment_order_reject_fulfillment_request = sgqlc.types.Field(FulfillmentOrderRejectFulfillmentRequestPayload, graphql_name='fulfillmentOrderRejectFulfillmentRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('message', sgqlc.types.Arg(String, graphql_name='message', default=None)),
))
    )
    fulfillment_order_submit_cancellation_request = sgqlc.types.Field(FulfillmentOrderSubmitCancellationRequestPayload, graphql_name='fulfillmentOrderSubmitCancellationRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('message', sgqlc.types.Arg(String, graphql_name='message', default=None)),
))
    )
    fulfillment_order_submit_fulfillment_request = sgqlc.types.Field(FulfillmentOrderSubmitFulfillmentRequestPayload, graphql_name='fulfillmentOrderSubmitFulfillmentRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('message', sgqlc.types.Arg(String, graphql_name='message', default=None)),
        ('notify_customer', sgqlc.types.Arg(Boolean, graphql_name='notifyCustomer', default=None)),
        ('fulfillment_order_line_items', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(FulfillmentOrderLineItemInput)), graphql_name='fulfillmentOrderLineItems', default=None)),
        ('shipping_method', sgqlc.types.Arg(String, graphql_name='shippingMethod', default=None)),
))
    )
    fulfillment_service_create = sgqlc.types.Field(FulfillmentServiceCreatePayload, graphql_name='fulfillmentServiceCreate', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
        ('callback_url', sgqlc.types.Arg(URL, graphql_name='callbackUrl', default=None)),
        ('tracking_support', sgqlc.types.Arg(Boolean, graphql_name='trackingSupport', default=False)),
))
    )
    fulfillment_service_delete = sgqlc.types.Field(FulfillmentServiceDeletePayload, graphql_name='fulfillmentServiceDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('destination_location_id', sgqlc.types.Arg(ID, graphql_name='destinationLocationId', default=None)),
))
    )
    fulfillment_service_update = sgqlc.types.Field(FulfillmentServiceUpdatePayload, graphql_name='fulfillmentServiceUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
        ('callback_url', sgqlc.types.Arg(URL, graphql_name='callbackUrl', default=None)),
        ('tracking_support', sgqlc.types.Arg(Boolean, graphql_name='trackingSupport', default=None)),
        ('fulfillment_orders_opt_in', sgqlc.types.Arg(Boolean, graphql_name='fulfillmentOrdersOptIn', default=None)),
))
    )
    fulfillment_tracking_info_update_v2 = sgqlc.types.Field(FulfillmentTrackingInfoUpdateV2Payload, graphql_name='fulfillmentTrackingInfoUpdateV2', args=sgqlc.types.ArgDict((
        ('fulfillment_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='fulfillmentId', default=None)),
        ('tracking_info_input', sgqlc.types.Arg(sgqlc.types.non_null(FulfillmentTrackingInput), graphql_name='trackingInfoInput', default=None)),
        ('notify_customer', sgqlc.types.Arg(Boolean, graphql_name='notifyCustomer', default=None)),
))
    )
    inventory_activate = sgqlc.types.Field(InventoryActivatePayload, graphql_name='inventoryActivate', args=sgqlc.types.ArgDict((
        ('inventory_item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='inventoryItemId', default=None)),
        ('location_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='locationId', default=None)),
        ('available', sgqlc.types.Arg(Int, graphql_name='available', default=None)),
))
    )
    inventory_adjust_quantity = sgqlc.types.Field(InventoryAdjustQuantityPayload, graphql_name='inventoryAdjustQuantity', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InventoryAdjustQuantityInput), graphql_name='input', default=None)),
))
    )
    inventory_bulk_adjust_quantity_at_location = sgqlc.types.Field(InventoryBulkAdjustQuantityAtLocationPayload, graphql_name='inventoryBulkAdjustQuantityAtLocation', args=sgqlc.types.ArgDict((
        ('inventory_item_adjustments', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InventoryAdjustItemInput))), graphql_name='inventoryItemAdjustments', default=None)),
        ('location_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='locationId', default=None)),
))
    )
    inventory_deactivate = sgqlc.types.Field(InventoryDeactivatePayload, graphql_name='inventoryDeactivate', args=sgqlc.types.ArgDict((
        ('inventory_level_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='inventoryLevelId', default=None)),
))
    )
    inventory_item_update = sgqlc.types.Field(InventoryItemUpdatePayload, graphql_name='inventoryItemUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InventoryItemUpdateInput), graphql_name='input', default=None)),
))
    )
    kit_skill_trigger_request = sgqlc.types.Field(KitSkillTriggerRequestPayload, graphql_name='kitSkillTriggerRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('locale', sgqlc.types.Arg(sgqlc.types.non_null(KitSkillLocale), graphql_name='locale', default=None)),
        ('placeholders', sgqlc.types.Arg(JSON, graphql_name='placeholders', default='{}')),
))
    )
    marketing_activity_create = sgqlc.types.Field(MarketingActivityCreatePayload, graphql_name='marketingActivityCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MarketingActivityCreateInput), graphql_name='input', default=None)),
))
    )
    marketing_activity_update = sgqlc.types.Field(MarketingActivityUpdatePayload, graphql_name='marketingActivityUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MarketingActivityUpdateInput), graphql_name='input', default=None)),
))
    )
    marketing_engagement_create = sgqlc.types.Field(MarketingEngagementCreatePayload, graphql_name='marketingEngagementCreate', args=sgqlc.types.ArgDict((
        ('marketing_activity_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='marketingActivityId', default=None)),
        ('marketing_engagement', sgqlc.types.Arg(sgqlc.types.non_null(MarketingEngagementInput), graphql_name='marketingEngagement', default=None)),
))
    )
    metafield_delete = sgqlc.types.Field(MetafieldDeletePayload, graphql_name='metafieldDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MetafieldDeleteInput), graphql_name='input', default=None)),
))
    )
    metafield_storefront_visibility_create = sgqlc.types.Field(MetafieldStorefrontVisibilityCreatePayload, graphql_name='metafieldStorefrontVisibilityCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MetafieldStorefrontVisibilityInput), graphql_name='input', default=None)),
))
    )
    metafield_storefront_visibility_delete = sgqlc.types.Field(MetafieldStorefrontVisibilityDeletePayload, graphql_name='metafieldStorefrontVisibilityDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    order_capture = sgqlc.types.Field('OrderCapturePayload', graphql_name='orderCapture', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrderCaptureInput), graphql_name='input', default=None)),
))
    )
    order_close = sgqlc.types.Field('OrderClosePayload', graphql_name='orderClose', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrderCloseInput), graphql_name='input', default=None)),
))
    )
    order_edit_add_custom_item = sgqlc.types.Field('OrderEditAddCustomItemPayload', graphql_name='orderEditAddCustomItem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('location_id', sgqlc.types.Arg(ID, graphql_name='locationId', default=None)),
        ('price', sgqlc.types.Arg(sgqlc.types.non_null(MoneyInput), graphql_name='price', default=None)),
        ('quantity', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='quantity', default=None)),
        ('taxable', sgqlc.types.Arg(Boolean, graphql_name='taxable', default=None)),
        ('requires_shipping', sgqlc.types.Arg(Boolean, graphql_name='requiresShipping', default=None)),
))
    )
    order_edit_add_line_item_discount = sgqlc.types.Field('OrderEditAddLineItemDiscountPayload', graphql_name='orderEditAddLineItemDiscount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('line_item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='lineItemId', default=None)),
        ('discount', sgqlc.types.Arg(sgqlc.types.non_null(OrderEditAppliedDiscountInput), graphql_name='discount', default=None)),
))
    )
    order_edit_add_variant = sgqlc.types.Field('OrderEditAddVariantPayload', graphql_name='orderEditAddVariant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('variant_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='variantId', default=None)),
        ('location_id', sgqlc.types.Arg(ID, graphql_name='locationId', default=None)),
        ('quantity', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='quantity', default=None)),
        ('allow_duplicates', sgqlc.types.Arg(Boolean, graphql_name='allowDuplicates', default=None)),
))
    )
    order_edit_begin = sgqlc.types.Field('OrderEditBeginPayload', graphql_name='orderEditBegin', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    order_edit_commit = sgqlc.types.Field('OrderEditCommitPayload', graphql_name='orderEditCommit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('notify_customer', sgqlc.types.Arg(Boolean, graphql_name='notifyCustomer', default=None)),
        ('staff_note', sgqlc.types.Arg(String, graphql_name='staffNote', default=None)),
))
    )
    order_edit_remove_line_item_discount = sgqlc.types.Field('OrderEditRemoveLineItemDiscountPayload', graphql_name='orderEditRemoveLineItemDiscount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('discount_application_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='discountApplicationId', default=None)),
))
    )
    order_edit_set_quantity = sgqlc.types.Field('OrderEditSetQuantityPayload', graphql_name='orderEditSetQuantity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('line_item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='lineItemId', default=None)),
        ('quantity', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='quantity', default=None)),
        ('restock', sgqlc.types.Arg(Boolean, graphql_name='restock', default=None)),
        ('location_id', sgqlc.types.Arg(ID, graphql_name='locationId', default=None)),
))
    )
    order_mark_as_paid = sgqlc.types.Field('OrderMarkAsPaidPayload', graphql_name='orderMarkAsPaid', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrderMarkAsPaidInput), graphql_name='input', default=None)),
))
    )
    order_open = sgqlc.types.Field('OrderOpenPayload', graphql_name='orderOpen', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrderOpenInput), graphql_name='input', default=None)),
))
    )
    order_update = sgqlc.types.Field('OrderUpdatePayload', graphql_name='orderUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(OrderInput), graphql_name='input', default=None)),
))
    )
    price_rule_activate = sgqlc.types.Field('PriceRuleActivatePayload', graphql_name='priceRuleActivate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    price_rule_create = sgqlc.types.Field('PriceRuleCreatePayload', graphql_name='priceRuleCreate', args=sgqlc.types.ArgDict((
        ('price_rule', sgqlc.types.Arg(sgqlc.types.non_null(PriceRuleInput), graphql_name='priceRule', default=None)),
        ('price_rule_discount_code', sgqlc.types.Arg(PriceRuleDiscountCodeInput, graphql_name='priceRuleDiscountCode', default=None)),
))
    )
    price_rule_deactivate = sgqlc.types.Field('PriceRuleDeactivatePayload', graphql_name='priceRuleDeactivate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    price_rule_delete = sgqlc.types.Field('PriceRuleDeletePayload', graphql_name='priceRuleDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    price_rule_discount_code_create = sgqlc.types.Field('PriceRuleDiscountCodeCreatePayload', graphql_name='priceRuleDiscountCodeCreate', args=sgqlc.types.ArgDict((
        ('price_rule_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='priceRuleId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    price_rule_discount_code_update = sgqlc.types.Field('PriceRuleDiscountCodeUpdatePayload', graphql_name='priceRuleDiscountCodeUpdate', args=sgqlc.types.ArgDict((
        ('price_rule_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='priceRuleId', default=None)),
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    price_rule_update = sgqlc.types.Field('PriceRuleUpdatePayload', graphql_name='priceRuleUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('price_rule', sgqlc.types.Arg(sgqlc.types.non_null(PriceRuleInput), graphql_name='priceRule', default=None)),
        ('price_rule_discount_code', sgqlc.types.Arg(PriceRuleDiscountCodeInput, graphql_name='priceRuleDiscountCode', default=None)),
))
    )
    private_metafield_delete = sgqlc.types.Field('PrivateMetafieldDeletePayload', graphql_name='privateMetafieldDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PrivateMetafieldDeleteInput), graphql_name='input', default=None)),
))
    )
    private_metafield_upsert = sgqlc.types.Field('PrivateMetafieldUpsertPayload', graphql_name='privateMetafieldUpsert', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PrivateMetafieldInput), graphql_name='input', default=None)),
))
    )
    product_append_images = sgqlc.types.Field('ProductAppendImagesPayload', graphql_name='productAppendImages', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProductAppendImagesInput), graphql_name='input', default=None)),
))
    )
    product_change_status = sgqlc.types.Field('ProductChangeStatusPayload', graphql_name='productChangeStatus', args=sgqlc.types.ArgDict((
        ('product_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='productId', default=None)),
        ('status', sgqlc.types.Arg(sgqlc.types.non_null(ProductStatus), graphql_name='status', default=None)),
))
    )
    product_create = sgqlc.types.Field('ProductCreatePayload', graphql_name='productCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProductInput), graphql_name='input', default=None)),
        ('media', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateMediaInput)), graphql_name='media', default=None)),
))
    )
    product_create_media = sgqlc.types.Field('ProductCreateMediaPayload', graphql_name='productCreateMedia', args=sgqlc.types.ArgDict((
        ('product_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='productId', default=None)),
        ('media', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateMediaInput))), graphql_name='media', default=None)),
))
    )
    product_delete = sgqlc.types.Field('ProductDeletePayload', graphql_name='productDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProductDeleteInput), graphql_name='input', default=None)),
))
    )
    product_delete_images = sgqlc.types.Field('ProductDeleteImagesPayload', graphql_name='productDeleteImages', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('image_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='imageIds', default=None)),
))
    )
    product_delete_media = sgqlc.types.Field('ProductDeleteMediaPayload', graphql_name='productDeleteMedia', args=sgqlc.types.ArgDict((
        ('product_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='productId', default=None)),
        ('media_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='mediaIds', default=None)),
))
    )
    product_duplicate = sgqlc.types.Field('ProductDuplicatePayload', graphql_name='productDuplicate', args=sgqlc.types.ArgDict((
        ('product_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='productId', default=None)),
        ('new_title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='newTitle', default=None)),
        ('new_status', sgqlc.types.Arg(ProductStatus, graphql_name='newStatus', default=None)),
        ('include_images', sgqlc.types.Arg(Boolean, graphql_name='includeImages', default=False)),
))
    )
    product_image_update = sgqlc.types.Field('ProductImageUpdatePayload', graphql_name='productImageUpdate', args=sgqlc.types.ArgDict((
        ('product_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='productId', default=None)),
        ('image', sgqlc.types.Arg(sgqlc.types.non_null(ImageInput), graphql_name='image', default=None)),
))
    )
    product_reorder_images = sgqlc.types.Field('ProductReorderImagesPayload', graphql_name='productReorderImages', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('moves', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MoveInput))), graphql_name='moves', default=None)),
))
    )
    product_reorder_media = sgqlc.types.Field('ProductReorderMediaPayload', graphql_name='productReorderMedia', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('moves', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MoveInput))), graphql_name='moves', default=None)),
))
    )
    product_update = sgqlc.types.Field('ProductUpdatePayload', graphql_name='productUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProductInput), graphql_name='input', default=None)),
))
    )
    product_update_media = sgqlc.types.Field('ProductUpdateMediaPayload', graphql_name='productUpdateMedia', args=sgqlc.types.ArgDict((
        ('product_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='productId', default=None)),
        ('media', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UpdateMediaInput))), graphql_name='media', default=None)),
))
    )
    product_variant_append_media = sgqlc.types.Field('ProductVariantAppendMediaPayload', graphql_name='productVariantAppendMedia', args=sgqlc.types.ArgDict((
        ('product_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='productId', default=None)),
        ('variant_media', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductVariantAppendMediaInput))), graphql_name='variantMedia', default=None)),
))
    )
    product_variant_create = sgqlc.types.Field('ProductVariantCreatePayload', graphql_name='productVariantCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProductVariantInput), graphql_name='input', default=None)),
))
    )
    product_variant_delete = sgqlc.types.Field('ProductVariantDeletePayload', graphql_name='productVariantDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    product_variant_detach_media = sgqlc.types.Field('ProductVariantDetachMediaPayload', graphql_name='productVariantDetachMedia', args=sgqlc.types.ArgDict((
        ('product_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='productId', default=None)),
        ('variant_media', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductVariantDetachMediaInput))), graphql_name='variantMedia', default=None)),
))
    )
    product_variant_update = sgqlc.types.Field('ProductVariantUpdatePayload', graphql_name='productVariantUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ProductVariantInput), graphql_name='input', default=None)),
))
    )
    publishable_publish = sgqlc.types.Field('PublishablePublishPayload', graphql_name='publishablePublish', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PublicationInput))), graphql_name='input', default=None)),
))
    )
    publishable_publish_to_current_channel = sgqlc.types.Field('PublishablePublishToCurrentChannelPayload', graphql_name='publishablePublishToCurrentChannel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    publishable_unpublish = sgqlc.types.Field('PublishableUnpublishPayload', graphql_name='publishableUnpublish', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PublicationInput))), graphql_name='input', default=None)),
))
    )
    publishable_unpublish_to_current_channel = sgqlc.types.Field('PublishableUnpublishToCurrentChannelPayload', graphql_name='publishableUnpublishToCurrentChannel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    refund_create = sgqlc.types.Field('RefundCreatePayload', graphql_name='refundCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RefundInput), graphql_name='input', default=None)),
))
    )
    saved_search_create = sgqlc.types.Field('SavedSearchCreatePayload', graphql_name='savedSearchCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SavedSearchCreateInput), graphql_name='input', default=None)),
))
    )
    saved_search_delete = sgqlc.types.Field('SavedSearchDeletePayload', graphql_name='savedSearchDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SavedSearchDeleteInput), graphql_name='input', default=None)),
))
    )
    saved_search_update = sgqlc.types.Field('SavedSearchUpdatePayload', graphql_name='savedSearchUpdate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SavedSearchUpdateInput), graphql_name='input', default=None)),
))
    )
    script_tag_create = sgqlc.types.Field('ScriptTagCreatePayload', graphql_name='scriptTagCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ScriptTagInput), graphql_name='input', default=None)),
))
    )
    script_tag_delete = sgqlc.types.Field('ScriptTagDeletePayload', graphql_name='scriptTagDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    script_tag_update = sgqlc.types.Field('ScriptTagUpdatePayload', graphql_name='scriptTagUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ScriptTagInput), graphql_name='input', default=None)),
))
    )
    shipping_package_delete = sgqlc.types.Field('ShippingPackageDeletePayload', graphql_name='shippingPackageDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    shipping_package_make_default = sgqlc.types.Field('ShippingPackageMakeDefaultPayload', graphql_name='shippingPackageMakeDefault', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    shipping_package_update = sgqlc.types.Field('ShippingPackageUpdatePayload', graphql_name='shippingPackageUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    shop_locale_disable = sgqlc.types.Field('ShopLocaleDisablePayload', graphql_name='shopLocaleDisable', args=sgqlc.types.ArgDict((
        ('locale', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='locale', default=None)),
))
    )
    shop_locale_enable = sgqlc.types.Field('ShopLocaleEnablePayload', graphql_name='shopLocaleEnable', args=sgqlc.types.ArgDict((
        ('locale', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='locale', default=None)),
))
    )
    shop_locale_update = sgqlc.types.Field('ShopLocaleUpdatePayload', graphql_name='shopLocaleUpdate', args=sgqlc.types.ArgDict((
        ('locale', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='locale', default=None)),
        ('shop_locale', sgqlc.types.Arg(sgqlc.types.non_null(ShopLocaleInput), graphql_name='shopLocale', default=None)),
))
    )
    shop_policy_update = sgqlc.types.Field('ShopPolicyUpdatePayload', graphql_name='shopPolicyUpdate', args=sgqlc.types.ArgDict((
        ('shop_policy', sgqlc.types.Arg(sgqlc.types.non_null(ShopPolicyInput), graphql_name='shopPolicy', default=None)),
))
    )
    staged_uploads_create = sgqlc.types.Field('StagedUploadsCreatePayload', graphql_name='stagedUploadsCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(StagedUploadInput))), graphql_name='input', default=None)),
))
    )
    storefront_access_token_create = sgqlc.types.Field('StorefrontAccessTokenCreatePayload', graphql_name='storefrontAccessTokenCreate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StorefrontAccessTokenInput), graphql_name='input', default=None)),
))
    )
    storefront_access_token_delete = sgqlc.types.Field('StorefrontAccessTokenDeletePayload', graphql_name='storefrontAccessTokenDelete', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StorefrontAccessTokenDeleteInput), graphql_name='input', default=None)),
))
    )
    tags_add = sgqlc.types.Field('TagsAddPayload', graphql_name='tagsAdd', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
))
    )
    tags_remove = sgqlc.types.Field('TagsRemovePayload', graphql_name='tagsRemove', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
))
    )
    translations_register = sgqlc.types.Field('TranslationsRegisterPayload', graphql_name='translationsRegister', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='resourceId', default=None)),
        ('translations', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TranslationInput))), graphql_name='translations', default=None)),
))
    )
    translations_remove = sgqlc.types.Field('TranslationsRemovePayload', graphql_name='translationsRemove', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='resourceId', default=None)),
        ('translation_keys', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='translationKeys', default=None)),
        ('locales', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='locales', default=None)),
))
    )
    webhook_subscription_create = sgqlc.types.Field('WebhookSubscriptionCreatePayload', graphql_name='webhookSubscriptionCreate', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(WebhookSubscriptionTopic), graphql_name='topic', default=None)),
        ('webhook_subscription', sgqlc.types.Arg(sgqlc.types.non_null(WebhookSubscriptionInput), graphql_name='webhookSubscription', default=None)),
))
    )
    webhook_subscription_delete = sgqlc.types.Field('WebhookSubscriptionDeletePayload', graphql_name='webhookSubscriptionDelete', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    webhook_subscription_update = sgqlc.types.Field('WebhookSubscriptionUpdatePayload', graphql_name='webhookSubscriptionUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('webhook_subscription', sgqlc.types.Arg(sgqlc.types.non_null(WebhookSubscriptionInput), graphql_name='webhookSubscription', default=None)),
))
    )


class MutationsStagedUploadTargetGenerateUploadParameter(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class Navigable(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('default_cursor',)
    default_cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='defaultCursor')


class NavigationItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('id', 'title', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class Node(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OnlineStorePreviewable(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('online_store_preview_url',)
    online_store_preview_url = sgqlc.types.Field(URL, graphql_name='onlineStorePreviewUrl')


class OrderCapturePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('transaction', 'user_errors')
    transaction = sgqlc.types.Field('OrderTransaction', graphql_name='transaction')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderClosePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('order', 'user_errors')
    order = sgqlc.types.Field('Order', graphql_name='order')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrderEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class OrderEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Order'), graphql_name='node')


class OrderEditAddCustomItemPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('calculated_line_item', 'calculated_order', 'user_errors')
    calculated_line_item = sgqlc.types.Field(CalculatedLineItem, graphql_name='calculatedLineItem')
    calculated_order = sgqlc.types.Field('CalculatedOrder', graphql_name='calculatedOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderEditAddLineItemDiscountPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('added_discount_staged_change', 'calculated_line_item', 'calculated_order', 'user_errors')
    added_discount_staged_change = sgqlc.types.Field('OrderStagedChangeAddLineItemDiscount', graphql_name='addedDiscountStagedChange')
    calculated_line_item = sgqlc.types.Field(CalculatedLineItem, graphql_name='calculatedLineItem')
    calculated_order = sgqlc.types.Field('CalculatedOrder', graphql_name='calculatedOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderEditAddVariantPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('calculated_line_item', 'calculated_order', 'user_errors')
    calculated_line_item = sgqlc.types.Field(CalculatedLineItem, graphql_name='calculatedLineItem')
    calculated_order = sgqlc.types.Field('CalculatedOrder', graphql_name='calculatedOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderEditBeginPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('calculated_order', 'user_errors')
    calculated_order = sgqlc.types.Field('CalculatedOrder', graphql_name='calculatedOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderEditCommitPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('order', 'user_errors')
    order = sgqlc.types.Field('Order', graphql_name='order')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderEditRemoveLineItemDiscountPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('calculated_line_item', 'calculated_order', 'user_errors')
    calculated_line_item = sgqlc.types.Field(CalculatedLineItem, graphql_name='calculatedLineItem')
    calculated_order = sgqlc.types.Field('CalculatedOrder', graphql_name='calculatedOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderEditSetQuantityPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('calculated_line_item', 'calculated_order', 'user_errors')
    calculated_line_item = sgqlc.types.Field(CalculatedLineItem, graphql_name='calculatedLineItem')
    calculated_order = sgqlc.types.Field('CalculatedOrder', graphql_name='calculatedOrder')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderMarkAsPaidPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('order', 'user_errors')
    order = sgqlc.types.Field('Order', graphql_name='order')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderOpenPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('order', 'user_errors')
    order = sgqlc.types.Field('Order', graphql_name='order')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class OrderPaymentCollectionDetails(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('additional_payment_collection_url',)
    additional_payment_collection_url = sgqlc.types.Field(URL, graphql_name='additionalPaymentCollectionUrl')


class OrderRisk(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('display', 'level', 'message')
    display = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='display')
    level = sgqlc.types.Field(OrderRiskLevel, graphql_name='level')
    message = sgqlc.types.Field(String, graphql_name='message')


class OrderStagedChangeAddCustomItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('original_unit_price', 'quantity', 'title')
    original_unit_price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='originalUnitPrice')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class OrderStagedChangeAddLineItemDiscount(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('description', 'id', 'value')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    value = sgqlc.types.Field(sgqlc.types.non_null('PricingValue'), graphql_name='value')


class OrderStagedChangeAddShippingLine(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('phone', 'presentment_title', 'price', 'title')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    presentment_title = sgqlc.types.Field(String, graphql_name='presentmentTitle')
    price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='price')
    title = sgqlc.types.Field(String, graphql_name='title')


class OrderStagedChangeAddVariant(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('quantity', 'variant')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    variant = sgqlc.types.Field(sgqlc.types.non_null('ProductVariant'), graphql_name='variant')


class OrderStagedChangeConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrderStagedChangeEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class OrderStagedChangeDecrementItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('delta', 'line_item', 'restock')
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='delta')
    line_item = sgqlc.types.Field(sgqlc.types.non_null('LineItem'), graphql_name='lineItem')
    restock = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restock')


class OrderStagedChangeEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('OrderStagedChange'), graphql_name='node')


class OrderStagedChangeIncrementItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('delta', 'line_item')
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='delta')
    line_item = sgqlc.types.Field(sgqlc.types.non_null('LineItem'), graphql_name='lineItem')


class OrderTransactionConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrderTransactionEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class OrderTransactionEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('OrderTransaction'), graphql_name='node')


class OrderUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('order', 'user_errors')
    order = sgqlc.types.Field('Order', graphql_name='order')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class PageInfo(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('has_next_page', 'has_previous_page')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')


class PaymentSettings(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('supported_digital_wallets',)
    supported_digital_wallets = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DigitalWallet))), graphql_name='supportedDigitalWallets')


class PriceRuleActivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('price_rule', 'price_rule_user_errors')
    price_rule = sgqlc.types.Field('PriceRule', graphql_name='priceRule')
    price_rule_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleUserError'))), graphql_name='priceRuleUserErrors')


class PriceRuleConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PriceRuleCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('price_rule', 'price_rule_discount_code', 'price_rule_user_errors')
    price_rule = sgqlc.types.Field('PriceRule', graphql_name='priceRule')
    price_rule_discount_code = sgqlc.types.Field('PriceRuleDiscountCode', graphql_name='priceRuleDiscountCode')
    price_rule_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleUserError'))), graphql_name='priceRuleUserErrors')


class PriceRuleCustomerSelection(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('customers', 'for_all_customers', 'saved_searches')
    customers = sgqlc.types.Field(sgqlc.types.non_null(CustomerConnection), graphql_name='customers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(CustomerSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    for_all_customers = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='forAllCustomers')
    saved_searches = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SavedSearch'))), graphql_name='savedSearches')


class PriceRuleDeactivatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('price_rule', 'price_rule_user_errors')
    price_rule = sgqlc.types.Field('PriceRule', graphql_name='priceRule')
    price_rule_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleUserError'))), graphql_name='priceRuleUserErrors')


class PriceRuleDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_price_rule_id', 'price_rule_user_errors', 'shop')
    deleted_price_rule_id = sgqlc.types.Field(ID, graphql_name='deletedPriceRuleId')
    price_rule_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleUserError'))), graphql_name='priceRuleUserErrors')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')


class PriceRuleDiscountCodeConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleDiscountCodeEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PriceRuleDiscountCodeCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('price_rule', 'price_rule_discount_code', 'price_rule_user_errors')
    price_rule = sgqlc.types.Field('PriceRule', graphql_name='priceRule')
    price_rule_discount_code = sgqlc.types.Field('PriceRuleDiscountCode', graphql_name='priceRuleDiscountCode')
    price_rule_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleUserError'))), graphql_name='priceRuleUserErrors')


class PriceRuleDiscountCodeEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PriceRuleDiscountCode'), graphql_name='node')


class PriceRuleDiscountCodeUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('price_rule', 'price_rule_discount_code', 'price_rule_user_errors')
    price_rule = sgqlc.types.Field('PriceRule', graphql_name='priceRule')
    price_rule_discount_code = sgqlc.types.Field('PriceRuleDiscountCode', graphql_name='priceRuleDiscountCode')
    price_rule_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleUserError'))), graphql_name='priceRuleUserErrors')


class PriceRuleEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PriceRule'), graphql_name='node')


class PriceRuleEntitlementToPrerequisiteQuantityRatio(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('entitlement_quantity', 'prerequisite_quantity')
    entitlement_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='entitlementQuantity')
    prerequisite_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='prerequisiteQuantity')


class PriceRuleFixedAmountValue(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('amount',)
    amount = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='amount')


class PriceRuleItemEntitlements(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collections', 'product_variants', 'products', 'target_all_line_items')
    collections = sgqlc.types.Field(sgqlc.types.non_null(CollectionConnection), graphql_name='collections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    product_variants = sgqlc.types.Field(sgqlc.types.non_null('ProductVariantConnection'), graphql_name='productVariants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    products = sgqlc.types.Field(sgqlc.types.non_null('ProductConnection'), graphql_name='products', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    target_all_line_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='targetAllLineItems')


class PriceRuleLineItemPrerequisites(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('collections', 'product_variants', 'products')
    collections = sgqlc.types.Field(sgqlc.types.non_null(CollectionConnection), graphql_name='collections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    product_variants = sgqlc.types.Field(sgqlc.types.non_null('ProductVariantConnection'), graphql_name='productVariants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    products = sgqlc.types.Field(sgqlc.types.non_null('ProductConnection'), graphql_name='products', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )


class PriceRuleMoneyRange(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('greater_than', 'greater_than_or_equal_to', 'less_than', 'less_than_or_equal_to')
    greater_than = sgqlc.types.Field(Money, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(Money, graphql_name='greaterThanOrEqualTo')
    less_than = sgqlc.types.Field(Money, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(Money, graphql_name='lessThanOrEqualTo')


class PriceRulePercentValue(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('percentage',)
    percentage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='percentage')


class PriceRulePrerequisiteToEntitlementQuantityRatio(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('entitlement_quantity', 'prerequisite_quantity')
    entitlement_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='entitlementQuantity')
    prerequisite_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='prerequisiteQuantity')


class PriceRuleQuantityRange(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('greater_than', 'greater_than_or_equal_to', 'less_than', 'less_than_or_equal_to')
    greater_than = sgqlc.types.Field(Int, graphql_name='greaterThan')
    greater_than_or_equal_to = sgqlc.types.Field(Int, graphql_name='greaterThanOrEqualTo')
    less_than = sgqlc.types.Field(Int, graphql_name='lessThan')
    less_than_or_equal_to = sgqlc.types.Field(Int, graphql_name='lessThanOrEqualTo')


class PriceRuleShareableUrl(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('target_item_image', 'target_type', 'title', 'url')
    target_item_image = sgqlc.types.Field('Image', graphql_name='targetItemImage')
    target_type = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleShareableUrlTargetType), graphql_name='targetType')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class PriceRuleShippingLineEntitlements(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('country_codes', 'include_rest_of_world', 'target_all_shipping_lines')
    country_codes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode))), graphql_name='countryCodes')
    include_rest_of_world = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includeRestOfWorld')
    target_all_shipping_lines = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='targetAllShippingLines')


class PriceRuleUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('price_rule', 'price_rule_discount_code', 'price_rule_user_errors')
    price_rule = sgqlc.types.Field('PriceRule', graphql_name='priceRule')
    price_rule_discount_code = sgqlc.types.Field('PriceRuleDiscountCode', graphql_name='priceRuleDiscountCode')
    price_rule_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PriceRuleUserError'))), graphql_name='priceRuleUserErrors')


class PriceRuleValidityPeriod(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('end', 'start')
    end = sgqlc.types.Field(DateTime, graphql_name='end')
    start = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='start')


class PricingPercentageValue(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('percentage',)
    percentage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='percentage')


class PrivateMetafieldConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PrivateMetafieldEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PrivateMetafieldDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_private_metafield_id', 'user_errors')
    deleted_private_metafield_id = sgqlc.types.Field(ID, graphql_name='deletedPrivateMetafieldId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class PrivateMetafieldEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PrivateMetafield'), graphql_name='node')


class PrivateMetafieldUpsertPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('private_metafield', 'user_errors')
    private_metafield = sgqlc.types.Field('PrivateMetafield', graphql_name='privateMetafield')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductAppendImagesPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('new_images', 'product', 'user_errors')
    new_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Image')), graphql_name='newImages', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    product = sgqlc.types.Field('Product', graphql_name='product')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductChangeStatusPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductChangeStatusUserError'))), graphql_name='userErrors')


class ProductConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProductCreateMediaPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('media', 'media_user_errors', 'product')
    media = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Media)), graphql_name='media')
    media_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaUserError'))), graphql_name='mediaUserErrors')
    product = sgqlc.types.Field('Product', graphql_name='product')


class ProductCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'shop', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductDeleteImagesPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_image_ids', 'product', 'user_errors')
    deleted_image_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deletedImageIds')
    product = sgqlc.types.Field('Product', graphql_name='product')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductDeleteMediaPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_media_ids', 'deleted_product_image_ids', 'media_user_errors', 'product')
    deleted_media_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='deletedMediaIds')
    deleted_product_image_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='deletedProductImageIds')
    media_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaUserError'))), graphql_name='mediaUserErrors')
    product = sgqlc.types.Field('Product', graphql_name='product')


class ProductDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_product_id', 'shop', 'user_errors')
    deleted_product_id = sgqlc.types.Field(ID, graphql_name='deletedProductId')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductDuplicatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('image_job', 'new_product', 'shop', 'user_errors')
    image_job = sgqlc.types.Field(Job, graphql_name='imageJob')
    new_product = sgqlc.types.Field('Product', graphql_name='newProduct')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Product'), graphql_name='node')


class ProductImageUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('image', 'user_errors')
    image = sgqlc.types.Field('Image', graphql_name='image', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductPriceRange(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('max_variant_price', 'min_variant_price')
    max_variant_price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='maxVariantPrice')
    min_variant_price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='minVariantPrice')


class ProductPriceRangeV2(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('max_variant_price', 'min_variant_price')
    max_variant_price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='maxVariantPrice')
    min_variant_price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='minVariantPrice')


class ProductPublication(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('channel', 'is_published', 'product', 'publish_date')
    channel = sgqlc.types.Field(sgqlc.types.non_null('Channel'), graphql_name='channel')
    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')
    product = sgqlc.types.Field(sgqlc.types.non_null('Product'), graphql_name='product')
    publish_date = sgqlc.types.Field(DateTime, graphql_name='publishDate')


class ProductPublicationConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductPublicationEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProductPublicationEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(ProductPublication), graphql_name='node')


class ProductPublishPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'shop', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductReorderImagesPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field(Job, graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductReorderMediaPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'media_user_errors')
    job = sgqlc.types.Field(Job, graphql_name='job')
    media_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaUserError'))), graphql_name='mediaUserErrors')


class ProductUnpublishPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'shop', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductUpdateMediaPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('media', 'media_user_errors', 'product')
    media = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Media)), graphql_name='media')
    media_user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaUserError'))), graphql_name='mediaUserErrors')
    product = sgqlc.types.Field('Product', graphql_name='product')


class ProductUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductVariantAppendMediaPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'product_variants', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    product_variants = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProductVariant')), graphql_name='productVariants')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaUserError'))), graphql_name='userErrors')


class ProductVariantConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductVariantEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProductVariantCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'product_variant', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    product_variant = sgqlc.types.Field('ProductVariant', graphql_name='productVariant')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductVariantDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_product_variant_id', 'product', 'user_errors')
    deleted_product_variant_id = sgqlc.types.Field(ID, graphql_name='deletedProductVariantId')
    product = sgqlc.types.Field('Product', graphql_name='product')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ProductVariantDetachMediaPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'product_variants', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    product_variants = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProductVariant')), graphql_name='productVariants')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaUserError'))), graphql_name='userErrors')


class ProductVariantEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ProductVariant'), graphql_name='node')


class ProductVariantPricePair(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('compare_at_price', 'price')
    compare_at_price = sgqlc.types.Field(MoneyV2, graphql_name='compareAtPrice')
    price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='price')


class ProductVariantPricePairConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductVariantPricePairEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ProductVariantPricePairEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(ProductVariantPricePair), graphql_name='node')


class ProductVariantUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product', 'product_variant', 'user_errors')
    product = sgqlc.types.Field('Product', graphql_name='product')
    product_variant = sgqlc.types.Field('ProductVariant', graphql_name='productVariant')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class PublicationConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PublicationEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class PublicationEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Publication'), graphql_name='node')


class Publishable(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('available_publication_count', 'publication_count', 'published_on_current_publication', 'published_on_publication', 'resource_publications', 'resource_publications_v2', 'unpublished_publications')
    available_publication_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='availablePublicationCount')
    publication_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='publicationCount', args=sgqlc.types.ArgDict((
        ('only_published', sgqlc.types.Arg(Boolean, graphql_name='onlyPublished', default=True)),
))
    )
    published_on_current_publication = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='publishedOnCurrentPublication')
    published_on_publication = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='publishedOnPublication', args=sgqlc.types.ArgDict((
        ('publication_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='publicationId', default=None)),
))
    )
    resource_publications = sgqlc.types.Field(sgqlc.types.non_null('ResourcePublicationConnection'), graphql_name='resourcePublications', args=sgqlc.types.ArgDict((
        ('only_published', sgqlc.types.Arg(Boolean, graphql_name='onlyPublished', default=True)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    resource_publications_v2 = sgqlc.types.Field(sgqlc.types.non_null('ResourcePublicationV2Connection'), graphql_name='resourcePublicationsV2', args=sgqlc.types.ArgDict((
        ('only_published', sgqlc.types.Arg(Boolean, graphql_name='onlyPublished', default=True)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    unpublished_publications = sgqlc.types.Field(sgqlc.types.non_null(PublicationConnection), graphql_name='unpublishedPublications', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )


class PublishablePublishPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('publishable', 'shop', 'user_errors')
    publishable = sgqlc.types.Field(Publishable, graphql_name='publishable')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class PublishablePublishToCurrentChannelPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('publishable', 'shop', 'user_errors')
    publishable = sgqlc.types.Field(Publishable, graphql_name='publishable')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class PublishableUnpublishPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('publishable', 'shop', 'user_errors')
    publishable = sgqlc.types.Field(Publishable, graphql_name='publishable')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class PublishableUnpublishToCurrentChannelPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('publishable', 'shop', 'user_errors')
    publishable = sgqlc.types.Field(Publishable, graphql_name='publishable')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class PublishedTranslation(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('key', 'locale', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    locale = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='locale')
    value = sgqlc.types.Field(String, graphql_name='value')


class QueryRoot(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('app', 'app_by_handle', 'app_by_key', 'app_installation', 'app_installations', 'automatic_discount_node', 'automatic_discount_nodes', 'automatic_discount_saved_searches', 'available_carrier_services', 'available_locales', 'carrier_service', 'code_discount_node', 'code_discount_node_by_code', 'code_discount_nodes', 'code_discount_saved_searches', 'collection', 'collection_by_handle', 'collection_rules_conditions', 'collection_saved_searches', 'collections', 'current_app_installation', 'current_bulk_operation', 'customer', 'customer_saved_searches', 'customers', 'deletion_events', 'delivery_profile', 'delivery_profiles', 'delivery_settings', 'discount_redeem_code_saved_searches', 'domain', 'draft_order', 'draft_order_saved_searches', 'draft_orders', 'fulfillment', 'fulfillment_order', 'fulfillment_service', 'inventory_item', 'inventory_items', 'inventory_level', 'job', 'location', 'locations', 'locations_available_for_delivery_profiles_connection', 'marketing_activities', 'marketing_activity', 'marketing_event', 'marketing_events', 'metafield_storefront_visibilities', 'metafield_storefront_visibility', 'node', 'nodes', 'order', 'order_saved_searches', 'orders', 'price_rule', 'price_rule_saved_searches', 'price_rules', 'private_metafield', 'private_metafields', 'product', 'product_by_handle', 'product_saved_searches', 'product_variant', 'product_variants', 'products', 'public_api_versions', 'publication', 'publications', 'refund', 'script_tag', 'script_tags', 'shop', 'shop_locales', 'shopify_payments_account', 'tender_transactions', 'translatable_resource', 'translatable_resources', 'webhook_subscription', 'webhook_subscriptions')
    app = sgqlc.types.Field('App', graphql_name='app', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    app_by_handle = sgqlc.types.Field('App', graphql_name='appByHandle', args=sgqlc.types.ArgDict((
        ('handle', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='handle', default=None)),
))
    )
    app_by_key = sgqlc.types.Field('App', graphql_name='appByKey', args=sgqlc.types.ArgDict((
        ('api_key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='apiKey', default=None)),
))
    )
    app_installation = sgqlc.types.Field('AppInstallation', graphql_name='appInstallation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    app_installations = sgqlc.types.Field(sgqlc.types.non_null(AppInstallationConnection), graphql_name='appInstallations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(AppInstallationSortKeys, graphql_name='sortKey', default='INSTALLED_AT')),
        ('category', sgqlc.types.Arg(AppInstallationCategory, graphql_name='category', default=None)),
        ('privacy', sgqlc.types.Arg(AppInstallationPrivacy, graphql_name='privacy', default='PUBLIC')),
))
    )
    automatic_discount_node = sgqlc.types.Field('DiscountAutomaticNode', graphql_name='automaticDiscountNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    automatic_discount_nodes = sgqlc.types.Field(sgqlc.types.non_null(DiscountAutomaticNodeConnection), graphql_name='automaticDiscountNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(AutomaticDiscountSortKeys, graphql_name='sortKey', default='CREATED_AT')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    automatic_discount_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='automaticDiscountSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    available_carrier_services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryCarrierServiceAndLocations))), graphql_name='availableCarrierServices')
    available_locales = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Locale))), graphql_name='availableLocales')
    carrier_service = sgqlc.types.Field('DeliveryCarrierService', graphql_name='carrierService', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    code_discount_node = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    code_discount_node_by_code = sgqlc.types.Field('DiscountCodeNode', graphql_name='codeDiscountNodeByCode', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
))
    )
    code_discount_nodes = sgqlc.types.Field(sgqlc.types.non_null(DiscountCodeNodeConnection), graphql_name='codeDiscountNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(CodeDiscountSortKeys, graphql_name='sortKey', default='CREATED_AT')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    code_discount_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='codeDiscountSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    collection = sgqlc.types.Field('Collection', graphql_name='collection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    collection_by_handle = sgqlc.types.Field('Collection', graphql_name='collectionByHandle', args=sgqlc.types.ArgDict((
        ('handle', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='handle', default=None)),
))
    )
    collection_rules_conditions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CollectionRuleConditions))), graphql_name='collectionRulesConditions')
    collection_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='collectionSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    collections = sgqlc.types.Field(sgqlc.types.non_null(CollectionConnection), graphql_name='collections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(CollectionSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    current_app_installation = sgqlc.types.Field(sgqlc.types.non_null('AppInstallation'), graphql_name='currentAppInstallation')
    current_bulk_operation = sgqlc.types.Field('BulkOperation', graphql_name='currentBulkOperation')
    customer = sgqlc.types.Field('Customer', graphql_name='customer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    customer_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='customerSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(CustomerSavedSearchSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    customers = sgqlc.types.Field(sgqlc.types.non_null(CustomerConnection), graphql_name='customers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(CustomerSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    deletion_events = sgqlc.types.Field(sgqlc.types.non_null(DeletionEventConnection), graphql_name='deletionEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(DeletionEventSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('subject_types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(DeletionEventSubjectType)), graphql_name='subjectTypes', default=None)),
))
    )
    delivery_profile = sgqlc.types.Field('DeliveryProfile', graphql_name='deliveryProfile', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delivery_profiles = sgqlc.types.Field(sgqlc.types.non_null(DeliveryProfileConnection), graphql_name='deliveryProfiles', args=sgqlc.types.ArgDict((
        ('merchant_owned_only', sgqlc.types.Arg(Boolean, graphql_name='merchantOwnedOnly', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    delivery_settings = sgqlc.types.Field(DeliverySetting, graphql_name='deliverySettings')
    discount_redeem_code_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='discountRedeemCodeSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(DiscountCodeSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    domain = sgqlc.types.Field('Domain', graphql_name='domain', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    draft_order = sgqlc.types.Field('DraftOrder', graphql_name='draftOrder', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    draft_order_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='draftOrderSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    draft_orders = sgqlc.types.Field(sgqlc.types.non_null(DraftOrderConnection), graphql_name='draftOrders', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(DraftOrderSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    fulfillment = sgqlc.types.Field('Fulfillment', graphql_name='fulfillment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    fulfillment_order = sgqlc.types.Field('FulfillmentOrder', graphql_name='fulfillmentOrder', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    fulfillment_service = sgqlc.types.Field(FulfillmentService, graphql_name='fulfillmentService', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    inventory_item = sgqlc.types.Field('InventoryItem', graphql_name='inventoryItem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    inventory_items = sgqlc.types.Field(sgqlc.types.non_null(InventoryItemConnection), graphql_name='inventoryItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    inventory_level = sgqlc.types.Field('InventoryLevel', graphql_name='inventoryLevel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    job = sgqlc.types.Field(Job, graphql_name='job', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    location = sgqlc.types.Field('Location', graphql_name='location', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    locations = sgqlc.types.Field(sgqlc.types.non_null(LocationConnection), graphql_name='locations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(LocationSortKeys, graphql_name='sortKey', default='NAME')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('include_legacy', sgqlc.types.Arg(Boolean, graphql_name='includeLegacy', default=False)),
        ('include_inactive', sgqlc.types.Arg(Boolean, graphql_name='includeInactive', default=False)),
))
    )
    locations_available_for_delivery_profiles_connection = sgqlc.types.Field(sgqlc.types.non_null(LocationConnection), graphql_name='locationsAvailableForDeliveryProfilesConnection', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    marketing_activities = sgqlc.types.Field(sgqlc.types.non_null(MarketingActivityConnection), graphql_name='marketingActivities', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(MarketingActivitySortKeys, graphql_name='sortKey', default='CREATED_AT')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    marketing_activity = sgqlc.types.Field('MarketingActivity', graphql_name='marketingActivity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    marketing_event = sgqlc.types.Field('MarketingEvent', graphql_name='marketingEvent', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    marketing_events = sgqlc.types.Field(sgqlc.types.non_null(MarketingEventConnection), graphql_name='marketingEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(MarketingEventSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    metafield_storefront_visibilities = sgqlc.types.Field(sgqlc.types.non_null(MetafieldStorefrontVisibilityConnection), graphql_name='metafieldStorefrontVisibilities', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    metafield_storefront_visibility = sgqlc.types.Field('MetafieldStorefrontVisibility', graphql_name='metafieldStorefrontVisibility', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Node)), graphql_name='nodes', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    order = sgqlc.types.Field('Order', graphql_name='order', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    order_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='orderSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    orders = sgqlc.types.Field(sgqlc.types.non_null(OrderConnection), graphql_name='orders', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(OrderSortKeys, graphql_name='sortKey', default='PROCESSED_AT')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    price_rule = sgqlc.types.Field('PriceRule', graphql_name='priceRule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    price_rule_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='priceRuleSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    price_rules = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleConnection), graphql_name='priceRules', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(PriceRuleSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    private_metafield = sgqlc.types.Field('PrivateMetafield', graphql_name='privateMetafield', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    private_metafields = sgqlc.types.Field(sgqlc.types.non_null(PrivateMetafieldConnection), graphql_name='privateMetafields', args=sgqlc.types.ArgDict((
        ('namespace', sgqlc.types.Arg(String, graphql_name='namespace', default=None)),
        ('owner', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='owner', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    product = sgqlc.types.Field('Product', graphql_name='product', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    product_by_handle = sgqlc.types.Field('Product', graphql_name='productByHandle', args=sgqlc.types.ArgDict((
        ('handle', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='handle', default=None)),
))
    )
    product_saved_searches = sgqlc.types.Field(sgqlc.types.non_null('SavedSearchConnection'), graphql_name='productSavedSearches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    product_variant = sgqlc.types.Field('ProductVariant', graphql_name='productVariant', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    product_variants = sgqlc.types.Field(sgqlc.types.non_null(ProductVariantConnection), graphql_name='productVariants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProductVariantSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    products = sgqlc.types.Field(sgqlc.types.non_null(ProductConnection), graphql_name='products', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProductSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    public_api_versions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ApiVersion))), graphql_name='publicApiVersions')
    publication = sgqlc.types.Field('Publication', graphql_name='publication', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    publications = sgqlc.types.Field(sgqlc.types.non_null(PublicationConnection), graphql_name='publications', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    refund = sgqlc.types.Field('Refund', graphql_name='refund', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    script_tag = sgqlc.types.Field('ScriptTag', graphql_name='scriptTag', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    script_tags = sgqlc.types.Field(sgqlc.types.non_null('ScriptTagConnection'), graphql_name='scriptTags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('src', sgqlc.types.Arg(URL, graphql_name='src', default=None)),
))
    )
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    shop_locales = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShopLocale'))), graphql_name='shopLocales', args=sgqlc.types.ArgDict((
        ('published', sgqlc.types.Arg(Boolean, graphql_name='published', default=None)),
))
    )
    shopify_payments_account = sgqlc.types.Field('ShopifyPaymentsAccount', graphql_name='shopifyPaymentsAccount')
    tender_transactions = sgqlc.types.Field(sgqlc.types.non_null('TenderTransactionConnection'), graphql_name='tenderTransactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    translatable_resource = sgqlc.types.Field('TranslatableResource', graphql_name='translatableResource', args=sgqlc.types.ArgDict((
        ('resource_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='resourceId', default=None)),
))
    )
    translatable_resources = sgqlc.types.Field(sgqlc.types.non_null('TranslatableResourceConnection'), graphql_name='translatableResources', args=sgqlc.types.ArgDict((
        ('resource_type', sgqlc.types.Arg(sgqlc.types.non_null(TranslatableResourceType), graphql_name='resourceType', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    webhook_subscription = sgqlc.types.Field('WebhookSubscription', graphql_name='webhookSubscription', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    webhook_subscriptions = sgqlc.types.Field(sgqlc.types.non_null('WebhookSubscriptionConnection'), graphql_name='webhookSubscriptions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(WebhookSubscriptionSortKeys, graphql_name='sortKey', default='CREATED_AT')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('callback_url', sgqlc.types.Arg(URL, graphql_name='callbackUrl', default=None)),
        ('format', sgqlc.types.Arg(WebhookSubscriptionFormat, graphql_name='format', default=None)),
        ('topics', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WebhookSubscriptionTopic)), graphql_name='topics', default=None)),
))
    )


class RefundCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('order', 'refund', 'user_errors')
    order = sgqlc.types.Field('Order', graphql_name='order')
    refund = sgqlc.types.Field('Refund', graphql_name='refund')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class RefundDuty(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('amount_set', 'original_duty')
    amount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='amountSet')
    original_duty = sgqlc.types.Field('Duty', graphql_name='originalDuty')


class RefundLineItem(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('line_item', 'location', 'price_set', 'quantity', 'restock_type', 'restocked', 'subtotal_set', 'total_tax_set')
    line_item = sgqlc.types.Field(sgqlc.types.non_null('LineItem'), graphql_name='lineItem')
    location = sgqlc.types.Field('Location', graphql_name='location')
    price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='priceSet')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    restock_type = sgqlc.types.Field(sgqlc.types.non_null(RefundLineItemRestockType), graphql_name='restockType')
    restocked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restocked')
    subtotal_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='subtotalSet')
    total_tax_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalTaxSet')


class RefundLineItemConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RefundLineItemEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class RefundLineItemEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(RefundLineItem), graphql_name='node')


class ResourceAlert(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('actions', 'content', 'dismissible_handle', 'icon', 'severity', 'title')
    actions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResourceAlertAction'))), graphql_name='actions')
    content = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='content')
    dismissible_handle = sgqlc.types.Field(String, graphql_name='dismissibleHandle')
    icon = sgqlc.types.Field(ResourceAlertIcon, graphql_name='icon')
    severity = sgqlc.types.Field(sgqlc.types.non_null(ResourceAlertSeverity), graphql_name='severity')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class ResourceAlertAction(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('primary', 'show', 'title', 'url')
    primary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='primary')
    show = sgqlc.types.Field(String, graphql_name='show')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class ResourceFeedback(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('details', 'summary')
    details = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AppFeedback))), graphql_name='details')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')


class ResourceLimit(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('available', 'quantity_available', 'quantity_limit', 'quantity_used')
    available = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='available')
    quantity_available = sgqlc.types.Field(Int, graphql_name='quantityAvailable')
    quantity_limit = sgqlc.types.Field(Int, graphql_name='quantityLimit')
    quantity_used = sgqlc.types.Field(Int, graphql_name='quantityUsed')


class ResourcePublication(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('is_published', 'publication', 'publish_date', 'publishable')
    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')
    publication = sgqlc.types.Field(sgqlc.types.non_null('Publication'), graphql_name='publication')
    publish_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='publishDate')
    publishable = sgqlc.types.Field(sgqlc.types.non_null(Publishable), graphql_name='publishable')


class ResourcePublicationConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResourcePublicationEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ResourcePublicationEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(ResourcePublication), graphql_name='node')


class ResourcePublicationV2(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('is_published', 'publication', 'publish_date', 'publishable')
    is_published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublished')
    publication = sgqlc.types.Field(sgqlc.types.non_null('Publication'), graphql_name='publication')
    publish_date = sgqlc.types.Field(DateTime, graphql_name='publishDate')
    publishable = sgqlc.types.Field(sgqlc.types.non_null(Publishable), graphql_name='publishable')


class ResourcePublicationV2Connection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ResourcePublicationV2Edge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ResourcePublicationV2Edge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(ResourcePublicationV2), graphql_name='node')


class SEO(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('description', 'title')
    description = sgqlc.types.Field(String, graphql_name='description')
    title = sgqlc.types.Field(String, graphql_name='title')


class SavedSearchConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SavedSearchEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class SavedSearchCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('saved_search', 'user_errors')
    saved_search = sgqlc.types.Field('SavedSearch', graphql_name='savedSearch')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class SavedSearchDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_saved_search_id', 'shop', 'user_errors')
    deleted_saved_search_id = sgqlc.types.Field(ID, graphql_name='deletedSavedSearchId')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class SavedSearchEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('SavedSearch'), graphql_name='node')


class SavedSearchUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('saved_search', 'user_errors')
    saved_search = sgqlc.types.Field('SavedSearch', graphql_name='savedSearch')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ScriptTagConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ScriptTagEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ScriptTagCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('script_tag', 'user_errors')
    script_tag = sgqlc.types.Field('ScriptTag', graphql_name='scriptTag')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ScriptTagDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_script_tag_id', 'user_errors')
    deleted_script_tag_id = sgqlc.types.Field(ID, graphql_name='deletedScriptTagId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ScriptTagEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ScriptTag'), graphql_name='node')


class ScriptTagUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('script_tag', 'user_errors')
    script_tag = sgqlc.types.Field('ScriptTag', graphql_name='scriptTag')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class SearchFilter(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('key', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class SearchFilterOptions(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('product_availability',)
    product_availability = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FilterOption))), graphql_name='productAvailability')


class SearchResult(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('description', 'image', 'reference', 'title', 'url')
    description = sgqlc.types.Field(String, graphql_name='description')
    image = sgqlc.types.Field('Image', graphql_name='image')
    reference = sgqlc.types.Field(sgqlc.types.non_null(Node), graphql_name='reference')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class SearchResultConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SearchResultEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class SearchResultEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(SearchResult), graphql_name='node')


class SelectedOption(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class ShippingLine(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('carrier_identifier', 'code', 'custom', 'delivery_category', 'discount_allocations', 'discounted_price_set', 'id', 'original_price_set', 'phone', 'requested_fulfillment_service', 'shipping_rate_handle', 'source', 'tax_lines', 'title')
    carrier_identifier = sgqlc.types.Field(String, graphql_name='carrierIdentifier')
    code = sgqlc.types.Field(String, graphql_name='code')
    custom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='custom')
    delivery_category = sgqlc.types.Field(String, graphql_name='deliveryCategory')
    discount_allocations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DiscountAllocation))), graphql_name='discountAllocations')
    discounted_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='discountedPriceSet')
    id = sgqlc.types.Field(ID, graphql_name='id')
    original_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='originalPriceSet')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    requested_fulfillment_service = sgqlc.types.Field(FulfillmentService, graphql_name='requestedFulfillmentService')
    shipping_rate_handle = sgqlc.types.Field(String, graphql_name='shippingRateHandle')
    source = sgqlc.types.Field(String, graphql_name='source')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TaxLine'))), graphql_name='taxLines')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class ShippingLineConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShippingLineEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ShippingLineEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(ShippingLine), graphql_name='node')


class ShippingMethod(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('code', 'label')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class ShippingPackageDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_id', 'user_errors')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ShippingPackageMakeDefaultPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors',)
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ShippingPackageUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors',)
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ShippingRate(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('handle', 'price', 'title')
    handle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='handle')
    price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='price')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class ShippingRefund(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('amount_set', 'maximum_refundable_set', 'tax_set')
    amount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='amountSet')
    maximum_refundable_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='maximumRefundableSet')
    tax_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='taxSet')


class ShopAlert(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('action', 'description')
    action = sgqlc.types.Field(sgqlc.types.non_null('ShopAlertAction'), graphql_name='action')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')


class ShopAlertAction(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('title', 'url')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class ShopFeatures(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('avalara_avatax', 'branding', 'captcha', 'captcha_external_domains', 'dynamic_remarketing', 'gift_cards', 'harmonized_system_code', 'international_domains', 'live_view', 'multi_location', 'onboarding_visual', 'reports', 'show_metrics', 'storefront')
    avalara_avatax = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='avalaraAvatax')
    branding = sgqlc.types.Field(sgqlc.types.non_null(ShopBranding), graphql_name='branding')
    captcha = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='captcha')
    captcha_external_domains = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='captchaExternalDomains')
    dynamic_remarketing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dynamicRemarketing')
    gift_cards = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='giftCards')
    harmonized_system_code = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='harmonizedSystemCode')
    international_domains = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='internationalDomains')
    live_view = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='liveView')
    multi_location = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='multiLocation')
    onboarding_visual = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='onboardingVisual')
    reports = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reports')
    show_metrics = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='showMetrics')
    storefront = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='storefront')


class ShopLocale(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('locale', 'name', 'primary', 'published')
    locale = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='locale')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    primary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='primary')
    published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='published')


class ShopLocaleDisablePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('locale', 'user_errors')
    locale = sgqlc.types.Field(String, graphql_name='locale')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ShopLocaleEnablePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('shop_locale', 'user_errors')
    shop_locale = sgqlc.types.Field(ShopLocale, graphql_name='shopLocale')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ShopLocaleUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('shop_locale', 'user_errors')
    shop_locale = sgqlc.types.Field(ShopLocale, graphql_name='shopLocale')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class ShopPlan(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('display_name', 'partner_development', 'shopify_plus')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    partner_development = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='partnerDevelopment')
    shopify_plus = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shopifyPlus')


class ShopPolicyUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('shop_policy', 'user_errors')
    shop_policy = sgqlc.types.Field('ShopPolicy', graphql_name='shopPolicy')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShopPolicyUserError'))), graphql_name='userErrors')


class ShopResourceLimits(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('location_limit', 'max_product_options', 'max_product_variants', 'redirect_limit_reached', 'sku_resource_limits')
    location_limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='locationLimit')
    max_product_options = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxProductOptions')
    max_product_variants = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxProductVariants')
    redirect_limit_reached = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='redirectLimitReached')
    sku_resource_limits = sgqlc.types.Field(sgqlc.types.non_null(ResourceLimit), graphql_name='skuResourceLimits')


class ShopifyPaymentsBankAccountConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShopifyPaymentsBankAccountEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ShopifyPaymentsBankAccountEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ShopifyPaymentsBankAccount'), graphql_name='node')


class ShopifyPaymentsChargeStatementDescriptor(sgqlc.types.Interface):
    __schema__ = shopify_schema
    __field_names__ = ('default', 'prefix')
    default = sgqlc.types.Field(String, graphql_name='default')
    prefix = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='prefix')


class ShopifyPaymentsDisputeConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShopifyPaymentsDisputeEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ShopifyPaymentsDisputeEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ShopifyPaymentsDispute'), graphql_name='node')


class ShopifyPaymentsDisputeReasonDetails(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('network_reason_code', 'reason')
    network_reason_code = sgqlc.types.Field(String, graphql_name='networkReasonCode')
    reason = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsDisputeReason), graphql_name='reason')


class ShopifyPaymentsFraudSettings(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('decline_charge_on_avs_failure', 'decline_charge_on_cvc_failure')
    decline_charge_on_avs_failure = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='declineChargeOnAvsFailure')
    decline_charge_on_cvc_failure = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='declineChargeOnCvcFailure')


class ShopifyPaymentsNotificationSettings(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('payouts',)
    payouts = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='payouts')


class ShopifyPaymentsPayoutConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShopifyPaymentsPayoutEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class ShopifyPaymentsPayoutEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ShopifyPaymentsPayout'), graphql_name='node')


class ShopifyPaymentsPayoutSchedule(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('interval', 'monthly_anchor', 'weekly_anchor')
    interval = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsPayoutInterval), graphql_name='interval')
    monthly_anchor = sgqlc.types.Field(Int, graphql_name='monthlyAnchor')
    weekly_anchor = sgqlc.types.Field(DayOfTheWeek, graphql_name='weeklyAnchor')


class ShopifyPaymentsPayoutSummary(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('adjustments_fee', 'adjustments_gross', 'charges_fee', 'charges_gross', 'refunds_fee', 'refunds_fee_gross', 'reserved_funds_fee', 'reserved_funds_gross', 'retried_payouts_fee', 'retried_payouts_gross')
    adjustments_fee = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='adjustmentsFee')
    adjustments_gross = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='adjustmentsGross')
    charges_fee = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='chargesFee')
    charges_gross = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='chargesGross')
    refunds_fee = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='refundsFee')
    refunds_fee_gross = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='refundsFeeGross')
    reserved_funds_fee = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='reservedFundsFee')
    reserved_funds_gross = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='reservedFundsGross')
    retried_payouts_fee = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='retriedPayoutsFee')
    retried_payouts_gross = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='retriedPayoutsGross')


class ShopifyPaymentsVerificationDocument(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('back_required', 'front_required', 'type')
    back_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='backRequired')
    front_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='frontRequired')
    type = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsVerificationDocumentType), graphql_name='type')


class ShopifyPaymentsVerificationSubject(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('family_name', 'given_name')
    family_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='familyName')
    given_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='givenName')


class StagedMediaUploadTarget(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('parameters', 'resource_url', 'url')
    parameters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StagedUploadParameter'))), graphql_name='parameters')
    resource_url = sgqlc.types.Field(URL, graphql_name='resourceUrl')
    url = sgqlc.types.Field(URL, graphql_name='url')


class StagedUploadParameter(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class StagedUploadTarget(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('parameters', 'url')
    parameters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ImageUploadParameter))), graphql_name='parameters')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class StagedUploadTargetGeneratePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('parameters', 'url', 'user_errors')
    parameters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MutationsStagedUploadTargetGenerateUploadParameter))), graphql_name='parameters')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class StagedUploadTargetsGeneratePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('urls', 'user_errors')
    urls = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StagedUploadTarget)), graphql_name='urls')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class StagedUploadsCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('staged_targets', 'user_errors')
    staged_targets = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StagedMediaUploadTarget)), graphql_name='stagedTargets')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class StorefrontAccessTokenConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StorefrontAccessTokenEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class StorefrontAccessTokenCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('shop', 'storefront_access_token', 'user_errors')
    shop = sgqlc.types.Field(sgqlc.types.non_null('Shop'), graphql_name='shop')
    storefront_access_token = sgqlc.types.Field('StorefrontAccessToken', graphql_name='storefrontAccessToken')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class StorefrontAccessTokenDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_storefront_access_token_id', 'user_errors')
    deleted_storefront_access_token_id = sgqlc.types.Field(ID, graphql_name='deletedStorefrontAccessTokenId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class StorefrontAccessTokenEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('StorefrontAccessToken'), graphql_name='node')


class StringConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class StringEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='node')


class SuggestedOrderTransaction(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('account_number', 'amount_set', 'formatted_gateway', 'gateway', 'kind', 'maximum_refundable_set', 'parent_transaction')
    account_number = sgqlc.types.Field(String, graphql_name='accountNumber')
    amount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='amountSet')
    formatted_gateway = sgqlc.types.Field(String, graphql_name='formattedGateway')
    gateway = sgqlc.types.Field(String, graphql_name='gateway')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SuggestedOrderTransactionKind), graphql_name='kind')
    maximum_refundable_set = sgqlc.types.Field(MoneyBag, graphql_name='maximumRefundableSet')
    parent_transaction = sgqlc.types.Field('OrderTransaction', graphql_name='parentTransaction')


class SuggestedRefund(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('amount_set', 'discounted_subtotal_set', 'maximum_refundable_set', 'refund_duties', 'refund_line_items', 'shipping', 'subtotal_set', 'suggested_transactions', 'total_cart_discount_amount_set', 'total_duties_set', 'total_tax_set')
    amount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='amountSet')
    discounted_subtotal_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='discountedSubtotalSet')
    maximum_refundable_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='maximumRefundableSet')
    refund_duties = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RefundDuty))), graphql_name='refundDuties')
    refund_line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RefundLineItem))), graphql_name='refundLineItems')
    shipping = sgqlc.types.Field(sgqlc.types.non_null(ShippingRefund), graphql_name='shipping')
    subtotal_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='subtotalSet')
    suggested_transactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SuggestedOrderTransaction))), graphql_name='suggestedTransactions')
    total_cart_discount_amount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalCartDiscountAmountSet')
    total_duties_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalDutiesSet')
    total_tax_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalTaxSet')


class TagsAddPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('node', 'user_errors')
    node = sgqlc.types.Field(Node, graphql_name='node')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class TagsRemovePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('node', 'user_errors')
    node = sgqlc.types.Field(Node, graphql_name='node')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class TaxLine(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('price_set', 'rate', 'rate_percentage', 'title')
    price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='priceSet')
    rate = sgqlc.types.Field(Float, graphql_name='rate')
    rate_percentage = sgqlc.types.Field(Float, graphql_name='ratePercentage')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class TenderTransactionConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TenderTransactionEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TenderTransactionCreditCardDetails(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('credit_card_company', 'credit_card_number')
    credit_card_company = sgqlc.types.Field(String, graphql_name='creditCardCompany')
    credit_card_number = sgqlc.types.Field(String, graphql_name='creditCardNumber')


class TenderTransactionEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('TenderTransaction'), graphql_name='node')


class TranslatableContent(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('digest', 'key', 'locale', 'value')
    digest = sgqlc.types.Field(String, graphql_name='digest')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    locale = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='locale')
    value = sgqlc.types.Field(String, graphql_name='value')


class TranslatableResource(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('resource_id', 'translatable_content', 'translations')
    resource_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='resourceId')
    translatable_content = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TranslatableContent))), graphql_name='translatableContent')
    translations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Translation'))), graphql_name='translations', args=sgqlc.types.ArgDict((
        ('locale', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='locale', default=None)),
        ('outdated', sgqlc.types.Arg(Boolean, graphql_name='outdated', default=None)),
))
    )


class TranslatableResourceConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TranslatableResourceEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class TranslatableResourceEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(TranslatableResource), graphql_name='node')


class Translation(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('key', 'locale', 'outdated', 'value')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    locale = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='locale')
    outdated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='outdated')
    value = sgqlc.types.Field(String, graphql_name='value')


class TranslationsRegisterPayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('translations', 'user_errors')
    translations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Translation)), graphql_name='translations')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TranslationUserError'))), graphql_name='userErrors')


class TranslationsRemovePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('translations', 'user_errors')
    translations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Translation)), graphql_name='translations')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TranslationUserError'))), graphql_name='userErrors')


class UTMParameters(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('campaign', 'content', 'medium', 'source', 'term')
    campaign = sgqlc.types.Field(String, graphql_name='campaign')
    content = sgqlc.types.Field(String, graphql_name='content')
    medium = sgqlc.types.Field(String, graphql_name='medium')
    source = sgqlc.types.Field(String, graphql_name='source')
    term = sgqlc.types.Field(String, graphql_name='term')


class VideoSource(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('format', 'height', 'mime_type', 'url', 'width')
    format = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='format')
    height = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='height')
    mime_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mimeType')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    width = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='width')


class WebhookEventBridgeEndpoint(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('arn',)
    arn = sgqlc.types.Field(sgqlc.types.non_null(ARN), graphql_name='arn')


class WebhookHttpEndpoint(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('callback_url',)
    callback_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='callbackUrl')


class WebhookSubscriptionConnection(sgqlc.types.relay.Connection):
    __schema__ = shopify_schema
    __field_names__ = ('edges', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WebhookSubscriptionEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')


class WebhookSubscriptionCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors', 'webhook_subscription')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')
    webhook_subscription = sgqlc.types.Field('WebhookSubscription', graphql_name='webhookSubscription')


class WebhookSubscriptionDeletePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('deleted_webhook_subscription_id', 'user_errors')
    deleted_webhook_subscription_id = sgqlc.types.Field(ID, graphql_name='deletedWebhookSubscriptionId')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class WebhookSubscriptionEdge(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('WebhookSubscription'), graphql_name='node')


class WebhookSubscriptionUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('user_errors', 'webhook_subscription')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')
    webhook_subscription = sgqlc.types.Field('WebhookSubscription', graphql_name='webhookSubscription')


class Weight(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('unit', 'value')
    unit = sgqlc.types.Field(sgqlc.types.non_null(WeightUnit), graphql_name='unit')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class deliveryProfileCreatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('profile', 'user_errors')
    profile = sgqlc.types.Field('DeliveryProfile', graphql_name='profile')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class deliveryProfileRemovePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('job', 'user_errors')
    job = sgqlc.types.Field(Job, graphql_name='job')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class deliveryProfileUpdatePayload(sgqlc.types.Type):
    __schema__ = shopify_schema
    __field_names__ = ('profile', 'user_errors')
    profile = sgqlc.types.Field('DeliveryProfile', graphql_name='profile')
    user_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserError'))), graphql_name='userErrors')


class App(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('api_key', 'app_store_app_url', 'app_store_developer_url', 'banner', 'description', 'developer_name', 'embedded', 'failed_requirements', 'features', 'feedback', 'handle', 'icon', 'install_url', 'installation', 'pricing_details', 'pricing_details_summary', 'privacy_policy_url', 'published', 'screenshots', 'shopify_developed', 'title', 'uninstall_message')
    api_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='apiKey')
    app_store_app_url = sgqlc.types.Field(URL, graphql_name='appStoreAppUrl')
    app_store_developer_url = sgqlc.types.Field(URL, graphql_name='appStoreDeveloperUrl')
    banner = sgqlc.types.Field(sgqlc.types.non_null('Image'), graphql_name='banner')
    description = sgqlc.types.Field(String, graphql_name='description')
    developer_name = sgqlc.types.Field(String, graphql_name='developerName')
    embedded = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='embedded')
    failed_requirements = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FailedRequirement))), graphql_name='failedRequirements')
    features = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='features')
    feedback = sgqlc.types.Field(AppFeedback, graphql_name='feedback')
    handle = sgqlc.types.Field(String, graphql_name='handle')
    icon = sgqlc.types.Field(sgqlc.types.non_null('Image'), graphql_name='icon')
    install_url = sgqlc.types.Field(URL, graphql_name='installUrl')
    installation = sgqlc.types.Field('AppInstallation', graphql_name='installation')
    pricing_details = sgqlc.types.Field(String, graphql_name='pricingDetails')
    pricing_details_summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pricingDetailsSummary')
    privacy_policy_url = sgqlc.types.Field(URL, graphql_name='privacyPolicyUrl')
    published = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='published')
    screenshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Image'))), graphql_name='screenshots')
    shopify_developed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shopifyDeveloped')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    uninstall_message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uninstallMessage')


class AppCredit(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'created_at', 'description', 'test')
    amount = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='amount')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    test = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='test')


class AppInstallation(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('access_scopes', 'active_subscriptions', 'all_subscriptions', 'app', 'credits', 'launch_url', 'one_time_purchases', 'publication', 'uninstall_url')
    access_scopes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccessScope))), graphql_name='accessScopes')
    active_subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppSubscription'))), graphql_name='activeSubscriptions')
    all_subscriptions = sgqlc.types.Field(sgqlc.types.non_null(AppSubscriptionConnection), graphql_name='allSubscriptions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(AppSubscriptionSortKeys, graphql_name='sortKey', default='CREATED_AT')),
))
    )
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    credits = sgqlc.types.Field(sgqlc.types.non_null(AppCreditConnection), graphql_name='credits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(AppTransactionSortKeys, graphql_name='sortKey', default='CREATED_AT')),
))
    )
    launch_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='launchUrl')
    one_time_purchases = sgqlc.types.Field(sgqlc.types.non_null(AppPurchaseOneTimeConnection), graphql_name='oneTimePurchases', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(AppTransactionSortKeys, graphql_name='sortKey', default='CREATED_AT')),
))
    )
    publication = sgqlc.types.Field('Publication', graphql_name='publication')
    uninstall_url = sgqlc.types.Field(URL, graphql_name='uninstallUrl')


class AppPurchaseOneTime(sgqlc.types.Type, AppPurchase, Node):
    __schema__ = shopify_schema
    __field_names__ = ()


class AppSubscription(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'current_period_end', 'line_items', 'name', 'return_url', 'status', 'test', 'trial_days')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    current_period_end = sgqlc.types.Field(DateTime, graphql_name='currentPeriodEnd')
    line_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AppSubscriptionLineItem))), graphql_name='lineItems')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    return_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='returnUrl')
    status = sgqlc.types.Field(sgqlc.types.non_null(AppSubscriptionStatus), graphql_name='status')
    test = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='test')
    trial_days = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='trialDays')


class AppUsageRecord(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'description', 'price', 'subscription_line_item')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='price')
    subscription_line_item = sgqlc.types.Field(sgqlc.types.non_null(AppSubscriptionLineItem), graphql_name='subscriptionLineItem')


class AutomaticDiscountApplication(sgqlc.types.Type, DiscountApplication):
    __schema__ = shopify_schema
    __field_names__ = ('title',)
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class BasicEvent(sgqlc.types.Type, Node, Event):
    __schema__ = shopify_schema
    __field_names__ = ()


class BulkOperation(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('completed_at', 'created_at', 'error_code', 'file_size', 'object_count', 'partial_data_url', 'query', 'root_object_count', 'status', 'url')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    error_code = sgqlc.types.Field(BulkOperationErrorCode, graphql_name='errorCode')
    file_size = sgqlc.types.Field(UnsignedInt64, graphql_name='fileSize')
    object_count = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='objectCount')
    partial_data_url = sgqlc.types.Field(URL, graphql_name='partialDataUrl')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    root_object_count = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='rootObjectCount')
    status = sgqlc.types.Field(sgqlc.types.non_null(BulkOperationStatus), graphql_name='status')
    url = sgqlc.types.Field(URL, graphql_name='url')


class CalculatedAutomaticDiscountApplication(sgqlc.types.Type, CalculatedDiscountApplication):
    __schema__ = shopify_schema
    __field_names__ = ()


class CalculatedDiscountCodeApplication(sgqlc.types.Type, CalculatedDiscountApplication):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')


class CalculatedManualDiscountApplication(sgqlc.types.Type, CalculatedDiscountApplication):
    __schema__ = shopify_schema
    __field_names__ = ()


class CalculatedOrder(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('added_discount_applications', 'added_line_items', 'cart_discount_amount_set', 'committed', 'line_items', 'notification_preview_html', 'notification_preview_title', 'original_order', 'staged_changes', 'subtotal_line_items_quantity', 'subtotal_price_set', 'tax_lines', 'total_outstanding_set', 'total_price_set')
    added_discount_applications = sgqlc.types.Field(sgqlc.types.non_null(CalculatedDiscountApplicationConnection), graphql_name='addedDiscountApplications', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    added_line_items = sgqlc.types.Field(sgqlc.types.non_null(CalculatedLineItemConnection), graphql_name='addedLineItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    cart_discount_amount_set = sgqlc.types.Field(MoneyBag, graphql_name='cartDiscountAmountSet')
    committed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='committed')
    line_items = sgqlc.types.Field(sgqlc.types.non_null(CalculatedLineItemConnection), graphql_name='lineItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    notification_preview_html = sgqlc.types.Field(HTML, graphql_name='notificationPreviewHtml')
    notification_preview_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='notificationPreviewTitle')
    original_order = sgqlc.types.Field(sgqlc.types.non_null('Order'), graphql_name='originalOrder')
    staged_changes = sgqlc.types.Field(sgqlc.types.non_null(OrderStagedChangeConnection), graphql_name='stagedChanges', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    subtotal_line_items_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='subtotalLineItemsQuantity')
    subtotal_price_set = sgqlc.types.Field(MoneyBag, graphql_name='subtotalPriceSet')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxLine))), graphql_name='taxLines')
    total_outstanding_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalOutstandingSet')
    total_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalPriceSet')


class CalculatedScriptDiscountApplication(sgqlc.types.Type, CalculatedDiscountApplication):
    __schema__ = shopify_schema
    __field_names__ = ()


class Channel(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('app', 'collection_publications_v3', 'collections', 'has_collection', 'name', 'product_publications_v3', 'products', 'supports_future_publishing')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    collection_publications_v3 = sgqlc.types.Field(sgqlc.types.non_null(ResourcePublicationConnection), graphql_name='collectionPublicationsV3', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    collections = sgqlc.types.Field(sgqlc.types.non_null(CollectionConnection), graphql_name='collections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    has_collection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasCollection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    product_publications_v3 = sgqlc.types.Field(sgqlc.types.non_null(ResourcePublicationConnection), graphql_name='productPublicationsV3', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    products = sgqlc.types.Field(sgqlc.types.non_null(ProductConnection), graphql_name='products', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    supports_future_publishing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='supportsFuturePublishing')


class Collection(sgqlc.types.Type, HasMetafields, Node, Publishable, HasPublishedTranslations):
    __schema__ = shopify_schema
    __field_names__ = ('description', 'description_html', 'feedback', 'handle', 'has_product', 'image', 'products', 'products_count', 'rule_set', 'seo', 'sort_order', 'storefront_id', 'template_suffix', 'title', 'updated_at')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description', args=sgqlc.types.ArgDict((
        ('truncate_at', sgqlc.types.Arg(Int, graphql_name='truncateAt', default=None)),
))
    )
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHtml')
    feedback = sgqlc.types.Field(ResourceFeedback, graphql_name='feedback')
    handle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='handle')
    has_product = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasProduct', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    image = sgqlc.types.Field('Image', graphql_name='image', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    products = sgqlc.types.Field(sgqlc.types.non_null(ProductConnection), graphql_name='products', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProductCollectionSortKeys, graphql_name='sortKey', default='COLLECTION_DEFAULT')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    products_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='productsCount')
    rule_set = sgqlc.types.Field(CollectionRuleSet, graphql_name='ruleSet')
    seo = sgqlc.types.Field(sgqlc.types.non_null(SEO), graphql_name='seo')
    sort_order = sgqlc.types.Field(sgqlc.types.non_null(CollectionSortOrder), graphql_name='sortOrder')
    storefront_id = sgqlc.types.Field(sgqlc.types.non_null(StorefrontID), graphql_name='storefrontId')
    template_suffix = sgqlc.types.Field(String, graphql_name='templateSuffix')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class CommentEvent(sgqlc.types.Type, Node, Event):
    __schema__ = shopify_schema
    __field_names__ = ('attachments', 'can_delete', 'can_edit', 'edited', 'embed', 'raw_message', 'subject')
    attachments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentEventAttachment))), graphql_name='attachments')
    can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canDelete')
    can_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canEdit')
    edited = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='edited')
    embed = sgqlc.types.Field('CommentEventEmbed', graphql_name='embed')
    raw_message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rawMessage')
    subject = sgqlc.types.Field(sgqlc.types.non_null(CommentEventSubject), graphql_name='subject')


class Customer(sgqlc.types.Type, Node, CommentEventSubject, HasMetafields, LegacyInteroperability, HasEvents):
    __schema__ = shopify_schema
    __field_names__ = ('accepts_marketing', 'accepts_marketing_updated_at', 'addresses', 'average_order_amount_v2', 'can_delete', 'created_at', 'default_address', 'display_name', 'email', 'first_name', 'has_note', 'image', 'last_name', 'last_order', 'lifetime_duration', 'locale', 'marketing_opt_in_level', 'multipass_identifier', 'note', 'orders', 'orders_count', 'phone', 'state', 'tags', 'tax_exempt', 'tax_exemptions', 'total_spent', 'total_spent_v2', 'updated_at', 'valid_email_address', 'verified_email')
    accepts_marketing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptsMarketing')
    accepts_marketing_updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='acceptsMarketingUpdatedAt')
    addresses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MailingAddress'))), graphql_name='addresses', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    average_order_amount_v2 = sgqlc.types.Field(MoneyV2, graphql_name='averageOrderAmountV2')
    can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canDelete')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    default_address = sgqlc.types.Field('MailingAddress', graphql_name='defaultAddress')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    email = sgqlc.types.Field(String, graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    has_note = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNote')
    image = sgqlc.types.Field(sgqlc.types.non_null('Image'), graphql_name='image', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    last_order = sgqlc.types.Field('Order', graphql_name='lastOrder')
    lifetime_duration = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lifetimeDuration')
    locale = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='locale')
    marketing_opt_in_level = sgqlc.types.Field(CustomerMarketingOptInLevel, graphql_name='marketingOptInLevel')
    multipass_identifier = sgqlc.types.Field(String, graphql_name='multipassIdentifier')
    note = sgqlc.types.Field(String, graphql_name='note')
    orders = sgqlc.types.Field(sgqlc.types.non_null(OrderConnection), graphql_name='orders', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(OrderSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    orders_count = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='ordersCount')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    state = sgqlc.types.Field(sgqlc.types.non_null(CustomerState), graphql_name='state')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags')
    tax_exempt = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxExempt')
    tax_exemptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxExemption))), graphql_name='taxExemptions')
    total_spent = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='totalSpent')
    total_spent_v2 = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='totalSpentV2')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    valid_email_address = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='validEmailAddress')
    verified_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verifiedEmail')


class CustomerVisit(sgqlc.types.Type, CustomerMoment, Node):
    __schema__ = shopify_schema
    __field_names__ = ('landing_page', 'landing_page_html', 'marketing_event', 'referral_code', 'referral_info_html', 'referrer_url', 'source', 'source_description', 'source_type', 'utm_parameters')
    landing_page = sgqlc.types.Field(URL, graphql_name='landingPage')
    landing_page_html = sgqlc.types.Field(HTML, graphql_name='landingPageHtml')
    marketing_event = sgqlc.types.Field('MarketingEvent', graphql_name='marketingEvent')
    referral_code = sgqlc.types.Field(String, graphql_name='referralCode')
    referral_info_html = sgqlc.types.Field(sgqlc.types.non_null(FormattedString), graphql_name='referralInfoHtml')
    referrer_url = sgqlc.types.Field(URL, graphql_name='referrerUrl')
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='source')
    source_description = sgqlc.types.Field(String, graphql_name='sourceDescription')
    source_type = sgqlc.types.Field(MarketingTactic, graphql_name='sourceType')
    utm_parameters = sgqlc.types.Field(UTMParameters, graphql_name='utmParameters')


class DeliveryCarrierService(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('available_services_for_countries', 'formatted_name', 'icon', 'name')
    available_services_for_countries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryAvailableService))), graphql_name='availableServicesForCountries', args=sgqlc.types.ArgDict((
        ('origins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='origins', default=None)),
        ('country_codes', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode)), graphql_name='countryCodes', default=None)),
        ('rest_of_world', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='restOfWorld', default=None)),
))
    )
    formatted_name = sgqlc.types.Field(String, graphql_name='formattedName')
    icon = sgqlc.types.Field(sgqlc.types.non_null('Image'), graphql_name='icon')
    name = sgqlc.types.Field(String, graphql_name='name')


class DeliveryCondition(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('condition_criteria', 'field', 'operator')
    condition_criteria = sgqlc.types.Field(sgqlc.types.non_null('DeliveryConditionCriteria'), graphql_name='conditionCriteria')
    field = sgqlc.types.Field(sgqlc.types.non_null(DeliveryConditionField), graphql_name='field')
    operator = sgqlc.types.Field(sgqlc.types.non_null(DeliveryConditionOperator), graphql_name='operator')


class DeliveryCountry(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('code', 'name', 'provinces')
    code = sgqlc.types.Field(sgqlc.types.non_null(DeliveryCountryCodeOrRestOfWorld), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    provinces = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DeliveryProvince'))), graphql_name='provinces')


class DeliveryLocationGroup(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('locations',)
    locations = sgqlc.types.Field(sgqlc.types.non_null(LocationConnection), graphql_name='locations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(LocationSortKeys, graphql_name='sortKey', default='NAME')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('include_legacy', sgqlc.types.Arg(Boolean, graphql_name='includeLegacy', default=False)),
        ('include_inactive', sgqlc.types.Arg(Boolean, graphql_name='includeInactive', default=False)),
))
    )


class DeliveryMethod(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('method_type',)
    method_type = sgqlc.types.Field(sgqlc.types.non_null(DeliveryMethodType), graphql_name='methodType')


class DeliveryMethodDefinition(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('active', 'description', 'method_conditions', 'name', 'rate_provider')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    description = sgqlc.types.Field(String, graphql_name='description')
    method_conditions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryCondition))), graphql_name='methodConditions')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    rate_provider = sgqlc.types.Field(sgqlc.types.non_null('DeliveryRateProvider'), graphql_name='rateProvider')


class DeliveryParticipant(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('adapt_to_new_services_flag', 'carrier_service', 'fixed_fee', 'participant_services', 'percentage_of_rate_fee')
    adapt_to_new_services_flag = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='adaptToNewServicesFlag')
    carrier_service = sgqlc.types.Field(sgqlc.types.non_null(DeliveryCarrierService), graphql_name='carrierService')
    fixed_fee = sgqlc.types.Field(MoneyV2, graphql_name='fixedFee')
    participant_services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryParticipantService))), graphql_name='participantServices')
    percentage_of_rate_fee = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='percentageOfRateFee')


class DeliveryProfile(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('active_method_definitions_count', 'default', 'legacy_mode', 'locations_without_rates_count', 'name', 'origin_location_count', 'product_variants_count_v2', 'profile_items', 'profile_location_groups', 'unassigned_locations', 'zone_country_count')
    active_method_definitions_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='activeMethodDefinitionsCount')
    default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='default')
    legacy_mode = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='legacyMode')
    locations_without_rates_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='locationsWithoutRatesCount')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    origin_location_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='originLocationCount')
    product_variants_count_v2 = sgqlc.types.Field(sgqlc.types.non_null(DeliveryProductVariantsCount), graphql_name='productVariantsCountV2')
    profile_items = sgqlc.types.Field(sgqlc.types.non_null(DeliveryProfileItemConnection), graphql_name='profileItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProfileItemSortKeys, graphql_name='sortKey', default='ID')),
))
    )
    profile_location_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryProfileLocationGroup))), graphql_name='profileLocationGroups')
    unassigned_locations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Location'))), graphql_name='unassignedLocations')
    zone_country_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='zoneCountryCount')


class DeliveryProvince(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('code', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DeliveryRateDefinition(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('price',)
    price = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='price')


class DeliveryZone(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('countries', 'name')
    countries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DeliveryCountry))), graphql_name='countries')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DiscountAutomaticBxgy(sgqlc.types.Type, Node, HasEvents):
    __schema__ = shopify_schema
    __field_names__ = ('async_usage_count', 'created_at', 'customer_buys', 'customer_gets', 'ends_at', 'starts_at', 'status', 'summary', 'title', 'uses_per_order_limit')
    async_usage_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='asyncUsageCount')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_buys = sgqlc.types.Field(sgqlc.types.non_null(DiscountCustomerBuys), graphql_name='customerBuys')
    customer_gets = sgqlc.types.Field(sgqlc.types.non_null(DiscountCustomerGets), graphql_name='customerGets')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(DiscountStatus), graphql_name='status')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    uses_per_order_limit = sgqlc.types.Field(Int, graphql_name='usesPerOrderLimit')


class DiscountAutomaticNode(sgqlc.types.Type, Node, HasEvents):
    __schema__ = shopify_schema
    __field_names__ = ('automatic_discount',)
    automatic_discount = sgqlc.types.Field(sgqlc.types.non_null('DiscountAutomatic'), graphql_name='automaticDiscount')


class DiscountCodeApplication(sgqlc.types.Type, DiscountApplication):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')


class DiscountCodeNode(sgqlc.types.Type, Node, HasEvents):
    __schema__ = shopify_schema
    __field_names__ = ('code_discount',)
    code_discount = sgqlc.types.Field(sgqlc.types.non_null('DiscountCode'), graphql_name='codeDiscount')


class DiscountUserError(sgqlc.types.Type, DisplayableError):
    __schema__ = shopify_schema
    __field_names__ = ('code', 'extra_info')
    code = sgqlc.types.Field(DiscountErrorCode, graphql_name='code')
    extra_info = sgqlc.types.Field(String, graphql_name='extraInfo')


class Domain(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('host', 'localization', 'ssl_enabled', 'url')
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='host')
    localization = sgqlc.types.Field(DomainLocalization, graphql_name='localization')
    ssl_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='sslEnabled')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class DraftOrder(sgqlc.types.Type, Node, HasMetafields, CommentEventSubject, LegacyInteroperability, HasEvents):
    __schema__ = shopify_schema
    __field_names__ = ('applied_discount', 'billing_address', 'completed_at', 'created_at', 'currency_code', 'custom_attributes', 'customer', 'email', 'invoice_sent_at', 'invoice_url', 'line_items', 'name', 'note2', 'order', 'ready', 'shipping_address', 'shipping_line', 'status', 'subtotal_price', 'tags', 'tax_exempt', 'tax_lines', 'taxes_included', 'total_price', 'total_shipping_price', 'total_tax', 'total_weight', 'updated_at')
    applied_discount = sgqlc.types.Field(DraftOrderAppliedDiscount, graphql_name='appliedDiscount')
    billing_address = sgqlc.types.Field('MailingAddress', graphql_name='billingAddress')
    completed_at = sgqlc.types.Field(DateTime, graphql_name='completedAt')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    currency_code = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='currencyCode')
    custom_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='customAttributes')
    customer = sgqlc.types.Field(Customer, graphql_name='customer')
    email = sgqlc.types.Field(String, graphql_name='email')
    invoice_sent_at = sgqlc.types.Field(DateTime, graphql_name='invoiceSentAt')
    invoice_url = sgqlc.types.Field(URL, graphql_name='invoiceUrl')
    line_items = sgqlc.types.Field(sgqlc.types.non_null(DraftOrderLineItemConnection), graphql_name='lineItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    note2 = sgqlc.types.Field(String, graphql_name='note2')
    order = sgqlc.types.Field('Order', graphql_name='order')
    ready = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='ready')
    shipping_address = sgqlc.types.Field('MailingAddress', graphql_name='shippingAddress')
    shipping_line = sgqlc.types.Field(ShippingLine, graphql_name='shippingLine')
    status = sgqlc.types.Field(sgqlc.types.non_null(DraftOrderStatus), graphql_name='status')
    subtotal_price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='subtotalPrice')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags')
    tax_exempt = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxExempt')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxLine))), graphql_name='taxLines')
    taxes_included = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxesIncluded')
    total_price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='totalPrice')
    total_shipping_price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='totalShippingPrice')
    total_tax = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='totalTax')
    total_weight = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='totalWeight')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class DraftOrderLineItem(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('applied_discount', 'custom', 'custom_attributes', 'discounted_total', 'discounted_unit_price', 'fulfillment_service', 'image', 'is_gift_card', 'name', 'original_total', 'original_unit_price', 'product', 'quantity', 'requires_shipping', 'sku', 'tax_lines', 'taxable', 'title', 'total_discount', 'variant', 'variant_title', 'vendor', 'weight')
    applied_discount = sgqlc.types.Field(DraftOrderAppliedDiscount, graphql_name='appliedDiscount')
    custom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='custom')
    custom_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='customAttributes')
    discounted_total = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='discountedTotal')
    discounted_unit_price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='discountedUnitPrice')
    fulfillment_service = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentService), graphql_name='fulfillmentService')
    image = sgqlc.types.Field('Image', graphql_name='image', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    is_gift_card = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGiftCard')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    original_total = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='originalTotal')
    original_unit_price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='originalUnitPrice')
    product = sgqlc.types.Field('Product', graphql_name='product')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    requires_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresShipping')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxLine))), graphql_name='taxLines')
    taxable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxable')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_discount = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='totalDiscount')
    variant = sgqlc.types.Field('ProductVariant', graphql_name='variant')
    variant_title = sgqlc.types.Field(String, graphql_name='variantTitle')
    vendor = sgqlc.types.Field(String, graphql_name='vendor')
    weight = sgqlc.types.Field(Weight, graphql_name='weight')


class Duty(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('country_code_of_origin', 'harmonized_system_code', 'price', 'tax_lines')
    country_code_of_origin = sgqlc.types.Field(CountryCode, graphql_name='countryCodeOfOrigin')
    harmonized_system_code = sgqlc.types.Field(String, graphql_name='harmonizedSystemCode')
    price = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='price')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxLine))), graphql_name='taxLines')


class ExternalVideo(sgqlc.types.Type, Node, Media):
    __schema__ = shopify_schema
    __field_names__ = ('embedded_url',)
    embedded_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='embeddedUrl')


class Fulfillment(sgqlc.types.Type, LegacyInteroperability, Node):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'delivered_at', 'display_status', 'estimated_delivery_at', 'events', 'fulfillment_line_items', 'fulfillment_orders', 'in_transit_at', 'location', 'name', 'order', 'requires_shipping', 'service', 'status', 'total_quantity', 'tracking_info', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    delivered_at = sgqlc.types.Field(DateTime, graphql_name='deliveredAt')
    display_status = sgqlc.types.Field(FulfillmentDisplayStatus, graphql_name='displayStatus')
    estimated_delivery_at = sgqlc.types.Field(DateTime, graphql_name='estimatedDeliveryAt')
    events = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentEventConnection), graphql_name='events', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(FulfillmentEventSortKeys, graphql_name='sortKey', default='HAPPENED_AT')),
))
    )
    fulfillment_line_items = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentLineItemConnection), graphql_name='fulfillmentLineItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    fulfillment_orders = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderConnection), graphql_name='fulfillmentOrders', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    in_transit_at = sgqlc.types.Field(DateTime, graphql_name='inTransitAt')
    location = sgqlc.types.Field('Location', graphql_name='location')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(sgqlc.types.non_null('Order'), graphql_name='order')
    requires_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresShipping')
    service = sgqlc.types.Field(FulfillmentService, graphql_name='service')
    status = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentStatus), graphql_name='status')
    total_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalQuantity')
    tracking_info = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FulfillmentTrackingInfo))), graphql_name='trackingInfo', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class FulfillmentEvent(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('happened_at', 'status')
    happened_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='happenedAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentEventStatus), graphql_name='status')


class FulfillmentLineItem(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('discounted_total_set', 'line_item', 'original_total_set', 'quantity')
    discounted_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='discountedTotalSet')
    line_item = sgqlc.types.Field(sgqlc.types.non_null('LineItem'), graphql_name='lineItem')
    original_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='originalTotalSet')
    quantity = sgqlc.types.Field(Int, graphql_name='quantity')


class FulfillmentOrder(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('assigned_location', 'delivery_method', 'destination', 'fulfillments', 'line_items', 'locations_for_move', 'merchant_requests', 'order', 'request_status', 'status', 'supported_actions')
    assigned_location = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderAssignedLocation), graphql_name='assignedLocation')
    delivery_method = sgqlc.types.Field(DeliveryMethod, graphql_name='deliveryMethod')
    destination = sgqlc.types.Field('FulfillmentOrderDestination', graphql_name='destination')
    fulfillments = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentConnection), graphql_name='fulfillments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    line_items = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderLineItemConnection), graphql_name='lineItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    locations_for_move = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderLocationForMoveConnection), graphql_name='locationsForMove', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    merchant_requests = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderMerchantRequestConnection), graphql_name='merchantRequests', args=sgqlc.types.ArgDict((
        ('kind', sgqlc.types.Arg(FulfillmentOrderMerchantRequestKind, graphql_name='kind', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    order = sgqlc.types.Field(sgqlc.types.non_null('Order'), graphql_name='order')
    request_status = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderRequestStatus), graphql_name='requestStatus')
    status = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderStatus), graphql_name='status')
    supported_actions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FulfillmentOrderSupportedAction))), graphql_name='supportedActions')


class FulfillmentOrderDestination(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('address1', 'address2', 'city', 'company', 'country_code', 'email', 'first_name', 'last_name', 'phone', 'province', 'zip')
    address1 = sgqlc.types.Field(String, graphql_name='address1')
    address2 = sgqlc.types.Field(String, graphql_name='address2')
    city = sgqlc.types.Field(String, graphql_name='city')
    company = sgqlc.types.Field(String, graphql_name='company')
    country_code = sgqlc.types.Field(CountryCode, graphql_name='countryCode')
    email = sgqlc.types.Field(String, graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    zip = sgqlc.types.Field(String, graphql_name='zip')


class FulfillmentOrderLineItem(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('line_item', 'remaining_quantity', 'total_quantity')
    line_item = sgqlc.types.Field(sgqlc.types.non_null('LineItem'), graphql_name='lineItem')
    remaining_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='remainingQuantity')
    total_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalQuantity')


class FulfillmentOrderMerchantRequest(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('kind', 'message', 'request_options', 'response_data', 'sent_at')
    kind = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderMerchantRequestKind), graphql_name='kind')
    message = sgqlc.types.Field(String, graphql_name='message')
    request_options = sgqlc.types.Field(JSON, graphql_name='requestOptions')
    response_data = sgqlc.types.Field(JSON, graphql_name='responseData')
    sent_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='sentAt')


class Image(sgqlc.types.Type, HasMetafields):
    __schema__ = shopify_schema
    __field_names__ = ('alt_text', 'id', 'original_src', 'transformed_src')
    alt_text = sgqlc.types.Field(String, graphql_name='altText')
    id = sgqlc.types.Field(ID, graphql_name='id')
    original_src = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='originalSrc')
    transformed_src = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='transformedSrc', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
        ('preferred_content_type', sgqlc.types.Arg(ImageContentType, graphql_name='preferredContentType', default=None)),
))
    )


class InventoryItem(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('country_code_of_origin', 'country_harmonized_system_codes', 'created_at', 'duplicate_sku_count', 'harmonized_system_code', 'inventory_history_url', 'inventory_level', 'inventory_levels', 'locations_count', 'province_code_of_origin', 'requires_shipping', 'sku', 'tracked', 'tracked_editable', 'unit_cost', 'updated_at', 'variant')
    country_code_of_origin = sgqlc.types.Field(CountryCode, graphql_name='countryCodeOfOrigin')
    country_harmonized_system_codes = sgqlc.types.Field(sgqlc.types.non_null(CountryHarmonizedSystemCodeConnection), graphql_name='countryHarmonizedSystemCodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    duplicate_sku_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duplicateSkuCount')
    harmonized_system_code = sgqlc.types.Field(String, graphql_name='harmonizedSystemCode')
    inventory_history_url = sgqlc.types.Field(URL, graphql_name='inventoryHistoryUrl')
    inventory_level = sgqlc.types.Field('InventoryLevel', graphql_name='inventoryLevel', args=sgqlc.types.ArgDict((
        ('location_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='locationId', default=None)),
))
    )
    inventory_levels = sgqlc.types.Field(sgqlc.types.non_null(InventoryLevelConnection), graphql_name='inventoryLevels', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    locations_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='locationsCount')
    province_code_of_origin = sgqlc.types.Field(String, graphql_name='provinceCodeOfOrigin')
    requires_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresShipping')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    tracked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tracked')
    tracked_editable = sgqlc.types.Field(sgqlc.types.non_null(EditableProperty), graphql_name='trackedEditable')
    unit_cost = sgqlc.types.Field(MoneyV2, graphql_name='unitCost')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    variant = sgqlc.types.Field(sgqlc.types.non_null('ProductVariant'), graphql_name='variant')


class InventoryLevel(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('available', 'can_deactivate', 'created_at', 'deactivation_alert', 'deactivation_alert_html', 'incoming', 'item', 'location', 'updated_at')
    available = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='available')
    can_deactivate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canDeactivate')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    deactivation_alert = sgqlc.types.Field(String, graphql_name='deactivationAlert')
    deactivation_alert_html = sgqlc.types.Field(FormattedString, graphql_name='deactivationAlertHtml')
    incoming = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='incoming')
    item = sgqlc.types.Field(sgqlc.types.non_null(InventoryItem), graphql_name='item')
    location = sgqlc.types.Field(sgqlc.types.non_null('Location'), graphql_name='location')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class LineItem(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('custom_attributes', 'discount_allocations', 'discounted_total_set', 'discounted_unit_price_set', 'duties', 'fulfillable_quantity', 'fulfillment_service', 'fulfillment_status', 'image', 'merchant_editable', 'name', 'non_fulfillable_quantity', 'original_total_set', 'original_unit_price_set', 'product', 'quantity', 'refundable_quantity', 'requires_shipping', 'restockable', 'sku', 'tax_lines', 'taxable', 'title', 'total_discount_set', 'unfulfilled_discounted_total_set', 'unfulfilled_original_total_set', 'unfulfilled_quantity', 'variant', 'variant_title', 'vendor')
    custom_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='customAttributes')
    discount_allocations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DiscountAllocation))), graphql_name='discountAllocations')
    discounted_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='discountedTotalSet')
    discounted_unit_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='discountedUnitPriceSet')
    duties = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Duty))), graphql_name='duties')
    fulfillable_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fulfillableQuantity')
    fulfillment_service = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentService), graphql_name='fulfillmentService')
    fulfillment_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fulfillmentStatus')
    image = sgqlc.types.Field(Image, graphql_name='image', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    merchant_editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='merchantEditable')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    non_fulfillable_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nonFulfillableQuantity')
    original_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='originalTotalSet')
    original_unit_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='originalUnitPriceSet')
    product = sgqlc.types.Field('Product', graphql_name='product')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    refundable_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='refundableQuantity')
    requires_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresShipping')
    restockable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restockable')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxLine))), graphql_name='taxLines', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    taxable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxable')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_discount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalDiscountSet')
    unfulfilled_discounted_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='unfulfilledDiscountedTotalSet')
    unfulfilled_original_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='unfulfilledOriginalTotalSet')
    unfulfilled_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unfulfilledQuantity')
    variant = sgqlc.types.Field('ProductVariant', graphql_name='variant')
    variant_title = sgqlc.types.Field(String, graphql_name='variantTitle')
    vendor = sgqlc.types.Field(String, graphql_name='vendor')


class LineItemMutable(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('custom_attributes', 'discount_allocations', 'discounted_total_set', 'discounted_unit_price_set', 'fulfillable_quantity', 'fulfillment_service', 'fulfillment_status', 'image', 'merchant_editable', 'name', 'non_fulfillable_quantity', 'original_total_set', 'original_unit_price_set', 'product', 'quantity', 'refundable_quantity', 'requires_shipping', 'restockable', 'sku', 'tax_lines', 'taxable', 'title', 'total_discount_set', 'unfulfilled_discounted_total_set', 'unfulfilled_original_total_set', 'unfulfilled_quantity', 'variant', 'variant_title', 'vendor')
    custom_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='customAttributes')
    discount_allocations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DiscountAllocation))), graphql_name='discountAllocations')
    discounted_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='discountedTotalSet')
    discounted_unit_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='discountedUnitPriceSet')
    fulfillable_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fulfillableQuantity')
    fulfillment_service = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentService), graphql_name='fulfillmentService')
    fulfillment_status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fulfillmentStatus')
    image = sgqlc.types.Field(Image, graphql_name='image', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    merchant_editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='merchantEditable')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    non_fulfillable_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nonFulfillableQuantity')
    original_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='originalTotalSet')
    original_unit_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='originalUnitPriceSet')
    product = sgqlc.types.Field('Product', graphql_name='product')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    refundable_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='refundableQuantity')
    requires_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresShipping')
    restockable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restockable')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxLine))), graphql_name='taxLines', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    taxable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxable')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_discount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalDiscountSet')
    unfulfilled_discounted_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='unfulfilledDiscountedTotalSet')
    unfulfilled_original_total_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='unfulfilledOriginalTotalSet')
    unfulfilled_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unfulfilledQuantity')
    variant = sgqlc.types.Field('ProductVariant', graphql_name='variant')
    variant_title = sgqlc.types.Field(String, graphql_name='variantTitle')
    vendor = sgqlc.types.Field(String, graphql_name='vendor')


class Link(sgqlc.types.Type, HasPublishedTranslations):
    __schema__ = shopify_schema
    __field_names__ = ('label', 'url')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class Location(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('activatable', 'address', 'address_verified', 'deactivatable', 'deactivated_at', 'deletable', 'fulfillment_service', 'fulfills_online_orders', 'has_active_inventory', 'has_unfulfilled_orders', 'inventory_level', 'inventory_levels', 'is_active', 'name', 'ships_inventory', 'suggested_addresses')
    activatable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activatable')
    address = sgqlc.types.Field(sgqlc.types.non_null(LocationAddress), graphql_name='address')
    address_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addressVerified')
    deactivatable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deactivatable')
    deactivated_at = sgqlc.types.Field(String, graphql_name='deactivatedAt')
    deletable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deletable')
    fulfillment_service = sgqlc.types.Field(FulfillmentService, graphql_name='fulfillmentService')
    fulfills_online_orders = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fulfillsOnlineOrders')
    has_active_inventory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasActiveInventory')
    has_unfulfilled_orders = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasUnfulfilledOrders')
    inventory_level = sgqlc.types.Field(InventoryLevel, graphql_name='inventoryLevel', args=sgqlc.types.ArgDict((
        ('inventory_item_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='inventoryItemId', default=None)),
))
    )
    inventory_levels = sgqlc.types.Field(sgqlc.types.non_null(InventoryLevelConnection), graphql_name='inventoryLevels', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    ships_inventory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shipsInventory')
    suggested_addresses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LocationSuggestedAddress))), graphql_name='suggestedAddresses')


class MailingAddress(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('address1', 'address2', 'city', 'company', 'country', 'country_code_v2', 'first_name', 'formatted', 'formatted_area', 'last_name', 'latitude', 'longitude', 'name', 'phone', 'province', 'province_code', 'zip')
    address1 = sgqlc.types.Field(String, graphql_name='address1')
    address2 = sgqlc.types.Field(String, graphql_name='address2')
    city = sgqlc.types.Field(String, graphql_name='city')
    company = sgqlc.types.Field(String, graphql_name='company')
    country = sgqlc.types.Field(String, graphql_name='country')
    country_code_v2 = sgqlc.types.Field(CountryCode, graphql_name='countryCodeV2')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    formatted = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='formatted', args=sgqlc.types.ArgDict((
        ('with_name', sgqlc.types.Arg(Boolean, graphql_name='withName', default=False)),
        ('with_company', sgqlc.types.Arg(Boolean, graphql_name='withCompany', default=True)),
))
    )
    formatted_area = sgqlc.types.Field(String, graphql_name='formattedArea')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    latitude = sgqlc.types.Field(Float, graphql_name='latitude')
    longitude = sgqlc.types.Field(Float, graphql_name='longitude')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    province_code = sgqlc.types.Field(String, graphql_name='provinceCode')
    zip = sgqlc.types.Field(String, graphql_name='zip')


class ManualDiscountApplication(sgqlc.types.Type, DiscountApplication):
    __schema__ = shopify_schema
    __field_names__ = ('description', 'title')
    description = sgqlc.types.Field(String, graphql_name='description')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class MarketingActivity(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('activity_list_url', 'ad_spend', 'app', 'app_errors', 'budget', 'created_at', 'form_data', 'marketing_channel', 'marketing_event', 'source_and_medium', 'status', 'status_badge_type', 'status_label', 'status_transitioned_at', 'tactic', 'target_status', 'title', 'updated_at', 'utm_parameters')
    activity_list_url = sgqlc.types.Field(URL, graphql_name='activityListUrl')
    ad_spend = sgqlc.types.Field(MoneyV2, graphql_name='adSpend')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    app_errors = sgqlc.types.Field(MarketingActivityExtensionAppErrors, graphql_name='appErrors')
    budget = sgqlc.types.Field(MarketingBudget, graphql_name='budget')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    form_data = sgqlc.types.Field(String, graphql_name='formData')
    marketing_channel = sgqlc.types.Field(sgqlc.types.non_null(MarketingChannel), graphql_name='marketingChannel')
    marketing_event = sgqlc.types.Field('MarketingEvent', graphql_name='marketingEvent')
    source_and_medium = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceAndMedium')
    status = sgqlc.types.Field(sgqlc.types.non_null(MarketingActivityStatus), graphql_name='status')
    status_badge_type = sgqlc.types.Field(MarketingActivityStatusBadgeType, graphql_name='statusBadgeType')
    status_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='statusLabel')
    status_transitioned_at = sgqlc.types.Field(DateTime, graphql_name='statusTransitionedAt')
    tactic = sgqlc.types.Field(sgqlc.types.non_null(MarketingTactic), graphql_name='tactic')
    target_status = sgqlc.types.Field(MarketingActivityStatus, graphql_name='targetStatus')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    utm_parameters = sgqlc.types.Field(UTMParameters, graphql_name='utmParameters')


class MarketingEvent(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('app', 'channel', 'description', 'ended_at', 'manage_url', 'preview_url', 'remote_id', 'scheduled_to_end_at', 'source_and_medium', 'started_at', 'type', 'utm_campaign', 'utm_medium', 'utm_source')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    channel = sgqlc.types.Field(MarketingChannel, graphql_name='channel')
    description = sgqlc.types.Field(String, graphql_name='description')
    ended_at = sgqlc.types.Field(DateTime, graphql_name='endedAt')
    manage_url = sgqlc.types.Field(URL, graphql_name='manageUrl')
    preview_url = sgqlc.types.Field(URL, graphql_name='previewUrl')
    remote_id = sgqlc.types.Field(String, graphql_name='remoteId')
    scheduled_to_end_at = sgqlc.types.Field(DateTime, graphql_name='scheduledToEndAt')
    source_and_medium = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sourceAndMedium')
    started_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startedAt')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketingTactic), graphql_name='type')
    utm_campaign = sgqlc.types.Field(String, graphql_name='utmCampaign')
    utm_medium = sgqlc.types.Field(String, graphql_name='utmMedium')
    utm_source = sgqlc.types.Field(String, graphql_name='utmSource')


class MediaImage(sgqlc.types.Type, Node, Media):
    __schema__ = shopify_schema
    __field_names__ = ('image', 'mime_type')
    image = sgqlc.types.Field(Image, graphql_name='image')
    mime_type = sgqlc.types.Field(String, graphql_name='mimeType')


class MediaUserError(sgqlc.types.Type, DisplayableError):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(MediaUserErrorCode, graphql_name='code')


class Metafield(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'description', 'key', 'namespace', 'owner_type', 'updated_at', 'value', 'value_type')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    owner_type = sgqlc.types.Field(sgqlc.types.non_null(MetafieldOwnerType), graphql_name='ownerType')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(MetafieldValueType), graphql_name='valueType')


class MetafieldStorefrontVisibility(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'key', 'namespace', 'owner_type', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    owner_type = sgqlc.types.Field(sgqlc.types.non_null(MetafieldOwnerType), graphql_name='ownerType')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class Model3d(sgqlc.types.Type, Node, Media):
    __schema__ = shopify_schema
    __field_names__ = ('filename', 'original_source', 'sources')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    original_source = sgqlc.types.Field(Model3dSource, graphql_name='originalSource')
    sources = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Model3dSource))), graphql_name='sources')


class OnlineStoreArticle(sgqlc.types.Type, Node, Navigable, HasPublishedTranslations):
    __schema__ = shopify_schema
    __field_names__ = ()


class OnlineStoreBlog(sgqlc.types.Type, Node, HasPublishedTranslations):
    __schema__ = shopify_schema
    __field_names__ = ()


class OnlineStorePage(sgqlc.types.Type, Node, Navigable, HasPublishedTranslations):
    __schema__ = shopify_schema
    __field_names__ = ()


class Order(sgqlc.types.Type, Node, CommentEventSubject, HasMetafields, LegacyInteroperability, HasEvents, HasLocalizationExtensions):
    __schema__ = shopify_schema
    __field_names__ = ('alerts', 'billing_address', 'billing_address_matches_shipping_address', 'can_mark_as_paid', 'can_notify_customer', 'cancel_reason', 'cancelled_at', 'capturable', 'cart_discount_amount_set', 'client_ip', 'closed', 'closed_at', 'confirmed', 'created_at', 'currency_code', 'current_cart_discount_amount_set', 'current_subtotal_line_items_quantity', 'current_subtotal_price_set', 'current_tax_lines', 'current_total_discounts_set', 'current_total_duties_set', 'current_total_price_set', 'current_total_tax_set', 'current_total_weight', 'custom_attributes', 'customer', 'customer_accepts_marketing', 'customer_journey_summary', 'customer_locale', 'discount_applications', 'discount_code', 'display_address', 'display_financial_status', 'display_fulfillment_status', 'disputes', 'draft_fulfillments', 'edited', 'email', 'fulfillable', 'fulfillment_orders', 'fulfillments', 'fully_paid', 'line_items', 'line_items_mutable', 'merchant_editable', 'merchant_editable_errors', 'name', 'net_payment_set', 'non_fulfillable_line_items', 'note', 'original_total_duties_set', 'original_total_price_set', 'payment_collection_details', 'payment_gateway_names', 'phone', 'physical_location', 'presentment_currency_code', 'processed_at', 'publication', 'refund_discrepancy_set', 'refundable', 'refunds', 'requires_shipping', 'restockable', 'risk_level', 'risks', 'shipping_address', 'shipping_line', 'shipping_lines', 'subtotal_line_items_quantity', 'subtotal_price_set', 'suggested_refund', 'tags', 'tax_lines', 'taxes_included', 'test', 'total_capturable_set', 'total_discounts_set', 'total_outstanding_set', 'total_price_set', 'total_received_set', 'total_refunded_set', 'total_refunded_shipping_set', 'total_shipping_price_set', 'total_tax_set', 'total_weight', 'transactions', 'unpaid', 'updated_at')
    alerts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ResourceAlert))), graphql_name='alerts')
    billing_address = sgqlc.types.Field(MailingAddress, graphql_name='billingAddress')
    billing_address_matches_shipping_address = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='billingAddressMatchesShippingAddress')
    can_mark_as_paid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canMarkAsPaid')
    can_notify_customer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canNotifyCustomer')
    cancel_reason = sgqlc.types.Field(OrderCancelReason, graphql_name='cancelReason')
    cancelled_at = sgqlc.types.Field(DateTime, graphql_name='cancelledAt')
    capturable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='capturable')
    cart_discount_amount_set = sgqlc.types.Field(MoneyBag, graphql_name='cartDiscountAmountSet')
    client_ip = sgqlc.types.Field(String, graphql_name='clientIp')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    confirmed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmed')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    currency_code = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='currencyCode')
    current_cart_discount_amount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='currentCartDiscountAmountSet')
    current_subtotal_line_items_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentSubtotalLineItemsQuantity')
    current_subtotal_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='currentSubtotalPriceSet')
    current_tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxLine))), graphql_name='currentTaxLines')
    current_total_discounts_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='currentTotalDiscountsSet')
    current_total_duties_set = sgqlc.types.Field(MoneyBag, graphql_name='currentTotalDutiesSet')
    current_total_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='currentTotalPriceSet')
    current_total_tax_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='currentTotalTaxSet')
    current_total_weight = sgqlc.types.Field(sgqlc.types.non_null(UnsignedInt64), graphql_name='currentTotalWeight')
    custom_attributes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Attribute))), graphql_name='customAttributes')
    customer = sgqlc.types.Field(Customer, graphql_name='customer')
    customer_accepts_marketing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='customerAcceptsMarketing')
    customer_journey_summary = sgqlc.types.Field(CustomerJourneySummary, graphql_name='customerJourneySummary')
    customer_locale = sgqlc.types.Field(String, graphql_name='customerLocale')
    discount_applications = sgqlc.types.Field(sgqlc.types.non_null(DiscountApplicationConnection), graphql_name='discountApplications', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    discount_code = sgqlc.types.Field(String, graphql_name='discountCode')
    display_address = sgqlc.types.Field(MailingAddress, graphql_name='displayAddress')
    display_financial_status = sgqlc.types.Field(OrderDisplayFinancialStatus, graphql_name='displayFinancialStatus')
    display_fulfillment_status = sgqlc.types.Field(sgqlc.types.non_null(OrderDisplayFulfillmentStatus), graphql_name='displayFulfillmentStatus')
    disputes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrderDisputeSummary'))), graphql_name='disputes')
    draft_fulfillments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DraftFulfillment))), graphql_name='draftFulfillments')
    edited = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='edited')
    email = sgqlc.types.Field(String, graphql_name='email')
    fulfillable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fulfillable')
    fulfillment_orders = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderConnection), graphql_name='fulfillmentOrders', args=sgqlc.types.ArgDict((
        ('displayable', sgqlc.types.Arg(Boolean, graphql_name='displayable', default=False)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    fulfillments = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Fulfillment))), graphql_name='fulfillments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    fully_paid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='fullyPaid')
    line_items = sgqlc.types.Field(sgqlc.types.non_null(LineItemConnection), graphql_name='lineItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    line_items_mutable = sgqlc.types.Field(sgqlc.types.non_null(LineItemMutableConnection), graphql_name='lineItemsMutable', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    merchant_editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='merchantEditable')
    merchant_editable_errors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='merchantEditableErrors')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    net_payment_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='netPaymentSet')
    non_fulfillable_line_items = sgqlc.types.Field(sgqlc.types.non_null(LineItemConnection), graphql_name='nonFulfillableLineItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    note = sgqlc.types.Field(String, graphql_name='note')
    original_total_duties_set = sgqlc.types.Field(MoneyBag, graphql_name='originalTotalDutiesSet')
    original_total_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='originalTotalPriceSet')
    payment_collection_details = sgqlc.types.Field(sgqlc.types.non_null(OrderPaymentCollectionDetails), graphql_name='paymentCollectionDetails')
    payment_gateway_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='paymentGatewayNames')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    physical_location = sgqlc.types.Field(Location, graphql_name='physicalLocation')
    presentment_currency_code = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='presentmentCurrencyCode')
    processed_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='processedAt')
    publication = sgqlc.types.Field('Publication', graphql_name='publication')
    refund_discrepancy_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='refundDiscrepancySet')
    refundable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='refundable')
    refunds = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Refund'))), graphql_name='refunds', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    requires_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresShipping')
    restockable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restockable')
    risk_level = sgqlc.types.Field(sgqlc.types.non_null(OrderRiskLevel), graphql_name='riskLevel')
    risks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(OrderRisk))), graphql_name='risks', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    shipping_address = sgqlc.types.Field(MailingAddress, graphql_name='shippingAddress')
    shipping_line = sgqlc.types.Field(ShippingLine, graphql_name='shippingLine')
    shipping_lines = sgqlc.types.Field(sgqlc.types.non_null(ShippingLineConnection), graphql_name='shippingLines', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    subtotal_line_items_quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='subtotalLineItemsQuantity')
    subtotal_price_set = sgqlc.types.Field(MoneyBag, graphql_name='subtotalPriceSet')
    suggested_refund = sgqlc.types.Field(SuggestedRefund, graphql_name='suggestedRefund', args=sgqlc.types.ArgDict((
        ('shipping_amount', sgqlc.types.Arg(Money, graphql_name='shippingAmount', default=None)),
        ('refund_shipping', sgqlc.types.Arg(Boolean, graphql_name='refundShipping', default=None)),
        ('refund_line_items', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(RefundLineItemInput)), graphql_name='refundLineItems', default=None)),
        ('refund_duties', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(RefundDutyInput)), graphql_name='refundDuties', default=None)),
        ('suggest_full_refund', sgqlc.types.Arg(Boolean, graphql_name='suggestFullRefund', default=False)),
))
    )
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags')
    tax_lines = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TaxLine))), graphql_name='taxLines')
    taxes_included = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxesIncluded')
    test = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='test')
    total_capturable_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalCapturableSet')
    total_discounts_set = sgqlc.types.Field(MoneyBag, graphql_name='totalDiscountsSet')
    total_outstanding_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalOutstandingSet')
    total_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalPriceSet')
    total_received_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalReceivedSet')
    total_refunded_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalRefundedSet')
    total_refunded_shipping_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalRefundedShippingSet')
    total_shipping_price_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalShippingPriceSet')
    total_tax_set = sgqlc.types.Field(MoneyBag, graphql_name='totalTaxSet')
    total_weight = sgqlc.types.Field(UnsignedInt64, graphql_name='totalWeight')
    transactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrderTransaction'))), graphql_name='transactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('capturable', sgqlc.types.Arg(Boolean, graphql_name='capturable', default=None)),
        ('manually_resolvable', sgqlc.types.Arg(Boolean, graphql_name='manuallyResolvable', default=None)),
))
    )
    unpaid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='unpaid')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class OrderDisputeSummary(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('initiated_as', 'status')
    initiated_as = sgqlc.types.Field(sgqlc.types.non_null(DisputeType), graphql_name='initiatedAs')
    status = sgqlc.types.Field(sgqlc.types.non_null(DisputeStatus), graphql_name='status')


class OrderTransaction(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('account_number', 'amount_set', 'authorization_code', 'created_at', 'error_code', 'formatted_gateway', 'gateway', 'kind', 'manually_capturable', 'maximum_refundable_v2', 'order', 'parent_transaction', 'payment_icon', 'processed_at', 'status', 'test', 'total_unsettled_set')
    account_number = sgqlc.types.Field(String, graphql_name='accountNumber')
    amount_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='amountSet')
    authorization_code = sgqlc.types.Field(String, graphql_name='authorizationCode')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    error_code = sgqlc.types.Field(OrderTransactionErrorCode, graphql_name='errorCode')
    formatted_gateway = sgqlc.types.Field(String, graphql_name='formattedGateway')
    gateway = sgqlc.types.Field(String, graphql_name='gateway')
    kind = sgqlc.types.Field(sgqlc.types.non_null(OrderTransactionKind), graphql_name='kind')
    manually_capturable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='manuallyCapturable')
    maximum_refundable_v2 = sgqlc.types.Field(MoneyV2, graphql_name='maximumRefundableV2')
    order = sgqlc.types.Field(Order, graphql_name='order')
    parent_transaction = sgqlc.types.Field('OrderTransaction', graphql_name='parentTransaction')
    payment_icon = sgqlc.types.Field(Image, graphql_name='paymentIcon', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    processed_at = sgqlc.types.Field(DateTime, graphql_name='processedAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(OrderTransactionStatus), graphql_name='status')
    test = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='test')
    total_unsettled_set = sgqlc.types.Field(MoneyBag, graphql_name='totalUnsettledSet')


class PriceRule(sgqlc.types.Type, Node, CommentEventSubject, LegacyInteroperability, HasEvents):
    __schema__ = shopify_schema
    __field_names__ = ('allocation_limit', 'allocation_method', 'app', 'created_at', 'customer_selection', 'discount_codes', 'discount_codes_count', 'ends_at', 'features', 'item_entitlements', 'item_prerequisites', 'once_per_customer', 'prerequisite_quantity_range', 'prerequisite_shipping_price_range', 'prerequisite_subtotal_range', 'prerequisite_to_entitlement_quantity_ratio', 'shareable_urls', 'shipping_entitlements', 'starts_at', 'status', 'summary', 'target', 'title', 'total_sales', 'usage_count', 'usage_limit', 'validity_period', 'value_v2')
    allocation_limit = sgqlc.types.Field(Int, graphql_name='allocationLimit')
    allocation_method = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleAllocationMethod), graphql_name='allocationMethod')
    app = sgqlc.types.Field(App, graphql_name='app')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_selection = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleCustomerSelection), graphql_name='customerSelection')
    discount_codes = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleDiscountCodeConnection), graphql_name='discountCodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(DiscountCodeSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('saved_search_id', sgqlc.types.Arg(ID, graphql_name='savedSearchId', default=None)),
))
    )
    discount_codes_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='discountCodesCount')
    ends_at = sgqlc.types.Field(DateTime, graphql_name='endsAt')
    features = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PriceRuleFeature))), graphql_name='features')
    item_entitlements = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleItemEntitlements), graphql_name='itemEntitlements')
    item_prerequisites = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleLineItemPrerequisites), graphql_name='itemPrerequisites')
    once_per_customer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='oncePerCustomer')
    prerequisite_quantity_range = sgqlc.types.Field(PriceRuleQuantityRange, graphql_name='prerequisiteQuantityRange')
    prerequisite_shipping_price_range = sgqlc.types.Field(PriceRuleMoneyRange, graphql_name='prerequisiteShippingPriceRange')
    prerequisite_subtotal_range = sgqlc.types.Field(PriceRuleMoneyRange, graphql_name='prerequisiteSubtotalRange')
    prerequisite_to_entitlement_quantity_ratio = sgqlc.types.Field(PriceRulePrerequisiteToEntitlementQuantityRatio, graphql_name='prerequisiteToEntitlementQuantityRatio')
    shareable_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PriceRuleShareableUrl))), graphql_name='shareableUrls')
    shipping_entitlements = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleShippingLineEntitlements), graphql_name='shippingEntitlements')
    starts_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startsAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleStatus), graphql_name='status')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    target = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleTarget), graphql_name='target')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_sales = sgqlc.types.Field(MoneyV2, graphql_name='totalSales')
    usage_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usageCount')
    usage_limit = sgqlc.types.Field(Int, graphql_name='usageLimit')
    validity_period = sgqlc.types.Field(sgqlc.types.non_null(PriceRuleValidityPeriod), graphql_name='validityPeriod')
    value_v2 = sgqlc.types.Field(sgqlc.types.non_null('PricingValue'), graphql_name='valueV2')


class PriceRuleDiscountCode(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('app', 'code', 'usage_count')
    app = sgqlc.types.Field(App, graphql_name='app')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    usage_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='usageCount')


class PriceRuleUserError(sgqlc.types.Type, DisplayableError):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(PriceRuleErrorCode, graphql_name='code')


class PrivateMetafield(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'key', 'namespace', 'updated_at', 'value', 'value_type')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    namespace = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='namespace')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    value_type = sgqlc.types.Field(sgqlc.types.non_null(PrivateMetafieldValueType), graphql_name='valueType')


class Product(sgqlc.types.Type, Node, Navigable, HasMetafields, HasPublishedTranslations, Publishable, OnlineStorePreviewable, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('collections', 'created_at', 'description', 'description_html', 'featured_image', 'featured_media', 'feedback', 'gift_card_template_suffix', 'handle', 'has_only_default_variant', 'has_out_of_stock_variants', 'images', 'in_collection', 'is_gift_card', 'media', 'media_count', 'online_store_url', 'options', 'price_range_v2', 'product_type', 'published_at', 'seo', 'status', 'storefront_id', 'tags', 'template_suffix', 'title', 'total_inventory', 'total_variants', 'tracks_inventory', 'updated_at', 'variants', 'vendor')
    collections = sgqlc.types.Field(sgqlc.types.non_null(CollectionConnection), graphql_name='collections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(CollectionSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description', args=sgqlc.types.ArgDict((
        ('truncate_at', sgqlc.types.Arg(Int, graphql_name='truncateAt', default=None)),
))
    )
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHtml')
    featured_image = sgqlc.types.Field(Image, graphql_name='featuredImage')
    featured_media = sgqlc.types.Field(Media, graphql_name='featuredMedia')
    feedback = sgqlc.types.Field(ResourceFeedback, graphql_name='feedback')
    gift_card_template_suffix = sgqlc.types.Field(String, graphql_name='giftCardTemplateSuffix')
    handle = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='handle')
    has_only_default_variant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasOnlyDefaultVariant')
    has_out_of_stock_variants = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasOutOfStockVariants')
    images = sgqlc.types.Field(sgqlc.types.non_null(ImageConnection), graphql_name='images', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProductImageSortKeys, graphql_name='sortKey', default='POSITION')),
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    in_collection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='inCollection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    is_gift_card = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isGiftCard')
    media = sgqlc.types.Field(sgqlc.types.non_null(MediaConnection), graphql_name='media', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProductMediaSortKeys, graphql_name='sortKey', default='POSITION')),
))
    )
    media_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mediaCount')
    online_store_url = sgqlc.types.Field(URL, graphql_name='onlineStoreUrl')
    options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductOption'))), graphql_name='options', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
))
    )
    price_range_v2 = sgqlc.types.Field(sgqlc.types.non_null(ProductPriceRangeV2), graphql_name='priceRangeV2')
    product_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productType')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    seo = sgqlc.types.Field(sgqlc.types.non_null(SEO), graphql_name='seo')
    status = sgqlc.types.Field(sgqlc.types.non_null(ProductStatus), graphql_name='status')
    storefront_id = sgqlc.types.Field(sgqlc.types.non_null(StorefrontID), graphql_name='storefrontId')
    tags = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags')
    template_suffix = sgqlc.types.Field(String, graphql_name='templateSuffix')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    total_inventory = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalInventory')
    total_variants = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalVariants')
    tracks_inventory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tracksInventory')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    variants = sgqlc.types.Field(sgqlc.types.non_null(ProductVariantConnection), graphql_name='variants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProductVariantSortKeys, graphql_name='sortKey', default='POSITION')),
))
    )
    vendor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vendor')


class ProductChangeStatusUserError(sgqlc.types.Type, DisplayableError):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(ProductChangeStatusUserErrorCode, graphql_name='code')


class ProductOption(sgqlc.types.Type, Node, HasPublishedTranslations):
    __schema__ = shopify_schema
    __field_names__ = ('name', 'position', 'values')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    values = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='values')


class ProductVariant(sgqlc.types.Type, Node, HasMetafields, HasPublishedTranslations, Navigable, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('available_for_sale', 'barcode', 'compare_at_price', 'created_at', 'delivery_profile', 'display_name', 'fulfillment_service', 'fulfillment_service_editable', 'image', 'inventory_item', 'inventory_policy', 'inventory_quantity', 'media', 'position', 'presentment_prices', 'price', 'product', 'selected_options', 'sku', 'storefront_id', 'tax_code', 'taxable', 'title', 'updated_at', 'weight', 'weight_unit')
    available_for_sale = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='availableForSale')
    barcode = sgqlc.types.Field(String, graphql_name='barcode')
    compare_at_price = sgqlc.types.Field(Money, graphql_name='compareAtPrice')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    delivery_profile = sgqlc.types.Field(DeliveryProfile, graphql_name='deliveryProfile')
    display_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='displayName')
    fulfillment_service = sgqlc.types.Field(FulfillmentService, graphql_name='fulfillmentService')
    fulfillment_service_editable = sgqlc.types.Field(sgqlc.types.non_null(EditableProperty), graphql_name='fulfillmentServiceEditable')
    image = sgqlc.types.Field(Image, graphql_name='image', args=sgqlc.types.ArgDict((
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    inventory_item = sgqlc.types.Field(sgqlc.types.non_null(InventoryItem), graphql_name='inventoryItem')
    inventory_policy = sgqlc.types.Field(sgqlc.types.non_null(ProductVariantInventoryPolicy), graphql_name='inventoryPolicy')
    inventory_quantity = sgqlc.types.Field(Int, graphql_name='inventoryQuantity')
    media = sgqlc.types.Field(sgqlc.types.non_null(MediaConnection), graphql_name='media', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    presentment_prices = sgqlc.types.Field(sgqlc.types.non_null(ProductVariantPricePairConnection), graphql_name='presentmentPrices', args=sgqlc.types.ArgDict((
        ('presentment_currencies', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CurrencyCode)), graphql_name='presentmentCurrencies', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    price = sgqlc.types.Field(sgqlc.types.non_null(Money), graphql_name='price')
    product = sgqlc.types.Field(sgqlc.types.non_null(Product), graphql_name='product')
    selected_options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SelectedOption))), graphql_name='selectedOptions')
    sku = sgqlc.types.Field(String, graphql_name='sku')
    storefront_id = sgqlc.types.Field(sgqlc.types.non_null(StorefrontID), graphql_name='storefrontId')
    tax_code = sgqlc.types.Field(String, graphql_name='taxCode')
    taxable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxable')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    weight = sgqlc.types.Field(Float, graphql_name='weight')
    weight_unit = sgqlc.types.Field(sgqlc.types.non_null(WeightUnit), graphql_name='weightUnit')


class Publication(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('app', 'collection_publications_v3', 'collections', 'has_collection', 'name', 'product_publications_v3', 'products', 'supports_future_publishing')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    collection_publications_v3 = sgqlc.types.Field(sgqlc.types.non_null(ResourcePublicationConnection), graphql_name='collectionPublicationsV3', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    collections = sgqlc.types.Field(sgqlc.types.non_null(CollectionConnection), graphql_name='collections', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    has_collection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasCollection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    product_publications_v3 = sgqlc.types.Field(sgqlc.types.non_null(ResourcePublicationConnection), graphql_name='productPublicationsV3', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    products = sgqlc.types.Field(sgqlc.types.non_null(ProductConnection), graphql_name='products', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    supports_future_publishing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='supportsFuturePublishing')


class Refund(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'duties', 'note', 'order', 'refund_line_items', 'total_refunded_set', 'transactions', 'updated_at')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    duties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RefundDuty)), graphql_name='duties')
    note = sgqlc.types.Field(String, graphql_name='note')
    order = sgqlc.types.Field(sgqlc.types.non_null(Order), graphql_name='order')
    refund_line_items = sgqlc.types.Field(sgqlc.types.non_null(RefundLineItemConnection), graphql_name='refundLineItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    total_refunded_set = sgqlc.types.Field(sgqlc.types.non_null(MoneyBag), graphql_name='totalRefundedSet')
    transactions = sgqlc.types.Field(sgqlc.types.non_null(OrderTransactionConnection), graphql_name='transactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class SavedSearch(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('filters', 'name', 'query', 'resource_type', 'search_terms')
    filters = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SearchFilter))), graphql_name='filters')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    resource_type = sgqlc.types.Field(sgqlc.types.non_null(SearchResultType), graphql_name='resourceType')
    search_terms = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='searchTerms')


class ScriptDiscountApplication(sgqlc.types.Type, DiscountApplication):
    __schema__ = shopify_schema
    __field_names__ = ('title',)
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class ScriptTag(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'display_scope', 'src', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    display_scope = sgqlc.types.Field(sgqlc.types.non_null(ScriptTagDisplayScope), graphql_name='displayScope')
    src = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='src')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class Shop(sgqlc.types.Type, Node, HasPublishedTranslations, HasMetafields):
    __schema__ = shopify_schema
    __field_names__ = ('alerts', 'analytics_token', 'assigned_fulfillment_orders', 'available_channel_apps', 'billing_address', 'checkout_api_supported', 'contact_email', 'countries_in_shipping_zones', 'currency_code', 'currency_formats', 'currency_settings', 'customer_accounts', 'customer_tags', 'description', 'domains', 'draft_order_tags', 'email', 'enabled_presentment_currencies', 'features', 'fulfillment_orders', 'fulfillment_services', 'iana_timezone', 'limited_pending_order_count', 'myshopify_domain', 'name', 'navigation_settings', 'order_number_format_prefix', 'order_number_format_suffix', 'order_tags', 'payment_settings', 'plan', 'primary_domain', 'product_images', 'product_tags', 'product_types', 'product_vendors', 'publication_count', 'resource_limits', 'rich_text_editor_url', 'search', 'search_filters', 'setup_required', 'ships_to_countries', 'shop_policies', 'storefront_access_tokens', 'tax_shipping', 'taxes_included', 'timezone_abbreviation', 'timezone_offset', 'timezone_offset_minutes', 'unit_system', 'uploaded_images', 'uploaded_images_by_ids', 'url', 'weight_unit')
    alerts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ShopAlert))), graphql_name='alerts')
    analytics_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='analyticsToken')
    assigned_fulfillment_orders = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderConnection), graphql_name='assignedFulfillmentOrders', args=sgqlc.types.ArgDict((
        ('assignment_status', sgqlc.types.Arg(FulfillmentOrderAssignmentStatus, graphql_name='assignmentStatus', default=None)),
        ('location_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='locationIds', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(FulfillmentOrderSortKeys, graphql_name='sortKey', default='ID')),
))
    )
    available_channel_apps = sgqlc.types.Field(sgqlc.types.non_null(AppConnection), graphql_name='availableChannelApps', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    billing_address = sgqlc.types.Field(sgqlc.types.non_null(MailingAddress), graphql_name='billingAddress')
    checkout_api_supported = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkoutApiSupported')
    contact_email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contactEmail')
    countries_in_shipping_zones = sgqlc.types.Field(sgqlc.types.non_null(CountriesInShippingZones), graphql_name='countriesInShippingZones')
    currency_code = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='currencyCode')
    currency_formats = sgqlc.types.Field(sgqlc.types.non_null(CurrencyFormats), graphql_name='currencyFormats')
    currency_settings = sgqlc.types.Field(sgqlc.types.non_null(CurrencySettingConnection), graphql_name='currencySettings', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    customer_accounts = sgqlc.types.Field(sgqlc.types.non_null(ShopCustomerAccountsSetting), graphql_name='customerAccounts')
    customer_tags = sgqlc.types.Field(sgqlc.types.non_null(StringConnection), graphql_name='customerTags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    domains = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Domain))), graphql_name='domains')
    draft_order_tags = sgqlc.types.Field(sgqlc.types.non_null(StringConnection), graphql_name='draftOrderTags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    enabled_presentment_currencies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CurrencyCode))), graphql_name='enabledPresentmentCurrencies')
    features = sgqlc.types.Field(sgqlc.types.non_null(ShopFeatures), graphql_name='features')
    fulfillment_orders = sgqlc.types.Field(sgqlc.types.non_null(FulfillmentOrderConnection), graphql_name='fulfillmentOrders', args=sgqlc.types.ArgDict((
        ('include_closed', sgqlc.types.Arg(Boolean, graphql_name='includeClosed', default=False)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(FulfillmentOrderSortKeys, graphql_name='sortKey', default='ID')),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    fulfillment_services = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FulfillmentService))), graphql_name='fulfillmentServices')
    iana_timezone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ianaTimezone')
    limited_pending_order_count = sgqlc.types.Field(sgqlc.types.non_null(LimitedPendingOrderCount), graphql_name='limitedPendingOrderCount')
    myshopify_domain = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='myshopifyDomain')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    navigation_settings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NavigationItem))), graphql_name='navigationSettings')
    order_number_format_prefix = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='orderNumberFormatPrefix')
    order_number_format_suffix = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='orderNumberFormatSuffix')
    order_tags = sgqlc.types.Field(sgqlc.types.non_null(StringConnection), graphql_name='orderTags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('sort', sgqlc.types.Arg(ShopTagSort, graphql_name='sort', default='ALPHABETICAL')),
))
    )
    payment_settings = sgqlc.types.Field(sgqlc.types.non_null(PaymentSettings), graphql_name='paymentSettings')
    plan = sgqlc.types.Field(sgqlc.types.non_null(ShopPlan), graphql_name='plan')
    primary_domain = sgqlc.types.Field(sgqlc.types.non_null(Domain), graphql_name='primaryDomain')
    product_images = sgqlc.types.Field(sgqlc.types.non_null(ImageConnection), graphql_name='productImages', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ProductImageSortKeys, graphql_name='sortKey', default='CREATED_AT')),
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    product_tags = sgqlc.types.Field(sgqlc.types.non_null(StringConnection), graphql_name='productTags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    product_types = sgqlc.types.Field(sgqlc.types.non_null(StringConnection), graphql_name='productTypes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    product_vendors = sgqlc.types.Field(sgqlc.types.non_null(StringConnection), graphql_name='productVendors', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
))
    )
    publication_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='publicationCount')
    resource_limits = sgqlc.types.Field(sgqlc.types.non_null(ShopResourceLimits), graphql_name='resourceLimits')
    rich_text_editor_url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='richTextEditorUrl')
    search = sgqlc.types.Field(sgqlc.types.non_null(SearchResultConnection), graphql_name='search', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SearchResultType)), graphql_name='types', default=None)),
        ('first', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
))
    )
    search_filters = sgqlc.types.Field(sgqlc.types.non_null(SearchFilterOptions), graphql_name='searchFilters')
    setup_required = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setupRequired')
    ships_to_countries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CountryCode))), graphql_name='shipsToCountries')
    shop_policies = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShopPolicy'))), graphql_name='shopPolicies')
    storefront_access_tokens = sgqlc.types.Field(sgqlc.types.non_null(StorefrontAccessTokenConnection), graphql_name='storefrontAccessTokens', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    tax_shipping = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxShipping')
    taxes_included = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='taxesIncluded')
    timezone_abbreviation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezoneAbbreviation')
    timezone_offset = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timezoneOffset')
    timezone_offset_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timezoneOffsetMinutes')
    unit_system = sgqlc.types.Field(sgqlc.types.non_null(UnitSystem), graphql_name='unitSystem')
    uploaded_images = sgqlc.types.Field(sgqlc.types.non_null(ImageConnection), graphql_name='uploadedImages', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('sort_key', sgqlc.types.Arg(ShopImageSortKeys, graphql_name='sortKey', default='CREATED_AT')),
        ('max_width', sgqlc.types.Arg(Int, graphql_name='maxWidth', default=None)),
        ('max_height', sgqlc.types.Arg(Int, graphql_name='maxHeight', default=None)),
        ('crop', sgqlc.types.Arg(CropRegion, graphql_name='crop', default=None)),
        ('scale', sgqlc.types.Arg(Int, graphql_name='scale', default=1)),
))
    )
    uploaded_images_by_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Image))), graphql_name='uploadedImagesByIds', args=sgqlc.types.ArgDict((
        ('image_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='imageIds', default=None)),
))
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')
    weight_unit = sgqlc.types.Field(sgqlc.types.non_null(WeightUnit), graphql_name='weightUnit')


class ShopPolicy(sgqlc.types.Type, Node, HasPublishedTranslations):
    __schema__ = shopify_schema
    __field_names__ = ('body', 'type', 'url')
    body = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='body')
    type = sgqlc.types.Field(sgqlc.types.non_null(ShopPolicyType), graphql_name='type')
    url = sgqlc.types.Field(sgqlc.types.non_null(URL), graphql_name='url')


class ShopPolicyUserError(sgqlc.types.Type, DisplayableError):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(ShopPolicyErrorCode, graphql_name='code')


class ShopifyPaymentsAccount(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('activated', 'balance', 'bank_accounts', 'charge_statement_descriptors', 'country', 'default_currency', 'disputes', 'fraud_settings', 'notification_settings', 'onboardable', 'payout_schedule', 'payout_statement_descriptor', 'payouts', 'permitted_verification_documents', 'verifications')
    activated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activated')
    balance = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MoneyV2))), graphql_name='balance')
    bank_accounts = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsBankAccountConnection), graphql_name='bankAccounts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    charge_statement_descriptors = sgqlc.types.Field(ShopifyPaymentsChargeStatementDescriptor, graphql_name='chargeStatementDescriptors')
    country = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='country')
    default_currency = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='defaultCurrency')
    disputes = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsDisputeConnection), graphql_name='disputes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    fraud_settings = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsFraudSettings), graphql_name='fraudSettings')
    notification_settings = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsNotificationSettings), graphql_name='notificationSettings')
    onboardable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='onboardable')
    payout_schedule = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsPayoutSchedule), graphql_name='payoutSchedule')
    payout_statement_descriptor = sgqlc.types.Field(String, graphql_name='payoutStatementDescriptor')
    payouts = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsPayoutConnection), graphql_name='payouts', args=sgqlc.types.ArgDict((
        ('transaction_type', sgqlc.types.Arg(ShopifyPaymentsPayoutTransactionType, graphql_name='transactionType', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    permitted_verification_documents = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ShopifyPaymentsVerificationDocument))), graphql_name='permittedVerificationDocuments')
    verifications = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ShopifyPaymentsVerification'))), graphql_name='verifications')


class ShopifyPaymentsBankAccount(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('account_number', 'account_number_last_digits', 'bank_name', 'country', 'created_at', 'currency', 'payouts', 'routing_number', 'status')
    account_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountNumber')
    account_number_last_digits = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accountNumberLastDigits')
    bank_name = sgqlc.types.Field(String, graphql_name='bankName')
    country = sgqlc.types.Field(sgqlc.types.non_null(CountryCode), graphql_name='country')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    currency = sgqlc.types.Field(sgqlc.types.non_null(CurrencyCode), graphql_name='currency')
    payouts = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsPayoutConnection), graphql_name='payouts', args=sgqlc.types.ArgDict((
        ('transaction_type', sgqlc.types.Arg(ShopifyPaymentsPayoutTransactionType, graphql_name='transactionType', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('reverse', sgqlc.types.Arg(Boolean, graphql_name='reverse', default=False)),
))
    )
    routing_number = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='routingNumber')
    status = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsBankAccountStatus), graphql_name='status')


class ShopifyPaymentsDefaultChargeStatementDescriptor(sgqlc.types.Type, ShopifyPaymentsChargeStatementDescriptor):
    __schema__ = shopify_schema
    __field_names__ = ()


class ShopifyPaymentsDispute(sgqlc.types.Type, LegacyInteroperability, Node):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'evidence_due_by', 'evidence_sent_on', 'finalized_on', 'initiated_at', 'order', 'reason_details', 'status', 'type')
    amount = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='amount')
    evidence_due_by = sgqlc.types.Field(Date, graphql_name='evidenceDueBy')
    evidence_sent_on = sgqlc.types.Field(Date, graphql_name='evidenceSentOn')
    finalized_on = sgqlc.types.Field(Date, graphql_name='finalizedOn')
    initiated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='initiatedAt')
    order = sgqlc.types.Field(Order, graphql_name='order')
    reason_details = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsDisputeReasonDetails), graphql_name='reasonDetails')
    status = sgqlc.types.Field(sgqlc.types.non_null(DisputeStatus), graphql_name='status')
    type = sgqlc.types.Field(sgqlc.types.non_null(DisputeType), graphql_name='type')


class ShopifyPaymentsJpChargeStatementDescriptor(sgqlc.types.Type, ShopifyPaymentsChargeStatementDescriptor):
    __schema__ = shopify_schema
    __field_names__ = ('kana', 'kanji')
    kana = sgqlc.types.Field(String, graphql_name='kana')
    kanji = sgqlc.types.Field(String, graphql_name='kanji')


class ShopifyPaymentsPayout(sgqlc.types.Type, LegacyInteroperability, Node):
    __schema__ = shopify_schema
    __field_names__ = ('bank_account', 'issued_at', 'net', 'status', 'summary', 'transaction_type')
    bank_account = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsBankAccount), graphql_name='bankAccount')
    issued_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='issuedAt')
    net = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='net')
    status = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsPayoutStatus), graphql_name='status')
    summary = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsPayoutSummary), graphql_name='summary')
    transaction_type = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsPayoutTransactionType), graphql_name='transactionType')


class ShopifyPaymentsVerification(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('status', 'subject')
    status = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsVerificationStatus), graphql_name='status')
    subject = sgqlc.types.Field(sgqlc.types.non_null(ShopifyPaymentsVerificationSubject), graphql_name='subject')


class StorefrontAccessToken(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('access_scopes', 'access_token', 'created_at', 'title', 'updated_at')
    access_scopes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AccessScope))), graphql_name='accessScopes')
    access_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accessToken')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class TenderTransaction(sgqlc.types.Type, Node):
    __schema__ = shopify_schema
    __field_names__ = ('amount', 'payment_method', 'processed_at', 'remote_reference', 'test', 'transaction_details')
    amount = sgqlc.types.Field(sgqlc.types.non_null(MoneyV2), graphql_name='amount')
    payment_method = sgqlc.types.Field(String, graphql_name='paymentMethod')
    processed_at = sgqlc.types.Field(DateTime, graphql_name='processedAt')
    remote_reference = sgqlc.types.Field(String, graphql_name='remoteReference')
    test = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='test')
    transaction_details = sgqlc.types.Field('TenderTransactionDetails', graphql_name='transactionDetails')


class TranslationUserError(sgqlc.types.Type, DisplayableError):
    __schema__ = shopify_schema
    __field_names__ = ('code',)
    code = sgqlc.types.Field(TranslationErrorCode, graphql_name='code')


class UserError(sgqlc.types.Type, DisplayableError):
    __schema__ = shopify_schema
    __field_names__ = ()


class Video(sgqlc.types.Type, Node, Media):
    __schema__ = shopify_schema
    __field_names__ = ('filename', 'original_source', 'sources')
    filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='filename')
    original_source = sgqlc.types.Field(VideoSource, graphql_name='originalSource')
    sources = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(VideoSource))), graphql_name='sources')


class WebhookSubscription(sgqlc.types.Type, Node, LegacyInteroperability):
    __schema__ = shopify_schema
    __field_names__ = ('created_at', 'endpoint', 'format', 'include_fields', 'metafield_namespaces', 'topic', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    endpoint = sgqlc.types.Field(sgqlc.types.non_null('WebhookSubscriptionEndpoint'), graphql_name='endpoint')
    format = sgqlc.types.Field(sgqlc.types.non_null(WebhookSubscriptionFormat), graphql_name='format')
    include_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='includeFields')
    metafield_namespaces = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='metafieldNamespaces')
    topic = sgqlc.types.Field(sgqlc.types.non_null(WebhookSubscriptionTopic), graphql_name='topic')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')



########################################################################
# Unions
########################################################################
class AppPricingDetails(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (AppRecurringPricing, AppUsagePricing)


class CommentEventEmbed(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (Customer, DraftOrder, Order, Product, ProductVariant)


class DeliveryConditionCriteria(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (MoneyV2, Weight)


class DeliveryRateProvider(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DeliveryParticipant, DeliveryRateDefinition)


class DiscountAutomatic(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DiscountAutomaticBasic, DiscountAutomaticBxgy)


class DiscountCode(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DiscountCodeBasic, DiscountCodeBxgy, DiscountCodeFreeShipping)


class DiscountCustomerBuysValue(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DiscountPurchaseAmount, DiscountQuantity)


class DiscountCustomerGetsValue(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DiscountAmount, DiscountOnQuantity, DiscountPercentage)


class DiscountCustomerSelection(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DiscountCustomerAll, DiscountCustomerSavedSearches, DiscountCustomers)


class DiscountEffect(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DiscountPercentage,)


class DiscountItems(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (AllDiscountItems, DiscountCollections, DiscountProducts)


class DiscountMinimumRequirement(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DiscountMinimumQuantity, DiscountMinimumSubtotal)


class DiscountShippingDestinationSelection(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (DiscountCountries, DiscountCountryAll)


class OrderStagedChange(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (OrderStagedChangeAddCustomItem, OrderStagedChangeAddLineItemDiscount, OrderStagedChangeAddShippingLine, OrderStagedChangeAddVariant, OrderStagedChangeDecrementItem, OrderStagedChangeIncrementItem)


class PriceRuleValue(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (PriceRuleFixedAmountValue, PriceRulePercentValue)


class PricingValue(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (MoneyV2, PricingPercentageValue)


class TenderTransactionDetails(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (TenderTransactionCreditCardDetails,)


class WebhookSubscriptionEndpoint(sgqlc.types.Union):
    __schema__ = shopify_schema
    __types__ = (WebhookEventBridgeEndpoint, WebhookHttpEndpoint)



########################################################################
# Schema Entry Points
########################################################################
shopify_schema.query_type = QueryRoot
shopify_schema.mutation_type = Mutation
shopify_schema.subscription_type = None

