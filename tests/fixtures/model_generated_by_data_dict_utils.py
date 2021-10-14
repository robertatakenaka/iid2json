from iid2json.meta_record import MetaRecord


class RecordTypeRECORD(MetaRecord):

    def __init__(
            self, record, no_repetition_tags=None, no_subfield_tags=None,
            data_dictionary=None):
        super().__init__(
            record, no_repetition_tags, no_subfield_tags, data_dictionary)

    @property
    def field_name(self):
        return self.get_field_content(
            "tag",
            subfields={'subfield': 'subfield_name'},
            no_repetition=True,
            no_subfield=True)


class RecordTypeC(MetaRecord):

    def __init__(
            self, record, no_repetition_tags=None, no_subfield_tags=None,
            data_dictionary=None):
        super().__init__(
            record, no_repetition_tags, no_subfield_tags, data_dictionary)

    @property
    def article_ref(self):
        return self.get_field_content("v000")

    @property
    def analytic_author(self):
        return self.get_field_content(
            "v010",
            subfields={'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname', '_': 'anonym'})

    @property
    def monograph_update(self):
        return self.get_field_content("v107")

    @property
    def monograph_update_dateiso(self):
        return self.get_field_content("v108")

    @property
    def monograph_cited(self):
        return self.get_field_content("v109")

    @property
    def analytic_corpauth(self):
        return self.get_field_content(
            "v011",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def monograph_cited_dateiso(self):
        return self.get_field_content("v110")

    @property
    def no(self):
        return self.get_field_content("v118")

    @property
    def analytic_ctitle_title(self):
        return self.get_field_content(
            "v012",
            subfields={'l': 'language', '_': 'title'})

    @property
    def analytic_location(self):
        return self.get_field_content("v137")

    @property
    def analytic_pages(self):
        return self.get_field_content("v014")

    @property
    def monograph_author(self):
        return self.get_field_content(
            "v016",
            subfields={'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname', '_': 'anonym'})

    @property
    def monograph_corpauth(self):
        return self.get_field_content(
            "v017",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def monograph_ctitle_title(self):
        return self.get_field_content(
            "v018",
            subfields={'l': 'language', '_': 'title'})

    @property
    def monograph_extent(self):
        return self.get_field_content("v020")

    @property
    def monograph_tome(self):
        return self.get_field_content("v022")

    @property
    def monograph_doi(self):
        return self.get_field_content("v237")

    @property
    def monograph_coltitle(self):
        return self.get_field_content("v025")

    @property
    def monograph_colvolid(self):
        return self.get_field_content("v026")

    @property
    def serial_author(self):
        return self.get_field_content(
            "v028",
            subfields={'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname'})

    @property
    def serial_corpauth(self):
        return self.get_field_content(
            "v029",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def analytic_volid(self):
        return self.get_field_content("v031")

    @property
    def serial(self):
        return self.get_field_content(
            "v032",
            subfields={'s': 'suppl'})

    @property
    def serial_isstitle(self):
        return self.get_field_content("v033")

    @property
    def monograph_part(self):
        return self.get_field_content("v034")

    @property
    def serial_issn(self):
        return self.get_field_content("v035")

    @property
    def monograph_url(self):
        return self.get_field_content("v037")

    @property
    def serial_isdesig(self):
        return self.get_field_content("v039")

    @property
    def monograph_thesis_date(self):
        return self.get_field_content("v044")

    @property
    def monograph_thesis_date(self):
        return self.get_field_content("v045")

    @property
    def monograph_thesis(self):
        return self.get_field_content(
            "v046",
            subfields={'e': 'state', '_': 'city'})

    @property
    def monograph_thesis_country(self):
        return self.get_field_content("v047")

    @property
    def analytic_section(self):
        return self.get_field_content("v049")

    @property
    def monograph_thesis(self):
        return self.get_field_content(
            "v050",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def analytic_author_previous(self):
        return self.get_field_content(
            "v710",
            subfields={'_': 'previous'})

    @property
    def monograph_thesis_degree(self):
        return self.get_field_content("v051")

    @property
    def conference_sponsor(self):
        return self.get_field_content(
            "v052",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def conference(self):
        return self.get_field_content(
            "v053",
            subfields={'n': 'no'})

    @property
    def conference_date(self):
        return self.get_field_content(
            "v054",
            subfields={'_': 'date'})

    @property
    def conference_date_dateiso(self):
        return self.get_field_content(
            "v055",
            subfields={'_': 'dateiso'})

    @property
    def conference(self):
        return self.get_field_content(
            "v056",
            subfields={'e': 'state', '_': 'city'})

    @property
    def conference_country(self):
        return self.get_field_content(
            "v057",
            subfields={'_': 'country'})

    @property
    def monograph_report_rsponsor(self):
        return self.get_field_content(
            "v058",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def monograph_report_projname(self):
        return self.get_field_content("v059")

    @property
    def monograph_report_awarded(self):
        return self.get_field_content(
            "v591",
            subfields={'n': 'fname', 'd': 'orgdiv', 's': 'surname', '_': 'orgname'})

    @property
    def monograph_report_no(self):
        return self.get_field_content("v592")

    @property
    def monograph_report_contract(self):
        return self.get_field_content("v060")

    @property
    def analytic_notes(self):
        return self.get_field_content("v061")

    @property
    def monograph_mpubinfo_pubname(self):
        return self.get_field_content("v062")

    @property
    def monograph_edition(self):
        return self.get_field_content("v063")

    @property
    def analytic_date(self):
        return self.get_field_content("v064")

    @property
    def analytic_date_dateiso(self):
        return self.get_field_content("v065")

    @property
    def monograph(self):
        return self.get_field_content(
            "v066",
            subfields={'e': 'state', '_': 'city'})

    @property
    def monograph_country(self):
        return self.get_field_content("v067")

    @property
    def analytic_isbn(self):
        return self.get_field_content("v069")

    @property
    def analytic_vtitle_tp(self):
        return self.get_field_content("v071")

    @property
    def analytic_et_al(self):
        return self.get_field_content(
            "v810",
            subfields={'_': 'et_al'})

    @property
    def analytic_subresp(self):
        return self.get_field_content(
            "v093",
            subfields={'n': 'fname', 'r': 'role', 's': 'surname'})

    @property
    def monograph_subresp(self):
        return self.get_field_content(
            "v094",
            subfields={'n': 'fname', 'r': 'role', 's': 'surname'})

    @property
    def monograph_version(self):
        return self.get_field_content("v095")

    @property
    def monograph_inpress(self):
        return self.get_field_content("v096")

    @property
    def monograph_medium(self):
        return self.get_field_content("v098")


class RecordTypeF(MetaRecord):

    def __init__(
            self, record, no_repetition_tags=None, no_subfield_tags=None,
            data_dictionary=None):
        super().__init__(
            record, no_repetition_tags, no_subfield_tags, data_dictionary)

    @property
    def ccode(self):
        return self.get_field_content("v001")

    @property
    def authgrp_author(self):
        return self.get_field_content(
            "v010",
            subfields={'n': 'fname', '1': 'rid', 'r': 'role', 's': 'surname'})

    @property
    def authgrp_corpauth(self):
        return self.get_field_content(
            "v011",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def history_received(self):
        return self.get_field_content("v111")

    @property
    def history_received_dateiso(self):
        return self.get_field_content("v112")

    @property
    def history_accepted(self):
        return self.get_field_content("v113")

    @property
    def history_accepted_dateiso(self):
        return self.get_field_content("v114")

    @property
    def history_revised(self):
        return self.get_field_content("v115")

    @property
    def history_revised_dateiso(self):
        return self.get_field_content("v116")

    @property
    def biblist_head_standard(self):
        return self.get_field_content("v117")

    @property
    def title(self):
        return self.get_field_content(
            "v012",
            subfields={'l': 'language', '_': 'title'})

    @property
    def version(self):
        return self.get_field_content("v120")

    @property
    def order(self):
        return self.get_field_content("v121")

    @property
    def toccode(self):
        return self.get_field_content("v123")

    @property
    def supplvol(self):
        return self.get_field_content("v131")

    @property
    def supplno(self):
        return self.get_field_content("v132")

    @property
    def figgrp(self):
        return self.get_field_content(
            "v141",
            subfields={'r': 'figref', 'm': 'legend', 'n': 'no', 's': 'subtitle', 't': 'title', 'l': 'language'})

    @property
    def table(self):
        return self.get_field_content(
            "v142",
            subfields={'m': 'legend', 'n': 'no', 's': 'subtitle', 't': 'title', 'l': 'language'})

    @property
    def sponsor(self):
        return self.get_field_content("v158")

    @property
    def pii(self):
        return self.get_field_content("v002")

    @property
    def ahpdate(self):
        return self.get_field_content("v223")

    @property
    def rvpdate(self):
        return self.get_field_content("v224")

    @property
    def old_pid(self):
        return self.get_field_content("v225")

    @property
    def doi(self):
        return self.get_field_content("v237")

    @property
    def url(self):
        return self.get_field_content("v238")

    @property
    def product(self):
        return self.get_field_content(
            "v241",
            subfields={'t': 'reltype', 'i': 'relid', 'z': 'relidtp'})

    @property
    def hcomment(self):
        return self.get_field_content("v250")

    @property
    def deposit_embdate(self):
        return self.get_field_content("v264")

    @property
    def deposit_entrdate(self):
        return self.get_field_content("v265")

    @property
    def deposit_deposid(self):
        return self.get_field_content("v268")

    @property
    def issuegrp_volid(self):
        return self.get_field_content("v031")

    @property
    def issuegrp_issueno(self):
        return self.get_field_content("v032")

    @property
    def issn(self):
        return self.get_field_content("v035")

    @property
    def type(self):
        return self.get_field_content("v038")

    @property
    def language(self):
        return self.get_field_content("v040")

    @property
    def isidpart(self):
        return self.get_field_content("v041")

    @property
    def status(self):
        return self.get_field_content("v042")

    @property
    def thesis_date(self):
        return self.get_field_content("v044")

    @property
    def thesis_date_dateiso(self):
        return self.get_field_content("v045")

    @property
    def thesis(self):
        return self.get_field_content(
            "v046",
            subfields={'e': 'state', '_': 'city'})

    @property
    def thesis_country(self):
        return self.get_field_content("v047")

    @property
    def seccode(self):
        return self.get_field_content("v049")

    @property
    def thesis(self):
        return self.get_field_content(
            "v050",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def thesis_degree(self):
        return self.get_field_content("v051")

    @property
    def conference_sponsor(self):
        return self.get_field_content(
            "v052",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def conference(self):
        return self.get_field_content(
            "v053",
            subfields={'n': 'no'})

    @property
    def conference_date(self):
        return self.get_field_content(
            "v054",
            subfields={'_': 'date'})

    @property
    def license(self):
        return self.get_field_content(
            "v540",
            subfields={'u': 'href', 'l': 'language', 't': 'lictype', '_': 'licensep'})

    @property
    def conference_date_dateiso(self):
        return self.get_field_content(
            "v055",
            subfields={'_': 'dateiso'})

    @property
    def conference(self):
        return self.get_field_content(
            "v056",
            subfields={'e': 'state', '_': 'city'})

    @property
    def conference_country(self):
        return self.get_field_content(
            "v057",
            subfields={'_': 'country'})

    @property
    def projgrp_psponsor(self):
        return self.get_field_content(
            "v058",
            subfields={'d': 'orgdiv', '_': 'orgname'})

    @property
    def projgrp_projname(self):
        return self.get_field_content("v059")

    @property
    def report_awarded(self):
        return self.get_field_content(
            "v591",
            subfields={'n': 'fname', 'd': 'orgdiv', 's': 'surname', '_': 'orgname'})

    @property
    def report_no(self):
        return self.get_field_content("v592")

    @property
    def projgrp_psponsor_contract(self):
        return self.get_field_content("v060")

    @property
    def issuegrp_date(self):
        return self.get_field_content("v064")

    @property
    def dateiso(self):
        return self.get_field_content("v065")

    @property
    def aff(self):
        return self.get_field_content(
            "v070",
            subfields={'c': 'city', 'p': 'country', 'e': 'email', 'i': 'id', '1': 'orgdiv1', '2': 'orgdiv2', '3': 'orgdiv3', 'd': 'orgdiv', 's': 'state', 'z': 'zipcode', '_': 'orgname'})

    @property
    def doctopic(self):
        return self.get_field_content(
            "v071",
            no_repetition=True,
            no_subfield=True)

    @property
    def biblist_head_count(self):
        return self.get_field_content("v072")

    @property
    def keygrp_dperiod(self):
        return self.get_field_content(
            "v074",
            subfields={'f': 'from', 't': 'to'})

    @property
    def cltrial(self):
        return self.get_field_content(
            "v770",
            subfields={'a': 'ctreg', 'u': 'cturl', '_': 'ctdbid'})

    @property
    def v083(self):
        return self.get_field_content(
            "v083",
            subfields={'a': 'abstract', 'l': 'language'})

    @property
    def keygrp(self):
        return self.get_field_content(
            "v085",
            subfields={'k': 'keyword', 'd': 'scheme', 's': 'subkey', 'l': 'language', 't': 'type', '_': 'rid'})

    @property
    def fpage(self):
        return self.get_field_content("v914")

    @property
    def lpage(self):
        return self.get_field_content("v915")

