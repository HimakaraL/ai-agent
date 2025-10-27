from typing import Optional
from collections import Counter
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool


def save_to_file(content: str, file_name="search_output.txt", keywords: Optional[list[str]] = None):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(content + "\n")
        if keywords:
            f.write("Keywords: " + ", ".join(keywords) + "\n")
    return f"Saved to {file_name}"


def keyword_showcase(content: str):
    stopwords = {
        "the", "is", "in", "and", "to", "a", "of", "it", "that", "on", "for", "with",
        "as", "was", "were", "are", "by", "at", "be", "from", "this", "an", "or",
        "which", "but", "not", "have", "has", "had", "they", "you", "we", "can", "their"
    }

    words = [w.strip(".,!?()[]{}:;\"'").lower() for w in content.split()]

    filtered_words = [w for w in words if w and w not in stopwords]

    top_5 = Counter(filtered_words).most_common(5)
    return [word for word, _ in top_5]

keyword_tool = Tool(
    name="keyword_showcase",
    description="Showcase the most common keywords in the content",
    func=keyword_showcase,
)

save_tool = Tool(
    name="save_to_file",
    description="Save content to a file",
    func=save_to_file,
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    description="Search for information",
    func=search.run,
)

api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=2000)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
