from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['sarah'] = 'c'
favorite_languages['jen'] = 'python'
favorite_languages['phil'] = 'python'
favorite_languages['edward'] = 'ruby'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+ language.title() + ".")




