if __name__ == '__main__':

    try:
        raise TypeError('HA HA HA TEST TypeError')
        # raise Exception('HA HA HA TEST Exception')

    except (Exception, TypeError, NameError) as e:
        print('@e.args@', e.args)

        if isinstance(e, TypeError):
            print('ok, is TypeError')

        elif isinstance(e, Exception):
            print('ok, is Exception')
        else:
            print('not ok')
