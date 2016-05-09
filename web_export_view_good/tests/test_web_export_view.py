# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase
from openerp.addons.web_export_view_good.controllers.controllers import ExcelExportView
import os
# import json
import httplib
# import urllib


class TestWebExportView(TransactionCase):

    def test_web_export_view(self):
        self.env['report.template'].get_time('partner')

        # self.env['report.template'].create({'model': self.env.search([('name', '=', 'partner')]),
        #                                     'file_address': "%s\%s" % (os.path.split(os.path.realpath(__file__))[0], "hello.xls")})
        data = {u'headers': [u'\u5ba2\u6237', u' ', u' ', u' '],
                u'model': u'partner',
                u'rows': [[u'\u5ba2\u6237\u7c7b\u522b', u'\u7f16\u53f7', u'\u540d\u79f0', u'\u5e94\u6536\u4f59\u989d'],
                          [u'\u4e00\u7ea7\u5ba2\u6237', u'jd', u'\u4eac\u4e1c', 0], [u'\u5408\u8ba1', u' ', u' ', 0], [u'\u64cd\u4f5c\u4eba', u'admin', u'\u64cd\u4f5c\u65f6\u95f4', u'2016-05-05']],
                u'file_address': "%s%s" % (os.path.split(os.path.realpath(__file__))[0], "/hello.xls")}
        a = ExcelExportView()
        a.from_data(data.get('headers'), data.get("rows"), data.get("file_address"))
        a.from_data(data.get('headers'), data.get("rows"), '')