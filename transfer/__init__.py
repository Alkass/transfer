#!/usr/bin/python3

import os
import argparse
import requests

def upload(serviceUrl, files):
    for _file in files:
        print('Uploading %s to %s' % (_file, serviceUrl))
        r = requests.put(url='%s/%s' % (serviceUrl, _file), data=open(_file, 'rb'))
        print('|- %s' % (r.text.strip()))

def download(serviceUrl, urls, name):
    for url in urls:
        if not name:
            name = url.replace(serviceUrl, '').split('/')[-1]
        print('Saving %s as %s' % (url, name))
        r = requests.get(url=url, stream=True)
        with open(name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

def file_validator(arg):
    if not os.path.isfile(arg):
        raise Exception('Invalid file path: %s' % arg)
    return arg

def url_validator(arg):
    arg = arg.lower().strip()
    if not arg.startswith("https://") and not arg.startswith('http://'):
        raise Exception("%s doesn't appear to be a valid URL" % arg)
    return arg

def name_validator(arg):
    arg = arg.strip()
    if not len(arg):
        raise Exception("name can't be empty")
    return arg

class Defaults:
    DEFAULT_SERVICE_URL = 'https://transfer.sh'

def main():
    parser = argparse.ArgumentParser(description='transfer.sh CLI Utility')
    parser.add_argument('--upload',
                        nargs='*',
                        type=file_validator,
                        help='Files to upload')
    parser.add_argument('--download',
                        nargs='*',
                        type=url_validator,
                        help='File URLs to download')
    parser.add_argument('--name',
                        help='Rename downloaded file',
                        type=name_validator)
    parser.add_argument('--service',
                        help='File sharing service URL. Specify if uploading to a self-hosted version of transfer.sh',
                        type=url_validator,
                        default=Defaults.DEFAULT_SERVICE_URL)
    args = parser.parse_args()

    if (not args.upload or not len(args.upload)) and (not args.download or not len(args.download)):
        raise Exception('Neither --upload nor --download is specified')

    if args.upload and args.download:
        raise Exception('Both --upload and --download are specified')

    if args.name:
        if args.upload:
            raise Exception('--name is only available with --download')
        if args.download and len(set(args.download)) > 1:
            raise Exception('--name can be used with a single --download argument only')
    
    if args.service != Defaults.DEFAULT_SERVICE_URL and args.download:
        raise Exception('--service is not needed with --download')

    if args.upload:
        upload(args.service, set(args.upload))
    elif args.download:
        download(args.service, set(args.download), args.name)

if __name__ == '__main__':
    main()
