# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xlrd
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginator_list(obj, page, max_cnt):
    paginator = Paginator(obj, max_cnt)
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

