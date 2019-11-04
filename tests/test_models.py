# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from hashlib import md5
import os

from unittest import TestCase

from pybrreg.models import new_inquiry, sdo, manifest, recipients, application_receipt, decree, package
from pybrreg.xml import generated

from .common_testdata import BrregTestPackage


def get_test_file(folder, xml_file):
    base_path = os.path.dirname(os.path.realpath(__name__))
    xml_path = os.path.join('tests', 'test_files', folder, xml_file)
    file_path = os.path.join(base_path, xml_path)
    with open(file_path, 'r') as xml_file:
        file_data = xml_file.read()
    return file_data


class BrregNewInquiryTests(TestCase):

    def setUp(self):
        self.decree = get_test_file('vedtak', 'vedtak_melding_m_vedlegg.xml')
        self.application_receipt = get_test_file('applikasjonskvittering', 'melding_henvendelse.xml')
        self.sdo_inquiry_data = {
            'id': '62f3084d-a7ab-425b-a8cb-06c35f28a799',
            'recipient': {
                'id': '974760673',
                'id_type': 'orgnr',
            },
            'sender': {
                'id': '910731718',
                'id_type': 'orgnr',
            },
            'service_action': 'endring',
            'content': {
                'data': '<?xml version="1.0" encoding="utf-8"?><SDO xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schema.brreg.no/postmottak/frivintVerifisertMelding"><SignedObject>PGludGVncmFzam9uRVJGViB4bWxuczp4c2Q9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIiB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4bWxucz0iaHR0cDovL3NjaGVtYS5icnJlZy5uby9pbnRlZi9pbnRlZ3Jhc2pvbkVSRlYiPjxoZWFkZXIgTWVsZGluZ3NEYXRvPSIyMDE2LTExLTE2Ij48U0xzeXNJZD4xMDAxPC9TTHN5c0lkPjxTTHN5c01lbGRpbmdzSWQ+MjAyMTAtMTcwNzwvU0xzeXNNZWxkaW5nc0lkPjxzYWtzdHlwZT48aG92ZWRzYWtzdHlwZT5FPC9ob3ZlZHNha3N0eXBlPjx1bmRlcnNha3N0eXBlPkVOPC91bmRlcnNha3N0eXBlPjwvc2Frc3R5cGU+PG9yZ2FuaXNhc2pvbnNudW1tZXI+OTc2MDMzMjA1PC9vcmdhbmlzYXNqb25zbnVtbWVyPjxvcmdhbmlzYXNqb25zZm9ybT48b3JnZm9ybT5GTEk8L29yZ2Zvcm0+PC9vcmdhbmlzYXNqb25zZm9ybT48c3RhdHVzPjxFUnN0YXR1cz5OPC9FUnN0YXR1cz48RlZzdGF0dXM+SjwvRlZzdGF0dXM+PC9zdGF0dXM+PC9oZWFkZXI+PG1lbGRpbmc+PGthdGVnb3JpIGluZm9UeXBlPSJLQVRHIiByZWdpc3Rlcj0iRlYiPjxrb2RlPjExMDA8L2tvZGU+PHJhbmdlcmluZz4xPC9yYW5nZXJpbmc+PC9rYXRlZ29yaT48dmVkbGVnZz48dmVkbGVnZ3NUeXBlPkFOTlQ8L3ZlZGxlZ2dzVHlwZT48L3ZlZGxlZ2c+PHZlZGxlZ2c+PHZlZGxlZ2dzVHlwZT5QQUFSPC92ZWRsZWdnc1R5cGU+PC92ZWRsZWdnPjxzaWduZXJlcj4yNjEyOTMwODAzNTwvc2lnbmVyZXI+PC9tZWxkaW5nPjwvaW50ZWdyYXNqb25FUkZWPg==</SignedObject><Signatures><SignatureRecord><SignedObjectHash algorithm="SHA-256">8qdmj4vEjlmbwYe9SLT66+Z4y51nOw8LJ0dT9KofeyE=</SignedObjectHash><Authentication>PHNhbWw6QXNzZXJ0aW9uIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDphc3NlcnRpb24iIElEPSJzMjk4NDY3NWNhZjE2NDkzOTY4MGJkYWUxZmVlZjFkMzNlZjhiMzFiODYiIElzc3VlSW5zdGFudD0iMjAxNi0xMS0xNlQwOTo0MzoxM1oiIFZlcnNpb249IjIuMCI+CjxzYW1sOklzc3Vlcj5pZHBvcnRlbi12ZXIxLmRpZmkubm8tdjM8L3NhbWw6SXNzdWVyPjxkczpTaWduYXR1cmUgeG1sbnM6ZHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvMDkveG1sZHNpZyMiPjxkczpTaWduZWRJbmZvPjxkczpDYW5vbmljYWxpemF0aW9uTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIiAvPjxkczpTaWduYXR1cmVNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjcnNhLXNoYTEiIC8+PzOlJlZmVyZW5jZSBVUkk9IiNzMjk4NDY3NWNhZjE2NDkzOTY4MGJkYWUxZmVlZjFkMzNlZjhiMzFiODYiPjxkczpUcmFuc2Zvcm1zPjxkczpUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSIgLz48ZHM6VHJhbnNmb3JtIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS8xMC94bWwtZXhjLWMxNG4jIiAvPjwvZHM6VHJhbnNmb3Jtcz48ZHM6RGlnZXN0TWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3NoYTEiIC8+PGRzOkRpZ2VzdFZhbHVlPkp0OVdtNVE5bWFDejJVODVlOFJzbmVMREtaYz08L2RzOkRpZ2VzdFZhbHVlPjwvZHM6UmVmZXJlbmNlPjwvZHM6U2lnbmVkSW5mbz48ZHM6U2lnbmF0dXJlVmFsdWU+N0FDN3MrOWZSVnluaTZWSXR6T1NUaUNYRnE5K0JMVVUyNTVGc0NkMW4yeVhUNVBmVk5DbFNoK29TMHlOUWFSSmFrZnZqMFU1dFp1UGRTazBURkhJTDlQdmV2czJpQnBhYkE3enpuMDVWNE15dGh0ZE9WM3JNbWFRVHl3RGFiUGkzQTJQUDM3U0RhRWU1bXVHVFo0ekxFL0dqMXBGdDlFN0Nxb2ZhVzZkZHE3MEZNcXVtRDFWUjFLZWhvYngxTUJVT3hGN1VIZVJBZXA1THhobFN5ZFZ0akk5elRTMXp2ZktYVG83aU1PVWJFUTJ6V210dDJGZDdBRVdGN2ROLzJvamlyUHM4dFJjbW5JTjN2QnlwUGZacGozeWs5VDEwSHpFYjhrYWNWelpSZDcrdHpFZ2VwV1lBbXQyTFJnSkxSYjhoaTdvdTdRNmJ6bkwrRlA2SDVaemJnPT08L2RzOlNpZ25hdHVyZVZhbHVlPjxkczpLZXlJbmZvPjxkczpYNTA5RGF0YT48ZHM6WDUwOUNlcnRpZmljYXRlPk1JSUZEekNDQS9lZ0F3SUJBZ0lMQ0ROV1R2SlBidkxQekZRd0RRWUpLb1pJaHZjTkFRRUxCUUF3U3pFTE1Ba0dBMVVFQmhNQ1RrOHhIVEFiQmdOVkJBb01GRUoxZVhCaGMzTWdRVk10T1Rnek1UWXpNekkzTVIwd0d3WURWUVFEREJSQ2RYbHdZWE56SUVOc1lYTnpJRE1nUTBFZ016QWVGdzB4TlRFeU1ETXhNekU0TkRoYUZ3MHhPVEF6TWpBeU1qVTVNREJhTUlHaU1Rc3dDUVlEVlFRR0V3Sk9UekVzTUNvR0ExVUVDZ3dqUkVsU1JVdFVUMUpCVkVWVUlFWlBVaUJHVDFKV1FVeFVUa2xPUnlCUFJ5QkpTMVF4SXpBaEJnTlZCQXNNR2tsRUxYQnZjblJsYmk5TFVsSWdkbVZ5YVdacGEyRnphbTl1TVN3d0tnWURWUVFERENORVNWSkZTMVJQVWtGVVJWUWdSazlTSUVaUFVsWkJURlJPU1U1SElFOUhJRWxMVkRFU01CQUdBMVVFQlJNSk9Ua3hPREkxT0RJM01JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBN0YwQjFpVkRGUzRhN29RZVpsbG1YeVAyVzY1ZEpZaE5xSHhjcUREeDBJYTZWSjhBUi9UMEdLMjVKRmU4ZTVRMlY2TDM0OWVsaUEwSEtIeGhKd25HWEw5K0Q4K2EvclBEa2tZK1VMSGFoRzBQRlFDQTNhczhNRWtKOHMwVGEzWGRmWnpmbHRzV0VhWHM5T3JsYmFmQ1NiS1lUOUkxaFB0T2pyUk5TTDdwd1dFMmd6MG1VYno0eEZnVDdKUk5yMlpuR1dTeVNjcVoxcms1QjJYZ3BnVnlrSGdPWHVtZjY0NmZSSGRsMnFZTllWR0ZlYWsxc1B4L0g3OVI2ajRvQmhIODZ0Zm9WOGVjWlJ3emRMNlZYQXRlYkxqbzhNYkFYcktMeXVxRCsvbGEreW5uRktyZjJGM2xxRmV1VDhjbVZ6cms3bTNyY0VBNUd3cUU2bkk2Wk12cGp3SURBUUFCbzRJQm1qQ0NBWll3Q1FZRFZSMFRCQUl3QURBZkJnTlZIU01FR0RBV2dCVE13L2dIdDV4dGVrNzFweXNkQmZtelJ4eVIwVEFkQmdOVkhRNEVGZ1FVSGhqbDl6alF4Si9rSkt5WWpRdk44SEtDNGxrd0RnWURWUjBQQVFIL0JBUURBZ1N3TUJVR0ExVWRJQVFPTUF3d0NnWUlZSVJDQVJvQkF3SXdnYVVHQTFVZEh3U0JuVENCbWpBdm9DMmdLNFlwYUhSMGNEb3ZMMk55YkM1aWRYbHdZWE56TG01dkwyTnliQzlDVUVOc1lYTnpNME5CTXk1amNtd3daNkJsb0dPR1lXeGtZWEE2THk5c1pHRndMbUoxZVhCaGMzTXVibTh2WkdNOVFuVjVjR0Z6Y3l4a1l6MU9UeXhEVGoxQ2RYbHdZWE56SlRJd1EyeGhjM01sTWpBekpUSXdRMEVsTWpBelAyTmxjblJwWm1sallYUmxVbVYyYjJOaGRHbHZia3hwYzNRd2VnWUlLd1lCQlFVSEFRRUViakJzTURNR0NDc0dBUVVGQnpBQmhpZG9kSFJ3T2k4dmIyTnpjQzVpZFhsd1lYTnpMbTV2TDI5amMzQXZRbEJEYkdGemN6TkRRVE13TlFZSUt3WUJCUVVITUFLR0tXaDBkSEE2THk5amNuUXVZblY1Y0dGemN5NXVieTlqY25RdlFsQkRiR0Z6Y3pORFFUTXVZMlZ5TUEwR0NTcUdTSWIzRFFFQkN3VUFBNElCQVFCWkVSNmZVcXQ4ZlUrY0J5ak5aZDlCNTZ4QWdVTGJSRjdPMHVQNG5mRFlZVkhqakxpZ2JPNlhwNWJpWkllN042eDN1MzkwU1RIV0YxaGplRFVaOGVwNHUzY08wYndLSHNka3JwL0pJV1E2cThQcElKSGNDRHJ6L3RJS24ySkxweGJRZTlBUjZLV0REemdmeVJ4b0N5dWxPY25Yb1ZIK0NlU2ZpZVEzV2FwUjVWeW14cFBEQStqQzZmY2NQZkJEcEtyT3NvNFdwRkZ2d0pieUVoeERBZ0pBWHp3eDFSNUpGb3BCS1d0YTFiZDZhUzcva1pZZWFKamV5OU1udkNSQ05aZTcycFIrbEhUK3FCLzBON2t6MjdlUWEyZ1ZTM2xHUXA3Tjg3QlB2RnZWSzZQYmptTTBLY2J4K0QzMTJaRjJwQjZGM0NyVEZBZmt1OGNjazBoM3Y1RTQ8L2RzOlg1MDlDZXJ0aWZpY2F0ZT48L2RzOlg1MDlEYXRhPjwvZHM6S2V5SW5mbz48L2RzOlNpZ25hdHVyZT48c2FtbDpTdWJqZWN0Pgo8c2FtbDpOYW1lSUQgRm9ybWF0PSJ1cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6bmFtZWlkLWZvcm1hdDp0cmFuc2llbnQiIE5hbWVRdWFsaWZpZXI9ImlkcG9ydGVuLXZlcjEuZGlmaS5uby12MyIgU1BOYW1lUXVhbGlmaWVyPSJzYWxvY2FsLm5pZi5ubyI+RU9jdjZWT0RrWFVEY1hCalVxSmE3ZTFHRDdZdjwvc2FtbDpOYW1lSUQ+PHNhbWw6U3ViamVjdENvbmZpcm1hdGlvbiBNZXRob2Q9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpjbTpiZWFyZXIiPgo8c2FtbDpTdWJqZWN0Q29uZmlybWF0aW9uRGF0YSBJblJlc3BvbnNlVG89Il80OGI1NTE0Yy01MTIwLTQwODEtODYyYy04OTgzZWZjM2Q0OWMiIE5vdE9uT3JBZnRlcj0iMjAxNi0xMS0xNlQwOTo1MzoxM1oiIFJlY2lwaWVudD0iaHR0cHM6Ly9sb2NhbGhvc3Qvc3BvcnRzYWRtaW4vTXZjNS9CcnJlZ1VwZGF0ZS9Bc3NlcnRpb25SZXNwb25zZSIgLz48L3NhbWw6U3ViamVjdENvbmZpcm1hdGlvbj4KPC9zYW1sOlN1YmplY3Q+PHNhbWw6Q29uZGl0aW9ucyBOb3RCZWZvcmU9IjIwMTYtMTEtMTZUMDk6MzM6MTNaIiBOb3RPbk9yQWZ0ZXI9IjIwMTYtMTEtMTZUMDk6NTM6MTNaIj4KPHNhbWw6QXVkaWVuY2VSZXN0cmljdGlvbj4KPHNhbWw6QXVkaWVuY2U+c2Fsb2NhbC5uaWYubm88L3NhbWw6QXVkaWVuY2U+Cjwvc2FtbDpBdWRpZW5jZVJlc3RyaWN0aW9uPgo8L3NhbWw6Q29uZGl0aW9ucz4KPHNhbWw6QXV0aG5TdGF0ZW1lbnQgQXV0aG5JbnN0YW50PSIyMDE2LTExLTE2VDA5OjQzOjEyWiIgU2Vzc2lvbkluZGV4PSJzMjQ2NTcxZDZhODU2ODM5YmFmOGNmNTQ2MzMwZGQzYzI3NzdmN2RkMDEiPjxzYW1sOkF1dGhuQ29udGV4dD48c2FtbDpBdXRobkNvbnRleHRDbGFzc1JlZj51cm46b2FzaXM6bmFtZXM6dGM6U0FNTDoyLjA6YWM6Y2xhc3NlczpQYXNzd29yZFByb3RlY3RlZFRyYW5zcG9ydDwvc2FtbDpBdXRobkNvbnRleHRDbGFzc1JlZj48L3NhbWw6QXV0aG5Db250ZXh0Pjwvc2FtbDpBdXRoblN0YXRlbWVudD48c2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PHNhbWw6QXR0cmlidXRlIE5hbWU9InVpZCI+PHNhbWw6QXR0cmlidXRlVmFsdWUgeG1sbnM6eHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIiB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4c2k6dHlwZT0ieHM6c3RyaW5nIj4yNjEyOTMwODAzNTwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjxzYW1sOkF0dHJpYnV0ZSBOYW1lPSJTZWN1cml0eUxldmVsIj48c2FtbDpBdHRyaWJ1dGVWYWx1ZSB4bWxuczp4cz0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEiIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiIHhzaTp0eXBlPSJ4czpzdHJpbmciPjM8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgTmFtZT0iQ3VsdHVyZSI+PHNhbWw6QXR0cmlidXRlVmFsdWUgeG1sbnM6eHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIiB4bWxuczp4c2k9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hLWluc3RhbmNlIiB4c2k6dHlwZT0ieHM6c3RyaW5nIj5lbjwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjxzYW1sOkF0dHJpYnV0ZSBOYW1lPSJBdXRoTWV0aG9kIj48c2FtbDpBdHRyaWJ1dGVWYWx1ZSB4bWxuczp4cz0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEiIHhtbG5zOnhzaT0iaHR0cDovL3d3dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2UiIHhzaTp0eXBlPSJ4czpzdHJpbmciPk1pbmlkLVBJTjwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjwvc2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PC9zYW1sOkFzc2VydGlvbj4=</Authentication><RecordSeal algorithm="SHA-512">Y/71/7lCxDUvQQ+KCeWlTmUM5ZPuzjQLD2MfB0XVHZnyqGSuU2RsIuGu47Znzd3RQk9f2uKPrEj5/XrEzgUd8g==</RecordSeal></SignatureRecord></Signatures></SDO>',  # NOQA
            },
            'message': {
                'id': '173adcd9-0041-443e-8861-f52c7936b77e',
                'recipient': {
                    'id': '974760673',
                    'id_type': 'orgnr',
                },
                'sender': {
                    'id': '910731718',
                    'id_type': 'orgnr',
                },
                'attachments': [{
                    'type': 'PAAR',
                    'name': '\Beretning 2015.pdf',
                    'file_name': '\Beretning 2015.pdf',
                    'sequence_no': '1',
                }, {
                    'type': 'ANNT',
                    'name': '\Regnskaper Skikretsen samlet 2015.pdf',
                    'file_name': '\Regnskaper Skikretsen samlet 2015.pdf',
                    'sequence_no': '4',
                }]
            }
        }

    def test_decree_from_xml(self):
        document = new_inquiry.BrregNewInquiry(xml=self.decree)
        xml = document.to_xml()
        generated.melding.CreateFromDocument(xml)

    def test_application_receipt_from_xml(self):
        document = new_inquiry.BrregNewInquiry(xml=self.application_receipt)
        xml = document.to_xml()
        generated.melding.CreateFromDocument(xml)

    def test_sdo_from_dict(self):
        document = new_inquiry.BrregNewInquiry(**self.sdo_inquiry_data)
        xml = document.to_xml()
        generated.melding.CreateFromDocument(xml)

    def test_get_content_decree(self):
        document = new_inquiry.BrregNewInquiry(xml=self.decree)
        result = document.get_content()
        self.assertIsInstance(result, decree.BrregDecree)

    def test_get_content_app_receipt(self):
        document = new_inquiry.BrregNewInquiry(xml=self.application_receipt)
        result = document.get_content()
        self.assertIsInstance(result, application_receipt.BrregApplicationReceipt)


class BrregSDOTests(TestCase):

    def setUp(self):
        self.change_report = get_test_file('integrasjonERFV', 'integrasjonERFV.xml')
        self.assertion = get_test_file('saml', 'assertion.xml')

    def test_to_xml(self):
        document = sdo.BrregSDO(change_report=self.change_report, authentications=[self.assertion], secret='Secret')
        xml = document.to_xml()
        expected = get_test_file('sdo', 'valid_sdo.xml')
        self.assertEqual(xml, expected.strip())  # strip() avoids failing on trailing whitespace in xml
        generated.frivintVerifisertMelding.CreateFromDocument(xml)

    def test_from_dict(self):
        data = {
            'change_report': self.change_report,
            'authentications': [
                self.assertion, self.assertion
            ],
            'secret': 'secretvalue'
        }
        document = sdo.BrregSDO(**data)
        xml = document.to_xml()
        generated.frivintVerifisertMelding.CreateFromDocument(xml)

    def test_signed_object_hash(self):
        expected = 'Q1LDZ1N8CTtTONPGf+uxfcI3ZlYBuHj9IwVhFM1AA/k='
        value = b'encoded value'
        document = sdo.BrregSDO(change_report=value)
        self.assertEqual(document.signed_object_hash, expected)

    def test_signed_object(self):
        expected = 'ZW5jb2RlZCB2YWx1ZQ=='
        value = b'encoded value'
        document = sdo.BrregSDO(change_report=value)
        self.assertEqual(document.signed_object, expected)


class RecordSealTests(TestCase):

    def setUp(self):
        self.authentication = 'saml:assertion'
        self.signed_object_hash = 'Q1LDZ1N8CTtTONPGf+uxfcI3ZlYBuHj9IwVhFM1AA/k='
        self.secret = 'secretvalue'

    def test_value(self):
        expected = 'r+eKXQCAECm4yqlb2sDsJeAlSabqMtDr+998ZHNkKEYXuJroVyLpqfLh2251R59xc8kdW5V2u+/qhtV3wn3iBA=='
        record_seal = sdo.RecordSeal(self.authentication, self.signed_object_hash, self.secret)
        self.assertEqual(record_seal.value, expected)


class RecipientsTests(TestCase):

    def setUp(self):
        self.xml_file = get_test_file('applikasjonskvittering', 'recipients.xml')
        self.party_number = '910731718'

    def test_from_xml(self):
        document = recipients.BrregRecipientList(xml=self.xml_file)
        self.assertEqual(document.parties[0], self.party_number)
        xml = document.to_xml()
        generated.recipients.CreateFromDocument(xml)

    def test_from_dict(self):
        document = recipients.BrregRecipientList(parties=[self.party_number])
        self.assertEqual(document.parties[0], self.party_number)
        xml = document.to_xml()
        generated.recipients.CreateFromDocument(xml)


class ManifestTests(TestCase):

    def setUp(self):
        self.xml_file = get_test_file('applikasjonskvittering', 'manifest.xml')
        self.file_name = 'Henvendelse.xml'
        self.checksum = md5(self.file_name).hexdigest()
        self.property_key = 'SomeProperty'
        self.property_value = 'SomeValue'
        self.reportee = '910731718'
        self.senders_reference = 'f874c861-f0bd-4789-9ab5-2402320b2cb0'

    def test_from_xml(self):
        document = manifest.BrregManifest(xml=self.xml_file)
        self.assertEqual(document.file_list[0], self.file_name)
        self.assertEqual(document.reportee, self.reportee)
        self.assertEqual(document.senders_reference, self.senders_reference)
        xml = document.to_xml()
        generated.manifest.CreateFromDocument(xml)

    def test_from_dict(self):
        document = manifest.BrregManifest(senders_reference=self.senders_reference, reportee=self.reportee,
                                          file_list=[(self.file_name, self.checksum)],
                                          property_list=[(self.property_key, self.property_value)])
        self.assertEqual(document.reportee, self.reportee)
        self.assertEqual(document.senders_reference, self.senders_reference)
        self.assertEqual(document.file_list[0], (self.file_name, self.checksum))
        self.assertEqual(document.property_list[0], (self.property_key, self.property_value))
        xml = document.to_xml()
        generated.manifest.CreateFromDocument(xml)


class ApplicationReceiptTests(TestCase):

    def setUp(self):
        self.xml_error = get_test_file('applikasjonskvittering', 'app_receipt_error.xml')
        self.xml_ok = get_test_file('applikasjonskvittering', 'app_receipt_ok.xml')

    def test_from_xml_error(self):
        document = application_receipt.BrregApplicationReceipt(self.xml_error)
        self.assertEqual(document.status_code, 200)
        self.assertEqual(document.message_reference, '7664d174-7f54-11e6-ae22-56b6b6499611')

    def test_from_xml_ok(self):
        document = application_receipt.BrregApplicationReceipt(self.xml_ok)
        self.assertEqual(document.status_code, 201)
        self.assertEqual(document.message_reference, 'e05f3b3a-68be-4ed9-81fc-9a8225cfa4d4')


class DecreeTests(TestCase):

    def setUp(self):
        self.xml = get_test_file('vedtak', 'vedtak.xml')

    def test_from_xml(self):
        document = decree.BrregDecree(self.xml)
        self.assertEqual(document.system_message_id, '04012017-01')
        self.assertEqual(document.fv_status, 'I')
        self.assertEqual(document.er_status, 'G')
        self.assertEqual(document.organisation_number, '999999999')


class BrregPackageTests(TestCase):
    # pdf_attachment_list = ["20160002275012-001-20162463455.pdf",
    #                        "20160002275012-002-20162463455.pdf",
    #                        "20160002275012-003-20162463455.pdf"]
    pdf_attachment_list = ["20170000416650-001-2017022675.pdf",
                           "20170000416650-001-2017022676.pdf"]

    def test_missing_henvendelse(self):
        contents = {
            "manifest": "manifest.xml",
            "recipients": "recipients.xml",
            "attachments": self.pdf_attachment_list,
            "subfolder": "vedtak"
        }
        data = BrregTestPackage(**contents).zip
        with self.assertRaises(ValueError):
            package.BrregPackage(file_data=data)

    def test_missing_manifest(self):
        contents = {
            "henvendelse": "vedtak_melding_m_vedlegg.xml",
            "recipients": "recipients.xml",
            "attachments": self.pdf_attachment_list,
            "subfolder": "vedtak"
        }
        data = BrregTestPackage(**contents).zip
        with self.assertRaises(ValueError):
            package.BrregPackage(file_data=data)

    def test_complete(self):
        contents = {
            "manifest": "manifest.xml",
            "henvendelse": "vedtak_melding_m_vedlegg.xml",
            "recipients": "recipients.xml",
            "attachments": self.pdf_attachment_list,
            "subfolder": "vedtak"
        }
        package_data = BrregTestPackage(**contents)
        result = package.BrregPackage(file_data=package_data.zip)

        expected_inq = new_inquiry.BrregNewInquiry(xml=package_data.henvendelse)
        self.assertEqual(result.inquiry.to_xml(), expected_inq.to_xml())

        expected_rec = recipients.BrregRecipientList(xml=package_data.recipients)
        self.assertEqual(result.recipients.to_xml(), expected_rec.to_xml())

        expected_manifest = manifest.BrregManifest(xml=package_data.manifest)
        self.assertEqual(result.manifest.to_xml(), expected_manifest.to_xml())

        for att in package_data.attachments:
            inq_att = result.get_attachment(att.filename)
            self.assertEqual(inq_att.file_data, att.file_data)
