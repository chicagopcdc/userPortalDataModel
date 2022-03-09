from . import Base
from cdislogging import get_logger
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy import String, Column, MetaData, Table, Enum, Integer, Text
from .models import *  # noqa


class SQLAlchemyDriver(object):
    def __init__(self, conn, ignore_db_error=True, **config):
        """
        setup sqlalchemy engine and session
        Args:
            conn (str): database connection
            ignore_db_error (bool): whether to ignore database setup error,
                default to True because it errors out whenever you start
                multiple servers in parallel for new db
            config (dict): engine configuration
        """
        self.engine = create_engine(conn, **config)
        self.logger = get_logger("SQLAlchemyDriver")

        Base.metadata.bind = self.engine
        self.Session = sessionmaker(bind=self.engine, expire_on_commit=False)
        if ignore_db_error:
            try:
                self.setup_db()
            except Exception:
                self.logger.exception("Fail to setup database tables, continue anyways")
                pass
        else:
            self.setup_db()

    def setup_db(self):
        self.pre_migrate()
        Base.metadata.create_all()
        self.post_migrate()

    @property
    @contextmanager
    def session(self):
        """
        Provide a transactional scope around a series of operations.
        """
        session = self.Session()

        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_or_create(self, session, model, query, props=None):
        """
        Get or create a row
        Args:
            session: sqlalchemy session
            model: the ORM class from userdatamodel.models
            query: a dict of query parameters
            props: extra props aside from query to be added to the object on
                   creation
        Returns:
            result object of the model class
        """
        result = session.query(model).filter_by(**query).first()
        if result is None:
            args = props if props is not None else {}
            args.update(query)
            result = model(**args)
            session.add(result)
        return result

    def pre_migrate(self):
        """
        migration script to be run before create_all
        """
        if not self.engine.dialect.supports_alter:
            print(
                "This engine dialect doesn't support altering"
                " so we are not migrating even if necessary!"
            )
            return

        if not self.engine.dialect.has_table(
            self.engine, "Group"
        ) and self.engine.dialect.has_table(self.engine, "research_group"):
            print("Altering table research_group to group")
            with self.session as session:
                session.execute('ALTER TABLE research_group rename to "Group"')

    def post_migrate(self):
        md = MetaData()


        # add_foreign_key_column_if_not_exist(
        #     table_name=User.__tablename__,
        #     column_name="google_proxy_group_id",
        #     column_type=String,
        #     fk_table_name=GoogleProxyGroup.__tablename__,
        #     fk_column_name="id",
        #     driver=self,
        #     metadata=md,
        # )

        add_column_if_not_exist(
                table_name=Search.__tablename__,
                column=Column("filter_source", Enum(FilterSourceType)),
                driver=self,
                metadata=md,
            )
        add_column_if_not_exist(
                table_name=Search.__tablename__,
                column=Column("filter_source_internal_id", Integer),
                driver=self,
                metadata=md,
            )

        add_column_if_not_exist(
                table_name=Project.__tablename__,
                column=Column("name", String, nullable=True),
                driver=self,
                metadata=md,
            )
        add_column_if_not_exist(
                table_name=Project.__tablename__,
                column=Column("approved_url", String, nullable=True, default=None),
                driver=self,
                metadata=md,
            )

        add_value_to_existing_enum(
                table_name=Search.__tablename__, 
                column_name="filter_source", 
                driver=self,
                enum_obj=FilterSourceType,
                enum_name="filtersourcetype"
            )
        change_column_type_if_exist(
                table_name=Search.__tablename__, 
                column_name="ids_list", 
                driver=self, 
                column_type="text",
                metadata=md
            )


        # col_names = ["filter_souce", "filter_souce_internal_id"]
        # for col in col_names:
        #     add_column_if_not_exist(
        #         table_name=Search.__tablename__,
        #         column=Column(col, String),
        #         driver=self,
        #         metadata=md,
        #     )

def add_value_to_existing_enum(table_name, column_name, driver, enum_obj, enum_name):
    enum_name = enum_name
    tmp_enum_name = "tmp_" + enum_name
    with driver.session as session:
        # SHOULD work on PSQL >= 12 TODO test it
        # rs = session.execute(
        #         """\
        #         select array_agg(e.enumlabel) as enum_values
        #         from pg_type t 
        #             join pg_enum e on t.oid = e.enumtypid  
        #             join pg_catalog.pg_namespace n ON n.oid = t.typnamespace
        #         where t.typname = '{}'
        #         group by n.nspname, t.typname;
        #         """.format(enum_name)
        #     ).fetchall()

        # db_value = rs[0][0]
        # new_value = [e.value for e in enum_obj]

        # db_value.sort()
        # new_value.sort()

        # if db_value == new_value: 
        #     print ("The Enum {} is already up to date. skip.".format(enum_name)) 
        # else:
        #     for value in new_value:
        #         if value not in db_value:
        #             session.execute(
        #                 """\
        #                 ALTER TYPE {} ADD VALUE '{}';
        #                 """.format(enum_name, value)
        #             )

        # WORKAROUND FOr ABOVE  for lower version of psql
        rs = session.execute(
                """\
                select array_agg(e.enumlabel) as enum_values
                from pg_type t 
                    join pg_enum e on t.oid = e.enumtypid  
                    join pg_catalog.pg_namespace n ON n.oid = t.typnamespace
                where t.typname = '{}'
                group by n.nspname, t.typname;
                """.format(enum_name)
            ).fetchall()

        db_value = rs[0][0]
        new_value = [e.value for e in enum_obj]

        db_value.sort()
        new_value.sort()

        if db_value == new_value: 
            print ("The Enum {} is already up to date. skip.".format(enum_name)) 
        else:
            for value in new_value:
                if value not in db_value:
                    session.execute(
                        """\
                        ALTER TYPE {} ADD VALUE '{}';
                        """.format(enum_name, value)
                    )


            for value in new_value:
                if value not in db_value:
                    session.execute(
                        """\
                        INSERT INTO pg_enum (enumtypid, enumlabel, enumsortorder)
                            SELECT '{}'::regtype::oid, '{}', ( SELECT MAX(enumsortorder) + 1 FROM pg_enum WHERE enumtypid = '{}'::regtype )
                        """.format(enum_name, value, enum_name)
                    )




        # PREVIOUS VERSIONS
        # APPROACH 1

        # session.execute(
        #     """\
        #     BEGIN;
        #     LOCK TABLE {} IN ACCESS EXCLUSIVE MODE;
        #     select 1 from {};
        #     """.format(table_name, table_name)
        # )

        # rs = session.execute(
        #         """\
        #         select array_agg(e.enumlabel) as enum_values
        #         from pg_type t 
        #             join pg_enum e on t.oid = e.enumtypid  
        #             join pg_catalog.pg_namespace n ON n.oid = t.typnamespace
        #         where t.typname = '{}'
        #         group by n.nspname, t.typname;
        #         """.format(enum_name)
        #     ).fetchall()

        # print(rs)
        # db_value = rs[0][0]
        # new_value = [e.value for e in enum_obj]

        # db_value.sort()
        # new_value.sort()

        # if db_value == new_value: 
        #     print ("The Enum {} is already up to date. skip.".format(enum_name)) 
        #     session.execute(
        #         """\
        #         COMMIT WORK;
        #         """
        #     )
        # else:
        #     # CHECK FOR LOCK
        #     # rs = session.execute(
        #     #         """\
        #     #         select * from pg_locks l
        #     #         join pg_class t on l.relation = t.oid
        #     #         where t.relname = {};
        #     #         """.format(table_name)
        #     #     ).fetchall()


        #     session.execute(
        #         'ALTER TYPE {} RENAME TO {};'.format(
        #             enum_name, tmp_enum_name
        #         )
        #     )
        #     # DROP TYPE IF EXISTS
        #     # Create new enum type in db
        #     Enum(enum_obj).create(session.get_bind(), checkfirst=True)

        #     session.execute(
        #         """\
        #         COMMIT WORK;
        #         """
        #     )

        #     # Update column to use new enum type
        #     session.execute(
        #         'ALTER TABLE {} ALTER COLUMN {} TYPE {} USING ({}::text::{});'.format(
        #             table_name, column_name, enum_name, column_name, enum_name
        #         )
        #     )
        
        #     # Drop old enum type
        #     session.execute('DROP TYPE ' + tmp_enum_name)
        #     # session.commit()
        #     # session.execute(
        #     #     """\
        #     #     COMMIT WORK;
        #     #     """
        #     # )

        #ALTER TABLE table_name
        #     ALTER COLUMN column_name TYPE VARCHAR(255);
        # Drop and create again request_type enum:
        # DROP TYPE IF EXISTS request_type;
        # CREATE TYPE request_type AS ENUM (
        #     'OLD_VALUE_1',
        #     'OLD_VALUE_2',
        #     'NEW_VALUE_1',
        #     'NEW_VALUE_2'
        # );
        # Revert type from varchar to request_type for all columns/tables (revert step one):
        # ALTER TABLE table_name
        #     ALTER COLUMN column_name TYPE request_type
        #     USING (column_name::request_type);

        # APPROACH 2
        # DO $$
        # BEGIN
        #     IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'my_type') THEN
        #         CREATE TYPE my_type AS
        #         (
        #             --my fields here...
        #         );
        #     END IF;
        #     --more types here...
        # END$$;


def change_column_type_if_exist(table_name, column_name, driver, column_type, metadata):
    table = Table(table_name, metadata, autoload=True, autoload_with=driver.engine)
    if str(column_name) not in table.c:    
        print("ERROR: Column {} not in table {} - can't change the column type".format(column_name, table_name))
        return

    for c in table.c:
        if c.name == column_name and c.type != column_type:
            with driver.session as session:
                # Update column to use new type
                session.execute(
                    'ALTER TABLE {} ALTER COLUMN {} TYPE {};'.format(
                        table_name, column_name, column_type
                    )
                )
                session.commit()
        
def add_foreign_key_column_if_not_exist(
    table_name,
    column_name,
    column_type,
    fk_table_name,
    fk_column_name,
    driver,
    metadata,
):
    column = Column(column_name, column_type)
    add_column_if_not_exist(table_name, column, driver, metadata)
    add_foreign_key_constraint_if_not_exist(
        table_name, column_name, fk_table_name, fk_column_name, driver, metadata
    )

def drop_foreign_key_column_if_exist(table_name, column_name, driver, metadata):
    drop_foreign_key_constraint_if_exist(table_name, column_name, driver, metadata)
    drop_column_if_exist(table_name, column_name, driver, metadata)

def add_column_if_not_exist(table_name, column, driver, metadata):
    column_name = column.compile(dialect=driver.engine.dialect)
    column_type = column.type.compile(driver.engine.dialect)

    table = Table(table_name, metadata, autoload=True, autoload_with=driver.engine)
    if str(column_name) not in table.c:
        with driver.session as session:
            session.execute(
                'ALTER TABLE "{}" ADD COLUMN {} {};'.format(
                    table_name, column_name, column_type
                )
            )
            session.commit()

def drop_column_if_exist(table_name, column_name, driver, metadata):
    table = Table(table_name, metadata, autoload=True, autoload_with=driver.engine)
    if column_name in table.c:
        with driver.session as session:
            session.execute(
                'ALTER TABLE "{}" DROP COLUMN {};'.format(table_name, column_name)
            )
            session.commit()

def add_foreign_key_constraint_if_not_exist(
    table_name, column_name, fk_table_name, fk_column_name, driver, metadata
):
    table = Table(table_name, metadata, autoload=True, autoload_with=driver.engine)
    foreign_key_name = "{}_{}_fkey".format(table_name.lower(), column_name)

    if column_name in table.c:
        foreign_keys = [fk.name for fk in getattr(table.c, column_name).foreign_keys]
        if foreign_key_name not in foreign_keys:
            with driver.session as session:
                session.execute(
                    'ALTER TABLE "{}" ADD CONSTRAINT {} FOREIGN KEY({}) REFERENCES {} ({});'.format(
                        table_name,
                        foreign_key_name,
                        column_name,
                        fk_table_name,
                        fk_column_name,
                    )
                )
                session.commit()

def drop_foreign_key_constraint_if_exist(table_name, column_name, driver, metadata):
    table = Table(table_name, metadata, autoload=True, autoload_with=driver.engine)
    foreign_key_name = "{}_{}_fkey".format(table_name.lower(), column_name)

    if column_name in table.c:
        foreign_keys = [fk.name for fk in getattr(table.c, column_name).foreign_keys]
        if foreign_key_name in foreign_keys:
            with driver.session as session:
                session.execute(
                    'ALTER TABLE "{}" DROP CONSTRAINT {};'.format(
                        table_name, foreign_key_name
                    )
                )
                session.commit()



