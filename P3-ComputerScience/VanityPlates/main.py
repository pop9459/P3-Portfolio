from endpoints import *
from db_handler import *


# ##### Main execution #####
if __name__ == "__main__":
    db_initialize()
    flask_api.run(debug=True)