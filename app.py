import os

from dotenv import load_dotenv

from app import create_app, db_manager
from app.models.boiler_plate_object_1 import BoilerPlateObject1
from app.models.boiler_plate_object_2 import BoilerPlateObject2

# Load environment variables from .flaskenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db_manager,
        BoilerPlateObject1=BoilerPlateObject1,
        BoilerPlateObject2=BoilerPlateObject2,
    )
