# Ошибки

```python
def get_age(self):  
    now = datetime.datetime.now()  
    return self.yob - now.year #неправильно 
    return now.year - self.yob
```

    

2. def set_name(self, name):  
    ~~self.name = self.name~~  __self.name = name__  

3. def set_address(self, address):  
    ~~self.address == address~~ __self.address = address__