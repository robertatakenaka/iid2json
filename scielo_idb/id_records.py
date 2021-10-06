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


class IdRecord:

    def __init__(self, record, data_dictionary):
        self._record = record
        self._data_dict = data_dictionary
        self._alt_get_tag = self._get_tag_function

    @property
    def _get_data_function(self):
        first = min(self._record.keys(), key=lambda x: len(x))
        if len(first) < 4:
            return self._get_data
        else:
            return self._get_data_3

    def get_tag_content(self, tag):
        return self._record.get(tag) or self._alt_get_tag_content(tag)

    def _get_tag_content(self, tag):
        return self._record.get("v" + str(int(tag[1:])))

    def _get_tag_content_3(self, tag):
        return self._record.get("v" + tag[1:].zfill(3))

    def get_data(self, tag, subf_and_attr=None):
        """
        Retorna os dados do campo `tag` em formato `dict`

        Exemplo:
        tag: "v10"
        name: "authors"
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
        for occ in self.get_tag_content(tag):
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
                name, subf_and_attr = self._data_dict[tag]
            except KeyError:
                name = tag
                subf_and_attr = {}
            record[name] = self.get_data(tag, subf_and_attr)
        return record

    def build_dict(self, data_dict):
        """
        Cria atributos no obj baseado em `data_dict`
        """
        record = {}
        for tag, field_info in data_dict.items():
            name, subf_and_attr = field_info
            record[name] = self.get_data(tag, subf_and_attr)
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
