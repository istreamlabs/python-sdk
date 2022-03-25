# ChannelTranscodeSegmenter

Segmenter configures how video GOPs and segments get generated.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gop_duration_secs** | **float** | GOP (group of pictures) duration specifies the amount of time between I-frames. Shorter durations can lower quality slightly as each I-frame uses more bits than P- &amp; B-frames but can provide a better seeking experience when enabling thumbnail encoders and/or I-Frame Only playlists. | [optional] 
**partials_mode** | **str** | Not public because we haven&#39;t shipped low latency HLS yet and we probably need to update the naming. | [optional]  if omitted the server will use the default value of "GOP"
**segment_duration_secs** | **float** | Segment duration specifies the target duration of a single segment. Segments shorter than this duration can occur at signaling boundaries. This value _must_ be a multiple of the GOP duration value. | [optional] 
**temi** | **bool** | Include TEMI (Timeline and External Media Information ISO/IEC 13818-1:2019 Annex U) to mpeg-ts segments. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


