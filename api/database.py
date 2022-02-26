import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker


FSRT_DB_HOST = os.environ.get('FSTR_DB_HOST')
FSTR_DB_PORT = os.environ.get('FSTR_DB_PORT')
FSTR_LOGIN = os.environ.get('FSTR_LOGIN')
FSTR_PASS = os.environ.get('FSTR_PASS')

DATABASE_URL = f"postgresql://{FSTR_LOGIN}:{FSTR_PASS}@{FSRT_DB_HOST}:{FSTR_DB_PORT}/HakatonSK" #change base name to pereval

engine = create_engine(DATABASE_URL)

metadata = MetaData()
metadata.reflect(engine)
Base = automap_base(metadata=metadata)
Base.prepare()

Added = Base.classes.pereval_added
Areas = Base.classes.pereval_areas
Images = Base.classes.pereval_images
Activities_types = Base.classes.spr_activities_types

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)