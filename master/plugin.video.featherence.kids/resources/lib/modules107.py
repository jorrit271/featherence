# -*- coding: utf-8 -*-
import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc,os

from variables import *
from shared_modules import *
if "plugin." in addonID: from shared_modules3 import *
'''---------------------------'''


	
'''107'''
def CATEGORIES107C(General_LanguageL, background, background2): #בוב הבנאי
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PL_8KXLhQVQMK80XCn7g3qVj7RwhrwiGHG') #בוב הבנאי
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F78685-2.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F78685-2.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DBob%20the%20Builder%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fbob-the-builder')
		list.append('&youtube_pl=PLiluoe0QNL4EXc5qYPJWoqZ2iyBPk3ybk') #בוב הבנאי
		list.append('&youtube_pl=PL0sYiBnLzquZiY3lUx4gtdQjkYHEbls-4') #בוב הבנאי
		list.append('&youtube_id=Qh5AelBoSG8')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PL61W_aqonWD9cRbZnicuZ-7Z2YgI3pXb3') #בוב הבנאי
		list.append('&youtube_pl=PLMbHetlciXWlUFE3z4bv3U2wKNPB5gDLX') #בוב הבנאי
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PL6E6EC6BECB940729') #בוב הבנאי
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_id=89A-ElVAsRs') #בוב הבנאי #S1
		list.append('&youtube_id=OYqWJqw1fbE') #בוב הבנאי #S3
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLF493BCB7A2B5EF42') #בוב הבנאי
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PL8BA2003016C19A9C') #בוב הבנאי
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PL6CFD617813187A4E') #בוב הבנאי
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=PLdDOXpS6MzV9DkSRE3ubF53QEOFe18mzc') #בוב הבנאי
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PLF5B4300FE3419A74') #בוב הבנאי	
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10707).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/78685-2.jpg',addonString(107070).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/78685-2.jpg"))

def CATEGORIES107D(General_LanguageL, background, background2): #אדיבו
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1641.jpg&mode=5&name=%d7%a2%d7%95%d7%a0%d7%94%201&season_id=1&series_id=1641&series_name=%d7%90%d7%93%d7%99%d7%91%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91-adiboo%2fseason%2f1&summary=%d7%90%d7%93%d7%99%d7%91%d7%95%20%d7%94%d7%99%d7%90%20%d7%a1%d7%93%d7%a8%d7%aa%20%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%a0%d7%a4%d7%95%d7%a6%d7%94%20%d7%a9%d7%a2%d7%9c%20%d7%a4%d7%99%d7%94%20%d7%a0%d7%a2%d7%a9%d7%95%20%d7%9c%d7%90%20%d7%9e%d7%a2%d7%98%20%d7%9e%d7%a9%d7%97%d7%a7%d7%99%20%d7%9e%d7%97%d7%a9%d7%91%20%d7%94%d7%9e%d7%99%d7%95%d7%a2%d7%93%d7%99%d7%9d%20%d7%9c%d7%99%d7%9c%d7%93%d7%99%d7%9d.%d7%90%d7%93%d7%99%d7%91%d7%95%20%d7%95%d7%90%d7%93%d7%99%d7%9c%d7%99%d7%94%20%d7%94%d7%9d%20%d7%a9%d7%a0%d7%99%20%d7%90%d7%97%d7%99%d7%9d%20%d7%97%d7%99%d7%99%d7%96%d7%a8%d7%99%d7%9d%20%d7%97%d7%9e%d7%95%d7%93%d7%99%d7%9d%2c%20%d7%95%d7%99%d7%a9%20%d7%9c%d7%94%d7%9d%20%d7%97%d7%99%d7%99%d7%aa%20%d7%9e%d7%97%d7%9e%d7%93%20%d7%97%d7%99%d7%99%d7%96%d7%a8%d7%99%d7%aa%20-%20%d7%91%d7%95%d7%96%d7%99%2c%20%d7%95%d7%a8%d7%95%d7%91%d7%95%d7%98%20%d7%97%d7%9b%d7%9d%20%d7%95%d7%99%d7%93%d7%99%d7%93%d7%95%d7%aa%d7%99%20-%20%d7%a8%d7%95%d7%91%d7%99%d7%98%d7%95%d7%a7.%20%d7%9c%d7%9b%d7%9c%20%d7%94%d7%97%d7%91%d7%95%d7%a8%d7%94%20%d7%99%d7%a9%20%d7%97%d7%9c%d7%9c%d7%99%d7%aa%20%d7%9e%d7%99%d7%95%d7%97%d7%93%d7%aa%20%d7%a9%d7%99%d7%9b%d7%95%d7%9c%d7%94%20%d7%9c%d7%94%d7%aa%d7%9e%d7%96%d7%a2%d7%a8%20%d7%95%d7%9c%d7%98%d7%95%d7%a1%20%d7%91%d7%aa%d7%95%d7%9a%20%d7%94%d7%92%d7%95%d7%a3%20%d7%94%d7%90%d7%a0%d7%95%d7%a9%d7%99.%d7%91%d7%9b%d7%9c%20%d7%a4%d7%a8%d7%a7%20%d7%a8%d7%95%d7%91%d7%99%d7%98%d7%95%d7%a7%20%d7%9e%d7%9c%d7%9e%d7%93%20%d7%90%d7%aa%20%d7%90%d7%93%d7%99%d7%91%d7%95%20%d7%95%d7%90%d7%aa%20%d7%97%d7%91%d7%a8%d7%99%d7%95%20%d7%9e%d7%a9%d7%94%d7%95%20%d7%97%d7%93%d7%a9%20%d7%a2%d7%9c%20%d7%92%d7%95%d7%a3%20%d7%94%d7%90%d7%93%d7%9d%3a%20%d7%94%d7%97%d7%9c%20%d7%91%d7%93%d7%a8%d7%9a%20%d7%a4%d7%a2%d7%95%d7%9c%d7%aa%20%d7%94%d7%a2%d7%99%d7%9f%20%d7%95%d7%9b%d7%9c%d7%94%20%d7%91%d7%a4%d7%a2%d7%95%d7%9c%d7%95%d7%aa%20%d7%94%d7%9e%d7%a2%d7%99%d7%99%d7%9d%20%d7%94%d7%9e%d7%91%d7%99%d7%9b%d7%95%d7%aa%20%d7%99%d7%95%d7%aa%d7%a8.%d7%93%d7%a8%d7%9a%20%d7%9e%d7%a6%d7%95%d7%99%d7%a0%d7%aa%20%d7%a2%d7%91%d7%95%d7%a8%20%d7%94%d7%99%d7%9c%d7%93%d7%99%d7%9d%20%d7%9c%d7%94%d7%9b%d7%99%d7%a8%20%d7%90%d7%aa%20%d7%90%d7%91%d7%a8%d7%99%20%d7%94%d7%92%d7%95%d7%a3%2c%20%d7%aa%d7%a4%d7%a7%d7%99%d7%93%d7%9d%20%d7%95%d7%94%d7%a9%d7%9e%d7%95%d7%aa%20%d7%a9%d7%9c%d7%94%d7%9d.&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1641%2f%d7%90%d7%93%d7%99%d7%91%d7%95-%d7%9e%d7%93%d7%95%d7%91%d7%91-adiboo%2fseason%2f1')
		list.append('&youtube_pl=PL_8KXLhQVQMLeDwIbMl6RyoMQiCuY7tu-')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=PL9kZfQFPw4Wbah9W8Gg-6NBA_gOjBhJu2')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLtQng_nJbsU_brujZqJxr3YEtixW3Qs1Y')
		list.append('&youtube_pl=PL3E219D763F8FD9D7')
		
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=PLFHyzF424u27cQK87UejHcLui8dHImpgA')
		list.append('&youtube_pl=PL1qfM5cs2CNNWy-a6-vtRENZ-RVSVbsV-')
		
		
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10702).encode('utf-8'),list,17,"http://www.sdarot.pm/media/series/1641.jpg",addonString(107020).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://7-themes.com/data_images/out/63/6986632-dora-wallpaper-free.jpg", default=background2))

def CATEGORIES107E(General_LanguageL, background, background2): #דובי קטן
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLlqY465vYEEY8iThIr4BtesfH0T6ExzRu')
		list.append('&youtube_pl=PLbwCMddV8cuqr8EU1bjNdJbRI7RMzgnBc')
		list.append('&youtube_pl=PLJeeyg_bcp_-WwncCYAOXdCj2pxfuA7Q0')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PLF97EF182BD1F73B6')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLs8KL9s28cKa_3nK3ORd2dZb2Q-GAqmwk') #S6
		list.append('&youtube_pl=PLs8KL9s28cKa_3nK3ORd2dZb2Q-GAqmwk') #S6
		list.append('&youtube_pl=PLs8KL9s28cKYdBZ3wS4UFs0GtFNKl5g4N') #S4
		list.append('&youtube_pl=PLs8KL9s28cKYdBZ3wS4UFs0GtFNKl5g4N') #S5
		list.append('&youtube_pl=PLs8KL9s28cKa_3nK3ORd2dZb2Q-GAqmwk') #S6
		
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLDSSCTIW8JB_4dZ1zOdEsijFEyj7voLvj') #S1
		list.append('&youtube_pl=PLFTZtuukriqfDdNYOhH83Fmn-Ps9Hws8A')
		
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLhfvS2yf5dmWGBlmuw_pdp_m3HtZwnEhB')
		list.append('&youtube_pl=PLlqY465vYEEYZXq-gw1z8CGuEB0309fAl')
		list.append('&youtube_pl=PL50CN9ZQKkW_CzLpp0_K8cm896BxIbyBy')
		list.append('&dailymotion_pl=x28l9r')
		
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10709).encode('utf-8'),list,17,"http://thetvdb.com/banners/_cache/posters/80879-1.jpg",addonString(107090).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/_cache/fanart/original/80879-3.jpg"))

def CATEGORIES107F(General_LanguageL, background, background2): #קירוקי
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLG7lOHF8VEv8gIhF5E3iy1ueiwViDSrq7') #English #קירוקי
		list.append('&youtube_pl=ELz1kTQoPdsrA') #English
		list.append('&youtube_pl=PLt4Dp3dEhycrIJqrvsskqwdQc6hAWRVOq') #English
		list.append('&youtube_pl=PLjgHe0djQQ_OHBz_Cq2G6_Aiq7oWKLGBF') #English
		list.append('&youtube_pl=PLqjVAzhugdWJAuLvS573FPGGxD3AhzGUL') #English
		list.append('&youtube_pl=PL2Tx5J05NrCXL9JBnfy93K_zlGn2LRKAL') #English
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_id=') #S
		list.append('&youtube_pl=') #S
		
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PLG7lOHF8VEv8f8kpGhqrxeQW0ihsKF94-') #German
		list.append('&youtube_pl=PLeVA7eICJ6d08462ZW4aidVwfo_lLgDB8') #German
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL4ETIwkI6M_dn85hrTop5yvmVo7ypZjh2') #Dutch
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PL7D9A5D1CCBF96850') #Russian
		list.append('&youtube_pl=PLdBOR-FS76gzBslnoA7yjz9CsyX4d32Oz') #Russian
		list.append('&youtube_pl=PLK7zXb6tNkib1KxdOFqWGAxZEUBv3l_fv') #Russian
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	
	addDir(addonString(10769).encode('utf-8'),list,17,'http://www.nevcheeses.com/images/%D1%81%D0%BC.jpg',addonString(107690).encode('utf-8'),'1',0,getAddonFanart(background))

def CATEGORIES107G(General_LanguageL, background, background2): #סמי הכבאי
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f824.jpg&mode=3&name=%d7%a1%d7%9e%d7%99-%d7%94%d7%9b%d7%91%d7%90%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-fireman-sam%2fseason%2f1&series_id=824&series_name=%d7%a1%d7%9e%d7%99-%d7%94%d7%9b%d7%91%d7%90%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-fireman-sam%2fseason%2f1&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f824%2f%d7%a1%d7%9e%d7%99-%d7%94%d7%9b%d7%91%d7%90%d7%99-%d7%9e%d7%93%d7%95%d7%91%d7%91-fireman-sam%2fseason%2f1')
		list.append('&youtube_pl=PL8x83ieZ_yGXSJbCVjtUc6ZV3XWY95iEH')
		list.append('&youtube_id=yw1gocZyn8o')
		list.append('&youtube_id=e3ChxP5afl4')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F73517-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F73517-4.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DFireman%20Sam%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Ffireman-sam')
		list.append('&youtube_pl=PLaeuNQbB1tFJP37MahWFjlXWNx9q2eOl8') #S1
		list.append('&youtube_pl=PLaeuNQbB1tFIkXm9wgKKorHtO8c-xyOq9') #S2
		list.append('&youtube_pl=PLP22qIfK2ZNSC2R9NYO5F3mF5outv5EAG') #S3
		list.append('&youtube_pl=PLmUMsJYJMTVBaAzvHEnVzRtpZaUeTXJbf') #S5
		list.append('&youtube_id=0dMIMC4-JpA')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=PLO0hbSk8JYPHRgr8sfWQwr5XWdbXHbXrf')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_id=4UIKOWpb0eQ')
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=PL0HRnNtgh6QSTGsp7p5TXeqygL_hDlorG')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=PLm9GdA5yhq-gUTP9yxccOTe3vLpe7ZjcN')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PLzuZDIq28jxm4q-gZdmoYau8VdNLkLKpp')
		list.append('&youtube_pl=PLQVNyVTGpqiTk-R65MjlVf4n-OLfzn9wm')
		list.append('&youtube_pl=PLXEAKNX18DPxwnpKI4NjmHYKNIS0y4z0g')
		list.append('&youtube_pl=PL3RpBbnUrXqcIzyZRxudUIJJeM3Zg7fIN')
		
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=LSPzY6LzMYM')
		list.append('&youtube_id=MmCGFE4MIIk')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL4gBJNUuVvV06gyFbQxunDchCwAjZ27U_')
		list.append('&youtube_id=4UIKOWpb0eQ')
		
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10551).encode('utf-8'),list,17,'http://thetvdb.com/banners/_cache/posters/73517-4.jpg',addonString(105510).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/73517-3.jpg"))

def CATEGORIES107H(General_LanguageL, background, background2): #החברים של ברני
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLOC8r5xdaMIwZHJCwBBGU4IX8B1ELYAYn')
		list.append('&youtube_pl=PL60YbYUzvVHFrFguuZbLhTgvNLcEFQCq0')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLFw7KwIWHNB3eIoqm8vLyYpVzxzOtHrK-')
		list.append('&youtube_pl=PLi7zMhw4_OnTwM0U3AyTtDyOwaYu_GqdN')
		list.append('&youtube_id=Vv8JRBg6GHM')
		list.append('&youtube_id=8m3PCZft-tg') #החברים של ברני (שירים) 
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PLWpIoyWOpAbgZGLeK8RRmgdcahHfjzqDc')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PL8suba63GEdxfzQqmGWSRrmh69Tx6PBT_')
		list.append('&youtube_pl=PL3k8nucMMikq8FVJurH5JIKEzk3Jwn6pO')
		
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=PLqalBvUGdA4tk3bDOzVT2BBsPSdcjo7py')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=PL2UVY3IvCqRpHFQyNOzUALDdLzObmabaU') #החברים של ברני
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10735).encode('utf-8'),list,17,"http://images6.fanpop.com/image/photos/35900000/Barney-2-barney-and-friends-35910438-321-394.png",addonString(107350).encode('utf-8'),'1',0,getAddonFanart(background, custom = "http://fallytv.com/showinfo/72180/72180-1.jpg", default=background2))

def CATEGORIES107I(General_LanguageL, background, background2): #צוות אומי זומי
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%a8%d7%95%d7%91%d7%95%20%d7%90%d7%95%d7%98%d7%95%20%d7%a4%d7%95%d7%9c%d7%99&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2688025')
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLutDePOThX0RFKE-rZ6UKgsGiz3NFBF9s')
		list.append('&youtube_pl=PLPRy1JmMz4QOmRSZZ2fxUKHFg9Vkb5iEI')
		list.append('&youtube_pl=PLcfJOu27qflmFz9DBozS4vVIqM9e5Mwzy')
		list.append('&youtube_id=4XR8J406sIk')
		list.append('&youtube_id=bIqpps2vN24')
		list.append('&youtube_id=efPl8Mys1D8')
		list.append('&youtube_id=pliR-yV_qRM')
		list.append('&youtube_id=VwZ4xuN4tP0')
		list.append('&youtube_id=WXv-U0JNApc')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLAF73mLqa7Y4GGCfLyHqHrN5lcXubWv6c')
		list.append('&youtube_id=h6sIlfnn1UY')
		list.append('&youtube_id=ugP1tLV1ZZY')
		
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=-Xx2-uZoOwE')
		list.append('&youtube_id=5LynyKz1lSI')
		list.append('&youtube_id=dshp7NDr6y4')
		list.append('&youtube_id=')
		
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLPwB-heNwj26CnMHFPZzevMToO-7hmMz0')
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=PL3qHjxSSl7AFNR1UJVfgil5QeoRiH56XV')
			list.append('&youtube_pl=PL3qHjxSSl7AGZS5VkjgcTA0PM9pP_bDld')
		list.append('&youtube_id=ef8R0si5Ghg')
		list.append('&youtube_id=5ns0ShwFcA0')
		
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_id=T4vKPpONe2g')
		list.append('&youtube_id=TTeDlm_yA_M')
		list.append('&youtube_id=bcoBMCe3Rs0')
		list.append('&youtube_id=')
		
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10706).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/thumb/6/66/Team_Umizoomi_logo.png/250px-Team_Umizoomi_logo.png',addonString(107060).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://media.insidepulse.com/zones/insidepulse/uploads/2012/06/Teamumizoomi.jpg"))

def CATEGORIES107J(General_LanguageL, background, background2): #ארמון החיות
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLVwL64lSxWWy8lQUurv6EHnQHXN45Di98')
	
	'''אנגלית'''
	if 'English' in General_LanguageL:
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=PL2m1vjiMH_hNYF4U-PIk6-YAEbi88WSLg')
			list.append('&youtube_pl=PLJRUmfAHVXtmAqNuPmtsP3Mhz_Bg_QzUY')
		
		list.append('&youtube_pl=PLv042z7GzQ6tKPU-X9AqvetwM6CuIY65g')
		list.append('&youtube_id=ubE_Xez_tHg')
		list.append('&youtube_id=2Zr1s_0yB9Y')
		list.append('&youtube_id=IfYtzK-X90w')
		list.append('&youtube_id=SDqwXjw1vic')
		list.append('&youtube_id=IfYtzK-X90w')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10704).encode('utf-8'),list,17,"",addonString(107040).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))

def CATEGORIES107K(General_LanguageL, background, background2): #הנסיכה סופייה
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1636.jpg&mode=3&name=sofia-the-first-%d7%94%d7%a0%d7%a1%d7%99%d7%9b%d7%94-%d7%a1%d7%95%d7%a4%d7%99%d7%94-%d7%94%d7%a8%d7%90%d7%a9%d7%95%d7%a0%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91&series_id=1636&series_name=sofia-the-first-%d7%94%d7%a0%d7%a1%d7%99%d7%9b%d7%94-%d7%a1%d7%95%d7%a4%d7%99%d7%94-%d7%94%d7%a8%d7%90%d7%a9%d7%95%d7%a0%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1636%2fsofia-the-first-%d7%94%d7%a0%d7%a1%d7%99%d7%9b%d7%94-%d7%a1%d7%95%d7%a4%d7%99%d7%94-%d7%94%d7%a8%d7%90%d7%a9%d7%95%d7%a0%d7%94-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=PLVwL64lSxWWyAUC6Bv-GAbdgQAv3CuCrr') #Songs
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PLrKOegyIpj3T0oEzvMtDFsSOPYMhZ-7ZV')
		list.append('&youtube_pl=PL7HHeetyLbwHUDkTU9YJPU6lH_gyYGNir')
		list.append('&youtube_pl=PLv042z7GzQ6tH0CLphGp8jkbNvG5VbzMb')
		list.append('&youtube_pl=PLAWEtMG6fBxDDWchmhZmrU8nWHNZdcDSy')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=PL7HHeetyLbwE5jt_jg26jr9St5SgKlqUD')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=PL7HHeetyLbwGNoF6mHaMMzN3oPwNdtm2E')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=PLrd1OouY4uCOqFkLlBSIZcm57BL-WnJMB')

	addDir(addonString(10722).encode('utf-8'),list,17,'http://global.fncstatic.com/static/managed/img/fn-latino/lifestyle/Sofia_Logo.jpg',addonString(107220).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://vignette4.wikia.nocookie.net/disney/images/c/ce/Cinderella-Sofia-the-first.jpg/revision/latest?cb=20131006155938"))

def CATEGORIES107L(General_LanguageL, background, background2): #דוק רופאת הצעצועים
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLVwL64lSxWWyRD2CIOc5qkXUuSWSsyuRh')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=http%3A%2F%2Fthetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F258111-3.jpg&iconimage=http%3A%2F%2Fthetvdb.com%2Fbanners%2F_cache%2Fposters%2F258111-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DDoc%20McStuffins%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fdoc-mcstuffins')
		list.append('&youtube_pl=PLPYC---L3hwnlVCfoRsIaZQNe9AlH29qn')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10776).encode('utf-8'),list,17,"http://thetvdb.com/banners/_cache/posters/258111-1.jpg",addonString(107760).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://thetvdb.com/banners/fanart/original/258111-3.jpg", default=background2))

def CATEGORIES107M(General_LanguageL, background, background2): #קוסמות קטנות
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%d7%a7%d7%95%d7%a1%d7%9e%d7%95%d7%aa%20%d7%a7%d7%98%d7%a0%d7%95%d7%aa&url=http%3a%2f%2fnickjr.walla.co.il%2ftvshow%2f2868088')
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=EL7Kwi-2OHjHb8Ech3jKvIAA')
			list.append('&youtube_pl=ELhvenPOtveGfHK6i3jbqadA')
			
		list.append('&youtube_id=D4upnryYMRg')
		list.append('&youtube_id=mmMMMyzfvKQ')
		list.append('&youtube_id=44hT8FaNbZE')
		list.append('&youtube_id=kBHYY8zRmxg')
		list.append('&youtube_id=PpBgWswnsOE')
		list.append('&youtube_id=')
		list.append('&youtube_id=')
		list.append('&youtube_id=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		if not 'Hebrew' in General_LanguageL:
			list.append('&youtube_pl=PLsv1SZnjW6ZuzgvBnbMi6BgQDjYj4cRco')
		list.append('&youtube_id=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10775).encode('utf-8'),list,17,'https://upload.wikimedia.org/wikipedia/en/thumb/f/fa/Little_Charmers_logo.png/250px-Little_Charmers_logo.png',addonString(107750).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.movieforkids.it/wp-content/gallery/little-charmers/little-charmers-gallery-03.jpg"))

def CATEGORIES107N(General_LanguageL, background, background2): #נווה עצלנות
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLC2852E1A22D382A1')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL7FsWouQE3dJaukpwjpnD50IzVXAxxb-C') #S1
		list.append('&youtube_pl=PL7FsWouQE3dKVvbyvNocnbpInq28ZNLwj') #S2
		list.append('&youtube_pl=PLdLyptOpDCB-dE7z29FmGBf-tCx7f0-FL') #S3
		list.append('&youtube_pl=PL7FsWouQE3dKZEmZCadk5UZrhw2Da41fT') #S4
		
		list.append('&youtube_pl=PLYCwKmRHMXmn5L0iZQ1y00HSJh71d8WMg') #S3-4
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=PL7FsWouQE3dIM8XnXfVZuJPcAsz3twbAR')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=PLE5sdZSqvbvMk21EU1JP_y4eeF-uUmLji')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PLOUaJirAnKynyYAl8yAnri-KfkPXNdqa1')
		list.append('&youtube_pl=PLLbxiiLXUaFM0WgYnlC3d47hsg92fVTQ4')
		
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=PL7FsWouQE3dLasHbbuqSRL87tNGiy_Tvt')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=PLeFjfBNzNSCKPTbWpPPi5C6VWaB-R7sYO')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLxqQkDUHTw9TWjjQepnaqVYN5Dmdrk6aa')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLnq_ewBXCOcjgzr5RzrdgRZJhgN9ewYwS')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PL7FsWouQE3dKuIUEQGsIPHfMMfLvNgpHL')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10853).encode('utf-8'),list,17,"http://vignette3.wikia.nocookie.net/lazyton/images/c/c3/Showim.jpg/revision/latest?cb=20101201033336",addonString(108530).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.sproutonline.com/sites/sprout/files/styles/og_image/public/2015/06/LazyTown.jpg?itok=lBTIwnce", default=background2))

def CATEGORIES107O(General_LanguageL, background, background2): #החיוך של רוזי
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLeN0KBWXUjSdGlqn1m6Wm-5WiXccsllzw') #S1?
		list.append('&youtube_pl=PLfcYs4SRZfuKA9uxEK0kvYZNOObplk5jK') #S2
		list.append('&youtube_pl=PLcqSsX5HgsNORun3Zr_QhsyrC5x4U0SpA') #S2+
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL5PocvG5yvl595PaTAiRoxuwJG7JeDS4U') #Episodes
		list.append('&youtube_pl=PL5PocvG5yvl4n8lXAOoCNc3U58V3mRcFv') #Compilation 
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=PLjYjlw0dz8jN1kYkaj-MrlrjO_SsvSB-6') #פרקים
		list.append('&youtube_pl=PLjYjlw0dz8jOKPrw5FUgI6tv8zKkYCLFD')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		
		list.append('&youtube_pl=PL0RKCbHd0Td-yp1UCsfczz8lRmvZiwBM-') #פרקים
		list.append('&youtube_pl=PLVEU_xzaPmHIYSnQrN07DOL0uv5kmUdeH') #פרקים
		list.append('&youtube_pl=PLVEU_xzaPmHJsbztwV8tCqKOGif2v_5xc') #
		list.append('&youtube_id=BAcXMR-RbaQ')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=PLw_nS0jRO9hOSsWpBSSAiBQ_MyFu-QGYl')
		list.append('&youtube_pl=PLw_nS0jRO9hO1JNDma5EcTTxlhGRYZu02')
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10747).encode('utf-8'),list,17,"http://ichef.bbci.co.uk/childrens-responsive-ichef/r/400/1x/cbeebies/everythings-rosie-brand-shelf.png",addonString(107470).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://cdn.kidscreen.com/wp/wp-content/uploads/2011/12/Rosie-Image-3.jpg?be18c6", default=background2))

def CATEGORIES107P(General_LanguageL, background, background2): #סימסאלה גרים
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.sdarot.tv/?image=http%3a%2f%2fwww.sdarot.wf%2fmedia%2fseries%2f1775.jpg&mode=3&name=simsala-grimm-%d7%a1%d7%99%d7%9e%d7%a1%d7%90%d7%9c%d7%94-%d7%92%d7%a8%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91&series_id=1775&series_name=simsala-grimm-%d7%a1%d7%99%d7%9e%d7%a1%d7%90%d7%9c%d7%94-%d7%92%d7%a8%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91&summary&url=http%3a%2f%2fwww.sdarot.wf%2fwatch%2f1775%2fsimsala-grimm-%d7%a1%d7%99%d7%9e%d7%a1%d7%90%d7%9c%d7%94-%d7%92%d7%a8%d7%99%d7%9d-%d7%9e%d7%93%d7%95%d7%91%d7%91')
		list.append('&youtube_pl=PLxd2PvjbApyUmvVaMyQsaiqJnu4tultQw')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=PL3LdfNhqqQ-lkrCGtZr4qT64R4jSNAPq9') #English
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&dailymotion_pl=x40l0a') #Italian
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=PL5F6MEqlxrutgoR4ko34udGRnqIa17SQw')
		list.append('&youtube_pl=PLMF8M8SSX_r_uNXHRi4Ok0ir1kWUbHf_J')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=PLE0E8C0EBEBEF2B91') #Hungarian
		list.append('&youtube_pl=PLPLEUSKqvS1fiNXQ4_BBl6QzxJ-LNsLQj') #Hungarian
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&dailymotion_pl=x43w3p') #Turkish
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PL233EF9C219ABEBAF') #Polish
		list.append('&youtube_pl=PL791C506E16CD04D0') #Polish
		list.append('&youtube_pl=PLEF555DBE90B29343') #Polish
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PL_YdHp9RZVekRyT2Jj3HuiprfI6ciaZGq') #French
		list.append('&youtube_pl=PLYznXvGjt-p6ZpcGt4LVlDJn8kjpZMktW') #French
		list.append('&youtube_pl=PLqDeN75S4o4vvX_oOzY3g2Xw-zJkKDyuJ') #French
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=PLaNUoV-bytVWmdW0RKpabFc7JlfXgu5bl') #Haitian
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=PLOa2BPz-EgJUvWd-41sFUJdt6GP0UBOdb') #Romanian
		list.append('&youtube_pl=PL0y1UAtK1ewhzeIAuaKq01QGDEaaDNZZ3') #Romanian
		list.append('&youtube_pl=PLJQRbRKq93tF_6MW-5DrmGVy184f0Cyf8') #Romanian
		list.append('&youtube_pl=PL9GAhjwHmKIS6W4LnOv1N9We7TWDiAs1y')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	
	addDir(addonString(10756).encode('utf-8'),list,17,thumb,addonString(107560).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://www.greenlightmedia.com/sites/default/files/styles/xxl/public/PI_02_col_1920.jpg?itok=u_4ZQtF1", default=background2))

def CATEGORIES107Q(General_LanguageL, background, background2): #רובו אוטו פולי
	'''קטנטנים'''
	thumb = 'https://ae01.alicdn.com/kf/HTB1Q_29IpXXXXckXpXXq6xXFXXXJ/4pcs-Set-Robocar-Poli-Robot-Car-Transformation-Toys-Action-Anime-Figure-Kids-Toys-Gifts.jpg'
	fanart = 'https://i.ytimg.com/vi/DE09Q2rcybs/maxresdefault.jpg'
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.wallaNew.video/?mode=2&module=nickjr&name=%f8%e5%e1%e5%20%e0%e5%e8%e5%20%f4%e5%ec%e9&url=http%3a%2f%2fnickjr.walla.co.il%2f%3fw%3d%2f%2f2688025')
		list.append('&youtube_pl=')
		
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_id=mZxJzyK59Uw') #S1
		list.append('&youtube_pl=PLcyqaXyZIttUEJlDocJ9DdyQqEaNY_Bex')
		list.append('&youtube_ch=roivisual')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=PLRcpGe2aAjX2GmzL56qAn-UU4COcZaIn4')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=PLRcpGe2aAjX2BupOW4IMJJ923BOFv-TwT')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_pl=PLRcpGe2aAjX1QQEEXSrYBUEbL5JddDt3w')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=PLRcpGe2aAjX09n2_u9PFnYFRTugODMvQx')	
		list.append('&youtube_pl=PLRcpGe2aAjX3Fl_VH1yc1uVdN3qggqEsO')
		list.append('&youtube_pl=PLRcpGe2aAjX1qN0JS5B2UxcBzkPqIEHVN')
		list.append('&youtube_pl=PLRcpGe2aAjX0cpReAbAxJg8pOn264UWxy')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=PL3zlK7az2OJ1HVLHDoryakaTzbJGuM7iW')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')
	
	addDir(addonString(10736).encode('utf-8'),list,17,thumb,addonString(107360).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))

def CATEGORIES107R(General_LanguageL, background, background2): #מטוסי על
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLfcYs4SRZfuKHBFMWhKcZuL39ZrLY-52P')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&custom8=plugin://plugin.video.bobbycart/?description=https%3A%2F%2Fwww.thetvdb.com%2Fbanners%2Ffanart%2Foriginal%2F295184-1.jpg&iconimage=https%3A%2F%2Fwww.thetvdb.com%2Fbanners%2F_cache%2Fposters%2F295184-1.jpg&mode=2&name=%5BB%5D%5BCOLOR%20white%5DSuper%20Wings!%5B%2FCOLOR%5D%5B%2FB%5D&url=http%3A%2F%2Fwww.toonget.net%2Fsuper-wings')
		list.append('&youtube_id=mkGiWDnFIus')
		if not 'Hebrew' in General_LanguageL: list.append('&youtube_pl=PLme6PyN3c6adNPYYS9DJrg8Z2ttd8yJlH')
		
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
		if not 'Hebrew' in General_LanguageL: list.append('&youtube_pl=PLWi6nzVYwR35t7pmzPm8lj22dyWLqGfpK')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10737).encode('utf-8'),list,17,"https://www.thetvdb.com/banners/_cache/posters/295184-1.jpg",addonString(107370).encode('utf-8'),'1',0,getAddonFanart(background, custom="https://www.thetvdb.com/banners/fanart/original/295184-1.jpg", default=background2))

def CATEGORIES107S(General_LanguageL, background, background2): #בוב הבנאי
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=PLfcYs4SRZfuK9TAppk-HTAKz5j1owAlaE')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_ch=bobthebuilderchannel')
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3A%2F%2F9cartoon.me%2Fuploads%2Fthumbs%2F2016-05-10bob-the-builder-construction-heroes-2015r.jpg%7CUser-Agent%3DMozilla%2F5.0%20(Windows%20NT%206.1%3B%20rv%3A32.0)%20Gecko%2F20100101%20Firefox%2F32.0%26Cookie%3D__cfduid%3Dd050ec12fafe2c97100f5553b706772be1471118127%3Bcf_clearance%3D0e975e4108a6438c67d99a6f5a87d50a10302f79-1483801877-86400%3B__cfduid%3Dd48ee3d5e8750d48c2c735e712c4476201468881294%3B__cfduid%3Dde0bb4156da99183db0cc6a7c8325a0041470303966%3BPHPSESSID%3D86f31d8264a864fcba222bbadb97477b%3BPHPSESSID%3D0918e9805af889f932d3f1f7083de44b%3BPHPSESSID%3D71nhps357p41n36mj2h76hs486%3B&mode=2&name=Bob%20the%20Builder%3A%20Construction%20Heroes!%20(2015)&url=http%3A%2F%2F9cartoon.me%2FCartoon%2F10189%2Fbob-the-builder-construction-heroes-2015%2F')
		list.append('&custom8=plugin://plugin.video.cartoons8/?description&iconimage=http%3A%2F%2F9cartoon.me%2Fuploads%2Fthumbs%2F2015-11-11bob-the-builder-season-19-20159.jpg%7CUser-Agent%3DMozilla%2F5.0%20(Windows%20NT%206.1%3B%20rv%3A32.0)%20Gecko%2F20100101%20Firefox%2F32.0%26Cookie%3D__cfduid%3Dd050ec12fafe2c97100f5553b706772be1471118127%3Bcf_clearance%3D0e975e4108a6438c67d99a6f5a87d50a10302f79-1483801877-86400%3B__cfduid%3Dd48ee3d5e8750d48c2c735e712c4476201468881294%3B__cfduid%3Dde0bb4156da99183db0cc6a7c8325a0041470303966%3BPHPSESSID%3D86f31d8264a864fcba222bbadb97477b%3BPHPSESSID%3D0918e9805af889f932d3f1f7083de44b%3BPHPSESSID%3D71nhps357p41n36mj2h76hs486%3B&mode=2&name=Bob%20the%20Builder%20Season%2019%20(2015)&url=http%3A%2F%2F9cartoon.me%2FCartoon%2F8876%2Fbob-the-builder-season-19-2015%2F')
		list.append('&youtube_id=h-5QPsTUQh4') #Episodes 11 - 20
		list.append('&youtube_id=3Zs4Zv3otpY') #Season 19 Episodes 1-10
		list.append('&youtube_id=msDQWiy5Bs4') #Season 19 Episode 21-30
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_ch=UCHnky6FROOhC7-EhVNdGhRw')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_ch=UC1gSKVovUYLmXoDnsTY039Q')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_ch=UCeX7M-YZnZYNV3HMb2VqBGQ')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_ch=UC-mRe05y88F1seMgOvbHAEQ')
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(10707).encode('utf-8') + space + '+',list,17,'http://www.hop.co.il/wp-content/uploads/2014/07/%D7%AA.%D7%96-%D7%91%D7%95%D7%91-%D7%94%D7%91%D7%A0%D7%90%D7%99.jpg',addonString(107070).encode('utf-8'),'1',0,getAddonFanart(background, custom="http://cdn.awn.com/sites/default/files/styles/original/public/image/featured/1027370-new-int-l-deals-announced-bob-builder.jpg?itok=Qwec2np0"))

def CATEGORIES107T(General_LanguageL, background, background2): #
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(108980).encode('utf-8'),list,17,"",addonString(108980).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))

def CATEGORIES107U(General_LanguageL, background, background2): #
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(108980).encode('utf-8'),list,17,"",addonString(108980).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))

def CATEGORIES107V(General_LanguageL, background, background2): #
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(108980).encode('utf-8'),list,17,"",addonString(108980).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))

def CATEGORIES107W(General_LanguageL, background, background2): #
	'''קטנטנים'''
	thumb = ''
	fanart = ''
	list = []
	
	'''עברית'''
	if 'Hebrew' in General_LanguageL:
		list.append('&youtube_pl=')
	'''אנגלית'''
	if 'English' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	'''אוזבקית'''
	if 'Uzbek' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''איטלקית'''
	if 'Italian' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''אוקראינית'''
	if 'Ukrainian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אינדונזית'''
	if 'Indonesian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''אירית'''
	if 'Irish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''בולגרית'''
	if 'Bulgarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גאורגית'''
	if 'Georgian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''גרמנית'''
	if 'German' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''דנית'''
	if 'Dansk' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''הודית'''
	if 'Hindi' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הולנדית'''
	if 'Dutch' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''הונגרית'''
	if 'Hungarian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''טורקית'''
	if 'Turkish' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
		list.append('&youtube_pl=')
	
	'''יוונית'''
	if 'Greek' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''יפנית'''
	if 'Japanese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סינית'''
	if 'Chinese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סלובקית'''
	if 'Slovak' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''ספרדית'''
	if 'Spanish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''סרבית'''
	if 'Serbian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פולנית'''
	if 'Polish' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פורטוגזית'''
	if 'Portuguese' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''פינית'''
	if 'Finnish' in General_LanguageL:
		list.append('&youtube_pl=')

	'''ערבית'''
	if 'Arabic' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''צ'כית'''
	if 'Czech' in General_LanguageL:
		list.append('&youtube_pl=')
		list.append('&youtube_id=')
		
	'''צרפתית'''
	if 'French' in General_LanguageL:
		list.append('&youtube_id=')
	
	'''קוריאנית'''
	if 'Korean' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קזחית'''
	if 'Kazakh' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קטלאנית'''
	if 'Catalan' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''קריאולית האיטית'''
	if 'Haitian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רומנית'''
	if 'Romanian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''רוסית'''
	if 'Russian' in General_LanguageL:
		list.append('&youtube_pl=')
	
	'''שוודית'''
	if 'Swedish' in General_LanguageL:
		list.append('&youtube_pl=')
		
	'''תאילנדית'''
	if 'Thai' in General_LanguageL:
		list.append('&youtube_pl=')

	addDir(addonString(108980).encode('utf-8'),list,17,"",addonString(108980).encode('utf-8'),'1',0,getAddonFanart(background, custom=fanart, default=background2))
