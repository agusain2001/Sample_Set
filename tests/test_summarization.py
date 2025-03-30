import pytest
from unittest.mock import Mock, patch
from src.summarization.llm_summarizer import LLMSummarizer

def test_summary_within_limit():
    """Test summarization within 280 characters."""
    summarizer = LLMSummarizer()
    mock_caption = "A very long caption " * 50  # ~1000 characters
    
    # Mock Gemini response
    with patch("google.generativeai.GenerativeModel") as mock_model:
        mock_model.return_value.generate_content.return_value = Mock(
            text="Concise summary under 280 characters."
        )
        summary = summarizer.summarize_for_tweet(mock_caption)
    
    assert len(summary) <= 280

def test_fallback_truncation():
    """Test fallback truncation when LLM fails."""
    summarizer = LLMSummarizer()
    mock_caption = "A" * 300  # Exceeds limit
    
    # Force LLM failure
    with patch("google.generativeai.GenerativeModel") as mock_model:
        mock_model.side_effect = Exception("API Error")
        summary = summarizer.summarize_for_tweet(mock_caption)
    
    assert len(summary) == 280
    assert summary.endswith("...")

def test_empty_caption():
    """Test empty caption handling."""
    summarizer = LLMSummarizer()
    with pytest.raises(ValueError) as exc:
        summarizer.summarize_for_tweet("")
    assert "Caption cannot be empty" in str(exc.value)