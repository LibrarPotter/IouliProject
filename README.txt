# This is the readme file for my project


Steps taken to clean up the URLs in order to run link_checker script:
- Added a duplicate column for "clean_link_text_not_article", which includes only the non-self-referential links on which all following actions were taken to preserve the original information in "link_text"
- Split URLs on "[" and "]"
- Removed the trailing symbols: ".", ",", "<", ">", "(", ")", ";", and "/"
- Removed trailing words "appendix" and "supplement" (pattern indicated these words were not part of actual links, but should have been the next word after the link)

check_new_location_for_300
- Eventually, this should be combined with the original link checker, because there is a great deal of duplication between the two, but for now this should be run after link_checker.pynb


Workflow:
- clean the data as mentioned above
- run link_checker
-- this adds columns for status and headers for URLs provided in the article (returned using the requests library)
- run check_location_for_300
-- this adds columns for the new/temporary/perminant "location" for all URLs that returned 300-304 statuses (these are refered to as status2, header2, and url2)
-- the locations are provided in the header fields
-- new columns are added to the dataframe
-- the new columns are: statusList2, headerList2, and urlList2