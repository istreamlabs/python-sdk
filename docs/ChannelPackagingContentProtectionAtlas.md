# ChannelPackagingContentProtectionAtlas

Only one of ['simple', 'atlas', 'cpix'] may be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The Asset Identifier which was taken from the token entitlement service request. | [optional] 
**company_id** | **str** | The Identifier of the Company that this token belongs. | [optional] 
**drms** | **[str]** | DRM system keys to request | [optional] 
**widevine_v0_pssh_box** | **bool** | When TRUE the KeyID is not embedded in the pssh box which sets the version to 0. Defaults to generating v1 pssh_boxes that includes the key_id | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


