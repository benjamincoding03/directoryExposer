#!/usr/bin/python
import sys, argparse, urllib2

def main():
	try:
		p = argparse.ArgumentParser(description='Directory exposer')
		r = p.add_argument_group('required arguments')
		r.add_argument('-u', '--url', dest='url', help='URL to scan')
		r.add_argument('-l', '--list', dest='list', help='List of directories to scan')
		args = p.parse_args()
		# parses arguments

		url = args.url
		list = args.list

		url = url.replace('http://', '')
		url = url.replace('https://', '')
		url = url.replace('/', '')
		url = 'http://' + url + '/'
		# changes url to valid url

		req = urllib2.Request(url)
		resp = urllib2.urlopen(req)
		# checks to see if url is valid

		with open(list) as List:
			print 'Scanning... '
			for line in List:
				try:
					currentURL = url + line
					req = urllib2.Request(currentURL)
					resp = urllib2.urlopen(req)
					print currentURL

				except urllib2.HTTPError:
					pass
					# checks every url in list

	except IOError:
		print 'Invalid worldist'
		sys.exit()

	except AttributeError:
		print 'Enter a URL'
		sys.exit()

	except urllib2.URLError:
		print 'Invalid URL'
		sys.exit()

	except KeyboardInterrupt:
		sys.exit()

main()
