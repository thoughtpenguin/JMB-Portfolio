import pytest
from datetime import datetime

pytest.main(['SeleniumTests/', '--html=results/AllSeleniumTests-' + str(datetime.now()) + '.html'])