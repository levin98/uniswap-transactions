import pytest
import responses
from http import HTTPStatus
from api import get_transactions, get_transaction_by_hash, get_block_number_by_timestamp


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
                "gasUsed": "77759"
            }
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
    assert transactions == []


@responses.activate
def test_get_transaction_by_hash_success(mocker):
    """Test get_transaction_by_hash function successfully returns transaction"""

    # Mock transaction data
    mock_transaction = {
        "result": {
            "blockHash": "0x6d5fad03919c7e988b91fbcde19fd35a59d61471144b7012e300e77603447036",
            "blockNumber": "0x109456b",
            "effectiveGasPrice": "0x734e1480a",
            "gasUsed": "0x3f0b1",
            "transactionHash": "0xe8fab79ea5a44c40dcec04f2184f3f203fb979009b70ffcf791480f72d88e5b7"
        }
    }

    # Create a mock requests response object
    mock_resp = mocker.Mock()
    # Mock the json method to return the mock transactions data
    mock_resp.json = mocker.Mock(return_value=mock_transaction)
    mock_resp.status_code = HTTPStatus.OK

    # Mock the requests.get method to return the mock response object
    mocker.patch("api.requests.get", return_value=mock_resp)

    transactions = get_transaction_by_hash("test-hash")
    assert transactions == mock_transaction.get('result')


@responses.activate
def test_get_transaction_by_hash_invalid_input(mocker):
    """Test get_transaction_by_hash function fails returns transaction with invalid input"""

    # Mock transaction data
    mock_transaction = {
        "result": {
            "blockHash": "0x6d5fad03919c7e988b91fbcde19fd35a59d61471144b7012e300e77603447036",
            "blockNumber": "0x109456b",
            "effectiveGasPrice": "0x734e1480a",
            "gasUsed": "0x3f0b1",
            "transactionHash": "0xe8fab79ea5a44c40dcec04f2184f3f203fb979009b70ffcf791480f72d88e5b7"
        }
    }

    # Create a mock requests response object
    mock_resp = mocker.Mock()
    # Mock the json method to return the mock transactions data
    mock_resp.json = mocker.Mock(return_value=mock_transaction)
    mock_resp.status_code = HTTPStatus.OK

    # Mock the requests.get method to return the mock response object
    mocker.patch("api.requests.get", return_value=mock_resp)

    with pytest.raises(Exception):
        transactions = get_transaction_by_hash()


@responses.activate
def test_get_transaction_by_hash_failure(mocker):
    """Test get_transaction_by_hash function fails to return transaction"""

    # Create a mock requests response object
    mock_resp = mocker.Mock()
    mock_resp.json = mocker.Mock(return_value={})
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    mocker.patch("api.requests.get", return_value=mock_resp)

    transactions = get_transaction_by_hash("test-hash")
    assert transactions == {}


@responses.activate
def test_get_block_number_by_timestamp(mocker):
    """Test get_block_number_by_timestamp function successfully returns transaction"""

    # Mock data
    mock_data = {
        "result": "12712551"
    }

    # Create a mock requests response object
    mock_resp = mocker.Mock()
    # Mock the json method to return the mock transactions data
    mock_resp.json = mocker.Mock(return_value=mock_data)
    mock_resp.status_code = HTTPStatus.OK

    # Mock the requests.get method to return the mock response object
    mocker.patch("api.requests.get", return_value=mock_resp)

    transactions = get_block_number_by_timestamp("1578638524")
    assert transactions == mock_data.get('result')


@responses.activate
def test_get_block_number_by_timestamp_invalid_input(mocker):
    """Test get_block_number_by_timestamp function fails returns transaction with invalid input"""

    # Mock data
    mock_data = {
        "result": "12712551"
    }

    # Create a mock requests response object
    mock_resp = mocker.Mock()
    # Mock the json method to return the mock transactions data
    mock_resp.json = mocker.Mock(return_value=mock_data)
    mock_resp.status_code = HTTPStatus.OK

    # Mock the requests.get method to return the mock response object
    mocker.patch("api.requests.get", return_value=mock_resp)

    with pytest.raises(Exception):
        transactions = get_block_number_by_timestamp()


@responses.activate
def test_get_block_number_by_timestamp_failure(mocker):
    """Test get_block_number_by_timestamp function fails to return transaction"""

    # Create a mock requests response object
    mock_resp = mocker.Mock()
    mock_resp.json = mocker.Mock(return_value={})
    mock_resp.status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    mocker.patch("api.requests.get", return_value=mock_resp)

    transactions = get_block_number_by_timestamp("test-hash")
    assert transactions == ""
