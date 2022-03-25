# ChannelPackagingContentProtectionCpix

Only one of ['simple', 'atlas', 'cpix'] may be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates_id** | **str** | Unique ID used for certificate settings, unique per distributor. | [optional] 
**content_id** | **str** | (Optional) Content ID that identifies this channel in the CPIX service. Value is defined by the DRM system owner, and if defined will be included as part of a POST request. | [optional] 
**credentials_id** | **str** | Unique ID used for credentials settings, unique per distributor. | [optional] 
**decryption_key_id** | **str** | Unique ID of the decryption key to use in case the server response contains content keys encrypted. The key is unique per distirutor, and configured ahead of time by the publishing team and the CPIX service owner. | [optional] 
**drms** | **[str]** | (Optional) DRM system keys to request. If not defined a GET request will be done, and any key returned will be handled. If defined, random kid(s) (key ids) will be generated on rotation for each DRM system, and a POST request will be done to create them. | [optional] 
**headers_id** | **str** | (Optional) An identifier to a list of HTTP headers to be added to the request sent to the CPIX service. | [optional] 
**uri** | **str** | CPIX service URI | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


