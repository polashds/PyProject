import pytest
from unittest.mock import patch, Mock
from demo_request import safe_get_users, safe_posts

@patch("demo_request.requests.get")
def test_safe_get_user_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "John Doe"}]
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    safe_get_users()


@patch("demo_request.requests.post")
def test_safe_post_success(mock_post):
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {
        "title": "Hello API World",
        "body": "This is a demo post from Python requests.",
        "userId": 1,
        "id": 101
    }
    mock_response.raise_for_status.return_value = None

    mock_post.return_value = mock_response

    safe_posts()
