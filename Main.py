# -*- coding: utf-8
import sys
import BasicRestXml
import BasicRestJson

class Main():
    user   = "admin"
    passwd = "admin"
    def run(self, uri, http_type):
        new BasicRestXml(uri, http_type, self.user, self.passwd)
        BasicRestJson(uri, http_type, self.user, self.passwd)


if __name__ == "__main__":
    arg = sys.argv
    argc = len(arg)
    uri =
    http_type =

    Main().run(uri, http_type)
