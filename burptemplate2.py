from burp import IBurpExtender
from burp import IHttpRequestResponse
from burp import IHttpListener
from burp import IContextMenuFactory
import json


'''
    TODO:
        currently the below serves as a template. Update this to utilize the rule list rather than having it hard-coded.
        - ingest the aftersought ruleset for the task, preferrably via engine
        - add a way to interact with cli in the engine
        - post-processing of data, or dispatch capability? 
'''
class BurpExtender(IBurpExtender, IContextMenuFactory, IHttpListener):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self.context = None
        callbacks.setExtensionName("PrintsCharming_burp2")
        callbacks.registerContextMenuFactory(self)
        callbacks.registerHttpListener(self)

    # createMenuItems does not currently work as intended, fix!
    def createMenuItems(self, context_menu):
        self.context = context_menu
        menu_list = []
        menu_list.append(JMenuItem("PrintsCharming_burp", actionPerformed=self.update))
        return menu_list

    def update(self, event):
        print("in update, add stuff here in the future")
        
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if messageIsRequest:
            request = messageInfo.getRequest()
            analyzedRequest = self._helpers.analyzeRequest(request)
            requestBody = request[analyzedRequest.getBodyOffset():]
            requestBodyString = self._helpers.bytesToString(requestBody)
            jsonMessage = {"data":"U2VydmVyOiBXZXJremV1Zy8yLjIuMyBQeXRob24vMy4xMC4xMAo=", "tags":["all"]} #do not use hardcoded value! Only for test
            jsonMessageString = json.dumps(jsonMessage)
            newRequestBodyString = requestBodyString + jsonMessageString
            
            # new request goes here
            newRequestBody = self._helpers.stringToBytes(newRequestBodyString)
            messageInfo.setRequest(self._helpers.buildHttpMessage(analyzedRequest.getHeaders(), newRequestBody))
            #remove below  content length if not strictly needed.. or keep. 
            contentLengthHeader = self._helpers.buildHttpHeader("Content-Length", str(len(newRequestBody)))
            messageInfo.getRequest().setHeader(contentLengthHeader)
