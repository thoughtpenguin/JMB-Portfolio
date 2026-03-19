import pytest
from datetime import datetime

pytest.main(['APITests/', '--html=results/AllAPITests-' + str(datetime.now()) + '.html'])