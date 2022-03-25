# ChannelSignalingSegmentSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_duration_secs** | **int** | Specifies the duration of a segment when the in-band SCTE-35 that initiates it (e.g. Distributor Placement Opportunity Start) is missing an explicit duration. N.B. for program and ad types, this also affects &#39;Simple Program&#39; and &#39;Simple Ad&#39; markers, respectively. | [optional] 
**emit_default_duration** | **bool** | Determines whether to include the default duration in the output SCTE-35 messages when the input SCTE-35 message did not specify a duration. | [optional] 
**offset_millis** | **int** | Specifies a &#39;correction&#39; to the splice_time of in-band SCTE-35 in milliseconds. | [optional] 
**segment_end_mode** | **str** | Determines which Segment End signaling mode to use for the provided segments. If unspecified, defaults to MATCH_END_EVENT_ID. | [optional] 
**segments** | **[str]** | Specifies the list of which segment types this setting applies to. Any segment type defined here _must_ also be present in the parent signaling configuration. | [optional] 
**tier_filter** | [**ChannelSignalingTierFilter**](ChannelSignalingTierFilter.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


