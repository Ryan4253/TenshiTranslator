"""
Name conversion tables. This is series-dependent
"""


"""
Name conversion table from Kanji to Katakana

Prevents names with meaning from affecting the translation
This is recommended to be used with the online translator where a character limit is imposed
"""
JAPANESE_TO_KATAKANA = {
    '藤宮'   : 'フジミヤ', 
    '志保子' : 'シホコ', 
    '修斗'   : 'フブキ', 
    '椎名'   : 'シイナ', 
    '真昼'   : 'マヒル', 
    '小夜'   : 'コヨル', 
    '朝陽'   : 'アサヒ', 
    '赤澤'   : 'アカザワ', 
    '樹'     : 'イツキ', 
    '大輝'   : 'タイキ', 
    '白河'   : 'シラカワ', 
    '千歳'   : 'チトセ', 
    '門脇'   : 'カドワキ', 
    '優太'   : 'ユウタ', 
    '九重'   : 'ココノエ', 
    '柊'     : 'ヒイラギ',
    '一哉'   : 'カズヤ',
    '木戸'   : 'キド',
    '彩香'   : 'アヤカ',
    '茅野'   : 'タツキ',
    '総司'   : 'ソウジ',
    '糸巻'   : 'イトマキ',
    '文華'   : 'フミカ',
    '大橋'   : 'オオハシ',
    '莉乃'   : 'リノ',
    '宮本'   : 'ミヤモト',
    '大地'   : 'ダイチ'
}

"""
Name conversion table from Kanji to English

Prevents names with meaning from affecting the translation. More accurate than katakana replacements
This is recommended to be used with the offline translator 
"""
JAPANESE_TO_ENGLISH = {
    '藤宮'     : 'Fujimiya', 
    '志保子'   : 'Shihoko', 
    '修斗'     : 'Shuuto', 
    '椎名'     : 'Shiina', 
    '真昼'     : 'Mahiru', 
    'まひるん' : 'Mahirun',
    '小夜'     : 'Koyoru', 
    '朝陽'     : 'Asahi', 
    '赤澤'     : 'Akazawa', 
    '樹'       : 'Itsuki', 
    '大輝'     : 'Daiki', 
    '白河'     : 'Shirakawa', 
    '千歳'     : 'Chitose', 
    '門脇'     : 'Kadowaki', 
    '優太'     : 'Yuuta', 
    '九重'     : 'Kokonoe', 
    '柊'       : 'Hiiragi',
    '一哉'     : 'Kazuya',
    '木戸'     : 'Kido',
    '彩香'     : 'Ayaka',
    '茅野'     : 'Kayano',
    '総司'     : 'Souji',
    '糸巻'     : 'Itomaki',
    '文華'     : 'Fumika',
    '大橋'     : 'Oohashi',
    '莉乃'     : 'Rino',
    '宮本'     : 'Miyamoto',
    '大地'     : 'Daichi'
}

"""
Correction table to correct any incorrectly translated names

Left side uses regex to prevent misreplacements
"""
ENGLISH_CORRECTION = {
    'Zhou'    : 'Amane',
    'Shu '    : 'Amane',
    'Shu-'    : 'Amane-',
    'Shu\.'   : 'Amane.',
    'Fubuki'  : 'Shuuto',
    'Fubuchi' : 'Shuuto',
    'Shina'   : 'Shiina',
    'mahiru'  : 'Mahiru',
    'Kojou'   : 'Koyoru',
    'Coconoe' : 'Kokonoe',
    'Tatsuki' : 'Kayano',
    'Itmaki'  : 'Itomaki',
    'Ituki'   : 'Itsuki'
}

