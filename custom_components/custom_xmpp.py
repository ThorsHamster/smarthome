import logging

DOMAIN = 'custom_xmpp'
REQUIREMENTS = ['slixmpp==1.4.2']
_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    _LOGGER.debug('Setting up Custom XMPP Component')
    jid = config[DOMAIN].get('jid', None)
    password = config[DOMAIN].get('password', None)
    recipient_me = config[DOMAIN].get('recipient_me', '')
    recipient_group = config[DOMAIN].get('recipient_group', None)

    if not jid:
        raise ValueError('jid is not set in configuration')
    if not password:
        raise ValueError('password is not set in configuration')
    if not recipient_me:
        raise ValueError('recipient_me is not set in configuration')
    if not recipient_group:
        raise ValueError('recipient_group is not set in configuration')

    custom_xmpp = CustomXMPP(
        jid=jid,
        password=password,
        recipient_me=recipient_me,
        recipient_group=recipient_group
    )

    hass.services.register(DOMAIN, 'send_to_me', custom_xmpp.send_to_me)
    hass.services.register(DOMAIN, 'send_to_group', custom_xmpp.send_to_group)
    return True


class CustomXMPP(object):

    def __init__(self, jid, password, recipient_me, recipient_group):
        self.jid = jid
        self.password = password
        self.recipient_me = recipient_me
        self.recipient_group = recipient_group

    def send_to_me(self, message):
        _LOGGER.info('Send Message to me.')
        from custom_components.custom_slixmpp import CustomSlixmpp
        CustomSlixmpp(
            jid=self.jid,
            password=self.password,
            recipient=self.recipient_me,
            msg=message,
            muc=False
        )

    def send_to_group(self, message):
        _LOGGER.info('Send Message to Group.')
        from custom_components.custom_slixmpp import CustomSlixmpp
        CustomSlixmpp(
            jid=self.jid,
            password=self.password,
            recipient=self.recipient_group,
            msg=message,
            muc=True
        )
