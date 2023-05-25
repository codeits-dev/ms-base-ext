import graphene

from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphene.types.generic import GenericScalar


import codeits.db.graphene.types as t
from codeits.db.graphene.util import UtilGraphene
from codeits.db.sql.util import UtilSQLAlchemy

import db.postgres.models as m

###############################################################################
# Person Schema
###############################################################################
class Person(SQLAlchemyObjectType):
    class Meta:
        model = m.Person
        
class PersonPaginableType(t.PaginableType):
    items = graphene.List(Person,source="items")
    
class PersonQuery(graphene.ObjectType):
    all_persons = graphene.Field(PersonPaginableType,
        offset=graphene.Int(required=False),
        limit=graphene.Int(),
        page=graphene.Int(),
        query=t.JSON(),
        sort=t.JSON()
    )
    
    def resolve_all_persons(parent, info,**kwargs):
        return UtilGraphene.as_paginable(m.Person.all_persons(**kwargs))

class PersonMutation(graphene.Mutation):
    class Arguments:
        person_args = t.JSON()
    
    person = graphene.Field(lambda: Person)
    
    def mutate(self, info,  **kwargs):
        print("[PersonMutation]",kwargs)
        p = m.Person.create(**kwargs['person_args'])
        return PersonMutation(person=p)
    
###############################################################################

class Mutations(graphene.ObjectType):
    person_create = PersonMutation.Field()    
    pass
    
    
class Querys(
    PersonQuery
):
	pass