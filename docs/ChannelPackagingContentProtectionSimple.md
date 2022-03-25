# ChannelPackagingContentProtectionSimple

Only one of ['simple', 'atlas', 'cpix'] may be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_points** | [**[ChannelPackagingContentProtectionSimplePublishPoints]**](ChannelPackagingContentProtectionSimplePublishPoints.md) | Pub points where keys should be published. If multiple are specified, only one needs to succeed to consider the key successfully published. | [optional] 
**require_publish** | **str** | Indicates which publish points must succeed for segment publishing to use the keys. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


