from collections import OrderedDict
import requests
import logging
import urllib
import json
import operator

from django.conf import settings

from .paginator import Paginator

API_TYPES = {
    "events": settings.FDA_DRUG_API_EVENT_URL,
    "labels": settings.FDA_DRUG_API_LABEL_URL,
    "enforcements": settings.FDA_DRUG_API_ENFORCEMENT_URL}

BROWSE_TYPES = {
    "events": "patient.reaction.reactionmeddrapt",
    "labels": "openfda.brand_name",
    "enforcements": "state",
    "manufacturers": {
        "labels": "openfda.manufacturer_name",
        #        "events": "patient.drug.openfda.manufacturer_name",
        #        "enforcements": "openfda.manufacturer_name"
    }
}

PARAMETER_MAPPINGS = {
    "serious": {
        "1": "The adverse event resulted in death, a life threatening condition, " +
             "hospitalization, disability, congenital anomaly, or other serious condition.",
        "2": "The adverse event did NOT result in death, a life threatening condition, " +
             "hospitalization, disability, congenital anomaly, or other serious condition."
    },
    "drugcharacterization": {
        "1": "Suspect",
        "2": "Concomitant",
        "3": "Interacting"
    },
    "drugadministrationroute": {
        # TODO: add the drug administration route mappingsf
    },
    "action": {
        "1": "Drug withdrawn",
        "2": "Dose reduced",
        "3": "Dose increased",
        "4": "Dose not changed",
        "5": "Unknown",
        "6": "N/A"
    }
}

# TODO: pull out some of the url strings
# TODO: we need to limit the number of results returned since the API only supports 5000 or less
# TODO: Create a wrapper around requests that customizes error handling


class ApiClient(object):
    """
    API client code for consuming FDA opendata apis
    """
    logger = logging.getLogger(__name__)

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.api_limit = 10

    def browse(self, browse_type):
        if browse_type == 'manufacturers':
            return self._browse_manufacturers()

        results = {}
        data = requests.get("%s?count=%s.exact" % (API_TYPES.get(browse_type), BROWSE_TYPES.get(browse_type)))
        if data:
            results = data.json()

        return results.get('results')

    def _browse_manufacturers(self):
        """
        Get each of the manufacturer lists from the api sources. Return the combined json object.
        :return: list of combined manufacturer names and counts
        """
        data = {}

        # get the response from each of the queries
        for api_type, api_path in BROWSE_TYPES.get('manufacturers').items():
            self.logger.debug('Browsing for manufacturers by %s' % api_type)
            api_type_data = requests.get("%s?count=%s.exact" % (API_TYPES.get(api_type), api_path))

            if api_type_data:
                data[api_type] = api_type_data

        # if we got response(s), flatten them down
        if data:
            results = []
            for api_type, api_response in data.items():
                results += api_response.json().get('results')

            # and sort the list in alphabetical order
            if results:
                results = sorted(results, key=operator.itemgetter('term'))

            return results

        return None

    def search_labels(self, query_term, page, tab=None):
        self.logger.debug("Searching for '%s'", query_term)
        data = {}

        labels_page = 1
        events_page = 1
        enforcements_page = 1

        if tab == 'events':
            events_page = page
        elif tab == 'enforcements':
            enforcements_page = page
        else:
            labels_page = page

        # get general drug info
        sub_data = self.get_sub_data("%s?search=openfda.brand_name:\"%s\"" % (
            API_TYPES['labels'], urllib.quote(query_term)), labels_page)
        if sub_data:
            label_pagination, labels = sub_data.clean_labels()
            data['labels'] = labels
            data['labels_paginator'] = Paginator(label_pagination)

        # get additional event info
        sub_data = self.get_sub_data("%s?search=patient.drug.medicinalproduct:\"%s\"" % (
            API_TYPES['events'], urllib.quote(query_term)), events_page)
        if sub_data:
            events_pagination, events = sub_data.clean_events()
            data['events'] = events
            data['events_paginator'] = Paginator(events_pagination)

        # get additional enforcement info
        sub_data = self.get_sub_data("%s?search=product_description:\"%s\"" % (
            API_TYPES['enforcements'], urllib.quote(query_term)), enforcements_page)
        if sub_data:
            enforcements_pagination, enforcements = sub_data.clean_enforcements()
            data['enforcements'] = enforcements
            data['enforcements_paginator'] = Paginator(enforcements_pagination)

        return data

    def search_events(self, query_term, page):
        self.logger.debug("Searching for event '%s'", query_term)
        data = {}

        # get events counts
        count_string = "&count=patient.drug.openfda.substance_name.exact"
        data['events_count'] = self.get_count_data(
            "%s?search=patient.reaction.reactionmeddrapt:\"%s\"%s" % (
                API_TYPES['events'], query_term, count_string))

        # get events info
        sub_data = self.get_sub_data("%s?search=patient.reaction.reactionmeddrapt:\"%s\"" % (
            API_TYPES['events'], query_term), page)
        if sub_data:
            events_pagination, events = sub_data.clean_events()
            data['events'] = events
            data['events_paginator'] = Paginator(events_pagination)

        return data

    def search_enforcements(self, query_term, page):
        self.logger.debug("Searching for enforcement '%s'", query_term)
        data = {}

        # get general enforcement info
        sub_data = self.get_sub_data("%s?search=state:\"%s\"" % (
            API_TYPES['enforcements'], urllib.quote(query_term)), page)
        if sub_data:
            enforcements_pagination, enforcements = sub_data.clean_enforcements()
            data['enforcements'] = enforcements
            data['enforcements_paginator'] = Paginator(enforcements_pagination)

        # get drug counts
        count_string = "&count=openfda.brand_name.exact"
        data['drugs_count'] = self.get_count_data(
            "%s?search=state:\"%s\"%s" % (
                API_TYPES['enforcements'], query_term, count_string))
        return data

    def search_manufacturers(self, query_term, page, tab=None):
        self.logger.debug("Searching for manufacturer '%s'", query_term)
        data = {}

        labels_page = 1
        events_page = 1
        enforcements_page = 1

        if tab == 'events':
            events_page = page
        elif tab == 'enforcements':
            enforcements_page = page
        else:
            labels_page = page

        # strip commas - api can't handle them in search terms
        query_term = query_term.replace(",", '')

        # get labels from this manufacturer
        sub_data = self.get_sub_data("%s?search=openfda.manufacturer_name:\"%s\"" % (
            API_TYPES['labels'], urllib.quote(query_term)), labels_page)
        if sub_data:
            labels_pagination, labels = sub_data.clean_labels()
            data['labels'] = labels
            data['labels_paginator'] = Paginator(labels_pagination)

        # get additional event info
        sub_data = self.get_sub_data("%s?search=patient.drug.openfda.manufacturer_name:\"%s\"" % (
            API_TYPES['events'], urllib.quote(query_term)), events_page)
        if sub_data:
            events_pagination, events = sub_data.clean_events()
            data['events'] = events
            data['events_paginator'] = Paginator(events_pagination)

        # get additional enforcement info. we search for the name as manufacturer
        # Our original search was for manufacturer or recalling firm for this api, but the 'or'
        # query does not work.
        # Eg, https://api.fda.gov/drug/enforcement.json?search=openfda.manufacturer_name:
        # %22Pharmacia+and+Upjohn+Company%22+recalling_firm:%22Target%22 is broken

        sub_data = self.get_sub_data("%s?search=openfda.manufacturer_name:\"%s\"" % (
            API_TYPES['enforcements'], urllib.quote(query_term)), enforcements_page)
        if sub_data:
            enforcements_pagination, enforcements = sub_data.clean_enforcements()
            data['enforcements'] = enforcements
            data['enforcements_paginator'] = Paginator(enforcements_pagination)

        return data

    def get_age_sex(self, api_type, param, filter_string):
        # TODO: implement grouping by age group
        total_male = self.filter_patient(api_type, filter_string, param, 1)
        total_female = self.filter_patient(api_type, filter_string, param, 2)

        return json.dumps([{
            "name": "Male",
            "data": [total_male]
        }, {
            "name": "Female",
            "data": [total_female]
        }])

    def filter_patient(self, api_type, filter_string, param, identifier):
        filter = '+AND+patient.drug.openfda.substance_name:%s+AND+patient.patientsex:%s' % (filter_string, identifier)
        url = '%s?search=%s%s' % (API_TYPES[api_type], urllib.quote(param), filter)
        self.logger.debug("url: %s", url)
        resp = requests.get(url)
        resp_json = resp.json()
        return resp_json['meta']['results']['total']

    def get_sub_data(self, query_string, page):
        """
        This is used by search to call the fda API
        """
        url = '%s&limit=%s&skip=%s' % (query_string, self.api_limit, (page - 1) * self.api_limit)
        self.logger.debug("url: %s", url)
        resp = requests.get(url)
        if resp.status_code == 200:
            resp = resp.json()
            return ApiResult(resp)
        self.logger.info('no results found for %s', query_string)
        return None

    def get_count_data(self, query_url):
        """
        This is used by browse to call the fda API
        """
        self.logger.debug("url: %s", query_url)
        count_json = requests.get(query_url).json()
        if 'error' in count_json:
            self.logger.error("Error getting at url %s: %s", query_url, count_json['error'])
            return None
        resp = count_json.get('results')
        return resp


class ApiResult(object):
    """
    Class to hold api results returned
    """

    def __init__(self, data):
        self.data = data

    def lookup(self, d, key_string, default=None):
        """
        returns values from nested dictionaries
        """
        key_list = key_string.split('.')[::-1]
        try:
            value = self._lookup(d, key_list)
            return value if value else default
        except KeyError:
            return default

    def _lookup(self, data_dict, key_list):
        if key_list:
            key = key_list.pop()
            data = data_dict[key]
            if isinstance(data, dict):
                return self._lookup(data, key_list)
            else:
                return data

    def clean_labels(self):
        """
        returns only the fields needed for labels
        """
        results = []
        meta = self.data.get('meta').get('results')
        for d in self.data.get('results'):
            clean_data = {
                "id": self.lookup(d, 'id'),
                "brand_name": self.lookup(d, 'openfda.brand_name'),
                "generic_name": self.lookup(d, 'openfda.generic_name'),
                "description": self.lookup(d, 'openfda.description'),
                "pharm_class_epc": self.lookup(d, 'openfda.pharm_class_epc'),
                "pharm_class cs": self.lookup(d, 'openfda.pharm_class_cs'),
                "route": self.lookup(d, 'openfda.route'),
                "manufacturer": self.lookup(d, 'openfda.manufacturer_name'),
                "do_not_use": self.lookup(d, 'openfda.do_not_use'),
                "active_ingredient": self.lookup(d, 'active_ingredient'),
                "inactive_ingredient": self.lookup(d, 'inactive_ingredient'),
                "dosage_and_administration": self.lookup(d, 'dosage_and_administration'),
                "warnings": self.lookup(d, 'warnings'),
                "adverse_reactions": self.lookup(d, 'adverse_reactions'),
                "drug_interactions": self.lookup(d, 'drug_interactions'),
                "pharmacokinetics": self.lookup(d, 'pharmacokinetics'),
            }
            results.append(clean_data)
        return meta, results

    def clean_events(self):
        results = []
        meta = self.data.get('meta').get('results')
        for d in self.data.get('results'):
            safety_data = OrderedDict()
            safety_data["safety_report"] = self.lookup(d, 'safetyreportid')
            safety_data["safety_report_version"] = self.lookup(d, 'safetyreportversion')
            safety_data["receive_date"] = self.format_date(self.lookup(d, 'receivedate'))
            safety_data["receipt_date_format"] = self.lookup(d, 'receiptdateformat')
            safety_data["seriousness"] = self.format_field_from_parameter_mapping('serious', self.lookup(d, 'serious'))
            safety_data["seriousness_details"] = \
                ["congenital anomaly: %s" % self.yes_or_no(self.lookup(d, "seriouscongenitalanomali")),
                 "death: %s" % self.yes_or_no(self.lookup(d, "seriousnessdeath")),
                 "disabling: %s" % self.yes_or_no(self.lookup(d, "seriousnessdisabling")),
                 "hospitalization: %s" % self.yes_or_no(self.lookup(d, "seriousnesshospitalization")),
                 "life threatening: %s" % self.yes_or_no(self.lookup(d, "seriousnesslifethreatening")),
                 "other: %s" % self.yes_or_no(self.lookup(d, "seriousnessother"))]
            safety_data["duplicate_report_source"] = self.lookup(d, 'reportduplicate.duplicatesource')
            safety_data["duplicate_report_number"] = self.lookup(d, 'reportduplicate.duplicatenumb')

            patient_data = OrderedDict()
            patient_data["patient_onset_age"] = "%s%s" % (self.lookup(d, 'patient.patientonsetstage', ""),
                                                          self.lookup(d, 'patientonsetageunit', ""))
            patient_data["patient_sex"] = self.male_or_female(self.lookup(d, 'patient.patientsex'))
            patient_data["patient_death_details"] = self.format_date(self.lookup(d, 'patient.patientdeath.patientdeathdate'))

            label_data = {}
            drugs = self.lookup(d, 'patient.drug')

            for drug in drugs:
                label_data[self.lookup(drug, "medicinalproduct")] = [
                    "drug administration route: %s" % (self.lookup(drug, 'drugadministrationroute')),
                    "actions taken with drug: %s" %
                    self.format_field_from_parameter_mapping('action', self.lookup(drug, 'actiondrug')),
                    "reported dosage: %s%s" %
                    (self.lookup(drug, 'drugcumulativedosagenumb'), self.lookup(drug, 'drugcumulativedosageunit', '')),
                    "number of doses: %s" % self.lookup(drug, 'drugstructuredosagenumb'),
                    "reported role of drug in adverse event: %s" %
                    self.format_field_from_parameter_mapping('drugcharacterization', self.lookup(drug, 'drugcharacterization'))
                ]
            # suppress details when seriousness is minor
            if safety_data["seriousness"] != PARAMETER_MAPPINGS.get('serious').get('1'):
                safety_data.pop("seriousness_details")

            results.append({'safety_data': safety_data,
                            'patient_data': patient_data,
                            'label_data': label_data})
        return meta, results

    def clean_enforcements(self):
        results = []
        meta = self.data.get('meta').get('results')
        for d in self.data.get('results'):
            clean_data = {
                'event_id': self.lookup(d, 'event_id'),
                'recall_number': self.lookup(d, 'recall_number'),
                'status': self.lookup(d, 'status'),
                'city': self.lookup(d, 'city'),
                'state': self.lookup(d, 'state'),
                'recalling_firm': self.lookup(d, 'recalling_firm'),
                'reason_for_recall': self.lookup(d, 'reason_for_recall'),
                'manufacturer_name': self.lookup(d, 'openfda.manufacturer_name'),
                'recall_initiation_date': self.format_date(self.lookup(d, 'recall_initiation_date')),
                'classification': self.lookup(d, 'classification'),
                'product_description': self.lookup(d, 'product_description'),
                'code_info': self.lookup(d, 'code_info'),
                'voluntary_mandated': self.lookup(d, 'voluntary_mandated'),
                'initial_firm_notification': self.lookup(d, 'initial_firm_notification'),
                'report_date': self.format_date(self.lookup(d, 'report_date')),
            }
            results.append(clean_data)
        return meta, results

    def yes_or_no(self, value):
        if value == "1":
            return "Yes"
        elif value == "2":
            return "No"

    def male_or_female(self, value):

        if value == "1":
            return 'Male'
        elif value == "2":
            return 'Female'
        elif value == "0":
            return 'Unknown'

    def format_date(self, value):
        """
        Convert value in date format YYYYMMDD to expected date format YYYY-MM-DD
        """
        if value and len(value) == 8:
            return "{0}-{1}-{2}".format(value[:4], value[4:6], value[6:])
        else:
            return "Unknown"

    def format_field_from_parameter_mapping(self, key, value):
        """
        Convert the given field into the value given in the parameter mapping or return the value
        as provided if no field is found matching the key
        :param key:
        :param value:
        :return:
        """
        parameter_values = PARAMETER_MAPPINGS.get(key, None)
        if parameter_values:
            return parameter_values.get(value, value)

        return value
