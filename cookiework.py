class CookieWork:
    def __init__(self):
        pass

    def formatCookie(coo):
        cookieSplit = coo.split(';')
        properCookie = {}
        for i in cookieSplit:
            newI = (i.replace('=', ':', 1)).replace(' ', '')
            reSplitter = (newI.split(':', 1))
            properCookie[reSplitter[0]] = reSplitter[1]
        return properCookie

    # sends a dict of cookies into a file to allow you to play around with cookies, remove cookies and see what works
    def intoFile(coo, file):
        try:
            with open(file, 'w') as f:
                for i in coo:
                    f.write('{}: {}'.format(i, coo[i]))
                    f.write('\n')
        except FileNotFoundError:
            print('Error Opening File')
        except:
            print('Error')

    # takes in a text file of headers, formats them into a key:value pairing
    def readFile(file):
        with open(file) as f:
            header_list = []
            for line in f:
                header_list.append((line.strip('\n')).replace(':', ''))

            data_dict = {header_list[i]: header_list[i + 1] for i in range(0, len(header_list), 2)}

        return data_dict

    # redirects to read file for headers
    def get_headers(file):
        return CookieWork.readFile(file)

    # redirects to read file for cookies
    def get_cookie(file):
        return CookieWork.readFile(file)

    # outdated, takes in old format of headers
    def get_headers2(file):
        headers = {}
        with open(file) as f:

            for line in f:
                # if line.count(':') > 1:
                #     line = line.replace(':', '', 1)
                trying = line.split(' ')
                if trying[0].count(':') > 1:
                    line = line.replace(':', '', 1)

                line = (line.strip('\n'))
                line = line.split(':', 1)
                line[1] = line[1].strip(' ')
                headers[line[0]] = line[1]

        return headers
