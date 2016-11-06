# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import twitter, random
import sys
import urllib2
import re
import hashlib

from twitter_count.models import TwitterCountJP

"""
twitter_developer : todayrt@gmail.com
"""

consumerKey = 'f5KtbqRo64YLpiYjhVZHrg'
consumerSecret = 'ZFPqyyMtIZiowESXBlWZMhMaf3owPy0FPF1MJv5k'
accessToken = '97829868-Xxo8rmnWeMZJqMik9eZirYrxGa8JHhDtMs46jKY1U'
accessSecret = 'Eno08dC8uq72SL2qr4bG71ZwHSuheSaF65CpqDEotS4bw'

DELETE_TEXT_LIST = {
    'pazudora',
    'juicyfactz',
    'Mayknowpeace',
}

def twitter_insert():
    api = twitter.Api(consumerKey,consumerSecret,accessToken,accessSecret)
    term = u'RT'
    lang = u'ja'
    locale = u'ja'
#     lang = u'ko'
#     locale = u'ko'
    result_type = 'recent'
    count = '100'
    
    tl = api.GetSearch(
                       term=term,
#                       locale=locale,
                       lang=lang,
                       result_type=result_type,
                       count=count,
                       )

    for t in tl:
        try:
            result_record, is_new = TwitterCountJP.objects.get_or_create(uniqu_id=t.retweeted_status.id)
            # 트위터 unicode created
            from datetime import datetime
            created = datetime.strptime(t.retweeted_status.created_at.strip('"'), "%a %b %d %H:%M:%S +0000 %Y")
        
            if is_new:
                result_record.body = _clean_text(t.text,"")
                result_record.text = _clean_text(t.text,"")
                result_record.profile_image_url = t.retweeted_status.user.profile_image_url
                result_record.url = t.retweeted_status.id
                result_record.owner = t.retweeted_status.user.screen_name
                result_record.rtCount = t.retweeted_status.retweet_count
                result_record.created_at = created
                 
                result_record.save()
            else :
                result_record.rtCount = t.retweet_count
                result_record.save()
        except :
            pass

    import datetime
    now = datetime.datetime.now()    
    time_ranking = now - datetime.timedelta(hours=200)
    
    #300시간이 지난 데이터는 삭제됨
    TwitterCountJP.objects.filter(created_at__lte=time_ranking).delete()
    
                        

def _clean_text(text, url):
    
    try:
        temp = text.replace("RT ", "")
        temp = temp.replace("&lt;", "")
        temp = temp.replace("&gt;", "")
        temp = temp.replace("&lt; ", "")
        temp = temp.replace("&amp;", "")
        temp = temp.replace(url, "")
        delete_text = temp[temp.find('@'):temp.find(': ')+2]
        result_temp = temp.replace(delete_text, "")
        return result_temp 
    except:
        return text
    

class Command(BaseCommand):
    def handle(self, *args, **options):
        twitter_insert()
        