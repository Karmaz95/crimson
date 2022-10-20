#
#  postMessage issue detector - Find postMessage client side issues
#
#  Copyright (c) 2020 Mariusz Poplawski from afine.pl team (mpoplawski@afine.pl)
#
from burp import IBurpExtender, IScannerCheck, IScanIssue, ITab
from java.io import PrintWriter
from java.net import URL
from java.util import ArrayList, List
from java.util.regex import Matcher, Pattern
import binascii
import base64
import re
from javax import swing
from java.awt import Font, Color
from threading import Thread
from array import array
from java.awt import EventQueue
from java.lang import Runnable
from thread import start_new_thread
from javax.swing import JFileChooser
import traceback
import re

class Run(Runnable):
    def __init__(self, runner):
        self.runner = runner

    def run(self):
        self.runner()

class BurpExtender(IBurpExtender, IScannerCheck, ITab):
    def registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName("pMDetector")

        callbacks.issueAlert("postMessage issue detector Passive Scanner enabled")

        stdout = PrintWriter(callbacks.getStdout(), True)
        stderr = PrintWriter(callbacks.getStderr(), True)
        callbacks.registerScannerCheck(self)
        self.initUI()
        self.callbacks.addSuiteTab(self)
        
        print ("postMessage issue detector loaded.")
        print ("Copyright (c) 2020 Mariusz Poplawski from afine.pl team (mpoplawski@afine.pl) ")
        self.outputTxtArea.setText("postMessage issue detector loaded." + "\n" + "Copyright (c) 2020 Mariusz Poplawski (afine.pl team) (mpoplawski@afine.com)" + "\n")

    def initUI(self):
        self.tab = swing.JPanel()

        # UI for Output
        self.outputLabel = swing.JLabel("pMDetector Log:")
        self.outputLabel.setFont(Font("Tahoma", Font.BOLD, 14))
        self.outputLabel.setForeground(Color(255,102,52))
        self.logPane = swing.JScrollPane()
        self.outputTxtArea = swing.JTextArea()
        self.outputTxtArea.setFont(Font("Consolas", Font.PLAIN, 12))
        self.outputTxtArea.setLineWrap(True)
        self.logPane.setViewportView(self.outputTxtArea)
        self.clearBtn = swing.JButton("Clear Log", actionPerformed=self.clear)
        self.exportBtn = swing.JButton("Export Log", actionPerformed=self.export)
        self.parentFrm = swing.JFileChooser()



        # Layout
        layout = swing.GroupLayout(self.tab)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)
        self.tab.setLayout(layout)
      
        layout.setHorizontalGroup(
            layout.createParallelGroup()
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup()
                    .addComponent(self.outputLabel)
                    .addComponent(self.logPane)
                    .addComponent(self.clearBtn)
                    .addComponent(self.exportBtn)
                )
            )
        )
        
        layout.setVerticalGroup(
            layout.createParallelGroup()
            .addGroup(layout.createParallelGroup()
                .addGroup(layout.createSequentialGroup()
                    .addComponent(self.outputLabel)
                    .addComponent(self.logPane)
                    .addComponent(self.clearBtn)
                    .addComponent(self.exportBtn)
                )
            )
        )

    def getTabCaption(self):
        return "pMDetector"

    def getUiComponent(self):
        return self.tab

    def clear(self, event):
          self.outputTxtArea.setText("postMessage issue detector loaded." + "\n" + "Copyright (c) 2020 Mariusz Poplawski (afine.pl team) (mpoplawski@afine.com)" + "\n" )

    def export(self, event):
        chooseFile = JFileChooser()
        ret = chooseFile.showDialog(self.logPane, "Choose file")
        filename = chooseFile.getSelectedFile().getCanonicalPath()
        print("\n" + "Export to : " + filename)
        open(filename, 'w', 0).write(self.outputTxtArea.text)

    
    def doPassiveScan(self, HTTPResponse):
        try:
            TargetUrl = HTTPResponse.getUrl()
            response = str(self.helpers.bytesToString(HTTPResponse.getResponse()).encode("utf-8","ignore"))
            #self.outputTxtArea.append("\n" + "[+] try: "+str(response))
            postMessageDetect = Analyse(response)
            scopes,datas = postMessageDetect.analyseURL(self)
            if scopes != "0":
                self.outputTxtArea.append("\n" + "[+] postMessage() Found in: "+str(TargetUrl))
                
                if isinstance(scopes, list): 
                    for i in range(0,len(scopes)):
                        self.outputTxtArea.append("\n" + "Data sent: %s as scope: %s " % (datas[i],scopes[i]))
                else:
                    self.outputTxtArea.append("\n" + "Data sent: %s as scope: %s " % (datas,scopes))
                self.outputTxtArea.append("\n" + "-----------------------------------")

                if '"*"' in scopes or "'*'" in scopes:
                    issues = ArrayList()
                    issues.add(AddIssue(HTTPResponse, self.helpers, "High", "Certain",scopes,datas))
                else:
                    issues = ArrayList()
                    issues.add(AddIssue(HTTPResponse, self.helpers, "High", "Tentative",scopes,datas))
                return issues
        #except Exception,e: self.outputTxtArea.append("\n"+str(e))
        except Exception as e:
            tb = traceback.format_exc()
            self.outputTxtArea.append("\n"+str(tb))
        return None


    def consolidateDuplicateIssues(self, isb, isa):
        return -1

    def extensionUnloaded(self):
        print "postMessage Detector unloaded"
        return

class Analyse():

    def __init__(self, response):
        self.response = response
    
    def findScope(self,match):
        scope = match.split(",")
        if ";" in scope[-1]:
            return scope[-1].split(");")[0]
        if "}" in scope[-1]:
            return scope[-1].split(")}")[0]
        if "))" in scope[-1]:
            return scope[-1].split("))")[0]

        return scope[-1].split(")")[0]

    def CheckValidDataInside(self,data):

        countOpenBracket = 0
        countClosedBracket = 0
        if "(" in data:
            countOpenBracket = data.count("(")
            countClosedBracket = data.count(")")

            if countOpenBracket != countClosedBracket:
                return "0"
        
        countOpenBracket = 0
        countClosedBracket = 0
        if "{" in data:
            countOpenBracket = data.count("{")
            countClosedBracket = data.count("}")

            if countOpenBracket != countClosedBracket:
                return "0"

        return data


    def findPmData(self,match):
        findDot = match.count(",")
        data = ""
        if findDot == 1:
            data = match.split(",")[0]
        else:
            for i in range (0,findDot):
                if not data:
                    data = match.split(",")[i]
                else:
                    data = data +","+ match.split(",")[i]
        data = data.replace("postmessage(","")

        return self.CheckValidDataInside(data)


    def postMessageFinnder(self,content):
        res = []
        idx = 0
        TrimmedContent = content[idx:len(content)]
        while True:
            TrimmedContent = TrimmedContent[idx:len(TrimmedContent)]
            OpenedBracket = 1
            PMBody = ""
            index = TrimmedContent.find("postmessage(", 0, len(content)) 
            if not index > 0:
                break

            #print(content[index:len(content)])
            index = index + 12
            outIndex = index
            for i in range(index,len(TrimmedContent)):
                if TrimmedContent[i] == "(":
                    OpenedBracket = OpenedBracket +1
                if TrimmedContent[i] == ")":
                    OpenedBracket = OpenedBracket -1

                PMBody = PMBody + TrimmedContent[i]
                if OpenedBracket == 0:
                    idx = i+1
                    break

            res.append("postmessage("+PMBody+";")
        return res

    def analyseURL(self,logger):
        try:
            if "postmessage(" in self.response.lower():
                content = str(self.response.lower())
                content = content.replace("\n","")
                content = content.replace("\t","")
                content = content.replace(" ","")

                #pattern = r"(postmessage(\s{0,}\S{0,})\((\s{0,}\S{0,})(\"|')([a-zA-Z0-9_-]+))(?!{)(\"|')(\s{0,}\S{0,}),(.+)(\"|')(\s{0,})([a-zA-Z0-9_-]+)(\s{0,})(\"|')"
                #pattern = r"(postmessage(([(])([a-zA-Z0-9\'\"\{\}\[\]\.\:\)\(\-\_\=\+\,]*)([,])([a-zA-Z0-9\!\@\#\$\%\^\&\*\)\-\_\=\+\[\{\]\;\:\'\"\,\<\.\>\/\?]*)(\;|\})))"
                #pattern = r"(postmessage(.*))"

                #matches = re.findall(pattern=pattern, string=content)
                
                scopes = []
                datas = []

                matches = self.postMessageFinnder(content)
                #logger.outputTxtArea.append("\n"+content)
                #logger.outputTxtArea.append("\n"+str("trying before match print:"))
                for match in matches:
                    #logger.outputTxtArea.append("\n"+str("trying match print:"))
                    
                    #logger.outputTxtArea.append("\n"+str(match))
                    if not "," in match:
                        continue
                    PMscope = self.findScope(match)
                    PMData = self.findPmData(match)

                    #if PMData == "0":
                    #    continue
                    scopes.append(PMscope)
                    datas.append(PMData)

                return scopes,datas
            return "0","0"
        #except Exception,e: logger.outputTxtArea.append("\n"+str(e))
        except Exception as e:
            tb = traceback.format_exc()
            logger.outputTxtArea.append("\n"+str(tb))

class AddIssue(IScanIssue,ITab):
    def __init__(self, reqres, helpers, mySeverity, myConfidence,scopes,datas):
        self.helpers = helpers
        self.reqres = reqres
        self.mySeverity = mySeverity
        self.myConfidence = myConfidence
        self.scopes = scopes
        self.datas = datas

    def getHost(self):
        return self.reqres.getHost()

    def getPort(self):
        return self.reqres.getPort()

    def getProtocol(self):
        return self.reqres.getProtocol()

    def getUrl(self):
        return self.reqres.getUrl()

    def getIssueName(self):
        return "postMessage potential issue detected"

    def getIssueType(self):
        return 0x08000000  # See http:#portswigger.net/burp/help/scanner_issuetypes.html

    def getSeverity(self):
        return self.mySeverity  # "High", "Medium", "Low", "Information" or "False positive"

    def getConfidence(self):
        return self.myConfidence  # "Certain", "Firm" or "Tentative"

    def getIssueBackground(self):
        return str("Insecure usage of postMessage(data,\"*\") can lead to leak of secret data, tokens, credentials and account takeover without notice of victim.")

    def getRemediationBackground(self):
        return "This is an <b>informational</b> finding only.<br>"

    def getIssueDetail(self):

        out = ""
        for i in range(0,len(self.scopes)):
            out = out + "Data sent: "+str(self.datas[i])+" as scope: "+str(self.scopes[i])+"<br>"

        return str("Burp Scanner has analysed the following response for postMessage() issues <b>"
                      "%s</b><br><br>%s" % (self.reqres.getUrl().toString(),out))

    def getRemediationDetail(self):
        return None

    def getHttpMessages(self):
        #print ("................raising issue................")
        rra = [self.reqres]
        return rra
        
    def getHttpService(self):
        return self.reqres.getHttpService()
        
        
if __name__ in ('__main__', 'main'):
    EventQueue.invokeLater(Run(BurpExtender))
