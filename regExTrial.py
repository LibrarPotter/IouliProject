 #!/usr/bin/python
          # -*- coding: utf-8 -*-
import os, sys
import re

from lxml import etree
from io import StringIO, BytesIO

filePath = "C:/Users/Megan/Desktop/test/nest/0223/S002228520300287X.xml"
tree = etree.parse(filePath)
justText = etree.tostring(tree, encoding='utf8', method='text')

print "a1"
#extract URLs
url = 'jhdlkjfd jdklfj jfdlfjsdjflk \t\t\t\nmldk jhhhttp://example.comjkj dsfd , d REs  English\n sentences, or e-mail addresses, orTeX commands, or anything you like. You can then ask questions such as “Does this string match the pattern?”, or “Is there a match for the pattern anywhere, or regexes, or regex patterns) are essentially a tiny, highly specialized programming language embedded inside Python and made available through dkgjfhskjahgk jjjhttp://example2.comjjj http://,  www.elbow.com, English sentences, or e-mail addresses, or TeX commands, or anything you like. You can then ask questions such as “Does this string match the pattern?”, or “Is there a match for the pattern anywhere English sentences, or e-mail addresses, or TeX commands, or anything you like. You can then ask questions such as “Does this string match the pattern?”, or “Is there a match for the pattern anywhere hgakjhaskgjhsa;;as https://example3.com'

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
print urls

print "a2"
fi = re.findall('(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|){,100}http', url) #this doesn't grab newlines and compiles too slowly for larger datasets
print fi

print "a3"


m = re.compile('(.|([^/\n+|/\t+])){,100}http', re.DOTALL)#the "." is any character because of "re.DOTALL". the "[\S]" is supposed to make it not return newlines or tabs but instead it's breaking The {,100} indicates to look for 0 to 100 characters before the http. Currently "http" will be included in the result.

l = re.findall(m, justText)
print l

print "a4"



print "a5a"

preLinks1 = re.findall('(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|){,50}http', justText) #breaking/taking forever
print preLinks1

print "a5"

#t1 = re.compile('(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|){,100}http')
#r1 = re.findall(t1, justText)

       

#print urls
#print r1
