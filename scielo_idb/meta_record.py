def build_object(obj, record_as_dict):
    """
    Cria atributos no obj baseado em `data_dict`
    """
    for name, data in record_as_dict.items():
        print(name)
        setattr(obj, name, data)


class MetaRecord:

    def __init__(self, record):
        self._record = record

    @property
    def rec_type(self):
        try:
            return self._record.get("v706")[0]["_"]
        except:
            return

    def get_data_as_dict(self, tag, field_name, subfields):
        """
        Retorna os dados do campo `tag` em formato `dict`

        Exemplo:
        tag: "v010"
        field_name: "authors"
        subfields:
        {
            "s": "surname",
            "n": "given-names",
            "r": "role",
        }
        Returns
        ```
        {"authors":
            {"surname": "", "given-names": "", "role": ""},
            {"surname": "", "given-names": "", "role": ""},
            {"surname": "", "given-names": "", "role": ""},
        }
        ```
        """
        return {field_name: self._get_occs(tag, subfields)}

    def _get_occs(self, tag, subfields):
        _occs = []
        for occ in self._record.get(tag) or []:
            value = self._get_occ(occ, subfields)
            if not value:
                continue
            try:
                if len(value.items()) == 1:
                    value = value["_"]
            except KeyError:
                pass
            _occs.append(value)
        if len(_occs) == 1 and not isinstance(_occs[0], dict):
            return _occs[0]
        return _occs

    def _get_occ(self, occ, subfields):
        return {
            subfields.get(subf_char) or subf_char: subf_name
            for subf_char, subf_name in occ.items()
        }

    def get_record_as_dict(self, data_dict={}):
        """
        Retorna o conteúdo de registro em formato de objeto
        """
        record = {}
        for tag in self._record.keys():
            try:
                template = data_dict[tag]
            except KeyError:
                # print(tag, data_dict.keys())
                field_name = tag
                subfields = {}
            else:
                field_name = template["field_name"]
                subfields = template["subfields"]
            record.update(self.get_data_as_dict(tag, field_name, subfields))
        return record
