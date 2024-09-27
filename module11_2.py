import inspect
import sys
from pprint import pprint

def introspection_info(obj):
    info_dict = {}
    attributes = []
    methods = []
    for i in dir(obj):
        attribute = getattr(obj, i)
        if callable(attribute):
            methods.append(f'Метод: {i}')
        else:
            attributes.append(f'Атрибут: {i}')
    info_dict['Тип объекта'] = type(obj).__name__
    info_dict['Принадлежит модулю'] = obj.__class__.__module__
    info_dict['Атрибуты'] = attributes
    info_dict['Методы'] = methods
    info_dict['Является ли модулем?'] = inspect.ismodule(obj)
    if hasattr(obj, '__doc__') and obj.__doc__:
        info_dict['Документация'] = obj.__doc__.strip()

    return info_dict


number_info = introspection_info(46)
pprint(number_info)
