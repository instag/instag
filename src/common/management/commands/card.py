# -*- coding: utf-8 -*-
from common import template_text as T
from django.core.management.base import BaseCommand
from instagram import client
from instagram_url.models import InstagramPlayer, InstagramPlayerMedia
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import random
CONFIG = T.CONFIG
unauthenticated_api = client.InstagramAPI(**CONFIG)

class Command(BaseCommand):
    def handle(self, *args, **options):
        list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        total = 0

        # list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        # list = random.sample([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10],  17)





        for i in list:
            list.remove(i)
            for j in list:
                list.remove(j)
                for k in list:
                    self.random_test(i,j,k)
                    # print i, j, k
                    # if (i+j+k) == 10:
                    total += 1
                    #     print (i,j,k)

        # print total



    def random_test(self,  i, j, k):

        total = 0
        list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        # print list
        # print i, j, k

        # print list
        list.remove(i)
        # print list
        list.remove(j)
        # print list
        list.remove(k)
        # print list

        # 리스트는 랜덤으로 3장 빠진 전부
        for a in list:
            if a in list:
                # 한장을 더 뺀 나머지 리스트
                print list
                print a
                print list.remove(a)

            list_b = list.remove(a)
            # print list_b


            # for b in list:
            #     for c in list:
            #         if (a+b+c) == 10:
            #             # print "->", a,b,c
            #             total += 1



        # for a in list:
        #     for b in list:
        #         for c in list:
        #             if (a+b+c) == 10:
        #                 # print "->", a,b,c
        #                 total += 1

        # print ("빠진카드"), i,j,k , "--->", total,"(경우의 수)"






        # for i in list:
        #     for j in list:
        #         for k in list:
        #             print i, j, k
