from scielo_idb.id_records import IdRecord


class RecordTypeRECORD(IdRecord):

    def __init__(self, record, data_dictionary):
        super().__init__(record, data_dictionary)

    @property
    def field_name(self):
        return self.get_data('tag_v3')


class RecordTypeC(IdRecord):

    def __init__(self, record, data_dictionary):
        super().__init__(record, data_dictionary)

    @property
    def article_ref(self):
        return self.get_data('v000')

    @property
    def analytic_author(self):
        return self.get_data('v010')

    @property
    def monograph_update(self):
        return self.get_data('v107')

    @property
    def monograph_update_dateiso(self):
        return self.get_data('v108')

    @property
    def monograph_cited(self):
        return self.get_data('v109')

    @property
    def analytic_corpauth(self):
        return self.get_data('v011')

    @property
    def monograph_cited_dateiso(self):
        return self.get_data('v110')

    @property
    def no(self):
        return self.get_data('v118')

    @property
    def analytic_ctitle_title(self):
        return self.get_data('v012')

    @property
    def analytic_location(self):
        return self.get_data('v137')

    @property
    def analytic_pages(self):
        return self.get_data('v014')

    @property
    def monograph_author(self):
        return self.get_data('v016')

    @property
    def monograph_corpauth(self):
        return self.get_data('v017')

    @property
    def monograph_ctitle_title(self):
        return self.get_data('v018')

    @property
    def monograph_extent(self):
        return self.get_data('v020')

    @property
    def monograph_tome(self):
        return self.get_data('v022')

    @property
    def monograph_doi(self):
        return self.get_data('v237')

    @property
    def monograph_coltitle(self):
        return self.get_data('v025')

    @property
    def monograph_colvolid(self):
        return self.get_data('v026')

    @property
    def serial_author(self):
        return self.get_data('v028')

    @property
    def serial_corpauth(self):
        return self.get_data('v029')

    @property
    def analytic_volid(self):
        return self.get_data('v031')

    @property
    def serial(self):
        return self.get_data('v032')

    @property
    def serial_isstitle(self):
        return self.get_data('v033')

    @property
    def monograph_part(self):
        return self.get_data('v034')

    @property
    def serial_issn(self):
        return self.get_data('v035')

    @property
    def monograph_url(self):
        return self.get_data('v037')

    @property
    def serial_isdesig(self):
        return self.get_data('v039')

    @property
    def monograph_thesis_date(self):
        return self.get_data('v044')

    @property
    def monograph_thesis_date(self):
        return self.get_data('v045')

    @property
    def monograph_thesis(self):
        return self.get_data('v046')

    @property
    def monograph_thesis_country(self):
        return self.get_data('v047')

    @property
    def analytic_section(self):
        return self.get_data('v049')

    @property
    def monograph_thesis(self):
        return self.get_data('v050')

    @property
    def analytic_author_previous(self):
        return self.get_data('v710')

    @property
    def monograph_thesis_degree(self):
        return self.get_data('v051')

    @property
    def conference_sponsor(self):
        return self.get_data('v052')

    @property
    def conference(self):
        return self.get_data('v053')

    @property
    def conference_date(self):
        return self.get_data('v054')

    @property
    def conference_date_dateiso(self):
        return self.get_data('v055')

    @property
    def conference(self):
        return self.get_data('v056')

    @property
    def conference_country(self):
        return self.get_data('v057')

    @property
    def monograph_report_rsponsor(self):
        return self.get_data('v058')

    @property
    def monograph_report_projname(self):
        return self.get_data('v059')

    @property
    def monograph_report_awarded(self):
        return self.get_data('v591')

    @property
    def monograph_report_no(self):
        return self.get_data('v592')

    @property
    def monograph_report_contract(self):
        return self.get_data('v060')

    @property
    def analytic_notes(self):
        return self.get_data('v061')

    @property
    def monograph_mpubinfo_pubname(self):
        return self.get_data('v062')

    @property
    def monograph_edition(self):
        return self.get_data('v063')

    @property
    def analytic_date(self):
        return self.get_data('v064')

    @property
    def analytic_date_dateiso(self):
        return self.get_data('v065')

    @property
    def monograph(self):
        return self.get_data('v066')

    @property
    def monograph_country(self):
        return self.get_data('v067')

    @property
    def analytic_isbn(self):
        return self.get_data('v069')

    @property
    def analytic_vtitle_tp(self):
        return self.get_data('v071')

    @property
    def analytic_et_al(self):
        return self.get_data('v810')

    @property
    def analytic_subresp(self):
        return self.get_data('v093')

    @property
    def monograph_subresp(self):
        return self.get_data('v094')

    @property
    def monograph_version(self):
        return self.get_data('v095')

    @property
    def monograph_inpress(self):
        return self.get_data('v096')

    @property
    def monograph_medium(self):
        return self.get_data('v098')


class RecordTypeF(IdRecord):

    def __init__(self, record, data_dictionary):
        super().__init__(record, data_dictionary)

    @property
    def ccode(self):
        return self.get_data('v001')

    @property
    def authgrp_author(self):
        return self.get_data('v010')

    @property
    def authgrp_corpauth(self):
        return self.get_data('v011')

    @property
    def history_received(self):
        return self.get_data('v111')

    @property
    def history_received_dateiso(self):
        return self.get_data('v112')

    @property
    def history_accepted(self):
        return self.get_data('v113')

    @property
    def history_accepted_dateiso(self):
        return self.get_data('v114')

    @property
    def history_revised(self):
        return self.get_data('v115')

    @property
    def history_revised_dateiso(self):
        return self.get_data('v116')

    @property
    def biblist_head_standard(self):
        return self.get_data('v117')

    @property
    def title(self):
        return self.get_data('v012')

    @property
    def version(self):
        return self.get_data('v120')

    @property
    def order(self):
        return self.get_data('v121')

    @property
    def toccode(self):
        return self.get_data('v123')

    @property
    def supplvol(self):
        return self.get_data('v131')

    @property
    def supplno(self):
        return self.get_data('v132')

    @property
    def figgrp(self):
        return self.get_data('v141')

    @property
    def table(self):
        return self.get_data('v142')

    @property
    def sponsor(self):
        return self.get_data('v158')

    @property
    def pii(self):
        return self.get_data('v002')

    @property
    def ahpdate(self):
        return self.get_data('v223')

    @property
    def rvpdate(self):
        return self.get_data('v224')

    @property
    def old_pid(self):
        return self.get_data('v225')

    @property
    def doi(self):
        return self.get_data('v237')

    @property
    def url(self):
        return self.get_data('v238')

    @property
    def product(self):
        return self.get_data('v241')

    @property
    def hcomment(self):
        return self.get_data('v250')

    @property
    def deposit_embdate(self):
        return self.get_data('v264')

    @property
    def deposit_entrdate(self):
        return self.get_data('v265')

    @property
    def deposit_deposid(self):
        return self.get_data('v268')

    @property
    def issuegrp_volid(self):
        return self.get_data('v031')

    @property
    def issuegrp_issueno(self):
        return self.get_data('v032')

    @property
    def issn(self):
        return self.get_data('v035')

    @property
    def type(self):
        return self.get_data('v038')

    @property
    def language(self):
        return self.get_data('v040')

    @property
    def isidpart(self):
        return self.get_data('v041')

    @property
    def status(self):
        return self.get_data('v042')

    @property
    def thesis_date(self):
        return self.get_data('v044')

    @property
    def thesis_date_dateiso(self):
        return self.get_data('v045')

    @property
    def thesis(self):
        return self.get_data('v046')

    @property
    def thesis_country(self):
        return self.get_data('v047')

    @property
    def seccode(self):
        return self.get_data('v049')

    @property
    def thesis(self):
        return self.get_data('v050')

    @property
    def thesis_degree(self):
        return self.get_data('v051')

    @property
    def conference_sponsor(self):
        return self.get_data('v052')

    @property
    def conference(self):
        return self.get_data('v053')

    @property
    def conference_date(self):
        return self.get_data('v054')

    @property
    def license(self):
        return self.get_data('v540')

    @property
    def conference_date_dateiso(self):
        return self.get_data('v055')

    @property
    def conference(self):
        return self.get_data('v056')

    @property
    def conference_country(self):
        return self.get_data('v057')

    @property
    def projgrp_psponsor(self):
        return self.get_data('v058')

    @property
    def projgrp_projname(self):
        return self.get_data('v059')

    @property
    def report_awarded(self):
        return self.get_data('v591')

    @property
    def report_no(self):
        return self.get_data('v592')

    @property
    def projgrp_psponsor_contract(self):
        return self.get_data('v060')

    @property
    def issuegrp_date(self):
        return self.get_data('v064')

    @property
    def dateiso(self):
        return self.get_data('v065')

    @property
    def aff(self):
        return self.get_data('v070')

    @property
    def doctopic(self):
        return self.get_data('v071')

    @property
    def biblist_head_count(self):
        return self.get_data('v072')

    @property
    def keygrp_dperiod(self):
        return self.get_data('v074')

    @property
    def cltrial(self):
        return self.get_data('v770')

    @property
    def abstract(self):
        return self.get_data('v083')

    @property
    def keygrp(self):
        return self.get_data('v085')

    @property
    def fpage(self):
        return self.get_data('v914')

    @property
    def lpage(self):
        return self.get_data('v915')

