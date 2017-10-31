import os
import PushCoT

ATAK_IP = os.getenv('ATAK_IP', '192.168.1.150')
ATAK_PORT = int(os.getenv('ATAK_PORT', '4242'))

params = {  # SWX parking lot
    "lat": 27.957261,
    "lon": -82.436587,
    "uid": "SWX",
    "identity": "friend",
    "dimension": "land-equipment",
    "entity": "military",
    "type": ""
}

print "Params:\n" + str(params)
cot = CoT.CursorOnTarget()
cot_xml = cot.atoms(params)

print "\nXML message:"
print cot_xml

print "\nPushing to ATAK..."
sent = cot.pushUDP(ATAK_IP, ATAK_PORT, cot_xml)
print str(sent) + " bytes sent to " + ATAK_IP + " on port " + str(ATAK_PORT)
