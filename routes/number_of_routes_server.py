import csv
import sys
import threading
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler
import json

dictGlobal = {}

def readCsv():
  csvfile = open('graph_dataset.csv', 'rb')
  reader = csv.reader(csvfile)
  return reader


def updatePath(row):
  global dictGlobal
  for elem in dictGlobal.keys():
    number = elem.split('-')
    if number[1] == row[0]:
      try:
        dictGlobal[str(number[0])+'-'+str(row[1])] = dictGlobal[str(number[0])+'-'+str(row[1])] + 1
      except KeyError as err:
        dictGlobal[str(number[0])+'-'+str(row[1])] = 1
  try:
    dictGlobal[str(row[0])+'-'+str(row[1])] = dictGlobal[str(row[0])+'-'+str(row[1])] + 1
  except KeyError as err:
    dictGlobal[str(row[0])+'-'+str(row[1])] = 1

def readThread():
  for row in readCsv():
    updatePath(row)

def getList(n):
  listOfNodes = []
  for elem in dictGlobal.keys():
    if dictGlobal[elem] == n:
      nodes = elem.split('-')
      listOfNodes.append('('+str(nodes[0])+','+str(nodes[1])+')')
  return listOfNodes

class MyHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    listOfNodes = getList(int(self.path[1:]))
    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(listOfNodes))


if __name__=='__main__':
  processThread = threading.Thread(target=readThread)  # <- note extra ','
  processThread.start()
  httpd = SocketServer.TCPServer(("", 5000), MyHandler)
  httpd.serve_forever()
