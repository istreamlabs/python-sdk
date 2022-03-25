# ChannelPackagingMp2t

Uses MP2T format for each segments. Only one of ['mp2t', 'mp4'] may be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_unmuxed_audio** | **bool** | Forces the Video and Audio Encodings to be unmuxed when there is one audio encodings. This setting will have to be uniformed across MP2T packagers within a config. When there are two or more audio encodings, unmuxed will be used automatically. | [optional] 
**insert_id3_utc_time** | **bool** | If true, insert ID3 tags that include a UTC timestamp. This is a Turner/WM-specific extension. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


