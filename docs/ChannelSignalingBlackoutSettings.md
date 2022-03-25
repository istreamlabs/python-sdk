# ChannelSignalingBlackoutSettings

Configure blackout: replacing content with custom slates based on program signaling.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_blackout_slate_url** | **str** | Default slate URL to use for blackouts. Can be overridden by the &#39;slates&#39; field. | [optional] 
**force_blackout_segments** | **[str]** | List of signaling segment types to force blackout, e.g. add &#39;SPLICE_INSERT&#39; to blackout all ads signaled via SCTE-35 splice_insert. | [optional] 
**honor_web_delivery_restriction** | **bool** | Determines whether to honor the web_delivery_allowed attribute in SCTE-35 segmentation descriptors. When this is enabled, a segmentation descriptor with web_delivery_allowed&#x3D;false will trigger a blackout. | [optional] 
**slates** | [**[ChannelSignalingBlackoutSettingsSlates]**](ChannelSignalingBlackoutSettingsSlates.md) | Per-segment type slate overrides. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


