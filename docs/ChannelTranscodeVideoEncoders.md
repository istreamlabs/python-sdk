# ChannelTranscodeVideoEncoders


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bit_rate** | **int** | Bit rate specifies the number in bits used per second. Higher values result in better video quality but bigger file sizes. For H.264 this value is the target of the constrained variable bit rate. | [optional] 
**frame_rate** | **str** | Frame rate specifies the number of images that are shown per second when playing back the video. For the best quality playback, this should match or be a multiple of the input source video stream. | [optional] 
**h264** | [**ChannelTranscodeH264**](ChannelTranscodeH264.md) |  | [optional] 
**h265** | [**ChannelTranscodeH265**](ChannelTranscodeH265.md) |  | [optional] 
**height** | **int** | Height specifies the video height in pixels. Must be a multiple of two. | [optional] 
**id** | **str** | Encoder ID. IDs must be unique for all video and thumbnail encoders. This ID is referenced when setting up playlist publishing. | [optional] 
**width** | **int** | Width specifies the video width in pixels. Must be a multiple of two. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


