# rest-fs
REST API FUSE experiment

Mount a remote API to your filesystem because why not?

I think there's some potential here, but it will ultimately have to be configuration heavy so that you can define
whether the endpoint resources should 'act like files' or 'act like directories', which would inform `readdir()`
what to do.

Ultimately I'd like to see this be able to POST/PATCH data too.


How to test this:
```
git clone https://github.com/terencehonles/fusepy.git
cd fusepy && python setup.py build && sudo python setup.py install

# put rest.py above somewhere then mount this public dogs api
python rest.py https://dog.ceo/api /tmp/test
cd /tmp/test
ls breeds/list
```

The API I am using above for testing is [https://dog.ceo/dog-api/](https://dog.ceo/dog-api/).
