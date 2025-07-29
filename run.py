import logging
from app import create_app

logging.basicConfig(level=logging.INFO)

app = create_app()

ASCII_ART = r"""

  ______      __              ______                     __
 /_  __/___  / /_____  ____  / ____/_  ______ __________/ /     TokenGuard 1.0.0
  / / / __ \/ //_/ _ \/ __ \/ / __/ / / / __ `/ ___/ __  /      Created by Kopilets I.S.
 / / / /_/ / ,< /  __/ / / / /_/ / /_/ / /_/ / /  / /_/ /  
/_/  \____/_/|_|\___/_/ /_/\____/\__,_/\__,_/_/   \__,_/        https://github.com/23kopa/site23
                                
"""

if __name__ == '__main__':
    print(ASCII_ART)
    app.run(
        host='0.0.0.0',
        port=5000
    )
