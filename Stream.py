import json
class Stream:

    def __init__(self, srcip,dstip,dstport="",protocol="",srcmask="255.255.255.255",dstmask="255.255.255.255"):
        self.srcip = []
        self.srcmask = srcmask
        self.dstip = []
        self.dstmask = dstmask
        self.dstport = []
        self.protocol = []
        self.srcip.append(srcip)
        self.dstip.append(dstip)
        self.dstport.append(dstport)
        self.protocol.append(protocol)


    def __eq__(self, other):
        return isinstance(self, Stream) and \
            self.srcip == other.srcip and \
            self.srcmask == other.srcmask and \
            self.dstip == other.dstip and \
            self.dstmask == other.dstmask and \
            self.dstport == other.dstport and \
            self.protocol == other.protocol

    def __str__(self):
        return self.to_json()

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__,
                            "Source IP: {}"
                            ", Source mask: {} "
                            ", Destination IP: {} "
                            ", Destination mask: {} "
                            ", Destination port: {} "
                            ", Destination protocol: {}".format(sorted(self.srcip),
                                                                self.srcmask,
                                                                sorted(self.dstip),
                                                                self.dstmask,
                                                                sorted(self.dstport),
                                                                sorted(self.protocol)))

    def to_json(self):
        data = {
            'source-ip': sorted(self.srcip),
            'source-mask': self.srcmask,
            'dst-ip': sorted(self.dstip),
            'dst-mask': self.dstmask,
            'dst-port': sorted(self.dstport),
            'protocol': sorted(self.protocol)
            }
        return json.dumps(data)


