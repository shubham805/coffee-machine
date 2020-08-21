from typing import List

from app.entities.entity import Entity


class Repository:
    entity_class = Entity

    def __init__(self, store: dict):
        if store is None:
            store = {}
        self._store = store

    def update(self, entity: Entity) -> Entity:
        self._store[entity.id] = vars(entity)
        return self.entity_class.from_dict(self._store[entity.id])

    def get_all(self) -> List[Entity]:
        return [self.entity_class.from_dict(entity) for entity in list(self._store.values())]

    def get_by_ids(self, ids: List[str]) -> List[Entity]:
        entities = list(filter(None, [self._store.get(entity_id) for entity_id in ids]))
        return [
            self.entity_class.from_dict(entity) for entity in entities]

    def get_by_id(self, entity_id: str) -> Entity:
        entity = self._store.get(entity_id)
        if entity is None:
            return None
        return self.entity_class.from_dict(entity)
