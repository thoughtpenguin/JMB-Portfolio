import pytest
from datetime import datetime

pytest.main(['APITests/', '--html=results/APITestResults' + str(datetime.now()) + '.html'])