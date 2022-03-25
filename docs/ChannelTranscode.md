# ChannelTranscode

Transcode configures audio/video conversion settings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio_encoders** | [**[ChannelTranscodeAudioEncoders]**](ChannelTranscodeAudioEncoders.md) | Audio encoders specify audio conversion settings, e.g. channels, samples, codec, bitrate, etc. | [optional] 
**feature_flags** | **[str]** | Feature flag strings enable experimental transcode features or functionality that are not yet or never will be promoted to the channeldoc model proper. | [optional] 
**id3_mode** | **str** | Specify how to process ID3 tags from the input source. If not specified, ID3 tags in the source will be ignored. | [optional]  if omitted the server will use the default value of "PASSTHROUGH"
**resize_mode** | **str** | Resize mode specifies how to scale a video up or down to match the output dimensions. | [optional] 
**segmenter** | [**ChannelTranscodeSegmenter**](ChannelTranscodeSegmenter.md) |  | [optional] 
**thumbnail_encoders** | [**[ChannelTranscodeThumbnailEncoders]**](ChannelTranscodeThumbnailEncoders.md) | Thumbnail encoders specify how to create image snapshots of the video stream. | [optional] 
**video_encoders** | [**[ChannelTranscodeVideoEncoders]**](ChannelTranscodeVideoEncoders.md) | Video encoders specify video conversion settings, e.g. dimensions, codec, bitrate, etc. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


