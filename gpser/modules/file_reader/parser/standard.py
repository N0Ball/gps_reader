from ..base import FReader

class Standard(FReader):

    _HEADER: list = []

    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    @property
    def HEADER(self) -> list:
        return self._HEADER

    @property
    def DATA(self) -> list:
        return self._PARSED_DATA

    def _parser(self):
        split_data = self._RAW_DATA.split(' \n')
        header = split_data[0].split()
        datas = split_data[1:]

        data_frame = self._create_data_frame(header)

        for data in datas:
            for dt, h in zip(data.split(), header):

                if dt == 0:
                    continue

                data_frame[h].append(self._check_data(dt))

        self._HEADER = header
        return data_frame

    def _check_data(self, data: str):

        try:
            return int(data)
        except ValueError:
            pass

        try:
            return float(data)
        except ValueError:
            pass

        return data

    def _create_data_frame(self, header: list) -> dict:
        
        new_data_frame = {}

        for e in header:
            new_data_frame.update({e: []})

        return new_data_frame