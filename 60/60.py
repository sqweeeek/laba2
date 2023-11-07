class Store:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        keys = key.split('.')
        cur_data = self.data
        for i, k in enumerate(keys):
            if k not in cur_data:
                if i == len(keys) - 1:
                    cur_data[k] = value
                else:
                    cur_data[k] = {}
            cur_data = cur_data[k]

    def get(self, key):
        keys = key.split('.')
        cur_data = self.data
        for k in keys:
            if k in cur_data:
                cur_data = cur_data[k]
            else:
                return None
        return cur_data

    def update(self, key, value):
        exist_data = self.get(key)
        if exist_data is not None:
            exist_data.update(value)

    def delete(self, key):
        keys = key.split('.')
        cur_data = self.data
        for i, k in enumerate(keys):
            if k in cur_data:
                if i == len(keys) - 1:
                    del cur_data[k]
                else:
                    cur_data = cur_data[k]


store = Store()

store.set('key', {'a': 1, 'b': 2, 'c': 3})

res = store.get('key')
print(res)

res = store.get('key.a')
print(res)

res = store.get('key.b')
print(res)

store.update('key', {'d': 4})
res = store.get('key.d')
print(res)

store.delete('key.c')
res = store.get('key.c')
print(res)