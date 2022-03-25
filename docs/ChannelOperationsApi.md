# openapi_client.ChannelOperationsApi

All URIs are relative to *https://api.istreamplanet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_dvr_window**](ChannelOperationsApi.md#clear_dvr_window) | **DELETE** /v2/channels/{channel-id}/dvr-window | Clear DVR Window
[**get_signals**](ChannelOperationsApi.md#get_signals) | **GET** /v2/channels/{channel-id}/signal | Get Signals
[**insert_id3**](ChannelOperationsApi.md#insert_id3) | **POST** /v2/channels/{channel-id}/id3 | Insert ID3
[**insert_scte35**](ChannelOperationsApi.md#insert_scte35) | **POST** /v2/channels/{channel-id}/scte35 | Insert SCTE-35
[**preview_image**](ChannelOperationsApi.md#preview_image) | **GET** /v2/channels/{channel-id}/preview-image | Get Preview Image
[**program_end**](ChannelOperationsApi.md#program_end) | **POST** /v2/channels/{channel-id}/program-end | Program End
[**program_start**](ChannelOperationsApi.md#program_start) | **POST** /v2/channels/{channel-id}/program-start | Program Start
[**signal**](ChannelOperationsApi.md#signal) | **POST** /v2/channels/{channel-id}/signal | Generic Signal
[**slate_in**](ChannelOperationsApi.md#slate_in) | **POST** /v2/channels/{channel-id}/slate | Slate in
[**slate_out**](ChannelOperationsApi.md#slate_out) | **DELETE** /v2/channels/{channel-id}/slate | Slate out
[**splice_end**](ChannelOperationsApi.md#splice_end) | **POST** /v2/channels/{channel-id}/splice-end | Splice Insert End
[**splice_start**](ChannelOperationsApi.md#splice_start) | **POST** /v2/channels/{channel-id}/splice-start | Splice Insert Start


# **clear_dvr_window**
> clear_dvr_window(channel_id)

Clear DVR Window

Clears the DVR window for the channel by removing all video segments in the manifest from before the request.  This sets the earliest time a player can rewind to this point.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier

    # example passing only required values which don't have defaults set
    try:
        # Clear DVR Window
        api_instance.clear_dvr_window(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->clear_dvr_window: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signals**
> SegmentList get_signals(channel_id)

Get Signals

Returns the active signals for a channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.segment_list import SegmentList
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier

    # example passing only required values which don't have defaults set
    try:
        # Get Signals
        api_response = api_instance.get_signals(channel_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->get_signals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |

### Return type

[**SegmentList**](SegmentList.md)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type - Content-Type <br>  * ETag - ETag <br>  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**406** | Not Acceptable |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_id3**
> InsertMetadataResult insert_id3(channel_id)

Insert ID3

Inserts the provided UTF-8 text metadata in the output stream embedded in a TXXX frame of a ID3 tag.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.insert_metadata_request import InsertMetadataRequest
from openapi_client.model.insert_metadata_result import InsertMetadataResult
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    accept = "Accept_example" # str | List of accepted Content-Type headers (optional)
    insert_metadata_request = InsertMetadataRequest(
        payload="payload_example",
    ) # InsertMetadataRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert ID3
        api_response = api_instance.insert_id3(channel_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->insert_id3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert ID3
        api_response = api_instance.insert_id3(channel_id, accept=accept, insert_metadata_request=insert_metadata_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->insert_id3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **accept** | **str**| List of accepted Content-Type headers | [optional]
 **insert_metadata_request** | [**InsertMetadataRequest**](InsertMetadataRequest.md)|  | [optional]

### Return type

[**InsertMetadataResult**](InsertMetadataResult.md)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type - Content-Type <br>  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_scte35**
> insert_scte35(channel_id)

Insert SCTE-35

Inserts a SCTE-35 formatted binary payload into the channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.scte35 import Scte35
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    scte35 = Scte35(
        payload="/DAvAAAAAAAAAP/wBQb/d2+7OgAZAhdDVUVJAAAD6ACACAic1fd1d2+7OjABAeo2v/g=",
    ) # Scte35 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert SCTE-35
        api_instance.insert_scte35(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->insert_scte35: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert SCTE-35
        api_instance.insert_scte35(channel_id, scte35=scte35)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->insert_scte35: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **scte35** | [**Scte35**](Scte35.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_image**
> preview_image(channel_id)

Get Preview Image

Get a static image of what your channel is outputting.  Valid Accept headers are: image/jpeg

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    accept = "Accept_example" # str | List of accepted Content-Type headers (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Preview Image
        api_instance.preview_image(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->preview_image: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Preview Image
        api_instance.preview_image(channel_id, accept=accept)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->preview_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **accept** | **str**| List of accepted Content-Type headers | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**406** | Not Acceptable |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**501** | Not Implemented |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **program_end**
> program_end(channel_id)

Program End

Inserts a 'program end' SCTE-35 message into the channel.  This route should only be used for non-overlapping program markers.  If you want overlapping program makers please use Generic Signal instead.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.program_signal import ProgramSignal
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    program_signal = ProgramSignal(
        event_id=1234,
    ) # ProgramSignal |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Program End
        api_instance.program_end(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->program_end: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Program End
        api_instance.program_end(channel_id, program_signal=program_signal)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->program_end: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **program_signal** | [**ProgramSignal**](ProgramSignal.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **program_start**
> program_start(channel_id)

Program Start

Inserts a 'program start' SCTE-35 message into the channel.  This route should only be used for non-overlapping program markers.  If you want overlapping program makers please use Generic Signal instead.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.program_signal import ProgramSignal
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    program_signal = ProgramSignal(
        event_id=1234,
    ) # ProgramSignal |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Program Start
        api_instance.program_start(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->program_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Program Start
        api_instance.program_start(channel_id, program_signal=program_signal)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->program_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **program_signal** | [**ProgramSignal**](ProgramSignal.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal**
> signal(channel_id)

Generic Signal

Inserts a SCTE-35 message into the channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.generic_signal_list import GenericSignalList
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    generic_signal_list = GenericSignalList([
        GenericSignal(
            duration=30000,
            event_id=1234,
            segment_type="program",
            signal_type="start",
            slate_uri="https://www.example.com/logo.ts",
            type="none",
            upids=["03:ABCD0001000H","08:0A42235B81BC70FC","06:0000-0001-2C52-0000-P-0000-0000-0"],
        ),
    ]) # GenericSignalList |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Generic Signal
        api_instance.signal(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->signal: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Generic Signal
        api_instance.signal(channel_id, generic_signal_list=generic_signal_list)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->signal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **generic_signal_list** | [**GenericSignalList**](GenericSignalList.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status response; see body for details |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slate_in**
> slate_in(channel_id)

Slate in

Replaces the current video source with a slate image or video.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.error_model import ErrorModel
from openapi_client.model.slate import Slate
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    slate = Slate(
        duration=30000,
        uri="https://www.example.com/logo.ts",
    ) # Slate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Slate in
        api_instance.slate_in(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->slate_in: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Slate in
        api_instance.slate_in(channel_id, slate=slate)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->slate_in: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **slate** | [**Slate**](Slate.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slate_out**
> slate_out(channel_id)

Slate out

Removes any active slate and show the source video content.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier

    # example passing only required values which don't have defaults set
    try:
        # Slate out
        api_instance.slate_out(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->slate_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **splice_end**
> splice_end(channel_id)

Splice Insert End

Inserts a 'splice insert end' SCTE-35 message into the channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.splice_insert_end_signal import SpliceInsertEndSignal
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    splice_insert_end_signal = SpliceInsertEndSignal(
        event_id=1234,
    ) # SpliceInsertEndSignal |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Splice Insert End
        api_instance.splice_end(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->splice_end: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Splice Insert End
        api_instance.splice_end(channel_id, splice_insert_end_signal=splice_insert_end_signal)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->splice_end: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **splice_insert_end_signal** | [**SpliceInsertEndSignal**](SpliceInsertEndSignal.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **splice_start**
> splice_start(channel_id)

Splice Insert Start

Inserts a 'splice insert start' SCTE-35 message into the channel.

### Example

* OAuth Authentication (authcode):
* OAuth Authentication (m2m):

```python
import time
import openapi_client
from openapi_client.api import channel_operations_api
from openapi_client.model.splice_insert_start_signal import SpliceInsertStartSignal
from openapi_client.model.error_model import ErrorModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.istreamplanet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: authcode
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Configure OAuth2 access token for authorization: m2m
configuration = openapi_client.Configuration(
    host = "https://api.istreamplanet.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = channel_operations_api.ChannelOperationsApi(api_client)
    channel_id = "8--------------------------------gckec0l3o4gi7xhk0jcy075ua034---------------------------------------------------------------------------------mug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6jaj4swhsa064e9ybn0---------------------------------------------------------------------------------n7dc0zj1z3o53ghg9i6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki---------------------------------------d4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6ae--------------------------------------------------------------------------------------d7zuvbrt5wycaueooksju6otpo------------------------------------------------------------------------------------ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8swoqa9woex6dzpdztprol4oxf1vlovr8----------------------------------------wu4jqkr6ra0y0uv60djw970jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l6igyo1l0q6ct9---------------------------------------------------------------------------------------------9yu4ivrxn214gibpahdtf93e57lhwd58------------------------------------------------------------------qiyhhil1f8etzy51e5k658pq6zsvrzx3d2hzptzd1mew2jaa-----------------------------------------------------------1ws6zuqa17fq0e006zbnf7ky56ke835tqzvhwsl6cx5bfv7f1y---------------idgmcllqh9bh04mnc8360eg2lqm8q8zljvpc--------ecm7gtpx6uypgs0csxv80zla1ucgb-----------------------------ire6yq8vfz9vn4em09ihhroayld----------------------------------------------uxbhqr3p2g1b3h3njw9yk4i4arqdwes12gq8i3yd83rb14------------00ift0zpojjsph0tqxs7w3atw99duoi0tknlj4-----------------------2t3xobvho6qy2iwy640v0hugc5yp6mxohh16xrscqda8kgk4uqu6a1kjv7e4qy5tfrididp6xyq3g5te74---------------------------------------------------------------------------------------------ly5akq2ccqc99nscwdfc9nlut64g3e4587h4gt1bgo83bcouxg5yf679om5f84bz4lnqnmsb1f7cpjb64xcrx4xg3xf38t2b0agz--------------------------------------------------------------------------------smbkt3rkgmypobk59nqk7zxnm8d0ncqlqevpg10uf1i2gvjh9e8ptfwch1dzh8mjcl4se6i7guhqpjck-------------------------------------------------------------hbcol81gj121x3spm5zc45n36k3eqdd9yjdqs1pkccezqbhcu2de1dtj5h9xwpewy7k8lhpp63kbb0----------------------------------------------------------------------------b16ayv4ij0w38grblikzgx1u1b5luh3bqti0samr35g90paagweihhdx02gck0z8ym--------------------------------------------------98eol00uxqtpqpaavx61j6y4u7xzv17lybocei9jwtad46vu4h6ubj3ayfw4qh2zfo--------------------------------------------------------------------------------------66njbzrs9minis3wvbjm1ssur2h4om2x8g5rb7f7mqz5nb8zfohjjqtj0d03-----------------------------------------------------------------------------j6sg--------------------------------------------------------------------0ruzas1z5ipr0l2aconeksz4dda22vc59h1m5y5dhwq4tali336n0mh5mtutv4k80y6mcjm87vcyjkvoqnja2o3---------------------------------------------------------------------------nlrzv5u------------------------------------------------------j5u4yrblhplugjo0tvpcsh3664thurk971nkuv9zv1scf44hwmeoeo34mhh---------------kmiqwgr5gl5d7zn9an403c7b3rzrcvrgpkug0lp59q---------------------------------------------------t2laeybl28q74so3egjbpnxt3s3v3yrt06k5nfrrjdnzz4itf023dj393zvm----------------------------------------------------------h08uwvy37vz7lntsnhji7g8g4pbmor0vdqmangvepzg3oqlz---------------------------------------------------------------------------f6minqnk2ormbwuh43nbp47tf856g3lnld84xthea5ir3rewrx3p4xy0ovfwe33x76z3r16nmuohngzec2se9s6k-----------------------------------------------------------------------------6b2que3piesq27mi5hg7nq1h1lcbi1lkydpmkkerem5j9q2it8et7r6vc148g3c7ix3x53d-----epd5dytvvy0nafom9uc9nb8tl4weepoth5f1jx6xo94nqdzxoh09lnt8kj---------------------------------------------------7didhcjhd3g4bcw1tal57kiyo9mcvrl6zyhwbyr5mpkob74ky1moopte------------------------------------------------------------------------------602ty1lq9mx6vlj6u82i8r6f1j0m2z6wq9tiqr9g1godh97m98iswwfi7tn0z311qyk7w3g8lys76lnam9czkttxv---------------------------j9w20xsabkvlrbnxw3ddgd3051sykqga71wscg658q6ok5revf94f9ljzlk90se93a1vhr20g67uzogxuu11oz--------------------------------------------c6lnj99wok1kkho2td4jdvf8r8l6d7zctbuykoi9q7be3z5czxkhobupf92jxc703gp2kqp2h37mx51zwk7u------------------------hqxl6vozz64e9ylqtlctszb27du5xaj94drh22a80u0za2eeqrwg4i7vn7m0mwpzhsn0mh4mp------------------------------------------------------------------------------------------d8r7jdgqzqqfk61c5m029vs21vjxujbhfroowyg7kermssr8wlz1p41z27wqc10hlz-----------------------------------------------------------------rcniq0ahgot5yfojxs7szzdlb0zprk3----------------------------------------------------------------0l96fe---------------------------------------------------------------------------------------------z2wmcwvloejyoq8gocptat3lpq2mdr4mogxzcatr3t5wg1mycnozhgto42b8pyvl4xojzaps2amu18wyw8zm5v0608wqjngg---------------------------------------d1phbf5n2nlntkdn6dizveuevujwayzorui28mvewnq5xsn8xb07ftdm6np3--------------------------y1n0qurq5phmem49tj3qkz7jqpa9182x8eplhwh7qxtgzfbsgfeaswz3c0bh827vs------------------------------------------------------0oohke7s6s3gor6shpxnuwltlo1qn3sag57na7-----------------------------------------------------ykfyueyid364gqpbz6q3c55i0pljcakamx2emf0vo7spohgmqmww8t23x90tfmbd5y020zplgz7mfx1imw4j4z31cbe--------------k43z-------------------------------------------9nx7yopdndbi3v1h33sn6esbxwj6wcjfbvf7j8v9l1r69tv35q8089x6n90sntwohathk46o708c3tnzbdi--------------------------------------------------------------------------------------j8nafq8x0pkqmw9k9bwpqz2i5u4bvn1rbrbchnsijuvu4j-------------------------------------------------------------------x8x8e3mmf------------------------------------------------------------------------1di1uhkl4cnqyx7a-----------------------------------------------------------------------------f65i3l3lch3igfv3sdwudh7gf8pmwscgo8c7z7ej0o8alw3ow9b4kko83nm25aenlj0c--------------------------------------------------------------------------------------------------pn09jfb3gqr5g9rlr5ijy1anfv2gk1tmhajpmq4v3u0l3k9pwn0chnjn0tg43rv5hf3r5lalmv4cwlprs5qyjd87j---------------------------------------------------------------------------------pa4v3tcgpy6z0nvqoywp0ug40nm12jiig560byubyng2da23ze1w32494nii19t6tzs62fkfqhven1x6-----------------sm4wkq555bzbeysmqs6ckp0g7l2mgoucuu855am5rs9s4fhccw3xvp1882igb-----------------1u2eszywhx2ewg0zyex4ngua1zo17xot9khril1kz17mfq6g7tf---------------------------------------------------------------------dw9uy1w0v6km4f95gskx1se2to7p3mbf7srgvsde5an96kvn0yt98lh4e3feqepupm8395rhmsutegzz0gn723nmoih75zj819---------------------------------------------------------k87yflkc1vta9qalfw9uha20k52roann89grgpjk15hqnqu9fuqeyn0tzwp35494i87nc3u20mc9lr2krbvdms0x3wt----------------------------------------------------------------------------------------kpy8hjjgsget22z438yh4f0fdip6h9ushdx43sxznz3olqasi7nbqnaybiti7m75c7o5trbm953i38kgyi6086--------------------------------------------------------------------------------------------mf9amrf1gh5zcvkppng9984t8mc4pgnd574m7ggci9u2lox4oh731c3u2gdzbmfp---------------------------------------------------------------------------------------8isqd6l0j7krk2qbsb0prow2lecnp29s32useq2aa4p808qpq46x2nd9k4ygcxt6unxmws1ver01lhoj65-------------------------------------------------------------ovi9-----------------------------------------------------------------o8t6j---------------------------------------------------------wqh6ahn27x9kmh1snssffay5gxnicsur0z10ea2r8xlsndzgvfz5gar4n-----------------------------------------q9ftph5s2wtsxqm7h3vs2qqod15yehxcx2h--------------------------------------------------------------------------------------------------ftthpygzhln3cnah67krboi6r32s21dx4t14twgm5mfrn63y54e42q6tf17enpyyh7ac" # str | Unique channel identifier
    splice_insert_start_signal = SpliceInsertStartSignal(
        duration=30000,
        event_id=1234,
        slate_uri="https://www.example.com/logo.ts",
        upids=["03:ABCD0001000H","08:0A42235B81BC70FC","06:0000-0001-2C52-0000-P-0000-0000-0"],
    ) # SpliceInsertStartSignal |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Splice Insert Start
        api_instance.splice_start(channel_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->splice_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Splice Insert Start
        api_instance.splice_start(channel_id, splice_insert_start_signal=splice_insert_start_signal)
    except openapi_client.ApiException as e:
        print("Exception when calling ChannelOperationsApi->splice_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Unique channel identifier |
 **splice_insert_start_signal** | [**SpliceInsertStartSignal**](SpliceInsertStartSignal.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[authcode](../README.md#authcode), [m2m](../README.md#m2m)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  * Content-Type - Content-Type <br>  |
**404** | Not Found |  * Content-Type - Content-Type <br>  |
**409** | Conflict |  * Content-Type - Content-Type <br>  |
**500** | Internal Server Error |  * Content-Type - Content-Type <br>  |
**503** | Service Unavailable |  * Content-Type - Content-Type <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

