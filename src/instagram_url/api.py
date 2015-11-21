# -*- coding: utf-8 -*-

from .models import InstagramPlayer

def set_tag(access, tag_1, tag_2, tag_3, tag_4, tag_5, tag_6):
    try :
#        result = InstagramPlayer.objects.get(oauth_token=access)
        result, is_new = InstagramPlayer.objects.get_or_create(oauth_token=access)
#        result = InstagramPlayer.objects.get(oauth_token=access)
        result.tag_1 = tag_1
        result.tag_2 = tag_2
        result.tag_3 = tag_3
        result.tag_4 = tag_4
        result.tag_5 = tag_5
        result.tag_6 = tag_6
        result.save()
    except:
        return None    
    return result

def get_instagram_player(user, code, access_token, site_user):
    """
    playerのクエスト情報を取得する
    """
    try :
        result, is_new = InstagramPlayer.objects.get_or_create(user_id=user['id'])
        result.user_name = user['username']
        result.profile_picture = user['profile_picture']
        result.code = code
        result.user_site_id = site_user.id
        result.oauth_token = access_token
        result.save()
        
    except:
        return None    
    return result    

def get_instagram_player_code(code):
    """
    playerのクエスト情報を取得する
    """
    try :
        result = InstagramPlayer.objects.get(code=code)        
    except:
        return None
    return result    

def get_instagram_player_token(access):
    try :
        result = InstagramPlayer.objects.get(oauth_token=access)        
    except:
        return None
    
    return result    


def set_instagram_tag(user, code, access_token):
    """
    playerのクエスト情報を取得する
    """
    try :
        result, is_new = InstagramPlayer.objects.get_or_create(user_id=user['id'])
                
        result.user_name = user['username']
        result.profile_picture = user['profile_picture']
        result.code = code
        result.oauth_token = access_token
        result.save()
        
    except:
        return None    
    return result    

def get_instagram_player_all():
        
        return InstagramPlayer.objects.all()
        
        
        
    