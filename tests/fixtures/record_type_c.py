from iid2json.meta_record import MetaRecord


class RecordTypeC(MetaRecord):

    def __init__(
            self, record, no_repetition_tags=None, no_subfield_tags=None,
            data_dictionary=None):
        super().__init__(
            record, no_repetition_tags, no_subfield_tags, data_dictionary)

    @property
    def article_ref(self):
                """
        article_ref

        v000 
        """
        return self.get_field_content("v000")

    @property
    def analytic_author(self):
                """
        analytic_author

        v010 {'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname', '_': 'anonym'}
        """
        return self.get_field_content(
            "v010",
            subfields={'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname', '_': 'anonym'})

    @property
    def monograph_update(self):
                """
        monograph_update

        v107 
        """
        return self.get_field_content("v107")

    @property
    def monograph_update_dateiso(self):
                """
        monograph_update_dateiso

        v108 
        """
        return self.get_field_content("v108")

    @property
    def monograph_cited(self):
                """
        monograph_cited

        v109 
        """
        return self.get_field_content("v109")

    @property
    def analytic_corpauth(self):
                """
        analytic_corpauth

        v011 {'d': 'orgdiv', '_': 'orgname'}
        """
        return self.get_field_content(
            "v011",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def monograph_cited_dateiso(self):
                """
        monograph_cited_dateiso

        v110 
        """
        return self.get_field_content("v110")

    @property
    def no(self):
                """
        no

        v118 
        """
        return self.get_field_content("v118")

    @property
    def analytic_ctitle_title(self):
                """
        analytic_ctitle_title

        v012 {'l': 'language', '_': 'title'}
        """
        return self.get_field_content(
            "v012",
            subfields={'l': 'language', '_': 'title'})

    @property
    def analytic_location(self):
                """
        analytic_location

        v137 
        """
        return self.get_field_content("v137")

    @property
    def analytic_pages(self):
                """
        analytic_pages

        v014 
        """
        return self.get_field_content("v014")

    @property
    def monograph_author(self):
                """
        monograph_author

        v016 {'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname', '_': 'anonym'}
        """
        return self.get_field_content(
            "v016",
            subfields={'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname', '_': 'anonym'})

    @property
    def monograph_corpauth(self):
                """
        monograph_corpauth

        v017 {'d': 'orgdiv', '_': 'orgname'}
        """
        return self.get_field_content(
            "v017",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def monograph_ctitle_title(self):
                """
        monograph_ctitle_title

        v018 {'l': 'language', '_': 'title'}
        """
        return self.get_field_content(
            "v018",
            subfields={'l': 'language', '_': 'title'})

    @property
    def monograph_extent(self):
                """
        monograph_extent

        v020 
        """
        return self.get_field_content("v020")

    @property
    def monograph_tome(self):
                """
        monograph_tome

        v022 
        """
        return self.get_field_content("v022")

    @property
    def monograph_doi(self):
                """
        monograph_doi

        v237 
        """
        return self.get_field_content("v237")

    @property
    def monograph_coltitle(self):
                """
        monograph_coltitle

        v025 
        """
        return self.get_field_content("v025")

    @property
    def monograph_colvolid(self):
                """
        monograph_colvolid

        v026 
        """
        return self.get_field_content("v026")

    @property
    def serial_author(self):
                """
        serial_author

        v028 {'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname'}
        """
        return self.get_field_content(
            "v028",
            subfields={'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname'})

    @property
    def serial_corpauth(self):
                """
        serial_corpauth

        v029 {'d': 'orgdiv', '_': 'orgname'}
        """
        return self.get_field_content(
            "v029",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def analytic_volid(self):
                """
        analytic_volid

        v031 
        """
        return self.get_field_content("v031")

    @property
    def serial(self):
                """
        serial

        v032 {'s': 'suppl'}
        """
        return self.get_field_content(
            "v032",
            subfields={'s': 'suppl'})

    @property
    def serial_isstitle(self):
                """
        serial_isstitle

        v033 
        """
        return self.get_field_content("v033")

    @property
    def monograph_part(self):
                """
        monograph_part

        v034 
        """
        return self.get_field_content("v034")

    @property
    def serial_issn(self):
                """
        serial_issn

        v035 
        """
        return self.get_field_content("v035")

    @property
    def monograph_url(self):
                """
        monograph_url

        v037 
        """
        return self.get_field_content("v037")

    @property
    def serial_isdesig(self):
                """
        serial_isdesig

        v039 
        """
        return self.get_field_content("v039")

    @property
    def monograph_thesis_date(self):
                """
        monograph_thesis_date

        v044 
        """
        return self.get_field_content("v044")

    @property
    def monograph_thesis_date(self):
                """
        monograph_thesis_date

        v045 
        """
        return self.get_field_content("v045")

    @property
    def monograph_thesis(self):
                """
        monograph_thesis

        v046 {'e': 'state', '_': 'city'}
        """
        return self.get_field_content(
            "v046",
            subfields={'e': 'state', '_': 'city'})

    @property
    def monograph_thesis_country(self):
                """
        monograph_thesis_country

        v047 
        """
        return self.get_field_content("v047")

    @property
    def analytic_section(self):
                """
        analytic_section

        v049 
        """
        return self.get_field_content("v049")

    @property
    def monograph_thesis(self):
                """
        monograph_thesis

        v050 {'d': 'orgdiv', '_': 'orgname'}
        """
        return self.get_field_content(
            "v050",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def analytic_author_previous(self):
                """
        analytic_author_previous

        v710 {'_': 'previous'}
        """
        return self.get_field_content(
            "v710",
            subfields={'_': 'previous'})

    @property
    def monograph_thesis_degree(self):
                """
        monograph_thesis_degree

        v051 
        """
        return self.get_field_content("v051")

    @property
    def conference_sponsor(self):
                """
        conference_sponsor

        v052 {'d': 'orgdiv', '_': 'orgname'}
        """
        return self.get_field_content(
            "v052",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def conference(self):
                """
        conference

        v053 {'n': 'no'}
        """
        return self.get_field_content(
            "v053",
            subfields={'n': 'no'})

    @property
    def conference_date(self):
                """
        conference_date

        v054 {'_': 'date'}
        """
        return self.get_field_content(
            "v054",
            subfields={'_': 'date'})

    @property
    def conference_date_dateiso(self):
                """
        conference_date_dateiso

        v055 {'_': 'dateiso'}
        """
        return self.get_field_content(
            "v055",
            subfields={'_': 'dateiso'})

    @property
    def conference(self):
                """
        conference

        v056 {'e': 'state', '_': 'city'}
        """
        return self.get_field_content(
            "v056",
            subfields={'e': 'state', '_': 'city'})

    @property
    def conference_country(self):
                """
        conference_country

        v057 {'_': 'country'}
        """
        return self.get_field_content(
            "v057",
            subfields={'_': 'country'})

    @property
    def monograph_report_rsponsor(self):
                """
        monograph_report_rsponsor

        v058 {'d': 'orgdiv', '_': 'orgname'}
        """
        return self.get_field_content(
            "v058",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def monograph_report_projname(self):
                """
        monograph_report_projname

        v059 
        """
        return self.get_field_content("v059")

    @property
    def monograph_report_awarded(self):
                """
        monograph_report_awarded

        v591 {'n': 'fname', 'd': 'orgdiv', 's': 'surname', '_': 'orgname'}
        """
        return self.get_field_content(
            "v591",
            subfields={'n': 'fname', 'd': 'orgdiv', 's': 'surname', '_': 'orgname'})

    @property
    def monograph_report_no(self):
                """
        monograph_report_no

        v592 
        """
        return self.get_field_content("v592")

    @property
    def monograph_report_contract(self):
                """
        monograph_report_contract

        v060 
        """
        return self.get_field_content("v060")

    @property
    def analytic_notes(self):
                """
        analytic_notes

        v061 
        """
        return self.get_field_content("v061")

    @property
    def monograph_mpubinfo_pubname(self):
                """
        monograph_mpubinfo_pubname

        v062 
        """
        return self.get_field_content("v062")

    @property
    def monograph_edition(self):
                """
        monograph_edition

        v063 
        """
        return self.get_field_content("v063")

    @property
    def analytic_date(self):
                """
        analytic_date

        v064 
        """
        return self.get_field_content("v064")

    @property
    def analytic_date_dateiso(self):
                """
        analytic_date_dateiso

        v065 
        """
        return self.get_field_content("v065")

    @property
    def monograph(self):
                """
        monograph

        v066 {'e': 'state', '_': 'city'}
        """
        return self.get_field_content(
            "v066",
            subfields={'e': 'state', '_': 'city'})

    @property
    def monograph_country(self):
                """
        monograph_country

        v067 
        """
        return self.get_field_content("v067")

    @property
    def analytic_isbn(self):
                """
        analytic_isbn

        v069 
        """
        return self.get_field_content("v069")

    @property
    def analytic_vtitle_tp(self):
                """
        analytic_vtitle_tp

        v071 
        """
        return self.get_field_content("v071")

    @property
    def analytic_et_al(self):
                """
        analytic_et_al

        v810 {'_': 'et_al'}
        """
        return self.get_field_content(
            "v810",
            subfields={'_': 'et_al'})

    @property
    def analytic_subresp(self):
                """
        analytic_subresp

        v093 {'n': 'fname', 'r': 'role', 's': 'surname'}
        """
        return self.get_field_content(
            "v093",
            subfields={'n': 'fname', 'r': 'role', 's': 'surname'})

    @property
    def monograph_subresp(self):
                """
        monograph_subresp

        v094 {'n': 'fname', 'r': 'role', 's': 'surname'}
        """
        return self.get_field_content(
            "v094",
            subfields={'n': 'fname', 'r': 'role', 's': 'surname'})

    @property
    def monograph_version(self):
                """
        monograph_version

        v095 
        """
        return self.get_field_content("v095")

    @property
    def monograph_inpress(self):
                """
        monograph_inpress

        v096 
        """
        return self.get_field_content("v096")

    @property
    def monograph_medium(self):
                """
        monograph_medium

        v098 
        """
        return self.get_field_content("v098")

