'''
:maintainer: Felippe Burk
:maturity: poc
:platform: linux

This module is a poc to show lastpass integration with salt pillar. This module
is incomplete. While the basic concept is sound, handling of the login using the lpass
binary has yet to be done.

example ext_pillar config:

.. code-block:: yaml

    ext_pillar:
      - lastpass:
          passwords:
            shared_password: 'shared_passwords/shared_password'
'''
import logging
import subprocess
log = logging.getLogger(__name__)

def __virtual__():
  return True

def ext_pillar(minion_id, pillar, passwords):

  lastpass = {"lastpass": {}}

  for name, path in passwords.iteritems():
    try:
      password = subprocess.check_output(['lpass', 'show', path, '-p']).strip('\n')
      lastpass["lastpass"][name] = password
    except:
      log.error('"{0}" is not a valid lastpass pillar config'.format(conf))

  return lastpass
