import pytest
from unittest.mock import Mock, patch
from src.instagram.instagram_client import fetch_latest_instagram_post
from src.comon.config import APIFY_API_TOKEN

def test_successful_post_retrieval(mocker):
    """Test successful retrieval of Instagram post data."""
    mock_response = {
        "items": [{
            "caption": "Breaking News: Test Caption",
            "image_url": "https://example.com/image.jpg"
        }]
    }
    
    # Mock ApifyClient response
    mocker.patch(
        "src.instagram.instagram_client.ApifyClient",
        return_value=Mock(
            actor=Mock(return_value=Mock(
                call=Mock(return_value={"defaultDatasetId": "123"}),
                dataset=Mock(return_value=Mock(
                    iterate_items=Mock(return_value=iter(mock_response["items"]))
                ))
            ))
    ))
    
    result = fetch_latest_instagram_post()
    item = next(result.iterate_items())
    assert item["caption"] == "Breaking News: Test Caption"

def test_api_rate_limit(mocker):
    """Test handling of API rate limits."""
    mocker.patch(
        "src.instagram.instagram_client.ApifyClient",
        side_effect=Exception("API rate limit exceeded")
    )
    
    with pytest.raises(Exception) as exc:
        fetch_latest_instagram_post()
    assert "API rate limit exceeded" in str(exc.value)

def test_invalid_credentials():
    """Test error when API token is missing."""
    original_token = APIFY_API_TOKEN
    APIFY_API_TOKEN = None  # Temporarily invalidate
    
    with pytest.raises(ValueError) as exc:
        fetch_latest_instagram_post()
    assert "APIFY_API_TOKEN is not set" in str(exc.value)
    
    APIFY_API_TOKEN = original_token  # Restore