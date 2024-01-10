class TreeStore:
    def __init__(self, object_list):
        """
        Инициализирует объект TreeStore.

        Parameters
        ----------
        object_list : list
            Список объектов, каждый из которых содержит поля id, parent и некоторый набор других полей.
        """
        self.tree = {}             # Словарь всех элементов
        self.parents = {}          # Словарь для хранения связей

        for obj in object_list:
            item_id = obj["id"]
            parent_id = obj["parent"]
            self.tree[item_id] = obj
            if parent_id not in self.parents:
                self.parents[parent_id] = []  # Если у элемента нет дочерних, возвращаем пустой массив
            self.parents[parent_id].append(obj)

    def getAll(self):
        """
        Возвращает все объекты.

        Returns
        -------
        list
            Список всех объектов.
        """
        return list(self.tree.values())

    def getItem(self, item_id):
        """
        Возвращает объект по заданному item_id.

        Parameters
        ----------
        item_id : int
            Идентификатор объекта.

        Returns
        -------
        dict or None
            Объект с указанным item_id или None, если объект не найден.
        """
        return self.tree.get(item_id, None)

    def getChildren(self, parent_id):
        """
        Возвращает дочерние объекты по заданному parent_id.

        Parameters
        ----------
        parent_id : int or str
            Идентификатор родительского объекта.

        Returns
        -------
        list of dict
            Список дочерних объектов или пустой список, если дочерних объектов нет.
        """
        return self.parents.get(parent_id, [])

    def getAllParents(self, item_id):
        """
        Возвращает список родительских объектов, начиная от текущего объекта к корневому


        Parameters
        ----------
        item_id : int
            Идентификатор объекта.

        Returns
        -------
        list
            Список родительских объектов в порядке от текущего объекта к корневому.
        """
        parents = []

        # Обходим дерево от текущего объекта до корневого объекта
        while item_id in self.tree:
            parent = self.tree[item_id]
            parents.append(parent)
            item_id = parent["parent"]

        return parents


# Исходные данные
items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

# Примеры использования:
print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))
