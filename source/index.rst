=======
enctext
=======

Install
=======

::

    git clone https://github.com/utisam/enctext.git
    pip install ./enctext

How to Use
==========

::

    vienc secret.txt
    catenc secret.txt

``vienc`` command uses ``vipe``, so you can use favorite ``EDITOR``.

::

    EDITOR=emacs; vienc secret.txt

.. warning::
    The editting text remain in the temporary directory if the editor failed.
    Please check and remove it.

For Developpers
===============

.. code-block:: python

    import enctext

    raw_password = 'secret_password'
    raw_text = b'This text will be encrypted.'

    encrypted = enctext.encrypt(raw_password, raw_text)
    decrypted = enctext.decrypt(raw_password, encrypted)
