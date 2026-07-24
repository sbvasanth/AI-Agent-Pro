from unittest.mock import patch
from datetime import datetime

from src.tools.system_tools import current_time


@patch("src.tools.system_tools.datetime")
def test_current_time(mock_datetime):
    """
    Verify current_time() returns the expected formatted datetime.
    """

    fake_time = datetime(2026, 7, 21, 14, 30, 45)

    mock_datetime.now.return_value = fake_time

    result = current_time.invoke({})

    assert result == "21-07-2026 14:30:45"
