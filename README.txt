# This is the readme file for my project


Steps taken to clean up the URLs in order to run link_checker script:
- Added a duplicate column for "clean_link_text_not_article", which includes only the non-self-referential links on which all following actions were taken to preserve the original information in "link_text"
- Split URLs on "[" and "]"
- Removed the trailing symbols: ".", ",", "<", ">", "(", ")", ";", and "/"
- Removed trailing words "appendix" and "supplement" (pattern indicated these words were not part of actual links, but should have been the next word after the link)