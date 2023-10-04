import strawberry

@strawberry.type
class Item:
    id: strawberry.ID
    name: str
    # Resolver functions for the Query type
    # In-memory data store 
    def __init__(self, id: strawberry.ID, name: str):
        self.id = id
        self.name = name
items = []

    # Sample data
sample_data = [
    {"id": "1", "name": "Item 1"},
    {"id": "2", "name": "Item 2"},
    {"id": "3", "name": "Item 3"},
]

    # Populate the items list with sample data
for data in sample_data:
    item = Item(id=data["id"], name=data["name"])
    items.append(item)




    # Helper function to find an item by ID
def find_item_by_id(item_id):
    for item in items:
        if item.id == item_id:
            return item
    return None
@strawberry.type
class Query:
    @strawberry.field
    def item(self, info, id: strawberry.ID) -> Item:
        # Find and return an item by ID from the data store
        return find_item_by_id(id)
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, name: str) -> Item:
        # Implement your logic to create an item here
        import uuid
        item_id = str(uuid.uuid4())

        # Create a new item and add it to the data store
        new_item = Item(id=item_id, name=name)
        items.append(new_item)

        return new_item

    @strawberry.mutation
    def update_item(self, id: strawberry.ID, name: str) -> Item:
        # Implement your logic to update an item here
        item = find_item_by_id(id)
        
        if not item:
            raise Exception("Item not found")

    # Update the item's name
        item.name = name

        return item
    @strawberry.mutation
    def delete_item(self, id: strawberry.ID) -> bool:
        # Implement your logic to delete an item here
        item = find_item_by_id(id)

        if not item:
            raise Exception("Item not found")

    # Remove the item from the data store
        items.remove(item)
        return True

schema = strawberry.Schema(query=Query, mutation=Mutation)

    