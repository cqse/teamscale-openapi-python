# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class TrackedFindingWithDiffInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'location': 'ElementLocation',
        'group_name': 'str',
        'category_name': 'str',
        'message': 'str',
        'assessment': 'str',
        'sibling_locations': 'list[ElementLocation]',
        'secondary_locations': 'list[ElementLocation]',
        'properties': 'dict(str, object)',
        'statement_path': 'list[StatementPathElement]',
        'analysis_timestamp': 'int',
        'type_id': 'str',
        'id': 'str',
        'birth': 'CommitDescriptor',
        'death': 'CommitDescriptor',
        'creation_diff': 'DiffInputDescription',
        'created_by_other_change': 'bool',
        'removal_diff': 'DiffInputDescription',
        'removed_by_other_change': 'bool'
    }

    attribute_map = {
        'location': 'location',
        'group_name': 'groupName',
        'category_name': 'categoryName',
        'message': 'message',
        'assessment': 'assessment',
        'sibling_locations': 'siblingLocations',
        'secondary_locations': 'secondaryLocations',
        'properties': 'properties',
        'statement_path': 'statementPath',
        'analysis_timestamp': 'analysisTimestamp',
        'type_id': 'typeId',
        'id': 'id',
        'birth': 'birth',
        'death': 'death',
        'creation_diff': 'creationDiff',
        'created_by_other_change': 'createdByOtherChange',
        'removal_diff': 'removalDiff',
        'removed_by_other_change': 'removedByOtherChange'
    }

    def __init__(self, location=None, group_name=None, category_name=None, message=None, assessment=None, sibling_locations=None, secondary_locations=None, properties=None, statement_path=None, analysis_timestamp=None, type_id=None, id=None, birth=None, death=None, creation_diff=None, created_by_other_change=None, removal_diff=None, removed_by_other_change=None, local_vars_configuration=None):  # noqa: E501
        """TrackedFindingWithDiffInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location = None
        self._group_name = None
        self._category_name = None
        self._message = None
        self._assessment = None
        self._sibling_locations = None
        self._secondary_locations = None
        self._properties = None
        self._statement_path = None
        self._analysis_timestamp = None
        self._type_id = None
        self._id = None
        self._birth = None
        self._death = None
        self._creation_diff = None
        self._created_by_other_change = None
        self._removal_diff = None
        self._removed_by_other_change = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if group_name is not None:
            self.group_name = group_name
        if category_name is not None:
            self.category_name = category_name
        if message is not None:
            self.message = message
        if assessment is not None:
            self.assessment = assessment
        if sibling_locations is not None:
            self.sibling_locations = sibling_locations
        if secondary_locations is not None:
            self.secondary_locations = secondary_locations
        if properties is not None:
            self.properties = properties
        if statement_path is not None:
            self.statement_path = statement_path
        if analysis_timestamp is not None:
            self.analysis_timestamp = analysis_timestamp
        if type_id is not None:
            self.type_id = type_id
        if id is not None:
            self.id = id
        if birth is not None:
            self.birth = birth
        if death is not None:
            self.death = death
        if creation_diff is not None:
            self.creation_diff = creation_diff
        if created_by_other_change is not None:
            self.created_by_other_change = created_by_other_change
        if removal_diff is not None:
            self.removal_diff = removal_diff
        if removed_by_other_change is not None:
            self.removed_by_other_change = removed_by_other_change

    @property
    def location(self):
        """Gets the location of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The location of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: ElementLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this TrackedFindingWithDiffInfo.


        :param location: The location of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: ElementLocation
        """

        self._location = location

    @property
    def group_name(self):
        """Gets the group_name of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The group_name of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this TrackedFindingWithDiffInfo.


        :param group_name: The group_name of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def category_name(self):
        """Gets the category_name of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The category_name of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this TrackedFindingWithDiffInfo.


        :param category_name: The category_name of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    @property
    def message(self):
        """Gets the message of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The message of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TrackedFindingWithDiffInfo.


        :param message: The message of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def assessment(self):
        """Gets the assessment of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The assessment of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: str
        """
        return self._assessment

    @assessment.setter
    def assessment(self, assessment):
        """Sets the assessment of this TrackedFindingWithDiffInfo.


        :param assessment: The assessment of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["RED", "ORANGE", "YELLOW", "GREEN", "BASELINE", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and assessment not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `assessment` ({0}), must be one of {1}"  # noqa: E501
                .format(assessment, allowed_values)
            )

        self._assessment = assessment

    @property
    def sibling_locations(self):
        """Gets the sibling_locations of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The sibling_locations of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: list[ElementLocation]
        """
        return self._sibling_locations

    @sibling_locations.setter
    def sibling_locations(self, sibling_locations):
        """Sets the sibling_locations of this TrackedFindingWithDiffInfo.


        :param sibling_locations: The sibling_locations of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: list[ElementLocation]
        """

        self._sibling_locations = sibling_locations

    @property
    def secondary_locations(self):
        """Gets the secondary_locations of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The secondary_locations of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: list[ElementLocation]
        """
        return self._secondary_locations

    @secondary_locations.setter
    def secondary_locations(self, secondary_locations):
        """Sets the secondary_locations of this TrackedFindingWithDiffInfo.


        :param secondary_locations: The secondary_locations of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: list[ElementLocation]
        """

        self._secondary_locations = secondary_locations

    @property
    def properties(self):
        """Gets the properties of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The properties of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TrackedFindingWithDiffInfo.


        :param properties: The properties of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def statement_path(self):
        """Gets the statement_path of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The statement_path of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: list[StatementPathElement]
        """
        return self._statement_path

    @statement_path.setter
    def statement_path(self, statement_path):
        """Sets the statement_path of this TrackedFindingWithDiffInfo.


        :param statement_path: The statement_path of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: list[StatementPathElement]
        """

        self._statement_path = statement_path

    @property
    def analysis_timestamp(self):
        """Gets the analysis_timestamp of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The analysis_timestamp of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: int
        """
        return self._analysis_timestamp

    @analysis_timestamp.setter
    def analysis_timestamp(self, analysis_timestamp):
        """Sets the analysis_timestamp of this TrackedFindingWithDiffInfo.


        :param analysis_timestamp: The analysis_timestamp of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: int
        """

        self._analysis_timestamp = analysis_timestamp

    @property
    def type_id(self):
        """Gets the type_id of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The type_id of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this TrackedFindingWithDiffInfo.


        :param type_id: The type_id of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: str
        """

        self._type_id = type_id

    @property
    def id(self):
        """Gets the id of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The id of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackedFindingWithDiffInfo.


        :param id: The id of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def birth(self):
        """Gets the birth of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The birth of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: CommitDescriptor
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this TrackedFindingWithDiffInfo.


        :param birth: The birth of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: CommitDescriptor
        """

        self._birth = birth

    @property
    def death(self):
        """Gets the death of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The death of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: CommitDescriptor
        """
        return self._death

    @death.setter
    def death(self, death):
        """Sets the death of this TrackedFindingWithDiffInfo.


        :param death: The death of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: CommitDescriptor
        """

        self._death = death

    @property
    def creation_diff(self):
        """Gets the creation_diff of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The creation_diff of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: DiffInputDescription
        """
        return self._creation_diff

    @creation_diff.setter
    def creation_diff(self, creation_diff):
        """Sets the creation_diff of this TrackedFindingWithDiffInfo.


        :param creation_diff: The creation_diff of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: DiffInputDescription
        """

        self._creation_diff = creation_diff

    @property
    def created_by_other_change(self):
        """Gets the created_by_other_change of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The created_by_other_change of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: bool
        """
        return self._created_by_other_change

    @created_by_other_change.setter
    def created_by_other_change(self, created_by_other_change):
        """Sets the created_by_other_change of this TrackedFindingWithDiffInfo.


        :param created_by_other_change: The created_by_other_change of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: bool
        """

        self._created_by_other_change = created_by_other_change

    @property
    def removal_diff(self):
        """Gets the removal_diff of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The removal_diff of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: DiffInputDescription
        """
        return self._removal_diff

    @removal_diff.setter
    def removal_diff(self, removal_diff):
        """Sets the removal_diff of this TrackedFindingWithDiffInfo.


        :param removal_diff: The removal_diff of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: DiffInputDescription
        """

        self._removal_diff = removal_diff

    @property
    def removed_by_other_change(self):
        """Gets the removed_by_other_change of this TrackedFindingWithDiffInfo.  # noqa: E501


        :return: The removed_by_other_change of this TrackedFindingWithDiffInfo.  # noqa: E501
        :rtype: bool
        """
        return self._removed_by_other_change

    @removed_by_other_change.setter
    def removed_by_other_change(self, removed_by_other_change):
        """Sets the removed_by_other_change of this TrackedFindingWithDiffInfo.


        :param removed_by_other_change: The removed_by_other_change of this TrackedFindingWithDiffInfo.  # noqa: E501
        :type: bool
        """

        self._removed_by_other_change = removed_by_other_change

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrackedFindingWithDiffInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedFindingWithDiffInfo):
            return True

        return self.to_dict() != other.to_dict()
