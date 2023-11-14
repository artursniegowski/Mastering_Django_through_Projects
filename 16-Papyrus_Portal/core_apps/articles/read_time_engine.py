"""
engine for a better estimation on how long does it take
to read an article
"""
from math import ceil


class ArticleReadTimeEngine:
    """class for estimating read time of article"""

    @staticmethod
    def word_count(text: str) -> int:
        """fiding the words"""
        # words = re.findall(r'\w+', text)
        words = text.split()
        return len(words)

    @staticmethod
    def estimate_reading_time(
        article,
        words_per_minute: int = 200,
        seconds_per_image: int = 10,
        seconds_per_tag: int = 2,
    ) -> int:
        """estimating the reading time based on words_per_mnute, returning
        the number of minutes"""
        total_word_cout = (
            ArticleReadTimeEngine.word_count(article.body)
            + ArticleReadTimeEngine.word_count(article.title)
            + ArticleReadTimeEngine.word_count(article.description)
        )

        reading_time = total_word_cout / words_per_minute
        if article.banner_image:
            reading_time += seconds_per_image / 60

        tag_count = article.tags.count()
        reading_time += (tag_count * seconds_per_tag) / 60

        return ceil(reading_time)
