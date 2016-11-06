# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import twitter, random
import sys
import urllib2
import re
import hashlib

from twitter_count.models import TwitterCountKO

"""
twitter_developer : todayrt@gmail.com
"""

consumerKey = 'f5KtbqRo64YLpiYjhVZHrg'
consumerSecret = 'ZFPqyyMtIZiowESXBlWZMhMaf3owPy0FPF1MJv5k'
accessToken = '97829868-Xxo8rmnWeMZJqMik9eZirYrxGa8JHhDtMs46jKY1U'
accessSecret = 'Eno08dC8uq72SL2qr4bG71ZwHSuheSaF65CpqDEotS4bw'

DELETE_TEXT_LIST = {
'4M_kkwonsso',
'ZEA_9','ukisskorea','4M_hyunah','lizzy_sy','infinitelkim','junsutime','joonkuni','Daksu20','QriPretty','Ja​cob​Tag​are​la','lucid_fall_jo','sujushow100','Eunsol0505','Famous_Jae','Hyomin',
'karam0628','code07lim','29rain','NBA0430',
'ikmubmik','chungxuan','Joker891219','mingkki21','taraeunjung1212','ssinz',
'ChoiKanism','eHyundai_tweets',
'batatofrito','Jelatinax','zunoxiahmom','sarcasticu','heungmin40','kirrard16','Two2Min','hwangkwanghee','_imzombie','drimcomtru1','fromtheline','rypaffo','kangfull74',
'Paradise_DongJu','sondongwoonnet','Only1yejun','SSG_GJ','HoonKwangShin','JYKIM_4',
'congjee','nae1004','jinuSEAN3000','ChrisOficiaI', 'lhamadorock','1adolescente','pjy1234','NaRi______','OutrasFrases','BSKworld','Girls_Day_Minah','chyh1202','HyundaiCard','fateflysy','SKtelecom','seeksik','coed_sm','B2STDH',
'hongcube','u_kisseli','KBSKISSTHERADIO','guitarjm','4M_Jiyunit','U_Kwon','Thsm1','G_NA_love','Radoworld','dominostory',
'dakaya007','kimjuha','pledisnews','thsgoku',
'SSG_GN','SSG_Main','SSG_CH','SSG_MS','SSG_CC','fateflysy','Gagkorea_Show','Topstar07','SSG_GG','SSG_IC','smcomedy','WeMakePrice','SingerIU','ROCKOUT529','blockbhyo','Himsenkangin','__BEKAH','Apinkjej','JOOJYPE',
'six2k','mbcstar','B1A4_JINYOUNG','MnetMcountdown',
'climix_joo','PPKA2000','b2ment','B1A4_CNU','JinseokYang','SANDEUL920320','xodusl80','YoonJaeloveBAR','WG_Lim','joy_rania','JSK91AJ',
'Prepix','elbowyeish','ASJuPal','raina57','ybrocks','B1A4_gongchan','100school','ChungMinCho','haeminsunim','yuhs56','b89530','Cemula1','jksjapan','misskahi','p_Lizzy',
'parkheykyoung','SeoWon_JANG',
'B2ST74','secret8823','JaeKyung_K','honeymallow8823',
'Apinksne','frog799','doublev89',
'cherry4eva84','KihaChang','infiniteyounges',
'leadergyu','Seongyeol1991','FtDrMH1111','RHY422','ddww1122','BARO920905','ZICO92','G_BoyFriend','treeJ_company','PPin_o','0430yes','BlockB2011','JUNUSofficial','hoya1991','Girls_Day_Hyeri','dmtn_danieLA','ginachoi87','SECRETsongjieun','_DHS',
'doublev89','AsiaPrince_JKS','koeuna1028','4M_jiyoonitt','BlockBkyung','B1A4_JINYOUNG','Nocutnews','eunhyuk45kg','Boram86322','nkh0625',
'soulmate_yys','ilikeyoutheb2st','SBS_BOSS','ZEA_Hyungsik','J_frog','ohboyzine','ZEA_MW',
'myjanggun','shining_smile_','woorissicacom','shinee_jh','TaeFung428','welovehani','mediamongu','unheim','AS_JungAh','actormoon','ICONTAEC','patriamea','xiahinsoul','prettyboy_jun','Kjjzz','JS_Americano','Realtaeyang','SSujining','doax',
'dogsul','mindjj','PresidentYSKim','mindgood','goodwriting_bot','yohjini','wonsoonpark','bulkoturi','your_rights',
'goodwriting_bot','YoToNews','sarabolle','heenews','du0280','HanMyeongSook',
'funronga','ddanzis','kennedian3','harooluvstar','BBK_Sniper',
'jessture_net',
'thestephicom','Osh_yoru','bot_beastdw','GoEuntae','DC2NE1','kmlee36','blobyblo','HooN91y','servant_imys','dosol22','woqjf012','1215thexiahtic','mettayoon','kebforever',    'imSMl','realjonghyun90','peedeebaby','ZELO96','realjonghyun90','ActorJungilwoo','Kangjaechon','itzmeys','NK_HumanRights','BAP_Daehyun','jrjyp',
'TAE_SAMA',
'ZELO96',
'nanako081',
'_jinyoung911118',
'BTS_twt','BTOB_SEKwang','all4b2uty','KYUNGPARK1992','BAP_Jongup','btob2mh','BTOB_6SJ','HeeZZinPang','BAP_Bangyongguk','BB_taeil','krungy21','bornfreeonekiss','whdgus1004','LeeCS_BTOB','Moonjunwon','ljoeljoe1123','BTS_twt',
'dlwnsghek','Khunnie0624','donghae861015','sechanmin','invincible9394','best_0922','EndearingMark','shfly3424','pledis_17','bts_bighit','jypnation','BamBam1A','OfficialMonstaX',
'pledis17_STAFF',
'showchampion1',
'Official_IFNT',
'TEEN_TOP',
'GOT7Official',
'2PMagreement211',
'TheArk_official',
'playonmark',
'Official_LVLZ',
'BTS_ARMY',
'special1004',
'CN_FANCLUB',
'seventhheaven_7',
'Praecipua94',
'jujujuju73',
'B2stGK',
'__exo___exo__',
'topstarnews',
'choichoi8989',
'nieltree',
'BTSOFFICIALSHOP',
'mrjoker1219',
'bbh_506_',
'def_jayb',
'YB_518',
'tinycute_xiumin',
'Lookatme_cj',
'EverBlooming_',
'A_B_0929',
'jo5929',
'IMUKYOU_H',
'vintage931005',
'noblespirits707',
'mshong_ftpri',
'honeyjoe1123',
}

def twitter_insert():
    api = twitter.Api(consumerKey,consumerSecret,accessToken,accessSecret)
    term = u'RT'
    lang = u'ko'
    locale = u'ko'
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
        insert_flag = True
        
        print t
        
        try:
            for i in DELETE_TEXT_LIST:
                if i == t.retweeted_status.user.screen_name:insert_flag = False
            if insert_flag:
                result_record, is_new = TwitterCountKO.objects.get_or_create(uniqu_id=t.retweeted_status.id)
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
    TwitterCountKO.objects.filter(created_at__lte=time_ranking).delete()
    
                        

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
        