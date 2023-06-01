import pytest
import responses
from http import HTTPStatus
from api import get_transactions


@responses.activate
def test_get_transactions_success(mocker):
    """Test get_transactions function successfully returns transactions"""

    # Mock transactions data
    mock_transactions = {
        "status": "1",
        "message": "OK",
        "result": [
            {
                "blockNumber": "4730207",
                "timeStamp": "1513240363",
                "hash": "0xe8c208398bd5ae8e4c237658580db56a2a94dfa0ca382c99b776fa6e7d31d5b4",
                "gas": "940000",
                "gasPrice": "32010000000",
                "gasUsed": "77759",
            },
        ]
    }

    # Create a mock requests response object
    mock_resp = mocker.Mock()
    # Mock the json method to return the mock transactions data
    mock_resp.json = mocker.Mock(return_value=mock_transactions)
    mock_resp.status_code = HTTPStatus.OK

    # Mock the requests.get method to return the mock response object
    mocker.patch("api.requests.get", return_value=mock_resp)

    transactions = get_transactions()
    assert transactions == mock_transactions.get('result')


@responses.activate
def test_get_transactions_failure(mocker):
    """Test get_transactions function fails to return transactions"""

    # Create a mock requests response object
    mock_resp = mocker.Mock()
    mock_resp.json = mocker.Mock(return_value={})
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    mocker.patch("api.requests.get", return_value=mock_resp)

    transactions = get_transactions()
    assert transactions == None
