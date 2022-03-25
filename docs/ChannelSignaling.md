# ChannelSignaling

Signaling configures in-band signaling (i.e. SCTE-35).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blackout_settings** | [**ChannelSignalingBlackoutSettings**](ChannelSignalingBlackoutSettings.md) |  | [optional] 
**disable_inband_parsing** | **bool** | Disable parsing SCTE-35 in-band signaling. Out-of-band signaling is still allowed. | [optional] 
**segment_settings** | [**[ChannelSignalingSegmentSettings]**](ChannelSignalingSegmentSettings.md) | Settings that apply to specific segments. | [optional] 
**segments** | **[str]** | Segment types to process for in-band signaling. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


