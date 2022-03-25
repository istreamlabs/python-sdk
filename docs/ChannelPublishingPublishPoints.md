# ChannelPublishingPublishPoints


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http** | [**ChannelPublishingHttp**](ChannelPublishingHttp.md) |  | [optional] 
**id** | **str** | uniquely identifies this publish_point within a channel configuration. Can be referenced by other publish_points in the &#39;playlist_only_for&#39; field. | [optional] 
**playlist_only_for** | **str** | playlist_only_for identifies the id of the publish_point that has the segments for this publish_point, which is only publishing a playlist for those segments. All publish_points within a publication must either have &#39;playlist_only_for&#39; all set or all not set. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


