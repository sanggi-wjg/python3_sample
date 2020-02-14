class PartnerApiInfo:

    def get_info(self, partnerId: str):
        dispatch = getattr(self, str(partnerId))
        return dispatch()

    def jamy(self):
        return {
            'url'    : '123',
            'timeout': 10
        }

    def baibang(self):
        return {
            'url'    : '456',
            'timeout': 10
        }


if __name__ == '__main__':
    PartnerApiInfo = PartnerApiInfo()

    api_info = PartnerApiInfo.get_info('jamy')
    print(api_info)
