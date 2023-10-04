from strawberry.asgi import GraphQL
from starlette.applications import Starlette
from starlette.routing import Route
from schema import schema

app = Starlette(routes=[Route("/", GraphQL(schema))])
