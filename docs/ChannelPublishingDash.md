# ChannelPublishingDash

DASH configures publication settings. Only one of HLS or DASH can be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_update_period_secs** | **int** | Sets the minimumUpdatePeriod field in MPD to be this value. If set to 0 (default), segment duration is used. The value shall not exceed the &#39;suggested_presentation_delay_secs&#39;. | [optional] 
**signaling_formats** | **[str]** | Signaling formats specifies which SCTE-35 timeline marker formatting to use when rendering playlists. | [optional] 
**suggested_presentation_delay_secs** | **int** | The suggested amount of time (in seconds) the player should be behind the live stream. This value must be greater or equal to &#39;minimum_update_period_secs&#39;. | [optional] 
**url_type** | **str** | If set to &#39;URL_TYPE_UNDEFINED&#39; playlist generation will use &#39;RELATIVE&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


