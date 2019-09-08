
import slixmpp


class CustomSlixmpp(slixmpp.ClientXMPP):

    def __init__(self, jid, password, recipient="", msg="", muc=False):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.jid = jid
        self.recipient = recipient
        self.msg = msg
        self.muc = muc

        self.register_plugin('xep_0045')  # Multi-User Chat
        self.register_plugin('xep_0030')  # Service Discovery
        self.register_plugin('xep_0199')  # XMPP Ping
        self.add_event_handler("session_start", self.start)

    def start(self, _):

        self.get_roster()
        self.send_presence()

        if self.muc:
            self.plugin['xep_0045'].join_muc(self.recipient,
                                             self.jid,
                                             wait=True)
            self.send_message(mto=self.recipient,
                              mbody=self.msg,
                              mtype='groupchat')
        else:
            self.send_message(mto=self.recipient,
                              mbody=self.msg,
                              mtype='chat')

        self.disconnect()
