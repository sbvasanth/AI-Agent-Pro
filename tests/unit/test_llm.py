from unittest.mock import patch
from src.llm import get_llm


@patch("src.llm.os.getenv")
@patch("src.llm.ChatGroq")
def test_get_llm(mock_chatgroq, mock_getenv):

    mock_getenv.return_value = "fake_api_key"

    get_llm()

    mock_chatgroq.assert_called_once_with(
        model="openai/gpt-oss-20b",
        api_key="fake_api_key",
        temperature=0,
    )
