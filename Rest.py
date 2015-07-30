# -*- conding: utf-8 -*-
import urllib2
import base64


class BasicRest:
    def __init__(self, uri, http_type, user, passwd):
        self.uri = uri
        self.http_type = http_type
        self.user = user
        self.passwd = passwd

    def create_request_Basic(self, uri, http_type):
        """

        :rtype : Type URLLIB2 Request  or None(NuLL)
        """
        if (http_type == "GET" or http_type == "POST" or
                    http_type == "PUT" or http_type == "DELETE"):
            # call rest api
            request = urllib2.Request(uri)
            base64str = base64.encodestring('%s:%s' % (self.user, self.passwd)).replace('\n', '')
            request.add_header("Authorization", "Basic %s" % base64str)
            return request
        else:
            print("http_type error  [ " + http_type + " ]")
            return None

    def rest_send(self, request):
        response = urllib2.urlopen(request)
        ret = response.read()
        print 'Response:', ret


class BasicRestXml(object, BasicRest):
    def __init__(self, uri, http_type, user, passwd):
        super(BasicRestXml, self).__init__(uri, http_type, user, passwd)  # extends

    def _request(self, uri, http_type):
        req = self.create_request_Basic(uri, http_type)
        if req is None:
            print('NG')
        req.add_header('Content-Type', 'application/xml')
        self.rest_send(req)


class BasicRestJson(object, BasicRest):
    def __init__(self, uri, http_type, user, passwd):
        super(BasicRestJson, self).__init__(uri, http_type, user, passwd)  # extends

    def _request(self, uri, http_type):
        req = self.create_request_Basic(uri, http_type)
        if req is None:
            print('NG')
        req.add_header('Content-Type', 'application/json')
        self.rest_send(req)
