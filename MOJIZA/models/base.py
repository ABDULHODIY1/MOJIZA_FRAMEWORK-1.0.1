class Field:
    def __init__(self, field_type):
        self.field_type = field_type

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super(ModelMeta, cls).__new__(cls, name, bases, attrs)
        new_class._fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                new_class._fields[key] = value
        return new_class

class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field in self._fields:
            setattr(self, field, kwargs.get(field))

    def save(self):
        # Oddiy saqlash funksiyasi (masalan, faylga yozish yoki konsolga chiqarish)
        print(f"Saving {self.__class__.__name__}: {self.__dict__}")
