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


class FindingsFilterSettings(object):
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
        'commit': 'str',
        'regex_filter': 'str',
        'exclude_regex_filter': 'bool',
        'filter_findings_added_to_tasks': 'bool',
        'category_and_groups_filters': 'list[str]',
        'invert_category_and_groups_filters': 'bool',
        'assessment_filters': 'list[str]',
        'blacklisting_option': 'str',
        'baseline': 'str',
        'qualified_name': 'str',
        'include_changed_code_findings': 'bool',
        'blacklist_rationale_filter': 'str'
    }

    attribute_map = {
        'commit': 'commit',
        'regex_filter': 'regexFilter',
        'exclude_regex_filter': 'excludeRegexFilter',
        'filter_findings_added_to_tasks': 'filterFindingsAddedToTasks',
        'category_and_groups_filters': 'categoryAndGroupsFilters',
        'invert_category_and_groups_filters': 'invertCategoryAndGroupsFilters',
        'assessment_filters': 'assessmentFilters',
        'blacklisting_option': 'blacklistingOption',
        'baseline': 'baseline',
        'qualified_name': 'qualifiedName',
        'include_changed_code_findings': 'includeChangedCodeFindings',
        'blacklist_rationale_filter': 'blacklistRationaleFilter'
    }

    def __init__(self, commit=None, regex_filter=None, exclude_regex_filter=None, filter_findings_added_to_tasks=None, category_and_groups_filters=None, invert_category_and_groups_filters=None, assessment_filters=None, blacklisting_option=None, baseline=None, qualified_name=None, include_changed_code_findings=None, blacklist_rationale_filter=None, local_vars_configuration=None):  # noqa: E501
        """FindingsFilterSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._commit = None
        self._regex_filter = None
        self._exclude_regex_filter = None
        self._filter_findings_added_to_tasks = None
        self._category_and_groups_filters = None
        self._invert_category_and_groups_filters = None
        self._assessment_filters = None
        self._blacklisting_option = None
        self._baseline = None
        self._qualified_name = None
        self._include_changed_code_findings = None
        self._blacklist_rationale_filter = None
        self.discriminator = None

        if commit is not None:
            self.commit = commit
        if regex_filter is not None:
            self.regex_filter = regex_filter
        if exclude_regex_filter is not None:
            self.exclude_regex_filter = exclude_regex_filter
        if filter_findings_added_to_tasks is not None:
            self.filter_findings_added_to_tasks = filter_findings_added_to_tasks
        if category_and_groups_filters is not None:
            self.category_and_groups_filters = category_and_groups_filters
        if invert_category_and_groups_filters is not None:
            self.invert_category_and_groups_filters = invert_category_and_groups_filters
        if assessment_filters is not None:
            self.assessment_filters = assessment_filters
        if blacklisting_option is not None:
            self.blacklisting_option = blacklisting_option
        if baseline is not None:
            self.baseline = baseline
        if qualified_name is not None:
            self.qualified_name = qualified_name
        if include_changed_code_findings is not None:
            self.include_changed_code_findings = include_changed_code_findings
        if blacklist_rationale_filter is not None:
            self.blacklist_rationale_filter = blacklist_rationale_filter

    @property
    def commit(self):
        """Gets the commit of this FindingsFilterSettings.  # noqa: E501


        :return: The commit of this FindingsFilterSettings.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this FindingsFilterSettings.


        :param commit: The commit of this FindingsFilterSettings.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                commit is not None and not re.search(r'(?:(.+):)?(HEAD|\d+)(?:p(\d+))?', commit)):  # noqa: E501
            raise ValueError(r"Invalid value for `commit`, must be a follow pattern or equal to `/(?:(.+):)?(HEAD|\d+)(?:p(\d+))?/`")  # noqa: E501

        self._commit = commit

    @property
    def regex_filter(self):
        """Gets the regex_filter of this FindingsFilterSettings.  # noqa: E501

        A case-insensitive Java regex pattern  # noqa: E501

        :return: The regex_filter of this FindingsFilterSettings.  # noqa: E501
        :rtype: str
        """
        return self._regex_filter

    @regex_filter.setter
    def regex_filter(self, regex_filter):
        """Sets the regex_filter of this FindingsFilterSettings.

        A case-insensitive Java regex pattern  # noqa: E501

        :param regex_filter: The regex_filter of this FindingsFilterSettings.  # noqa: E501
        :type: str
        """

        self._regex_filter = regex_filter

    @property
    def exclude_regex_filter(self):
        """Gets the exclude_regex_filter of this FindingsFilterSettings.  # noqa: E501


        :return: The exclude_regex_filter of this FindingsFilterSettings.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_regex_filter

    @exclude_regex_filter.setter
    def exclude_regex_filter(self, exclude_regex_filter):
        """Sets the exclude_regex_filter of this FindingsFilterSettings.


        :param exclude_regex_filter: The exclude_regex_filter of this FindingsFilterSettings.  # noqa: E501
        :type: bool
        """

        self._exclude_regex_filter = exclude_regex_filter

    @property
    def filter_findings_added_to_tasks(self):
        """Gets the filter_findings_added_to_tasks of this FindingsFilterSettings.  # noqa: E501


        :return: The filter_findings_added_to_tasks of this FindingsFilterSettings.  # noqa: E501
        :rtype: bool
        """
        return self._filter_findings_added_to_tasks

    @filter_findings_added_to_tasks.setter
    def filter_findings_added_to_tasks(self, filter_findings_added_to_tasks):
        """Sets the filter_findings_added_to_tasks of this FindingsFilterSettings.


        :param filter_findings_added_to_tasks: The filter_findings_added_to_tasks of this FindingsFilterSettings.  # noqa: E501
        :type: bool
        """

        self._filter_findings_added_to_tasks = filter_findings_added_to_tasks

    @property
    def category_and_groups_filters(self):
        """Gets the category_and_groups_filters of this FindingsFilterSettings.  # noqa: E501


        :return: The category_and_groups_filters of this FindingsFilterSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_and_groups_filters

    @category_and_groups_filters.setter
    def category_and_groups_filters(self, category_and_groups_filters):
        """Sets the category_and_groups_filters of this FindingsFilterSettings.


        :param category_and_groups_filters: The category_and_groups_filters of this FindingsFilterSettings.  # noqa: E501
        :type: list[str]
        """

        self._category_and_groups_filters = category_and_groups_filters

    @property
    def invert_category_and_groups_filters(self):
        """Gets the invert_category_and_groups_filters of this FindingsFilterSettings.  # noqa: E501


        :return: The invert_category_and_groups_filters of this FindingsFilterSettings.  # noqa: E501
        :rtype: bool
        """
        return self._invert_category_and_groups_filters

    @invert_category_and_groups_filters.setter
    def invert_category_and_groups_filters(self, invert_category_and_groups_filters):
        """Sets the invert_category_and_groups_filters of this FindingsFilterSettings.


        :param invert_category_and_groups_filters: The invert_category_and_groups_filters of this FindingsFilterSettings.  # noqa: E501
        :type: bool
        """

        self._invert_category_and_groups_filters = invert_category_and_groups_filters

    @property
    def assessment_filters(self):
        """Gets the assessment_filters of this FindingsFilterSettings.  # noqa: E501


        :return: The assessment_filters of this FindingsFilterSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._assessment_filters

    @assessment_filters.setter
    def assessment_filters(self, assessment_filters):
        """Sets the assessment_filters of this FindingsFilterSettings.


        :param assessment_filters: The assessment_filters of this FindingsFilterSettings.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["RED", "ORANGE", "YELLOW", "GREEN", "BASELINE", "UNKNOWN"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(assessment_filters).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `assessment_filters` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(assessment_filters) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._assessment_filters = assessment_filters

    @property
    def blacklisting_option(self):
        """Gets the blacklisting_option of this FindingsFilterSettings.  # noqa: E501


        :return: The blacklisting_option of this FindingsFilterSettings.  # noqa: E501
        :rtype: str
        """
        return self._blacklisting_option

    @blacklisting_option.setter
    def blacklisting_option(self, blacklisting_option):
        """Sets the blacklisting_option of this FindingsFilterSettings.


        :param blacklisting_option: The blacklisting_option of this FindingsFilterSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXCLUDED", "ALL", "ONLY_BLACKLISTED", "ONLY_TOLERATED", "ONLY_FALSE_POSITIVES"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and blacklisting_option not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `blacklisting_option` ({0}), must be one of {1}"  # noqa: E501
                .format(blacklisting_option, allowed_values)
            )

        self._blacklisting_option = blacklisting_option

    @property
    def baseline(self):
        """Gets the baseline of this FindingsFilterSettings.  # noqa: E501


        :return: The baseline of this FindingsFilterSettings.  # noqa: E501
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        """Sets the baseline of this FindingsFilterSettings.


        :param baseline: The baseline of this FindingsFilterSettings.  # noqa: E501
        :type: str
        """

        self._baseline = baseline

    @property
    def qualified_name(self):
        """Gets the qualified_name of this FindingsFilterSettings.  # noqa: E501


        :return: The qualified_name of this FindingsFilterSettings.  # noqa: E501
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        """Sets the qualified_name of this FindingsFilterSettings.


        :param qualified_name: The qualified_name of this FindingsFilterSettings.  # noqa: E501
        :type: str
        """

        self._qualified_name = qualified_name

    @property
    def include_changed_code_findings(self):
        """Gets the include_changed_code_findings of this FindingsFilterSettings.  # noqa: E501


        :return: The include_changed_code_findings of this FindingsFilterSettings.  # noqa: E501
        :rtype: bool
        """
        return self._include_changed_code_findings

    @include_changed_code_findings.setter
    def include_changed_code_findings(self, include_changed_code_findings):
        """Sets the include_changed_code_findings of this FindingsFilterSettings.


        :param include_changed_code_findings: The include_changed_code_findings of this FindingsFilterSettings.  # noqa: E501
        :type: bool
        """

        self._include_changed_code_findings = include_changed_code_findings

    @property
    def blacklist_rationale_filter(self):
        """Gets the blacklist_rationale_filter of this FindingsFilterSettings.  # noqa: E501

        A Java regex pattern  # noqa: E501

        :return: The blacklist_rationale_filter of this FindingsFilterSettings.  # noqa: E501
        :rtype: str
        """
        return self._blacklist_rationale_filter

    @blacklist_rationale_filter.setter
    def blacklist_rationale_filter(self, blacklist_rationale_filter):
        """Sets the blacklist_rationale_filter of this FindingsFilterSettings.

        A Java regex pattern  # noqa: E501

        :param blacklist_rationale_filter: The blacklist_rationale_filter of this FindingsFilterSettings.  # noqa: E501
        :type: str
        """

        self._blacklist_rationale_filter = blacklist_rationale_filter

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
        if not isinstance(other, FindingsFilterSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FindingsFilterSettings):
            return True

        return self.to_dict() != other.to_dict()