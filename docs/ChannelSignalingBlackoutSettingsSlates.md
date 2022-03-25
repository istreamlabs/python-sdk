# ChannelSignalingBlackoutSettingsSlates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blackout_slate_url** | **str** | Blackout slate URL to use for the specified segments. It must have one audio and one video stream. Either MPEG2 or H.264 can be used. | [optional] 
**segments** | **[str]** | Segment types that shall utilize the blackout slate URL. Any segment type defined here _must_ also be present in the parent signaling configuration. | [optional] 
**upids** | **[str]** | Exclusive list of hex string encoded colon separated UPID Type:ID pairs (e.g. &#39;0A:1A2B3C4D&#39;) to enable this blackout slate on. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


