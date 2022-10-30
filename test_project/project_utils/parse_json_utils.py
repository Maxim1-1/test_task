class JsonUtils:
    def get_value_json(self, data, value):

        data_response = data.get('response')

        for i in data_response:
            if isinstance(i, str):
                if value in data_response:
                    return data_response[value]
                elif isinstance(data_response[i], list):
                    return data_response[i][0][value]
            elif isinstance(i, dict):
                return i[value]
