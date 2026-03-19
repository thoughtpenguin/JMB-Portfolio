import pytest
from datetime import datetime

pytest.main(['SeleniumTests/', '--html=results/SeleniumResults-' + str(datetime.now()) + '.html'])