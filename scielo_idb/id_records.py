def _get_value(data, tag):
    """
    Returns first value of field `tag`
    """
    # data['v880'][0]['_']
    try:
        return data[tag][0]['_']
    except (KeyError, IndexError):
        return None


def _get_items(data, tag):
    """
    Returns first value of field `tag`
    """
    # data['v880'][0]['_']
    try:
        return [item['_'] for item in data[tag]]
    except KeyError:
        return None


class Record:

    def __init__(self, rec_type):
        self._rec_type = rec_type

    @property
    def rec_type(self):
        return self._rec_type


class IdRecord:

    def __init__(self, record, data_dictionary):
        self._record = record
        self._data_dict = data_dictionary
        if self.rec_type:
            try:
                self._data_dict = data_dictionary[self.rec_type]
            except KeyError:
                self._data_dict = data_dictionary

    @property
    def rec_type(self):
        try:
            return self._record.get("v706")[0]["_"]
        except:
            return

    def get_data(self, tag):
        """
        Retorna os dados do campo `tag` em formato `dict`

        Exemplo:
        tag: "v010"

        subf_and_attr:
        {
            "s": "surname",
            "n": "given-names",
            "r": "role",
        }
        Returns generator of
        ```
        [
            {"surname": "", "given-names": "", "role": ""},
            {"surname": "", "given-names": "", "role": ""},
            {"surname": "", "given-names": "", "role": ""},
        ]
        ```
        """
        try:
            template = self._data_dict[tag]
        except KeyError:
            subf_and_attr = {}
        else:
            subf_and_attr = template["subfields"]

        for occ in self._record.get(tag):
            item = self.get_occ(occ, subf_and_attr)
            if item:
                yield item

    def get_occ(self, occ, subf_and_attr):
        value = {
            subf_and_attr.get(subf) or subf: val
            for subf, val in occ.items()
        }
        if len(value.items()) > 1:
            return value
        try:
            return value["_"]
        except KeyError:
            return value

    def get_record_as_dict(self):
        """
        Retorna o conteúdo de registro em formato de objeto
        """
        record = {}
        for tag in self._record.keys():
            try:
                template = self._data_dict[tag]
            except KeyError:
                field_name = tag
            else:
                field_name = template["tag_v3"]
            record[field_name] = self.get_data(tag)
        return record

    def build_dict(self, data_dict):
        """
        Cria atributos no obj baseado em `data_dict`
        """
        record = {}
        for tag, template in data_dict.items():
            field_name = template["field_name"]
            subf_and_attr = template["subfields"]
            record[field_name] = self.get_data(tag, subf_and_attr)
        return record

    def get_record_as_object(self, obj):
        """
        Retorna o conteúdo de registro em formato de objeto
        """
        for name, data in self.get_record_as_dict():
            setattr(obj, name, data)

    def build_object(self, obj, data_dict):
        """
        Cria atributos no obj baseado em `data_dict`
        """
        for name, data in self.build_dict(data_dict):
            setattr(obj, name, data)
