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


class MetricThreshold(object):
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
        'name': 'str',
        'options': 'dict(str, str)',
        'custom_name': 'str',
        'threshold_yellow': 'float',
        'threshold_red': 'float',
        'sub_path': 'str',
        'metric_schema_source': 'str',
        'assessment_specification': 'str',
        'evaluation_options': 'list[str]',
        'inherited_from_configuration': 'str',
        'is_inherited': 'bool',
        'preceding_threshold_display_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'options': 'options',
        'custom_name': 'customName',
        'threshold_yellow': 'thresholdYellow',
        'threshold_red': 'thresholdRed',
        'sub_path': 'subPath',
        'metric_schema_source': 'metricSchemaSource',
        'assessment_specification': 'assessmentSpecification',
        'evaluation_options': 'evaluationOptions',
        'inherited_from_configuration': 'inheritedFromConfiguration',
        'is_inherited': 'isInherited',
        'preceding_threshold_display_name': 'precedingThresholdDisplayName'
    }

    def __init__(self, name=None, options=None, custom_name=None, threshold_yellow=None, threshold_red=None, sub_path=None, metric_schema_source=None, assessment_specification=None, evaluation_options=None, inherited_from_configuration=None, is_inherited=None, preceding_threshold_display_name=None, local_vars_configuration=None):  # noqa: E501
        """MetricThreshold - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._options = None
        self._custom_name = None
        self._threshold_yellow = None
        self._threshold_red = None
        self._sub_path = None
        self._metric_schema_source = None
        self._assessment_specification = None
        self._evaluation_options = None
        self._inherited_from_configuration = None
        self._is_inherited = None
        self._preceding_threshold_display_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if custom_name is not None:
            self.custom_name = custom_name
        if threshold_yellow is not None:
            self.threshold_yellow = threshold_yellow
        if threshold_red is not None:
            self.threshold_red = threshold_red
        if sub_path is not None:
            self.sub_path = sub_path
        if metric_schema_source is not None:
            self.metric_schema_source = metric_schema_source
        if assessment_specification is not None:
            self.assessment_specification = assessment_specification
        if evaluation_options is not None:
            self.evaluation_options = evaluation_options
        if inherited_from_configuration is not None:
            self.inherited_from_configuration = inherited_from_configuration
        if is_inherited is not None:
            self.is_inherited = is_inherited
        if preceding_threshold_display_name is not None:
            self.preceding_threshold_display_name = preceding_threshold_display_name

    @property
    def name(self):
        """Gets the name of this MetricThreshold.  # noqa: E501


        :return: The name of this MetricThreshold.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricThreshold.


        :param name: The name of this MetricThreshold.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this MetricThreshold.  # noqa: E501


        :return: The options of this MetricThreshold.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this MetricThreshold.


        :param options: The options of this MetricThreshold.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def custom_name(self):
        """Gets the custom_name of this MetricThreshold.  # noqa: E501


        :return: The custom_name of this MetricThreshold.  # noqa: E501
        :rtype: str
        """
        return self._custom_name

    @custom_name.setter
    def custom_name(self, custom_name):
        """Sets the custom_name of this MetricThreshold.


        :param custom_name: The custom_name of this MetricThreshold.  # noqa: E501
        :type: str
        """

        self._custom_name = custom_name

    @property
    def threshold_yellow(self):
        """Gets the threshold_yellow of this MetricThreshold.  # noqa: E501


        :return: The threshold_yellow of this MetricThreshold.  # noqa: E501
        :rtype: float
        """
        return self._threshold_yellow

    @threshold_yellow.setter
    def threshold_yellow(self, threshold_yellow):
        """Sets the threshold_yellow of this MetricThreshold.


        :param threshold_yellow: The threshold_yellow of this MetricThreshold.  # noqa: E501
        :type: float
        """

        self._threshold_yellow = threshold_yellow

    @property
    def threshold_red(self):
        """Gets the threshold_red of this MetricThreshold.  # noqa: E501


        :return: The threshold_red of this MetricThreshold.  # noqa: E501
        :rtype: float
        """
        return self._threshold_red

    @threshold_red.setter
    def threshold_red(self, threshold_red):
        """Sets the threshold_red of this MetricThreshold.


        :param threshold_red: The threshold_red of this MetricThreshold.  # noqa: E501
        :type: float
        """

        self._threshold_red = threshold_red

    @property
    def sub_path(self):
        """Gets the sub_path of this MetricThreshold.  # noqa: E501


        :return: The sub_path of this MetricThreshold.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this MetricThreshold.


        :param sub_path: The sub_path of this MetricThreshold.  # noqa: E501
        :type: str
        """

        self._sub_path = sub_path

    @property
    def metric_schema_source(self):
        """Gets the metric_schema_source of this MetricThreshold.  # noqa: E501


        :return: The metric_schema_source of this MetricThreshold.  # noqa: E501
        :rtype: str
        """
        return self._metric_schema_source

    @metric_schema_source.setter
    def metric_schema_source(self, metric_schema_source):
        """Sets the metric_schema_source of this MetricThreshold.


        :param metric_schema_source: The metric_schema_source of this MetricThreshold.  # noqa: E501
        :type: str
        """
        allowed_values = ["CODE_METRICS", "NON_CODE_METRICS", "TEST_EXECUTION_METRICS", "ISSUE_METRICS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and metric_schema_source not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `metric_schema_source` ({0}), must be one of {1}"  # noqa: E501
                .format(metric_schema_source, allowed_values)
            )

        self._metric_schema_source = metric_schema_source

    @property
    def assessment_specification(self):
        """Gets the assessment_specification of this MetricThreshold.  # noqa: E501


        :return: The assessment_specification of this MetricThreshold.  # noqa: E501
        :rtype: str
        """
        return self._assessment_specification

    @assessment_specification.setter
    def assessment_specification(self, assessment_specification):
        """Sets the assessment_specification of this MetricThreshold.


        :param assessment_specification: The assessment_specification of this MetricThreshold.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "FORCE_LOW_IS_BAD", "FORCE_HIGH_IS_BAD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and assessment_specification not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `assessment_specification` ({0}), must be one of {1}"  # noqa: E501
                .format(assessment_specification, allowed_values)
            )

        self._assessment_specification = assessment_specification

    @property
    def evaluation_options(self):
        """Gets the evaluation_options of this MetricThreshold.  # noqa: E501


        :return: The evaluation_options of this MetricThreshold.  # noqa: E501
        :rtype: list[str]
        """
        return self._evaluation_options

    @evaluation_options.setter
    def evaluation_options(self, evaluation_options):
        """Sets the evaluation_options of this MetricThreshold.


        :param evaluation_options: The evaluation_options of this MetricThreshold.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ASSESSMENT_METRIC_RED_IF_ANY_THRESHOLD_VIOLATED"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(evaluation_options).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `evaluation_options` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(evaluation_options) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._evaluation_options = evaluation_options

    @property
    def inherited_from_configuration(self):
        """Gets the inherited_from_configuration of this MetricThreshold.  # noqa: E501


        :return: The inherited_from_configuration of this MetricThreshold.  # noqa: E501
        :rtype: str
        """
        return self._inherited_from_configuration

    @inherited_from_configuration.setter
    def inherited_from_configuration(self, inherited_from_configuration):
        """Sets the inherited_from_configuration of this MetricThreshold.


        :param inherited_from_configuration: The inherited_from_configuration of this MetricThreshold.  # noqa: E501
        :type: str
        """

        self._inherited_from_configuration = inherited_from_configuration

    @property
    def is_inherited(self):
        """Gets the is_inherited of this MetricThreshold.  # noqa: E501


        :return: The is_inherited of this MetricThreshold.  # noqa: E501
        :rtype: bool
        """
        return self._is_inherited

    @is_inherited.setter
    def is_inherited(self, is_inherited):
        """Sets the is_inherited of this MetricThreshold.


        :param is_inherited: The is_inherited of this MetricThreshold.  # noqa: E501
        :type: bool
        """

        self._is_inherited = is_inherited

    @property
    def preceding_threshold_display_name(self):
        """Gets the preceding_threshold_display_name of this MetricThreshold.  # noqa: E501


        :return: The preceding_threshold_display_name of this MetricThreshold.  # noqa: E501
        :rtype: str
        """
        return self._preceding_threshold_display_name

    @preceding_threshold_display_name.setter
    def preceding_threshold_display_name(self, preceding_threshold_display_name):
        """Sets the preceding_threshold_display_name of this MetricThreshold.


        :param preceding_threshold_display_name: The preceding_threshold_display_name of this MetricThreshold.  # noqa: E501
        :type: str
        """

        self._preceding_threshold_display_name = preceding_threshold_display_name

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
        if not isinstance(other, MetricThreshold):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricThreshold):
            return True

        return self.to_dict() != other.to_dict()