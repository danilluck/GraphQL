import strawberry
import uvicorn
from fastapi import FastAPI

from configs import DatabaseSession

from app.query import Query
from app.mutation import Mutation

from strawberry.fastapi import GraphQLRouter


def init_app():
    db = DatabaseSession()
    app = FastAPI(
        title="GraphQL API",
        description="Test FastAPI GraphQL CRUD App",
        version="1.0.0"
    )

    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    # add graphql endpoint
    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    app.include_router(graphql_app, prefix="/graphql")

    return app


app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)