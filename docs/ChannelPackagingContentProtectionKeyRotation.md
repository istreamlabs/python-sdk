# ChannelPackagingContentProtectionKeyRotation

Configures how keys should be rotated

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval_secs** | **float** | Rotate keys based on the specified time interval. If Program is also provided then this time interval will only apply to media segments that are outside of program boundaries. If Program is NOT provided then only this time interval will be used to decided when to rotate keys. | [optional] 
**program** | **bool** | Rotate keys on (SCTE35) program boundaries such that no two programs will be protected with the same key. | [optional] 
**program_overlap_skip_encrypt** | **bool** | Do not encrypt segments that are part of more than one SCTE-35 program. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


