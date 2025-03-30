import pytest
from unittest.mock import Mock, patch
from src.xcom.xcom_client import XClient

def test_successful_tweet_post(mocker):
    """Test successful tweet posting."""
    mock_tweet = "Valid tweet under 280 characters"
    
    # Mock Tweepy API
    mocker.patch("tweepy.API.update_status", return_value=Mock(id=123))
    client = XClient()
    result = client.post_tweet(mock_tweet)
    
    assert result is True

def test_tweet_exceeds_limit():
    """Test tweet exceeding 280 characters."""
    client = XClient()
    long_tweet = "A" * 281
    
    with pytest.raises(ValueError) as exc:
        client.post_tweet(long_tweet)
    assert "Tweet exceeds 280 character limit" in str(exc.value)

def test_invalid_credentials():
    """Test invalid X.com credentials."""
    with patch("tweepy.OAuth1UserHandler") as mock_auth:
        mock_auth.side_effect = Exception("Invalid credentials")
        
        with pytest.raises(Exception) as exc:
            XClient()
        assert "X.com authentication failed" in str(exc.value)