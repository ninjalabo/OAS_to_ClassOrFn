# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.counting_site_v1_api import CountingSiteV1Api


class TestCountingSiteV1Api(unittest.TestCase):
    """CountingSiteV1Api unit test stubs"""

    def setUp(self) -> None:
        self.api = CountingSiteV1Api()

    def tearDown(self) -> None:
        pass

    def test_api_counting_site_v1_counters_counter_id_get(self) -> None:
        """Test case for api_counting_site_v1_counters_counter_id_get

        Return single counter
        """
        pass

    def test_api_counting_site_v1_counters_get(self) -> None:
        """Test case for api_counting_site_v1_counters_get

        Return all counters for domain
        """
        pass

    def test_api_counting_site_v1_directions_get(self) -> None:
        """Test case for api_counting_site_v1_directions_get

        Return all directions
        """
        pass

    def test_api_counting_site_v1_domains_get(self) -> None:
        """Test case for api_counting_site_v1_domains_get

        Return all domains
        """
        pass

    def test_api_counting_site_v1_user_types_get(self) -> None:
        """Test case for api_counting_site_v1_user_types_get

        Return all user types
        """
        pass

    def test_api_counting_site_v1_values_csv_get(self) -> None:
        """Test case for api_counting_site_v1_values_csv_get

        Return counter values in CSV. If no year&month specified, current month will be used
        """
        pass

    def test_api_counting_site_v1_values_get(self) -> None:
        """Test case for api_counting_site_v1_values_get

        Return counter values.  If no year&month specified, current month will be used.
        """
        pass


if __name__ == '__main__':
    unittest.main()