from api            import app
from config.config  import *
from modules.post   import *
from modules.get    import *
from modules.put    import *
from modules.delete import *


if __name__ == "__main__":
    app.run(debug=True)
