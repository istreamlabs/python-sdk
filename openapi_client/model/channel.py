"""
    iStreamPlanet Channels API

    This API provides a way to list, create, and run channels.  Channels consist of inputs (ingest), transcoding settings like codecs and bitrates, and outputs (publishing).  List calls use cursor-based pagination with [RFC 5988](https://tools.ietf.org/html/rfc5988) Link headers. Clients *should* read this header and follow the next link to read all pages of results.   # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: support@istreamplanet.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.channel_ingest import ChannelIngest
    from openapi_client.model.channel_packaging import ChannelPackaging
    from openapi_client.model.channel_publishing import ChannelPublishing
    from openapi_client.model.channel_signaling import ChannelSignaling
    from openapi_client.model.channel_tags import ChannelTags
    from openapi_client.model.channel_transcode import ChannelTranscode
    globals()['ChannelIngest'] = ChannelIngest
    globals()['ChannelPackaging'] = ChannelPackaging
    globals()['ChannelPublishing'] = ChannelPublishing
    globals()['ChannelSignaling'] = ChannelSignaling
    globals()['ChannelTags'] = ChannelTags
    globals()['ChannelTranscode'] = ChannelTranscode


class Channel(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('region',): {
            'WEST': "US_WEST",
            'EAST': "US_EAST",
        },
        ('resource_class',): {
            'DYNAMIC': "DYNAMIC",
            'STATIC': "STATIC",
        },
    }

    validations = {
        ('id',): {
            'min_length': 1,
            'regex': {
                'pattern': r'^([a-z0-9]+(-*[a-z0-9]+)*)$',  # noqa: E501
            },
        },
        ('labels',): {
            'max_items': 10,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'ingest': (ChannelIngest,),  # noqa: E501
            'transcode': (ChannelTranscode,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'labels': ([str],),  # noqa: E501
            'modified': (datetime,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'packaging': (ChannelPackaging,),  # noqa: E501
            'publishing': (ChannelPublishing,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'resource_class': (str,),  # noqa: E501
            'self': (str,),  # noqa: E501
            'signaling': (ChannelSignaling,),  # noqa: E501
            'tags': (ChannelTags,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ingest': 'ingest',  # noqa: E501
        'transcode': 'transcode',  # noqa: E501
        'created': 'created',  # noqa: E501
        'id': 'id',  # noqa: E501
        'labels': 'labels',  # noqa: E501
        'modified': 'modified',  # noqa: E501
        'name': 'name',  # noqa: E501
        'packaging': 'packaging',  # noqa: E501
        'publishing': 'publishing',  # noqa: E501
        'region': 'region',  # noqa: E501
        'resource_class': 'resource_class',  # noqa: E501
        'self': 'self',  # noqa: E501
        'signaling': 'signaling',  # noqa: E501
        'tags': 'tags',  # noqa: E501
    }

    read_only_vars = {
        'created',  # noqa: E501
        'id',  # noqa: E501
        'modified',  # noqa: E501
        'self',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, ingest, transcode, *args, **kwargs):  # noqa: E501
        """Channel - a model defined in OpenAPI

        Args:
            ingest (ChannelIngest):
            transcode (ChannelTranscode):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created (datetime): Date and time the channel was created.. [optional]  # noqa: E501
            id (str): External Channel ID provided at channel creation time. [optional]  # noqa: E501
            labels ([str]): Optional labels for a channel. Any included labels must be at least 1 character long, but no greater than 256 characters. The maximum number of labels is 10.. [optional]  # noqa: E501
            modified (datetime): Date and time the channel was last modified.. [optional]  # noqa: E501
            name (str): A friendly human-readable name for the channel. This will get displayed in user interfaces.. [optional]  # noqa: E501
            packaging (ChannelPackaging): [optional]  # noqa: E501
            publishing (ChannelPublishing): [optional]  # noqa: E501
            region (str): Region represents the general geolocation for transcoding and stream egress from iStreamPlanet. If no region is provided at channel creation time, then 'US_WEST' is used.. [optional]  # noqa: E501
            resource_class (str): If the ResourceClass is unspecified the channel will default to run in the 'DYNAMIC' ResourceClass. Note that changing the ResourceClass for a running channel is supported and will be performed with no downtime.. [optional]  # noqa: E501
            self (str): Self link for the channel.. [optional]  # noqa: E501
            signaling (ChannelSignaling): [optional]  # noqa: E501
            tags (ChannelTags): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.ingest = ingest
        self.transcode = transcode
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, ingest, transcode, *args, **kwargs):  # noqa: E501
        """Channel - a model defined in OpenAPI

        Args:
            ingest (ChannelIngest):
            transcode (ChannelTranscode):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created (datetime): Date and time the channel was created.. [optional]  # noqa: E501
            id (str): External Channel ID provided at channel creation time. [optional]  # noqa: E501
            labels ([str]): Optional labels for a channel. Any included labels must be at least 1 character long, but no greater than 256 characters. The maximum number of labels is 10.. [optional]  # noqa: E501
            modified (datetime): Date and time the channel was last modified.. [optional]  # noqa: E501
            name (str): A friendly human-readable name for the channel. This will get displayed in user interfaces.. [optional]  # noqa: E501
            packaging (ChannelPackaging): [optional]  # noqa: E501
            publishing (ChannelPublishing): [optional]  # noqa: E501
            region (str): Region represents the general geolocation for transcoding and stream egress from iStreamPlanet. If no region is provided at channel creation time, then 'US_WEST' is used.. [optional]  # noqa: E501
            resource_class (str): If the ResourceClass is unspecified the channel will default to run in the 'DYNAMIC' ResourceClass. Note that changing the ResourceClass for a running channel is supported and will be performed with no downtime.. [optional]  # noqa: E501
            self (str): Self link for the channel.. [optional]  # noqa: E501
            signaling (ChannelSignaling): [optional]  # noqa: E501
            tags (ChannelTags): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.ingest = ingest
        self.transcode = transcode
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
